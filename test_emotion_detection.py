import unittest 
from EmotionDetection import emotion_analyzer 

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_analyzer(self):

        result1 = emotion_analyzer('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')

    


if __name__ == '__main__':
    unittest.main()