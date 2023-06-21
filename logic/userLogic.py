from helpers.jwtFile import create_token
import bcrypt


def registerFunction(username, email, password, connection):
    cursor = connection.cursor()
    checkIfEmailIsTaken = "SELECT * FROM users WHERE email = %s"
    cursor.execute(checkIfEmailIsTaken, (email,))
    result = cursor.fetchall()

    if result:
        return {"error": "User already registered with this email."}

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, hashed_password))
    connection.commit()
    last_insert_id = cursor.lastrowid
    token = create_token(last_insert_id, username, email)
    return token



def loginFunction(email, cursor, password):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "0"
    id = rows[0][0]
    savedUsername = rows[0][1]
    savedEmail = rows[0][2]
    savedPassword = rows[0][3]
    if savedEmail == email and bcrypt.checkpw(password.encode('utf-8'), savedPassword.encode('utf-8')):
        token = create_token(id, savedUsername, savedEmail)
        return token
    else:
        return "0"
