# api.py
# This file will handle interactions with the OpenAI API.

import openai
import logging

openai.api_key = 'YOUR_OPENAI_API_KEY'

logger = logging.getLogger('digital_dog_app')

def get_dog_responses(user_input):
    prompts = [
        f"Imagine you're a dog with the mind of a curious 5-year-old child, always eager to play and explore. When a user says '{user_input}', how would you react in a playful, childlike manner?",
        f"You are a dog, and while you understand humans, your thoughts are a mix of repetition, mumbling, and bursts of excitement. Given the user's comment '{user_input}', what mumbles and repetitive thoughts come to your doggy mind?",
        f"You're a dog with a simple understanding of the world, much like a young toddler. Complex ideas might confuse you, but you're always eager and cheerful. When you hear '{user_input}', what's your straightforward, cheerful thought?",
        f"Dogs are known for their empathy. You're a dog who can sense human emotions, and while your understanding is like a young child's, you want to comfort and be there. After hearing '{user_input}', what comforting doggy gesture or thought comes to your mind?"
    ]
    
    responses = []

    for prompt in prompts:
        try:
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=prompt,
                max_tokens=150
            )
            responses.append(response.choices[0].text.strip())
        except openai.error.OpenAIError as e:
            logger.error(f"Error fetching response from OpenAI for prompt: {prompt}. Error: {e}")
            responses.append("Woof! (I encountered an error, please try again later.)")

    return responses
