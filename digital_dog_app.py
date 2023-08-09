# digital_dog_app.py
#
#
# A base implementation using streamlit 
#




import streamlit as st
from modules import api, database, cookie_manager, utilities
import logging

# Initialize logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('digital_dog_app')

# Title & Introduction
st.title("Digital Dog Companion")

# Check if user has a cookie already (this is a pseudo-function, in reality, you'd have to manage cookies differently with Streamlit)
user_id = cookie_manager.get_cookie()

if not user_id:
    user_id = cookie_manager.set_cookie()
    st.write("Welcome to the Digital Dog Companion! Let's get started.")
    dog_avatar = utilities.assign_dog_avatar()
    dog_name = st.text_input("What would you like to name your dog?")
    if dog_name:
        # Save user details to the database
        database.save_user_data(user_id, dog_name, dog_avatar)
else:
    user_data = database.get_user_data(user_id)
    dog_name = user_data['dog_name']
    dog_avatar = user_data['dog_avatar']

# Display Dog Avatar and Name
st.image(dog_avatar, caption=dog_name, use_column_width=True)

# Display previous conversations
previous_conversations = database.fetch_conversation(user_id)
for interaction in previous_conversations:
    st.write(f"You: {interaction['user']}")
    st.write(f"{dog_name}: {interaction['dog']}")

# Chat Interface
user_input = st.text_input("Talk to your dog:")
if user_input:
    dog_response = api.get_dog_response(user_input, dog_name)
    database.save_conversation(user_id, user_input, dog_response)
    st.write(f"You: {user_input}")
    st.write(f"{dog_name}: {dog_response}")

    # Optionally collect feedback
    feedback = st.text_area("Feedback on the response:", "Type feedback here...")
    if feedback:
        # Save feedback for analysis
        database.save_feedback(user_input, dog_response, feedback)

# Footer & Additional Information
st.write("---")
st.write("Digital Dog Companion - An Interactive Chatbot")
