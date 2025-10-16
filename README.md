# search-dom-app
a single-page application (SPA) where users can input a website URL and a search query. The application will return the top 10 matches of HTML DOM content (chunks) based on the search query.


# Project Structure
search-dom-app/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Frontend HTML file (SPA UI)
├── requirements.txt       # Python dependencies
└── README.md              # Project instructions and info

# Requirements.txt
Flask==3.0.0
beautifulsoup4==4.12.2
requests==2.31.0
lxml==5.0.0
scikit-learn==1.7.2
sentence-transformers==2.2.2  # optional if embeddings added later

# Installation & Running
*Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

*Install dependencies
pip install -r requirements.txt

*Run the application
python app.py

