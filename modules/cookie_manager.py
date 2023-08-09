# cookie_manager.py
# This file will handle setting and getting cookies using Flask.


from flask import Flask, request, make_response
import uuid

app = Flask(__name__)
logger = logging.getLogger('digital_dog_app')

@app.route('/set-cookie')
def set_cookie():
    try:
        user_id = str(uuid.uuid4())
        resp = make_response({"user_id": user_id})
        resp.set_cookie('user_id', user_id)
        return resp
    except Exception as e:
        logger.error(f"Error setting cookie: {e}")
        return {"error": "Failed to set cookie."}, 500

@app.route('/get-cookie')
def get_cookie():
    user_id = request.cookies.get('user_id')
    if user_id:
        return {"user_id": user_id}
    else:
        return {"error": "No cookie set."}, 404
