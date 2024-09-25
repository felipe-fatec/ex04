import logging
from flask import Flask
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)

@app.route('/')
def hello_world():
    logging.info('Este é um log simples.')
    return 'Hello, World!'
