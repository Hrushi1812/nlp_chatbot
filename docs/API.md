# API Documentation

## SimpleChatbot Class

### Methods

#### `__init__(self)`
Initialize the chatbot with predefined responses and NLP components.

#### `detect_intent(self, user_input)`
Detect the intent of user input using pattern matching.
- **Parameters**: `user_input` (str) - User's message
- **Returns**: Intent string

#### `generate_response(self, user_input)`
Generate appropriate response based on user input.
- **Parameters**: `user_input` (str) - User's message
- **Returns**: Response string

#### `chat(self)`
Main chat loop for interactive conversation.
