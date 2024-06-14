from faker import Faker
import sqlite3

def seed_database():
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    faker = Faker()
    
    # Додавання користувачів
    for _ in range(10):
        fullname = faker.name()
        email = faker.email()
        cursor.execute('''INSERT INTO users (fullname, email) VALUES (?, ?)''', (fullname, email))
    
    # Додавання статусів
    statuses = [('new',), ('in progress',), ('completed',)]
    for status in statuses:
        cursor.execute('''INSERT OR IGNORE INTO status (name) VALUES (?)''', status)
    
    # Додавання завдань
    for _ in range(20):
        title = faker.sentence()
        description = faker.text()
        status_id = faker.random_int(min=1, max=3)
        user_id = faker.random_int(min=1, max=10)
        cursor.execute('''INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)''',
                       (title, description, status_id, user_id))
    
    conn.commit()
    conn.close()

seed_database()