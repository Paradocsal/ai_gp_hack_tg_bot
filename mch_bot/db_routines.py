import sqlite3


def initialize_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT UNIQUE
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                link TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

    connection.commit()
    cursor.close()
    connection.close()


def add_user(chat_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('INSERT OR IGNORE INTO users (chat_id) VALUES (?)', (chat_id,))

    connection.commit()
    cursor.close()
    connection.close()


def add_timeseries_source_table(chat_id, link):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id FROM users WHERE chat_id = ?', (chat_id,))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO links (user_id, link) VALUES (?, ?)', (user_id, link))

    connection.commit()
    cursor.close()
    connection.close()


def delete_timeseries_source_table(chat_id, link):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id FROM users WHERE chat_id = ?', (chat_id,))
    user_id = cursor.fetchone()[0]

    cursor.execute('DELETE FROM links WHERE user_id = ? AND link = ?', (user_id, link))

    connection.commit()
    cursor.close()
    connection.close()


def get_unique_links_with_chat_ids():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
            SELECT DISTINCT chat_id, link 
            FROM links 
            JOIN users 
            WHERE users.id == links.user_id
        ''')
    links_with_ids = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return links_with_ids


def get_saved_links(chat_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id FROM users WHERE chat_id = ?', (chat_id,))
    user_id = cursor.fetchone()[0]

    cursor.execute('SELECT link FROM links WHERE user_id = ?', (user_id,))
    links = [row[0] for row in cursor.fetchall()]

    cursor.close()
    connection.close()

    return links
