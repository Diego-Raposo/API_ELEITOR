from flask import Flask, make_response, jsonify, request, Response
import sys
import os

# Atualizar o path do projeto para localizar os módulos da pasta
# repository
#modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
# sys.path.append(modulo)


from repository.usuario import *
from repository.produto import *
from repository.eleitor import * 
import repository.eleitor as eleitor

#import usuario as usuario

#import usuario
#import produto

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# --------------------------------------------------------
#           Inicio: Serviços da api usuário 
# --------------------------------------------------------



# Inserir eleitor
@app_api.route('/eleitor', methods=['POST'])
def criar_eleitor_api():
    eleitor_json = request.json
    try:
        cpf = eleitor_json['cpf']
        if existe_eleitor(cpf):
            return make_response(jsonify(status=False, mensagem='Eleitor já existe'), 400)
        
        criar_eleitor(eleitor_json)
        sucesso = True
        _mensagem = 'Eleitor inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusão do eleitor: {ex}'
    
    return make_response(jsonify(status=sucesso, mensagem=_mensagem))


@app_api.route('/eleitor', methods=['PUT'])
def atualizar_eleitor_api(eleitor_json):
    # Captura o JSON com os dados enviados pelo cliente
    eleitor_json = request.json  # corpo da requisição com os dados do eleitor
    cpf = eleitor_json['cpf']  # obtém o CPF do eleitor
    
    try:
        # Verifica se o eleitor existe
        if eleitor.existe_eleitor(cpf):
            # Atualiza o eleitor com os dados recebidos
            eleitor.atualizar_eleitor(eleitor_json)  # Passa o JSON como parâmetro
            sucesso = True
            _mensagem = 'Eleitor atualizado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor não existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro ao atualizar eleitor: {ex}'
    
    return make_response(
        jsonify(
            status=sucesso,
            mensagem=_mensagem
        )
    )
    
@app_api.route('/eleitor/<int:cpf>', methods=['DELETE'])
def deletar_eleitor(cpf):
    try:
        if existe_eleitor(cpf) == True:
            deletar_eleitor(cpf)
            sucesso = True
            _mensagem = 'Eleitor deletado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor nao existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Exclusao de eleitor: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem
        )
    )

@app_api.route('/eleitores', methods=['GET'])
def listar_eleitores():
    try:
        # Recupera todos os eleitores do banco de dados
        todos_eleitores = eleitor.listar_eleitor()
        
        return make_response(
            jsonify(
                status=True,
                mensagem='Lista de eleitores',
                dados=todos_eleitores
            ),
            200
        )
    
    except Exception as ex:
        print(f'Erro: {ex}')  # Log do erro
        return make_response(
            jsonify(
                status=False,
                mensagem=f'Erro ao listar eleitores: {ex}',
                dados=[]
            ),
            500
         )

    

# -- Fim: Serviços da api produto ------------------------


# Levantar/Executar API REST: api_database
app_api.run()



