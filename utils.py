from models import Pessoas, Usuarios

# Insere dados na tabela Pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=29)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela Pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Darlan').first()
    print(pessoa.idade)

# Altera dados na tabela Pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()

# Exclui dados na tabela Pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario('darlan', '1234')
    insere_usuario('galleani', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
