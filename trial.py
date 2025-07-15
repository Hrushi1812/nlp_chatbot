import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class SimpleChatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # Predefined responses for different intents
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Greetings! How are you doing?"
            ],
            'goodbye': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice talking to you!",
                "Farewell! Come back anytime!"
            ],
            'thanks': [
                "You're welcome! Happy to help!",
                "No problem at all!",
                "Glad I could assist you!",
                "Anytime! That's what I'm here for!"
            ],
            'name': [
                "I'm a simple chatbot created to help you!",
                "You can call me ChatBot! I'm here to assist you.",
                "I'm your friendly AI assistant!"
            ],
            'weather': [
                "I don't have access to real-time weather data, but you can check a weather app or website!",
                "For weather information, I'd recommend checking your local weather service.",
                "I wish I could tell you about the weather, but I don't have that capability yet!"
            ],
            'time': [
                "I don't have access to real-time clock data. You can check your device's clock!",
                "I can't tell you the current time, but your computer or phone can!"
            ],
            'help': [
                "I can chat with you about various topics! Try asking me about myself, saying hello, or just having a conversation.",
                "I'm here to chat! You can ask me questions, tell me about yourself, or just talk.",
                "I can help with basic conversation. Feel free to ask me anything!"
            ],
            'default': [
                "I'm not sure I understand. Can you rephrase that?",
                "That's interesting! Can you tell me more?",
                "I'm still learning. Could you ask that differently?",
                "I'm not quite sure about that. What else would you like to talk about?"
            ]
        }
        
        # Pattern matching for intents
        self.intent_patterns = {
            'greeting': [
                r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b',
                r'\b(howdy|hiya|sup)\b'
            ],
            'goodbye': [
                r'\b(bye|goodbye|see you|farewell|take care|catch you later)\b',
                r'\b(gotta go|leaving|exit|quit)\b'
            ],
            'thanks': [
                r'\b(thank you|thanks|thank|appreciate)\b',
                r'\b(grateful|cheers)\b'
            ],
            'name': [
                r'\b(what is your name|who are you|what are you called)\b',
                r'\b(your name|introduce yourself)\b'
            ],
            'weather': [
                r'\b(weather|temperature|rain|sunny|cloudy|forecast)\b',
                r'\b(how is the weather|what\'s the weather like)\b'
            ],
            'time': [
                r'\b(what time|current time|time is it)\b',
                r'\b(clock|hour|minute)\b'
            ],
            'help': [
                r'\b(help|assist|what can you do|capabilities)\b',
                r'\b(how to use|instructions|guide)\b'
            ]
        }
        
        # Knowledge base for similarity matching
        self.knowledge_base = [
            "I am a chatbot designed to have conversations with users.",
            "I use natural language processing to understand and respond to messages.",
            "I can help with basic conversations and answer simple questions.",
            "I was created using Python and NLTK library.",
            "I enjoy chatting with people and learning from conversations.",
            "I can recognize different types of messages like greetings and questions.",
            "I'm constantly trying to improve my responses based on what you say.",
            "I hope you find our conversation helpful and engaging."
        ]
        
        # Initialize TF-IDF vectorizer for similarity matching
        self.vectorizer = TfidfVectorizer(tokenizer=self.preprocess_text, lowercase=True)
        self.knowledge_vectors = self.vectorizer.fit_transform(self.knowledge_base)
    
    def preprocess_text(self, text):
        """Preprocess text for NLP operations"""
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and lemmatize
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens 
                 if token not in self.stop_words and token.isalpha()]
        
        return tokens
    
    def detect_intent(self, user_input):
        """Detect the intent of user input using pattern matching"""
        user_input = user_input.lower()
        
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    return intent
        
        return 'default'
    
    def get_similarity_response(self, user_input):
        """Get response based on similarity with knowledge base"""
        # Transform user input to vector
        user_vector = self.vectorizer.transform([user_input])
        
        # Calculate similarity with knowledge base
        similarities = cosine_similarity(user_vector, self.knowledge_vectors).flatten()
        
        # If similarity is high enough, return a relevant response
        max_similarity = np.max(similarities)
        if max_similarity > 0.1:  # Threshold for similarity
            most_similar_idx = np.argmax(similarities)
            return f"Based on what you said, I think you might be interested to know: {self.knowledge_base[most_similar_idx]}"
        
        return None
    
    def generate_response(self, user_input):
        """Generate appropriate response based on user input"""
        # First, try intent detection
        intent = self.detect_intent(user_input)
        
        if intent != 'default':
            return random.choice(self.responses[intent])
        
        # If no specific intent, try similarity matching
        similarity_response = self.get_similarity_response(user_input)
        if similarity_response:
            return similarity_response
        
        # Fall back to default responses
        return random.choice(self.responses['default'])
    
    def chat(self):
        """Main chat loop"""
        print("🤖 ChatBot: Hello! I'm your friendly chatbot. Type 'quit' to exit.")
        print("=" * 50)
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'stop']:
                print("🤖 ChatBot: Goodbye! Thanks for chatting with me!")
                break
            
            if not user_input:
                continue
            
            response = self.generate_response(user_input)
            print(f"🤖 ChatBot: {response}")
            print("-" * 30)

# Enhanced version with conversation context
class AdvancedChatbot(SimpleChatbot):
    def __init__(self):
        super().__init__()
        self.conversation_history = []
        self.user_name = None
        self.context_responses = {
            'name_asked': [
                "Nice to meet you, {}! How can I help you today?",
                "Hello {}! That's a lovely name. What would you like to chat about?",
                "Great to meet you, {}! I'm excited to talk with you."
            ],
            'repeat_greeting': [
                "Hello again! What else can I help you with?",
                "Hi there! Is there something specific you'd like to discuss?",
                "Hey! What's on your mind now?"
            ]
        }
    
    def extract_name(self, user_input):
        """Extract user's name from input"""
        patterns = [
            r"my name is (\w+)",
            r"i'm (\w+)",
            r"i am (\w+)",
            r"call me (\w+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                return match.group(1).capitalize()
        return None
    
    def generate_response(self, user_input):
        """Enhanced response generation with context"""
        # Store conversation history
        self.conversation_history.append(user_input)
        
        # Check if user is sharing their name
        name = self.extract_name(user_input)
        if name:
            self.user_name = name
            return random.choice(self.context_responses['name_asked']).format(name)
        
        # Check for repeated greetings
        if len(self.conversation_history) > 1:
            recent_intents = [self.detect_intent(msg) for msg in self.conversation_history[-3:]]
            if recent_intents.count('greeting') > 1:
                return random.choice(self.context_responses['repeat_greeting'])
        
        # Use user's name in responses if available
        response = super().generate_response(user_input)
        if self.user_name and random.random() < 0.3:  # 30% chance to use name
            response = f"{self.user_name}, {response.lower()}"
        
        return response

def main():
    print("Choose chatbot version:")
    print("1. Simple Chatbot")
    print("2. Advanced Chatbot (with context)")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        bot = AdvancedChatbot()
        print("\n🚀 Starting Advanced Chatbot with context awareness...")
    else:
        bot = SimpleChatbot()
        print("\n🚀 Starting Simple Chatbot...")
    
    bot.chat()

if __name__ == "__main__":
    main()