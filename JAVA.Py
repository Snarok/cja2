# NOMBRE_DEL_DUEÑO_CODIGO: JohnSmith123
# TEMATICA_DEL_CODIGO: Análisis de sentimientos utilizando procesamiento de lenguaje natural (NLP)
# IEM_ESCUELA_NORMAL_PASTO: IEM Normal de Pasto
# CURSO: Ciencia de Datos

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

text = "This movie is really good. I enjoyed it a lot!"
sentiment = analyze_sentiment(text)
print("Sentiment:", sentiment)
