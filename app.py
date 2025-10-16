from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

def fetch_html(url):
    """Fetch HTML content from URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return None

def chunk_html(html_content):
    """Parse HTML and create chunks from DOM elements"""
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Remove script and style elements
    for script in soup(["script", "style", "meta", "link"]):
        script.decompose()
    
    chunks = []
    
    # Extract text from various DOM elements
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'div', 'article', 'section']):
        text = tag.get_text(strip=True)
        
        # Filter out empty or very short chunks
        if text and len(text) > 30:
            chunks.append({
                'text': text,
                'tag': tag.name,
                'classes': ' '.join(tag.get('class', [])),
                'id': tag.get('id', '')
            })
    
    return chunks

def search_chunks(chunks, query, top_n=10):
    """Search chunks using TF-IDF and cosine similarity"""
    if not chunks:
        return []
    
    texts = [chunk['text'] for chunk in chunks]
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    
    try:
        tfidf_matrix = vectorizer.fit_transform(texts + [query])
        
        # Calculate cosine similarity between query and chunks
        query_vector = tfidf_matrix[-1]
        chunk_vectors = tfidf_matrix[:-1]
        
        similarities = cosine_similarity(query_vector, chunk_vectors).flatten()
        
        # Get top N matches
        top_indices = similarities.argsort()[-top_n:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:  # Only include non-zero matches
                results.append({
                    'text': chunks[idx]['text'],
                    'tag': chunks[idx]['tag'],
                    'score': float(similarities[idx]),
                    'classes': chunks[idx]['classes'],
                    'id': chunks[idx]['id']
                })
        
        return results
    except:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    url = data.get('url', '').strip()
    query = data.get('query', '').strip()
    
    if not url or not query:
        return jsonify({'error': 'URL and query are required'}), 400
    
    # Fetch HTML
    html_content = fetch_html(url)
    if not html_content:
        return jsonify({'error': 'Failed to fetch URL'}), 400
    
    # Create chunks
    chunks = chunk_html(html_content)
    
    if not chunks:
        return jsonify({'error': 'No content found to search'}), 404
    
    # Search chunks
    results = search_chunks(chunks, query, top_n=10)
    
    return jsonify({
        'results': results,
        'total_chunks': len(chunks)
    })

if __name__ == '__main__':
    app.run(debug=True)
