from armazenamento.dados_dos_alunos import cadastra_usuario, consulta_registros

def salvar_dados(dados):
    nome = dados['nome']
    email = dados['email']
    cep = dados['cep']
    endereco = dados['endereco']
    numero = dados['numero']
    cidade = dados['cidade']
    estado = dados['estado']
    complemento = dados['complemento']
    cadastra_usuario(nome=nome, email=email, cep=cep, endereco=endereco, numero=numero, cidade=cidade, estado=estado, complemento=complemento)

def recupera_registros():
    dados = consulta_registros()
    return dados
