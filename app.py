from flask import Flask, jsonify, request
from datetime import datetime
from func import calcular_horas

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'Olá, mundo! Esta é uma API básica em Python.'})

@app.route('/api', methods=['POST'])
def recebe_json():
    try:
        # Obter os dados do corpo da requisição em formato JSON
        data = request.get_json()

        # Extrair as datas
        data_inicial = data['dataInicial']
        data1 = datetime.strptime(data_inicial, '%Y-%m-%d %H:%M:%S')
        data_final = data['dataFinal']
        data2 = datetime.strptime(data_final, '%Y-%m-%d %H:%M:%S')
        returno = jsonify({'horas': str(calcular_horas(data1, data2))})
        return returno

        #return jsonify({'message': 'JSON recebido com sucesso'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True)
