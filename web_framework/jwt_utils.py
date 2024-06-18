import datetime
import json
import base64
import hmac
import hashlib

SECRET_KEY = "secret_key"


def base64url_decode(data):
    padding = '=' * (4 - len(data) % 4)
    return base64.urlsafe_b64decode(data + padding).decode('utf-8')


def verify_jwt(token):
    try:
        jwt_header_encoded, jwt_payload_encoded, jwt_signature = token.split('.')

        # Recreate the signature
        expected_signature = sign(jwt_header_encoded, jwt_payload_encoded)

        # Compare the signatures
        if hmac.compare_digest(jwt_signature, expected_signature):
            # Decode the payload and return
            payload_json = base64url_decode(jwt_payload_encoded)
            return json.loads(payload_json)
        else:
            return None
    except Exception as e:
        print(f"Verification failed: {e}")
        return None


def base64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')


def generate_jwt(alg, claims):
    jwt_header = header(alg)
    jwt_payload = payload(claims)

    jwt_header_encoded = base64url_encode(jwt_header.encode('utf-8'))
    jwt_payload_encoded = base64url_encode(jwt_payload.encode('utf-8'))

    signature = sign(jwt_header_encoded, jwt_payload_encoded)

    return f"{jwt_header_encoded}.{jwt_payload_encoded}.{signature}"


def header(alg):
    return json.dumps({
        "alg": alg,
        "typ": "JWT"
    })


def payload(claims):
    claims["iat"] = datetime.datetime(2024, 6, 19).timestamp()
    return json.dumps(claims)


def sign(jwt_header_encoded, jwt_payload_encoded):
    message = f"{jwt_header_encoded}.{jwt_payload_encoded}"
    signature = hmac.new(SECRET_KEY.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).digest()
    return base64url_encode(signature)

