import os
from flask import Flask, render_template, request, jsonify
from langchain_mistralai import ChatMistralAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Mistral model
mistral_api_key = os.getenv('MISTRAL_API_KEY')
if not mistral_api_key:
    raise ValueError("MISTRAL_API_KEY not found in environment variables")

llm = ChatMistralAI(
    mistral_api_key=mistral_api_key,
    model="mistral-small",
    temperature=0.1
)

def analyze_sentiment(text):
    """Analyze sentiment using Mistral via LangChain"""
    try:
        prompt = f"""
        Analyze the sentiment of the following text and respond with ONLY one word: either "positive", "negative", or "neutral".
        
        Text: "{text}"
        
        Response:"""
        
        message = HumanMessage(content=prompt)
        response = llm.invoke([message])
        
        sentiment = response.content.strip().lower()
        
        # Ensure we only return valid sentiments
        if sentiment in ['positive', 'negative', 'neutral']:
            return sentiment
        else:
            # Default to neutral if response is unclear
            return 'neutral'
            
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'neutral'

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze sentiment of submitted text"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        sentiment = analyze_sentiment(text)
        
        return jsonify({
            'sentiment': sentiment,
            'text': text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
