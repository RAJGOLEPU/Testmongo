from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB (Replace this with your MongoDB URI)
client = MongoClient('mongodb+srv://raj:12345@test.eol4j.mongodb.net/?retryWrites=true&w=majority&appName=Test')

# Create or connect to a database and collection
db = client['user_database']
collection = db['user_data']

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collecting data from the form
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']

    # Create a dictionary to hold the data
    user_data = {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address
    }

    # Insert the data into MongoDB
    collection.insert_one(user_data)

    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
  
