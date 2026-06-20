import random
import string


def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def get_register_payload(email=None, password=None, name=None):
    return {
        "email": email or f"test_{generate_random_string()}@ya.com",
        "password": password or generate_random_string(),
        "name": name or generate_random_string()
    }


def get_login_payload(email, password):
    return {
        "email": email,
        "password": password
    }


def get_payload_without_field(field_to_remove):
    payload = get_register_payload()
    del payload[field_to_remove]
    return payload