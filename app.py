from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Olá, mundo! Esta é uma API básica em Python.'})

@app.route('/api', methods=['POST'])
def post_api():
    data = request.get_json()  # Obtemos os dados enviados no corpo da requisição em formato JSON

    # Exemplo de manipulação dos dados
    if 'mensagem' in data:
        mensagem = data['mensagem']
        resposta = f'Você enviou a mensagem: {mensagem}'
        return jsonify({'resposta': resposta})

    return jsonify({'erro': 'Mensagem não encontrada no corpo da requisição'}), 400


if __name__ == '__main__':
    app.run(debug=True)
