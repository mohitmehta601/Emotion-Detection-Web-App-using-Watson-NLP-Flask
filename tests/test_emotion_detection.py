import unittest
from emotion_detection import emotion_predictor

class TestEmotionDetection(unittest.TestCase):
    def test_valid_text(self):
        result = emotion_predictor("I am so happy today!")
        self.assertIn("emotion", result)

    def test_empty_text(self):
        result = emotion_predictor("")
        self.assertEqual(result["error"], "Input text is empty.")
