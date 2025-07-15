import random
import json
import re


class SimpleChatbot:
    def __init__(self):
        with open('config/responses.json') as f:
            self.responses = json.load(f)

    def detect_intent(self, user_input):
        user_input = user_input.lower()
        if re.search(r'\b(hello|hi|hey)\b', user_input):
            return "greeting"
        elif re.search(r'\b(bye|goodbye|see you)\b', user_input):
                return "goodbye"
        elif re.search(r'\b(thank|thanks|thank you)\b', user_input):
                return "thanks"
        elif re.search(r'\b(my name is|i am)\b', user_input):
                return "name_intent"
        elif "name" in user_input:
                return "name"
        elif "help" in user_input or "can you" in user_input:
                return "help"
        else:
                return "default"
    def extract_name(self, user_input):
        match = re.search(r'\b(?:my name is|i am) (\w+)', user_input, re.IGNORECASE)
        if match:
            return match.group(1)
        return None


    def generate_response(self, user_input):
        intent = self.detect_intent(user_input)
        if intent == "name_intent":
                name = self.extract_name(user_input)
                if name:
                        return f"Nice to meet you, {name}! How can I help you today?"
        return random.choice(self.responses.get(intent, self.responses["default"]))


    def chat(self):
        print("🤖 ChatBot: Hello! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['bye', 'exit', 'quit']:
                print("🤖 ChatBot:", random.choice(self.responses["goodbye"]))
                break
            print("🤖 ChatBot:", self.generate_response(user_input))


if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()
