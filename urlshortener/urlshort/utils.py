import random
import string


def generate_short_url():
    """
    Generate a random short URL using alphanumeric characters.
    You can customize the length and characters used as needed.
    """
    characters = string.ascii_letters + string.digits
    short_url_length = 6
    short_url = ''.join(random.choice(characters) for _ in range(short_url_length))
    return short_url
