##Ko Chi Omocha##
## A I Pet##

### Overview
This project combines the interactive conversation of a chatbot with the nostalgic charm of a Tamagotchi-like virtual pet. The goal is to create a unique experience where users engage in meaningful dialogue while caring for a digital companion.

### Features

- **Engaging Conversations**: The chatbot can answer questions, provide information, and engage in lively discussions.
- **Virtual Pet Care**: Users interact with and nurture their virtual pet, influencing its growth and development through their actions.

### Purpose

The project aims to blend the best of both worlds, providing users with an AI companion that offers both intellectual stimulation and emotional connection.

17.11.24
Today, we made significant progress on your Kochiomocha AI pet project! Here's a summary of the work we accomplished:

**1. Enhanced Response Logic**

* We significantly expanded the `get_kochiomocha_response()` function in your `response_logic.py` file to include a wider range of responses and make Kochiomocha more conversational.
* We added logic to handle:
    * Greetings with more variations
    * Questions with more specific responses
    * Statements about feelings with empathetic replies
    * Recognition of names
    * Keyword-based responses
    * Synonym-based responses using WordNet
    * Time-related greetings
    * Weather-related comments
    * Activity matching
    * Empathetic responses to emotions

**2. Integrated Machine Learning**

* We incorporated a basic machine learning model (Naive Bayes) into your chatbot to enable it to learn from data and improve its performance over time.
* We used the `dialog.txt` file to provide training data for the model.
* We combined machine learning with rule-based logic to create a more robust response generation system.

**3. Improved Data Handling**

* We refined the code to correctly load and parse the training data from your `dialog.txt` file.
* We added error handling to gracefully handle invalid data formats or empty files.

**4. Addressed Code Issues**

* We fixed the "Undefined name 'token'" error in the name recognition logic.
* We ensured that the `tagged_tokens` variable is correctly used in the response logic.

**5. Expanded Training Data**

* We fleshed out the `dialog.txt` file with more diverse and representative examples of conversations to improve the chatbot's learning and accuracy.
