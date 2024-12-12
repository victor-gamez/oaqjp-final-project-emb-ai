from EmotionDetection.emotion_detection import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for joy
        result_1 = sentiment_analyzer('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], ['joy'])
    
        # Test case for anger
        result_2 = sentiment_analyzer('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], ['anger'])
    
        # Test case for disgust
        result_3 = sentiment_analyzer('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], ['disgust'])

        # Test case for sadness
        result_4 = sentiment_analyzer('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], ['sadness'])

        # Test case for fear
        result_5 = sentiment_analyzer('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], ['fear'])
    
    
unittest.main()