import mariadb
from dbcreds import user, password, host, database

# Infinite loop to keep the program running until the user chooses to quit
while True:
    # Establishing a connection to the MariaDB database
    connection = mariadb.connect(user=user, password=password, host=host, database=database)

    # Prompting the user to enter their username and password
    username = input('Enter your username: ')
    password_input = input('Enter your password: ')

    # Creating a cursor object to interact with the database
    cursor = connection.cursor()

    # Executing a SELECT query to check if the provided username and password are valid
    cursor.execute("SELECT id FROM client WHERE username=%s AND password=%s", (username, password_input,))
    user = cursor.fetchone()
    client_id = user[0] if user else None

    # Checking if the client_id is None, indicating invalid credentials
    if client_id is None:
        print('Invalid username or password')
        connection.close()
        break

    # Displaying the menu options
    print('1. Insert a new post')
    print('2. Read all posts')
    print('3. Quit')
    choice = input('Select 1, 2 or 3: ')

    if choice == '1':
        # Inserting a new post
        title = input('Enter title for the post: ')
        content = input('Enter content for the post: ')
        cursor.execute("INSERT INTO post (client_id, title, content) VALUES (%s, %s, %s)", (client_id, title, content,))
        connection.commit()

    elif choice == '2':
        # Reading all posts
        cursor.execute("SELECT title, content FROM post")
        posts = cursor.fetchall()
        for post in posts:
            print('Title: ', post[0])
            print('Content: ', post[1])

    elif choice == '3':
        # Quitting the program
        connection.close()
        break
