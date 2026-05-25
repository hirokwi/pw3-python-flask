listaGames = [
    {"titulo": "CS-GO", "ano": 2012, "categoria": "FPS online"}
]

def listar_games():
    return listaGames

def adicionar_game(titulo, ano, categoria):
    listaGames.append({
        "titulo": titulo,
        "ano": int(ano),
        "categoria": categoria
    })