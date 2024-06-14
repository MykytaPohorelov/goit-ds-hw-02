import sqlite3

def execute_queries():
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    
    
    user_id = 1
    cursor.execute('''SELECT * FROM tasks WHERE user_id = ?''', (user_id,))
    print("All tasks for user 1:", cursor.fetchall())
    
    
    status_name = 'new'
    cursor.execute('''SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = ?)''', (status_name,))
    print(f"All tasks with status '{status_name}':", cursor.fetchall())
    
    
    task_id = 1
    new_status_id = 2  # 'in progress'
    cursor.execute('''UPDATE tasks SET status_id = ? WHERE id = ?''', (new_status_id, task_id))
    conn.commit()
    
    
    cursor.execute('''SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks)''')
    print("Users with no tasks:", cursor.fetchall())
    
    
    new_task = ('New Task Title', 'New task description', 1, 1)
    cursor.execute('''INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)''', new_task)
    conn.commit()
    
    
    cursor.execute('''SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed')''')
    print("All tasks that are not completed:", cursor.fetchall())
    
    
    delete_task_id = 2
    cursor.execute('''DELETE FROM tasks WHERE id = ?''', (delete_task_id,))
    conn.commit()
    
    
    email_pattern = '%@example.com'
    cursor.execute('''SELECT * FROM users WHERE email LIKE ?''', (email_pattern,))
    print("Users with specific email domain:", cursor.fetchall())
    
    
    user_id_to_update = 1
    new_fullname = 'Updated Name'
    cursor.execute('''UPDATE users SET fullname = ? WHERE id = ?''', (new_fullname, user_id_to_update))
    conn.commit()
    
    
    cursor.execute('''SELECT status.name, COUNT(tasks.id) FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name''')
    print("Number of tasks per status:", cursor.fetchall())
    
    
    domain = '%@example.com'
    cursor.execute('''SELECT tasks.* FROM tasks JOIN users ON tasks.user_id = users.id WHERE users.email LIKE ?''', (domain,))
    print(f"Tasks assigned to users with email domain '{domain}':", cursor.fetchall())
    
    
    cursor.execute('''SELECT * FROM tasks WHERE description IS NULL OR description = '' ''')
    print("Tasks without description:", cursor.fetchall())
    
    
    cursor.execute('''SELECT users.fullname, tasks.title FROM tasks JOIN users ON tasks.user_id = users.id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress')''')
    print("Users and their 'in progress' tasks:", cursor.fetchall())
    
    
    cursor.execute('''SELECT users.fullname, COUNT(tasks.id) FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id''')
    print("Users and the number of their tasks:", cursor.fetchall())

    conn.close()

execute_queries()