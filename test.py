import unittest
from agent import ask_groq

class TestGROQAgent(unittest.TestCase):

    def test_general_query(self):
        response = ask_groq("What is the capital of France?")
        self.assertIn("Paris", response)

    def test_search_query(self):
        response = ask_groq("search: best programming languages")
        self.assertIn("Python", response)  # Adjust based on expected output

if __name__ == "__main__":
    unittest.main()
