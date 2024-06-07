FILEPATH = "thought.txt"
from textblob import TextBlob

def write_thought(thought, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.write(thought)

def read_thought(file_path=FILEPATH):
    try:
        with open(file_path, 'r') as file:
            thought=file.read()
    except FileNotFoundError:
        thought=""
    return thought

def get_sentiment(thought):
    analysis=TextBlob(thought)
    sentiment=analysis.sentiment.polarity

    if sentiment>0:
        return "Positive"
    elif sentiment<0:
        return "Negative"
    else:
        return "Neutral"