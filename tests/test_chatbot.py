import unittest
from chatbot import SimpleChatbot

class TestSimpleChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = SimpleChatbot()
    
    def test_greeting(self):
        self.assertEqual(self.bot.detect_intent("hello"), "greeting")
    
    def test_goodbye(self):
        self.assertEqual(self.bot.detect_intent("goodbye"), "goodbye")
    
    def test_thanks(self):
        self.assertEqual(self.bot.detect_intent("thank you"), "thanks")

    def test_response(self):
        response = self.bot.generate_response("hello")
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()
