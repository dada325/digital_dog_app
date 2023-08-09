import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase Initialization
cred = credentials.Certificate("path_to_service_account_key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Firestore Functions
def insert_message(user_id, sender, message):
    chats_ref = db.collection(u'chats').document(user_id).collection(u'messages')
    chats_ref.add({
        'sender': sender,
        'message': message,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

def get_chat_history(user_id):
    chats_ref = db.collection(u'chats').document(user_id).collection(u'messages').order_by('timestamp')
    chats = chats_ref.stream()
    
    chat_history = [{"sender": chat.to_dict()["sender"], "message": chat.to_dict()["message"]} for chat in chats]
    return chat_history

# Streamlit UI
st.title("Your Cosmo Doggie")

# Display the dog avatar
dog_avatar = "assets/path_to_dog_avatar.png"  # Replace with your path
st.image(dog_avatar, caption="Meet Rover, your digital dog!")

# Assuming you have some mechanism to identify users
user_id = "unique_user_identifier"  # Replace with your user identification mechanism

# Fetch chat history for the user
chat_history = get_chat_history(user_id)

# Display chat history
for chat in chat_history:
    if chat["sender"] == "User":
        st.container().write({"User": chat["message"]}, background_color="lightgray")
    else:
        st.container().write({"Rover": chat["message"]}, background_color="lightblue")

# Input Box and Send Button
user_input = st.text_input("Type your message here...")
if st.button("Send"):
    if user_input:  
        insert_message(user_id, "User", user_input)
        # Here, you'd handle sending the message to the backend/AI model
        # For simplicity, let's add a dummy dog response
        insert_message(user_id, "Rover", "Woof! I'm thinking...")
