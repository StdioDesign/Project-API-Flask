from models import Pessoas

# Insere dados na tabela Pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25)
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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
