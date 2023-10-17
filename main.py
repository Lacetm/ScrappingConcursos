import utils


class Concurso:
    def __init__(self, nome, status, vagas, cargos, situacao):
        self.nome = nome
        self.status = status
        self.vagas = vagas
        self.cargos = cargos
        self.situacao = situacao


listaConcursos = []
for i in range(16):

    nome = utils.get_nome(i)
    status = utils.get_status(i)
    vagas = utils.get_vagas(i)
    cargos = utils.get_cargos(i)
    situacao = utils.get_situacao(i)

    concursoAtual = Concurso(nome, status, vagas, cargos, situacao)
    listaConcursos.append(concursoAtual)

for i in range(16):
    print(listaConcursos[i].nome)
    print(listaConcursos[i].situacao)
    print("//////////")

