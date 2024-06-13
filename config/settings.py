# config/settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY').encode()
print(SECRET_KEY)
