import sqlite3

# สร้างฐานข้อมูล
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# สร้างตาราง Books
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT DEFAULT "Available"
)
''')

# สร้างตาราง Borrowers
cursor.execute('''
CREATE TABLE IF NOT EXISTS Borrowers (
    borrower_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    book_id INTEGER,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)
''')

conn.commit()
conn.close()
