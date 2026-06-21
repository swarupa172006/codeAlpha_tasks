import pandas as pd
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================
# FAQ DATASET
# =====================================

faq_data = {
    "Question": [
        "What is your return policy?",
        "How can I track my order?",
        "Do you offer international shipping?",
        "How can I contact customer support?",
        "What payment methods are accepted?",
        "How long does delivery take?",
        "Can I cancel my order?",
        "Do you provide refunds?",
        "What are your working hours?",
        "Where are you located?"
    ],

    "Answer": [
        "You can return products within 30 days of purchase.",
        "You can track your order using the tracking ID sent to your email.",
        "Yes, we ship to most countries worldwide.",
        "You can contact customer support via email or phone.",
        "We accept Credit Cards, Debit Cards, and PayPal.",
        "Delivery usually takes 3 to 7 business days.",
        "Yes, orders can be cancelled before shipment.",
        "Yes, refunds are processed after successful return verification.",
        "We are available from 9 AM to 6 PM, Monday to Friday.",
        "Our office is located in Hyderabad, India."
    ]
}

faq_df = pd.DataFrame(faq_data)

# =====================================
# TEXT PREPROCESSING
# =====================================

def preprocess(text):
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    return text

# Preprocess FAQ questions
processed_questions = [
    preprocess(q)
    for q in faq_df["Question"]
]

# =====================================
# TF-IDF MODEL
# =====================================

vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(
    processed_questions
)

# =====================================
# CHATBOT FUNCTION
# =====================================

def get_answer(user_question):

    processed_input = preprocess(user_question)

    user_vector = vectorizer.transform(
        [processed_input]
    )

    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match_index = similarity_scores.argmax()

    confidence = similarity_scores[0][best_match_index]

    if confidence < 0.20:
        return "Sorry, I couldn't find a matching FAQ."

    return faq_df["Answer"][best_match_index]

# =====================================
# CHAT INTERFACE
# =====================================

print("=" * 50)
print("        FAQ CHATBOT")
print("=" * 50)
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = get_answer(user_input)

    print("Bot:", response)
    print()