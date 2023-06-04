import mariadb

def get_db_connection():
    connection = mysql.connector.connect(user='root', password='password', host='localhost', database='blog')
    return connection

def get_client(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM client WHERE username=%s AND password=%s", (username, password,))
    user = cursor.fetchone()
    return user[0] if user else None

def insert_post(client_id, title, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO post (client_id, title, content) VALUES (%s, %s, %s)", (client_id, title, content,))
    conn.commit()

def get_all_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM post")
    posts = cursor.fetchall()
    for post in posts:
        print('Title: ', post[0])
        print('Content: ', post[1])

def main():
    while True:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        client_id = get_client(username, password)
        if client_id is None:
            print('Invalid username or password')
            return
        print('1. Insert a new post')
        print('2. Read all posts')
        print('3. Quit')
        choice = input('Select 1, 2 or 3: ')
        if choice == '1':
            title = input('Enter title for the post: ')
            content = input('Enter content for the post: ')
            insert_post(client_id, title, content)
        elif choice == '2':
            get_all_posts()
        elif choice == '3':
            break

if __name__ == "__main__":
    main()
