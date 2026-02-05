from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class EmotionAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text: str) -> str:
        """
        Analyzes the sentiment of the text and returns an emotional category.
        Categories: 'positive', 'negative', 'neutral'
        """
        if not text or not text.strip():
            return "neutral"

        scores = self.analyzer.polarity_scores(text)
        compound_score = scores['compound']
        # VADER compound score ranges from -1 to 1.
        # Check for Granular Emotions first (Heuristics)
        
        # 1. Surprised: High intensity, ends with '!'
        if "!" in text and (compound_score > 0.3 or compound_score < -0.3):
             return "surprised"

        # 2. Inquisitive: Ends with '?' and not strongly negative
        if "?" in text and compound_score > -0.2:
             return "inquisitive"
             
        # 3. Concerned: Negative sentiment + worry keywords
        worry_words = ["worry", "concerned", "afraid", "scared", "anxious", "trouble", "help"]
        if compound_score < -0.1 and any(word in text.lower() for word in worry_words):
             return "concerned"

        # Base Categories
        if compound_score >= 0.05:
            return "positive"
        elif compound_score <= -0.05:
            return "negative"
        else:
            return "neutral"

    def get_details(self, text: str) -> dict:
        """
        Returns full detailed scores.
        """
        return self.analyzer.polarity_scores(text)
