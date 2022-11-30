from flask import Flask

api = Flask(__name__)

ping = [
    {
        'ping': "ping"
    }
]
pong = [
    {
        'pong': "pong"
    }
]

# sem parametros
@api.route('/',methods=['GET'])
def returnInfo():
    return "Escreva '/ping' na URL para retornar 'pong', ou '/pong' para retornar 'ping'"

# retornar ping
@api.route('/pong',methods=['GET'])
def returnPing():
    return "ping"
    
# retornar pong
@api.route('/ping',methods=['GET'])
def returnPong():
    return "pong"
api.run(port=5000,host='localhost',debug=True)