import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector_anger(self):
        result = emotion_detector("I am very angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_emotion_detector_disgust(self):
        result = emotion_detector("I am disgusted")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_emotion_detector_fear(self):
        result = emotion_detector("I am really afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_emotion_detector_joy(self):
        result = emotion_detector("I am very happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_emotion_detector_sadness(self):
        result = emotion_detector("I am very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
