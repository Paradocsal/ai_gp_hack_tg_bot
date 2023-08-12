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
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('INSERT OR IGNORE INTO users (chat_id) VALUES (?)', (chat_id,))
    conn.commit()

    cursor.close()
    conn.close()


def add_timeseries_source_table(chat_id, link):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM users WHERE chat_id = ?', (chat_id,))
    user_id = cursor.fetchone()[0]

    cursor.execute('INSERT INTO links (user_id, link) VALUES (?, ?)', (user_id, link))
    conn.commit()

    cursor.close()
    conn.close()
