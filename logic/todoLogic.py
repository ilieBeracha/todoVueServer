def addTodo(connection, title, description, status, date, userId, label):
    cursor = connection.cursor()

    checkIfLabelExistQuery = "SELECT * FROM labels WHERE userId = %s AND labelName = %s"
    cursor.execute(checkIfLabelExistQuery, (userId, label))
    result = cursor.fetchall()

    if len(result) == 0:
        insertLabelQuery = "INSERT INTO labels (userId, labelName) VALUES (%s, %s)"
        cursor.execute(insertLabelQuery, (userId, label))
        connection.commit()
        labelId = cursor.lastrowid
    else:
        labelId = result[0][0]

    insertTodoQuery = "INSERT INTO todos (title, description, status, date, userId, labelId) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insertTodoQuery, (title, description, status, date, userId, labelId))
    connection.commit()
    return {"message": "Todo added successfully"}


def getTodos(connection, userId,status):
    cursor = connection.cursor()
    query = f"SELECT * FROM todos WHERE userId = {userId} AND status = '{status}'"
    cursor.execute(query)
    column_names = [column[0] for column in cursor.description]
    rows = cursor.fetchall()
    return [dict(zip(column_names, row)) for row in rows]


def deleteTodo(connection,id):
    cursor = connection.cursor()
    query = f"DELETE FROM todos WHERE id = {id}"
    cursor.execute(query)
    connection.commit()
    return {"message": "Todo added successfully"}


def getLabelsForUser(connection, userId):
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM labels WHERE userId = %s"
        cursor.execute(query, (userId,))
        column_names = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(column_names, row)) for row in rows]

    except Exception as e:
        print(f"An error occurred during getLabelsForUser: {e}")
        return []



