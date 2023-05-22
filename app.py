import eventlet
from eventlet import wsgi
from flask import Flask, request, jsonify, render_template
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/extract_data', methods=['POST'])
def extract_data():
    try:
        url = request.get_json().get('url')
        
        if is_valid_whatsapp_group_url(url) is None:
            raise ValueError('Invalid whatspgroup url')
            
        data = extract_group_info(url)
                
        output_file = 'whatsapp_groups.json'
        
        append_to_json_file(output_file, data)

        return jsonify(data)
    except ValueError as e:
        return jsonify({'error': str(e)})

@app.route('/api/data')
def json_data():
    try:
        data = read_json_file('whatsapp_groups.json')
        return jsonify(data)
    except ValueError as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    wsgi.server(eventlet.listen(('', 80)), app)
