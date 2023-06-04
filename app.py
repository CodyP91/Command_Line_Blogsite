import mariadb
from dbcreds import user, password, host, database

while True:
    connection = mariadb.connect(user=user, password=password, host=host, database=database)
    username = input('Enter your username: ')
    password_input = input('Enter your password: ')
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM client WHERE username=%s AND password=%s", (username, password_input,))
    user = cursor.fetchone()
    client_id = user[0] if user else None

    if client_id is None:
        print('Invalid username or password')
        connection.close()
        break

    print('1. Insert a new post')
    print('2. Read all posts')
    print('3. Quit')
    choice = input('Select 1, 2 or 3: ')

    if choice == '1':
        title = input('Enter title for the post: ')
        content = input('Enter content for the post: ')
        cursor.execute("INSERT INTO post (client_id, title, content) VALUES (%s, %s, %s)", (client_id, title, content,))
        connection.commit()
    elif choice == '2':
        cursor.execute("SELECT title, content FROM post")
        posts = cursor.fetchall()
        for post in posts:
            print('Title: ', post[0])
            print('Content: ', post[1])
    elif choice == '3':
        connection.close()
        break
