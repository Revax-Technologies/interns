# Sentiment Analyzer Web App

A simple web application that analyzes the sentiment of text using LangChain and Mistral AI. The background color changes based on sentiment:
- **Green** for positive sentiment
- **Red** for negative sentiment  
- **Yellow** for neutral sentiment

## Features

- Real-time sentiment analysis using Mistral AI
- Beautiful, responsive web interface
- Dynamic background color changes
- Smooth animations and transitions
- Error handling and loading states

## Prerequisites

- Python 3.8+
- Mistral AI API key

## Setup Instructions

1. **Clone or navigate to the project directory:**
   ```bash
   cd test
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Set up environment variables:**
   ```bash
   cp env.example .env
   ```
   
   Edit `.env` and add your Mistral AI API key:
   ```
   MISTRAL_API_KEY=your_mistral_api_key_here
   FLASK_ENV=development
   FLASK_DEBUG=True
   PORT=5000
   ```

5. **Get a Mistral AI API key:**
   - Visit [Mistral AI](https://mistral.ai/)
   - Sign up for an account
   - Generate an API key
   - Add it to your `.env` file

6. **Run the application:**
   ```bash
   python app.py
   ```

7. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

1. Type any message in the text area
2. Click "Analyze Sentiment" or press Enter
3. Watch the background color change based on the sentiment:
   - Blue/Green gradient = Positive
   - Red gradient = Negative
   - Yellow/Orange gradient = Neutral

## Project Structure

```
test/
├── app.py              # Flask server with sentiment analysis
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .env              # Your environment variables (not in git)
├── .gitignore        # Git ignore file
├── README.md         # This file
├── templates/
│   └── index.html    # Main web page
└── static/
    └── style.css     # Styling and animations
```

## Dependencies

- **Flask**: Web framework
- **LangChain**: LLM framework
- **LangChain-Mistral**: Mistral integration for LangChain
- **Mistral AI**: AI model for sentiment analysis
- **python-dotenv**: Environment variable management
- **gunicorn**: Production WSGI server

## Troubleshooting

1. **API Key Issues**: Make sure your Mistral AI API key is valid and properly set in the `.env` file
2. **Port Conflicts**: Change the PORT in `.env` if 5000 is already in use
3. **Dependencies**: Make sure you're in the virtual environment when installing packages

## Production Deployment

For production deployment, you can use gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## License

This project is for demonstration purposes. Please ensure you comply with Mistral AI's terms of service when using their API.
