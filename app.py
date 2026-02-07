import streamlit as st
import pickle
import random

# Load model and vectorizer
model = pickle.load(open("model/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

st.set_page_config(page_title="Fatih AI", page_icon="????")
st.title("Fatih AI Demo - An AI-driven Mental Support Bot")
st.write("This AI is still under development and it can make mistakes. We are continuously working to improve its accuracy and performance.")

# Multiple responses for variety
responses = {
    "Frustration": [
        'Calm down, brother. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Sit down, take a breathe. Make wudu, because anger is from fire and water cools fire. Shaytan loves when we lose control. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built.',

        "Calm down, brother. I understand that you are very angry. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Sit down. Take a breath. Drink water. Make wudu, because anger is from fire and water cools fire. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan wins when we lose control.",

        'It’s okay to feel angry sometimes. But, don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Sit down, take a breathe. Make wudu, because anger is from fire and water cools fire. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan loves when we lose control.',

        "Sit down. Take a breath with me. Drink water. Make wudu, because anger is from fire and water cools fire. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan wins when we lose control."
    ],

    "Anger": [
        'Calm down, brother. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Sit down, take a breathe. Make wudu, because anger is from fire and water cools fire. Shaytan loves when we lose control. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built.',

        "Calm down, brother. I understand that you are very angry. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Sit down. Take a breath. Drink water. Make wudu, because anger is from fire and water cools fire. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan wins when we lose control.",

        'It’s okay to feel angry sometimes. But, don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Sit down, take a breathe. Make wudu, because anger is from fire and water cools fire. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan loves when we lose control.',

        "Sit down. Take a breath with me. Drink water. Make wudu, because anger is from fire and water cools fire. Don’t make any decisions in anger. Words spoken in anger can destroy what years of effort built. Prophet (SM) said, “The strong person is not the one who overpowers others, but the one who controls himself when angry.” Shaytan wins when we lose control."
    ],

    "Fear": [
        "Don't be afraid, brother. You are not walking alone. Allah is with you. Nothing can touch you unless He allows it and nothing can protect you except Him. Say: HasbiAllahu la ilaha illa Huwa — Allah is enough for me, there is no god but Him.",
        "Allah is with you. Nothing can touch you unless He allows it and nothing can protect you except Him. Say: HasbiAllahu la ilaha illa Huwa — Allah is enough for me, there is no god but Him. Don't be afraid, brother. You are not walking alone.",
        "Nothing can touch you unless Allah allows it and nothing can protect you except Him. Say: HasbiAllahu la ilaha illa Huwa — Allah is enough for me, there is no god but Him. Don't be afraid, brother. You are not walking alone. Allah is with you.",
        "Don't be afraid, brother. Say: HasbiAllahu la ilaha illa Huwa — Allah is enough for me, there is no god but Him. You are not walking alone. Allah is with you. Nothing can touch you unless He allows it and nothing can protect you except Him."
    ],

    "Joy": [
        "That’s wonderful to hear. Your happiness is a gift from Allah. Say Alhamdulillah and use this joy in a way that pleases Him, because gratitude increases blessings. Share it. Lift someone else with it.",
        "Say Alhamdulillah, brother. Your happiness is a gift from Allah. Use this joy in a way that pleases Him, because gratitude increases blessings. Share it. Lift someone else with it.",
        "Praise be to Allah. Say Alhamdulillah. Your happiness is a gift from Allah. Use this joy in a way that pleases Him, because gratitude increases blessings. Share it. Lift someone else with it.",
        "Don't forget to say Alhamdulillah. Praise be to Allah. Your happiness is a gift from Allah. Use this joy in a way that pleases Him, because gratitude increases blessings. Share it. Lift someone else with it."
    ],

    "Love": [
        "Love for the sake of Allah is the purest love. If you love someone, love them with honesty, respect, and dua — not with sin.",
        "Love for the sake of Allah is the purest love. If you love someone, love them with honesty, respect, and dua — not with sin.",
        "Love for the sake of Allah is the purest love. If you love someone, love them with honesty, respect, and dua — not with sin.",
        "Love for the sake of Allah is the purest love. If you love someone, love them with honesty, respect, and dua — not with sin."
    ],

    "Sadness": [
        'Don’t be upset, brother. Allah is with you. He sees your pain. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'In Quran, Allah SWT says, "Indeed, there is ease with hardship." Don’t be upset, brother. Allah is with you. He sees your pain. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by."',

        'Hold your head up, brother. Don’t be upset, brother. Allah is with you. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'Hard times create strong men. Hold your head up, brother. Don’t be upset. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah SWT says in Quran, "Indeed what is to come will be better for you than what has gone by."'
    ],

    "Loneliness": [
        'Don’t be upset, brother. Allah is with you. He sees your pain. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'In Quran, Allah SWT says, "Indeed, there is ease with hardship." Don’t be upset, brother. Allah is with you. He sees your pain. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by."',

        'Hold your head up, brother. Don’t be upset, brother. Allah is with you. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'Hard times create strong men. Hold your head up, brother. Don’t be upset. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah SWT says in Quran, "Indeed what is to come will be better for you than what has gone by."'
    ],

    "Overwhelmed": [
        'Don’t be upset, brother. Allah is with you. He sees your pain. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'In Quran, Allah SWT says, "Indeed, there is ease with hardship." Don’t be upset, brother. Allah is with you. He sees your pain. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by."',

        'Hold your head up, brother. Don’t be upset, brother. Allah is with you. Allah SWT says in Quran, "Indeed, there is ease with hardship." This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah says, "Indeed what is to come will be better for you than what has gone by." Keep in mind that hard times create strong men.',

        'Hard times create strong men. Hold your head up, brother. Don’t be upset. This pain is not forever. Keep walking, keep fighting. Keep praying to Almighty Allah. The night is always followed by Fajr. Allah SWT says in Quran, "Indeed what is to come will be better for you than what has gone by."'
    ],

    "Hopeful": [
        "Nothing happens without Allah’s will. When something unexpected comes, say SubhanAllah and trust that Allah’s plan is better than what we imagine.",
        "When something unexpected comes, say SubhanAllah. Nothing happens without Allah’s will. Trust that Allah’s plan is better than what we imagine.",
        "Nothing happens without Allah’s will. When something unexpected comes, say SubhanAllah and trust that Allah’s plan is better than what we imagine.",
        "When something unexpected comes, say SubhanAllah. Nothing happens without Allah’s will. Trust that Allah’s plan is better than what we imagine."
    ],

    "Grateful": [
        "That's Beautiful",
        "That's Beautiful",
        "That's Beautiful",
        "That's Beautiful"
    ],

    "Surprise": [
        "Nothing happens without Allah’s will. When something unexpected comes, say SubhanAllah and trust that Allah’s plan is better than what we imagine.",
        "When something unexpected comes, say SubhanAllah. Nothing happens without Allah’s will. Trust that Allah’s plan is better than what we imagine.",
        "Nothing happens without Allah’s will. When something unexpected comes, say SubhanAllah and trust that Allah’s plan is better than what we imagine.",
        "When something unexpected comes, say SubhanAllah. Nothing happens without Allah’s will. Trust that Allah’s plan is better than what we imagine."
    ]
}
# Session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Type your message:")

send = st.button("Send")

if send and user_input:
    X = vectorizer.transform([user_input])
    emotion = model.predict(X)[0]
    bot_reply = random.choice(responses.get(emotion, ["I'm here for you. Tell me more."]))

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_reply))

# Display chat history
for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")
