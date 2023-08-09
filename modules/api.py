# api.py
# This file will handle interactions with the OpenAI API.

import openai
import logging

openai.api_key = 'YOUR_OPENAI_API_KEY'

logger = logging.getLogger('digital_dog_app')

def get_dog_response(user_input, dog_name):
    try:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=f"You are a dog named {dog_name}. {user_input}. How would you respond?",
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        logger.error(f"Error fetching response from OpenAI: {e}")
        return "Woof! (I encountered an error, please try again later.)"
