# utilities.py
# utility functions includes : random dogs name, random dog avatar etc.

import random
logger = logging.getLogger('digital_dog_app')

def assign_dog_avatar():
    try:
        # Assuming you have a list of dog avatar file paths
        dog_avatars = ['assets/dog1.png', 'assets/dog2.png', ...]  # Populate with your list
        return random.choice(dog_avatars)
    except Exception as e:
        logger.error(f"Error assigning dog avatar: {e}")
        return "assets/default_dog.png"  # Return a default avatar in case of error
