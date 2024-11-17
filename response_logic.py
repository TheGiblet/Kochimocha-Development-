# response_logic.py

import nltk
import random
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Download required NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# --- Machine Learning Integration ---

# Load and prepare training data from dialog.txt
data = []
with open("dialog.txt", "r") as f:
    for line in f:
        try:
            text, label = line.strip().split(",")  # Split by comma
            data.append({"text": text, "label": label})
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")  # Print the invalid line

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# Check if there are any texts and labels after loading the data
if texts and labels:
    # Create and train the model
    model = make_pipeline(TfidfVectorizer(stop_words=None), MultinomialNB())  # No stop words
    model.fit(texts, labels)
else:
    print("Error: No valid training data found in dialog.txt. "
            "Please check the file format and contents.")


def get_kochiomocha_response(user_input):
    # --- Machine Learning for Intent Recognition ---
    if texts and labels:  # Only predict intent if the model was trained
        predicted_intent = model.predict([user_input])[0]

        if predicted_intent == "greeting":
            greeting_responses = [
                "Hello there! I'm Kochiomocha!",
                "Hi! How can I help you today?",
                "Hey! What's up?",
                "Greetings! It's nice to hear from you."
            ]
            return random.choice(greeting_responses)

        elif predicted_intent == "question":
            question_responses = [
                "That's an interesting question! I'm still learning about that.",
                "Hmm, let me think about that...",
                "I'm not sure I know the answer to that yet.",
                "I'm still under development, but I'm learning new things every day!"
            ]
            return random.choice(question_responses)

        elif predicted_intent == "feeling":
            # You can add more specific responses based on the feeling here later
            feeling_responses = [
                "Tell me more about how you're feeling.",
                "I'm here to listen if you want to talk.",
                "It's okay to express your emotions."
            ]
            return random.choice(feeling_responses)

    # --- Rule-based responses (can be combined with ML) ---

    tokens = nltk.word_tokenize(user_input)
    tagged_tokens = nltk.pos_tag(tokens)  # This line is included

    # Check for names 
    if any(token[1] == "NNP" for token in tagged_tokens):
        for token, tag in tagged_tokens:  # Iterate through the tagged tokens
            if tag == "NNP":
                return f"I like the name {token}!"

    # Check for time-related words
    time_words = ["morning", "afternoon", "evening", "night", "time"]
    if any(word in user_input.lower() for word in time_words):
        current_time = datetime.datetime.now().time()
        if current_time.hour < 12:
            return "Good morning! It's a beautiful day."
        elif current_time.hour < 18:
            return "Good afternoon! How's your day going?"
        else:
            return "Good evening! Time to relax and unwind."

    # Check for weather-related words
    weather_words = ["weather", "rain", "sun", "cloud", "snow"]
    if any(word in user_input.lower() for word in weather_words):
        weather_responses = [
            "The weather seems nice today!",
            "I hope it's sunny!",
            "I wonder if it will rain?"
        ]
        return random.choice(weather_responses)

    # Check for activities
    activities = ["play", "read", "walk", "eat", "sleep", "draw", "sing", "dance", "code", "write"]
    for token in nltk.word_tokenize(user_input):
        if token.lower() in activities:
            return f"I like to {token.lower()} too!"

    # Check for emotions and provide empathetic responses (can be improved with sentiment analysis)
    emotions = {
        "happy": ["That's great to hear!", "I'm glad you're happy!", "Yay! 😊"],
        "sad": ["I'm sorry to hear that.", "Is there anything I can do to cheer you up?", "😔"],
        "angry": ["Take a deep breath and try to stay calm.", "It's okay to feel angry sometimes.", "😡"],
        # ... add more emotions
    }
    for emotion in emotions:
        if emotion in user_input.lower():
            return random.choice(emotions[emotion])

    # ... (Add even more response logic as needed) ...

    # Default response
    default_responses = [
        "I'm still learning and growing!",
        "Tell me more!",
        "That's interesting!",
        "Hmm, I'm not sure I understand.",
        "I'm still processing that."
    ]
    return random.choice(default_responses)