import jwt

my_secret = 'lausgdiusafisudevfywvf'
def create_token(id,username,email):

    payload_data = {
        "sub": id,
        "username": username,
        "email": email
    }
    token = jwt.encode(
        payload=payload_data,
        key=my_secret
    )
    return token


def decode_token(auth_header):
    token = auth_header.split(" ")[1]
    decoded_token = jwt.decode(token, my_secret, algorithms=["HS256"])
    return decoded_token.get('sub')