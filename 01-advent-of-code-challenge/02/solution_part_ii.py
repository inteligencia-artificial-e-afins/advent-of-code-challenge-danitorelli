entrada = {
    "A": "pedra",
    "B": "papel",
    "C": "tesoura",
    "X": "perdeu",
    "Y": "empatou",
    "Z": "ganhou",
}
pts_forma_jogada = {"pedra": 1, "papel": 2, "tesoura": 3}
pts_result_partida = {"perdeu": 0, "empatou": 3, "ganhou": 6}


with open(
    "advent-of-code-challenge-danitorelli/01-advent-of-code-challenge/02/sample.in", "r"
) as f:
    linhas = f.readlines()
    rodadas = [entrada.strip() for entrada in linhas]


def pts_por_rodada2(round_string):
    jogada_adversaria = entrada[round_string[0]]
    minha_jogada = entrada[round_string[2]]

    if (jogada_adversaria, minha_jogada) in [
        ("pedra", "empatou"),
        ("papel", "perdeu"),
        ("tesoura", "ganhou"),
    ]:
        return pts_result_partida[minha_jogada] + pts_forma_jogada["pedra"]
    elif (jogada_adversaria, minha_jogada) in [
        ("pedra", "ganhou"),
        ("papel", "empatou"),
        ("tesoura", "perdeu"),
    ]:
        return pts_result_partida[minha_jogada] + pts_forma_jogada["papel"]
    else:
        return pts_result_partida[minha_jogada] + pts_forma_jogada["tesoura"]


print(sum([pts_por_rodada2(round_string) for round_string in rodadas]))
