# ./generate_secret_key.py

import secrets

# 50자의 랜덤 문자열 생성
secret_key = secrets.token_urlsafe(50)
print(secret_key)
