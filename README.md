# 🤖 NLP Chatbot

A simple yet powerful chatbot built with Python and NLTK that can engage in natural conversations with users.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![NLTK](https://img.shields.io/badge/nltk-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Features

- **Natural Language Processing**: Uses NLTK for text preprocessing and understanding
- **Intent Recognition**: Pattern-based intent detection for various conversation types
- **Similarity Matching**: TF-IDF vectors and cosine similarity for intelligent responses
- **Context Awareness**: Advanced version remembers conversation context and user names
- **Extensible Design**: Easy to add new intents, responses, and capabilities

## 📋 Requirements

- Python 3.6+
- NLTK
- scikit-learn
- numpy

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Hrushi1812/nlp_chatbot.git
cd nlp_chatbot
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the chatbot:**
```bash
python chatbot.py
```

## 💬 Usage

The chatbot offers two versions:

### Simple Chatbot
Basic pattern matching and predefined responses.

### Advanced Chatbot
Includes conversation context, user name recognition, and enhanced interactions.

### Example Conversation
```
You: Hello there!
🤖 ChatBot: Hi there! What's on your mind?

You: My name is Alex
🤖 ChatBot: Nice to meet you, Alex! How can I help you today?

You: What can you do?
🤖 ChatBot: I can chat with you about various topics! Try asking me about myself, saying hello, or just having a conversation.
```

## 🔧 Configuration

Modify responses and intents in `config/responses.json` to customize the chatbot's behavior.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)
- [Changelog](docs/CHANGELOG.md)

## 🧪 Testing

Run tests with:
```bash
python -m pytest tests/
```

## 🎯 Roadmap

- [ ] Add sentiment analysis
- [ ] Implement voice recognition
- [ ] Create web interface
- [ ] Add database integration
- [ ] Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Hrushikesh Peddi - Initial work - [GitHub](https://github.com/Hrushi1812)

## 🙏 Acknowledgments

- NLTK team for the amazing NLP library
- scikit-learn for machine learning utilities
- The open-source community for inspiration

## 📞 Support

If you have any questions or issues, please open an issue on GitHub or contact [hrushikesh1812@gmail.com](mailto:hrushikesh1812@gmail.com).
