import sqlite3

DB_NAME = 'restaurant.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            payment TEXT,
            cashier TEXT,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            paid_by TEXT,
            description TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            supplier TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT,
            notes TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payroll (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month TEXT NOT NULL,
            role TEXT NOT NULL,
            department TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT
        )
    ''')

    conn.commit()
    conn.close()

# ── SALES ──────────────────────

def add_sale(data):
    conn = get_connection()
    conn.execute('''
        INSERT INTO sales (date, category, amount, payment, cashier, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'],
        data['category'],
        data['amount'],
        data['payment'],
        data['cashier'],
        data['description']
    ))
    conn.commit()
    conn.close()

def get_all_sales():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM sales ORDER BY date DESC').fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ── EXPENSES ──────────────────────

def add_expense(data):
    conn = get_connection()
    conn.execute('''
        INSERT INTO expenses (date, type, amount, paid_by, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['date'],
        data['type'],
        data['amount'],
        data['paid_by'],
        data['description']
    ))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ── PURCHASES ──────────────────────

def add_purchase(data):
    conn = get_connection()
    conn.execute('''
        INSERT INTO purchases (date, supplier, category, amount, status, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'],
        data['supplier'],
        data['category'],
        data['amount'],
        data['status'],
        data['notes']
    ))
    conn.commit()
    conn.close()

def get_all_purchases():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM purchases ORDER BY date DESC').fetchall()
    conn.close()
    return [dict(row) for row in rows]

# ── PAYROLL ──────────────────────

def add_payroll(data):
    conn = get_connection()
    conn.execute('''
        INSERT INTO payroll (month, role, department, amount, status)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        data['month'],
        data['role'],
        data['department'],
        data['amount'],
        data['status']
    ))
    conn.commit()
    conn.close()

def get_all_payroll():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM payroll ORDER BY month DESC').fetchall()
    conn.close()
    return [dict(row) for row in rows]
