listaMusicas = []

def listar_musicas():
    return listaMusicas

def adicionar_musica(nome, artista, genero, duracao):
    listaMusicas.append({
        "nome": nome,
        "artista": artista,
        "genero": genero,
        "duracao": duracao
    })