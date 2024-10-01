from repository import database


# Inserir eleitor
def criar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = (
            f"INSERT INTO eleitor(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais) "
            f"VALUES ('{eleitor['cpf']}', '{eleitor['nome']}', '{eleitor['data_nascimento']}', '{eleitor['nome_mae']}', '{eleitor['cep']}', '{eleitor['nro_endereco']}', "
            f"'{eleitor['nro_titulo']}', '{eleitor['situacao']}', '{eleitor['secao']}', '{eleitor['zona']}', '{eleitor['local_votacao']}', '{eleitor['endereco_votacao']}', "
            f"'{eleitor['bairro']}', '{eleitor['municipio_uf']}', '{eleitor['pais']}')"
        )
        
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')
    finally:
        cursor.close()
        conect.close()

def existe_eleitor(cpf):
    conect = database.criar_db()
    cursor = conect.cursor()
    try:
        cursor.execute("SELECT COUNT(1) FROM eleitor WHERE cpf = %s", (cpf,))
        return cursor.fetchone()[0] > 0
    except Exception as ex:
        print(f'Erro ao verificar eleitor: {ex}')
        return False
    finally:
        cursor.close()
        conect.close()
        
# Atualizar eleitor
def atualizar_eleitor(eleitor):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = (
            f"UPDATE eleitor SET "
            f"nome = '{eleitor['nome']}', "
            f"data_nascimento = '{eleitor['data_nascimento']}', "
            f"nome_mae = '{eleitor['nome_mae']}', "
            f"cep = '{eleitor['cep']}',"
            f"nro_titulo = '{eleitor['nro_titulo']}', "
            f"situacao = '{eleitor['situacao']}', "
            f"secao = '{eleitor['secao']}', "
            f"zona = '{eleitor['zona']}', "
            f"local_votacao = '{eleitor['local_votacao']}', "
            f"endereco_votacao = '{eleitor['endereco_votacao']}', "
            f"bairro = '{eleitor['bairro']}', "
            f"municipio_uf = '{eleitor['municipio_uf']}', "
            f"pais = '{eleitor['pais']}' "
            f"WHERE cpf = '{eleitor['cpf']}'"
        )
        print(sql)
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na alteração: {ex}')
    finally:
        cursor.close()
        conect.close()
        

# Deletar eleitor 
def deletar_eleitor(cpf):
    try:
        # Manipular o banco de dados
        conect = database.criar_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM eleitor WHERE cpf = {cpf}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
# Fim: deletar_usuario(id)

# Obter o eleitor pelo cpf


def obter_eleitor_cpf(cpf):
    # Declar uma tupla vazia
    eleitor = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM eleitor WHERE cpf = '{cpf}'" 
        cursor.execute(sql)
        eleitor = cursor.fetchone()
    except Exception as ex:
        print(f'Erro na verificacao da existencia do produto: {ex}')
    finally:
        cursor.close()
        conect.close()
    return eleitor
# fim: obter_eleitor_cpf(cpf)

def listar_eleitor():
    eleitores = []
    cursor = None
    conect = None
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM eleitor ORDER BY nome'
        cursor.execute(sql)
        lista_eleitor = cursor.fetchall()
        for eleitor in lista_eleitor:
            eleitores.append({
                'cpf': eleitor[0],
                'nome': eleitor[1],
                'data_nascimento': eleitor[2],
                'nome_mae': eleitor[3],
                'cep': eleitor[13],
                'nro_titulo': eleitor[4],
                'situacao': eleitor[5],
                'secao': eleitor[6],
                'zona': eleitor[7],
                'local_votacao': eleitor[8],
                'endereco': eleitor[9],
                'bairro': eleitor[10],
                'municipio_uf': eleitor[11],
                'pais': eleitor[12]
            })
    except Exception as ex:
        print(f'Erro: Listar todos os eleitores: {ex}')
        return []  # Retorna uma lista vazia em caso de erro
    finally:
        if cursor:
            cursor.close()
        if conect:
            conect.close()
    return eleitores

def existe_eleitor(cpf):
    existe: False
    # criar uma tupla vazia
    eleitor = ()
    try:
        conect = database.criar_db()
        cursor = conect.cursor() 
        sql = f"SELECT cpf FROM eleitor WHERE cpf = '{cpf}'" 
        cursor.execute(sql)
        eleitor = cursor.fetchone()
        if eleitor is not None:
            if len(eleitor) == 1:
                existe = True
            else:
                existe = False
        else:
           existe = False 

    except Exception as ex:
        print(f'Erro na verificacao da existencia do produto: {ex}')
    finally:
        cursor.close()
        conect.close()

    return existe

# Fim: criar_eleitor(produto)