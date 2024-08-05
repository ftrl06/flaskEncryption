from flask import Flask, request, jsonify
from .encryption.py import AESCipher

app = Flask(__name__)
cipher = AESCipher()

@app.route('/receive_data', methods=['POST'])
def receive_data():
    encrypted_data = request.json.get('data')
    decrypted_data = cipher.decrypt(encrypted_data)
    # Processing data
    print(f"Decrypted Data: {decrypted_data}")
    return jsonify({'status': 'success', 'decrypted_data': decrypted_data})

if __name__ == '__main__':
    app.run(debug=True)
