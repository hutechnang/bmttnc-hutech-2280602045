from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Initialize cipher objects (shared across routes)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

# --- API Routes ---

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    encrypted_text = data['encrypted_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- Web Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    text = ""
    key = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        key = request.form.get('key', '')
        action = request.form.get('action', '')
        if action == 'encrypt':
            result = caesar_cipher.encrypt_text(text, int(key))
        elif action == 'decrypt':
            result = caesar_cipher.decrypt_text(text, int(key))
    return render_template('caesar.html', text=text, key=key, result=result)

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    text = ""
    key = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        key = request.form.get('key', '')
        action = request.form.get('action', '')
        matrix = playfair_cipher.create_playfair_matrix(key)
        if action == 'encrypt':
            result = playfair_cipher.playfair_encrypt(text, matrix)
        elif action == 'decrypt':
            result = playfair_cipher.playfair_decrypt(text, matrix)
    return render_template('playfair.html', text=text, key=key, result=result)

@app.route('/railfence', methods=['GET', 'POST'])
def railfence():
    text = ""
    rails = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        rails = request.form.get('rails', '')
        action = request.form.get('action', '')
        if action == 'encrypt':
            result = railfence_cipher.rail_fence_encrypt(text, int(rails))
        elif action == 'decrypt':
            result = railfence_cipher.rail_fence_decrypt(text, int(rails))
    return render_template('railfence.html', text=text, rails=rails, result=result)

@app.route('/transposition', methods=['GET', 'POST'])
def transposition():
    text = ""
    key = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        key = request.form.get('key', '')
        action = request.form.get('action', '')
        if action == 'encrypt':
            result = transposition_cipher.encrypt(text, int(key))
        elif action == 'decrypt':
            result = transposition_cipher.decrypt(text, int(key))
    return render_template('transposition.html', text=text, key=key, result=result)

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    text = ""
    key = ""
    result = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        key = request.form.get('key', '')
        action = request.form.get('action', '')
        if action == 'encrypt':
            result = vigenere_cipher.vigenere_encrypt(text, key)
        elif action == 'decrypt':
            result = vigenere_cipher.vigenere_decrypt(text, key)
    return render_template('vigenere.html', result=result, text=text, key=key)

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2045, debug=True)