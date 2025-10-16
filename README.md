## Website Content Search - Flask Web Application

# Overview

This Flask-based single-page application (SPA) allows users to input a website URL and a search query, then returns the top 10 matching segments ("chunks") of HTML content from that website based on keyword relevance.

# Features

- Fetch and parse HTML content from any public URL.
- Extract meaningful DOM chunks (paragraphs, headings, divs, etc.).
- Search HTML chunks using TF-IDF and cosine similarity.
- Return the most relevant matching chunks with context and score.

---

# Prerequisites

- Python 3.10 or higher
- Git (optional for cloning the repo)
- Internet connectivity for fetching URLs

---

# Project Structure
search-dom-app/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML file (SPA UI)
├── requirements.txt       # Python dependencies
└── README.md              # Project instructions and info

---

# Requirements
Flask==3.0.0
beautifulsoup4==4.12.2
requests==2.31.0
lxml==5.0.0
scikit-learn==1.7.2
sentence-transformers==2.2.2  # optional if embeddings added later

---

# Setup Instructions(Installation and running)

*Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

*Install dependencies
pip install -r requirements.txt

*Run the application
python app.py

