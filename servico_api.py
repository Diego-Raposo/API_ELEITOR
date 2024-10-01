from flask import Flask, make_response, jsonify, request, Response
import mysql.connector
import sys
import os

# Atualizar o path do projeto para localizar os módulos da pasta
# repository
#modulo = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
# sys.path.append(modulo)


#from repository.usuario import *
#from repository.produto import *

import repository.produto as produto
import repository.usuario as usuario
import repository.eleitor as eleitor

#import usuario as usuario

#import usuario
#import produto

# Instanciar 
app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# --------------------------------------------------------
#           Inicio: Serviços da api eleitor
# --------------------------------------------------------

# Incluir um novo Eleitor
@app_api.route('/eleitor', methods=['POST'])
def criar_eleitor():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    eleitor_json = request.json # corpo da requisição
    try:
        eleitor.criar_eleitor(eleitor_json)
        sucesso = True
        _mensagem = 'Eleitor inserido com sucesso'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro: Inclusao do eleitor: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso,
                mensagem = _mensagem 
        )
    )


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
        if eleitor.existe_eleitor(cpf) == True:
            eleitor.deletar_eleitor(cpf)
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

@app_api.route('/eleitor/<string:cpf>', methods=['GET'])
def obter_eleitor_por_cpf(cpf):
    sucesso = False
    eleitor_cpf = {}
    
    try:
        if eleitor.existe_eleitor(cpf):
            eleitor_tuple = eleitor.obter_eleitor_cpf(cpf)
            # Converter a tupla para um dicionário com mapeamento correto
            eleitor_cpf = {
                'cpf': eleitor_tuple[0],
                'nome': eleitor_tuple[1],
                'data_nascimento': eleitor_tuple[2],
                'nome_mae': eleitor_tuple[3],
                'cep': eleitor_tuple[4],
                'nro_endereco': eleitor_tuple[5],
                'nro_titulo': eleitor_tuple[6],
                'situacao': eleitor_tuple[7],
                'secao': eleitor_tuple[8],
                'zona': eleitor_tuple[9],
                'local_votacao': eleitor_tuple[10],
                'endereco_votacao': eleitor_tuple[11],
                'bairro': eleitor_tuple[12],
                'municipio_uf': eleitor_tuple[13],
                'pais': eleitor_tuple[14]
            }
            sucesso = True
            _mensagem = 'Eleitor encontrado com sucesso'
        else:
            sucesso = False
            _mensagem = 'Eleitor não existe'
    except Exception as ex:
        sucesso = False
        _mensagem = f'Erro ao buscar eleitor: {ex}'
    
    return make_response(
        jsonify(status=sucesso, mensagem=_mensagem, dados=eleitor_cpf)
    )
  
    
@app_api.route('/eleitor', methods=['GET'])
def lista_eleitor():
    lista_eleitor = list()
    lista_eleitor = eleitor.listar_eleitor()
    if len(lista_eleitor) == 0:
        sucesso = False
        _mensagem = 'Lista de eleitores vazia'
    else:
        sucesso = True
        _mensagem = 'Lista de eleitores'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = sucesso, 
                mensagem = _mensagem,
                dados = lista_eleitor
        )
    )





# -- Fim: Serviços da api eleitor ------------------------


# Levantar/Executar API REST: api_database
app_api.run()



