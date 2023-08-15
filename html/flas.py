from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InputFile
from aiogram.utils import executor
from flask import Flask, render_template, request
from database import Database


db = Database()

app = Flask(__name__)
@app.route('/upload', methods=['POST'])
def upload():
    file_id = request.form['file_id']

    db.upload_file(file_id)
  
    return render_template('index.html', file_id=file_id)

@app.route('/')
def home():
    name = 'John'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
