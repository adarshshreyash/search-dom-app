# Website Content Search - Flask Web Application

## Overview

This Flask-based single-page application (SPA) allows users to input a website URL and a search query, then returns the top 10 matching segments ("chunks") of HTML content from that website based on keyword relevance.

## Features

- Fetch and parse HTML content from any public URL.
- Extract meaningful DOM chunks (paragraphs, headings, divs, etc.).
- Search HTML chunks using TF-IDF and cosine similarity.
- Return the most relevant matching chunks with context and score.

---

## Prerequisites

- Python 3.10 or higher
- Git (optional for cloning the repo)
- Internet connectivity for fetching URLs

---

## Requirements

The project depends on these Python packages:


- `Flask`: Web framework for building the backend server.
- `beautifulsoup4` & `lxml`: HTML parsing and DOM chunk extraction.
- `requests`: HTTP client to fetch webpage HTML.
- `scikit-learn`: TF-IDF vectorization and cosine similarity for search.
- `sentence-transformers`: Later use for generating semantic vector embeddings.




