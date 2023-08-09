# database.py
# function to communicate with GCP database, 


from google.cloud import firestore

db = firestore.Client()
logger = logging.getLogger('digital_dog_app')

def save_conversation(user_id, user_input, dog_response):
    try:
        conversations_ref = db.collection('conversations')
        doc_ref = conversations_ref.document(user_id)
        
        # Fetch existing conversation or initialize new
        doc = doc_ref.get()
        if doc.exists:
            conversation = doc.to_dict().get('history', [])
        else:
            conversation = []

        # Add new interaction and save
        conversation.append({"user": user_input, "dog": dog_response})
        doc_ref.set({"history": conversation})
    except Exception as e:
        logger.error(f"Error saving conversation for user {user_id}: {e}")

def fetch_conversation(user_id):
    try:
        conversations_ref = db.collection('conversations')
        doc_ref = conversations_ref.document(user_id)
        doc = doc_ref.get()
        
        if doc.exists:
            return doc.to_dict().get('history', [])
        return []
    except Exception as e:
        logger.error(f"Error fetching conversation for user {user_id}: {e}")
        return []
