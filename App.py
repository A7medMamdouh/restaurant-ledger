from flask import Flask, render_template, request, jsonify
import database

app = Flask(__name__)

# Initialize database on startup
database.init_db()

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/purchases')
def purchases():
    return render_template('purchases.html')

@app.route('/payroll')
def payroll():
    return render_template('payroll.html')

# ── API Routes ──────────────────────

@app.route('/api/sales', methods=['GET'])
def get_sales():
    return jsonify(database.get_all_sales())

@app.route('/api/sales', methods=['POST'])
def add_sale():
    data = request.get_json()
    database.add_sale(data)
    return jsonify({'status': 'ok'})

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    return jsonify(database.get_all_expenses())

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    database.add_expense(data)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
