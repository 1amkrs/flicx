# Flicx Website (Offline Mirror)

This is an offline copy of the [Flicx](https://fli.cx/) web application.

## Directory Structure
- `index.html`: Homepage
- `library/`, `discover/`, `collections/`, `genres/`, `anime/`, `4k/`, `awards/`: Section pages
- `movie/`, `tv/`: Sample movie and TV show pages
- `_next/static/chunks/`: Compiled Next.js JavaScript bundles and CSS styles
- `_next/static/media/`: Web fonts (woff2) and embedded icons
- `manifest.webmanifest`: Web App Manifest for PWA installation
- `serve.py`: Built-in local HTTP server with clean routing

## How to Run Locally

You can launch a local HTTP server with Python:

```bash
cd "C:\Users\Karthik Satheesh\.gemini\antigravity\scratch\flicx-website"
python serve.py
```

Then open your browser to:
[http://localhost:8080](http://localhost:8080)
