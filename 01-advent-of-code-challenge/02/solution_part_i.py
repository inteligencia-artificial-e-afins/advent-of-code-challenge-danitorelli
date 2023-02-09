entrada = {'A': 'Pedra', 'B': 'Papel', 'C': 'Tesoura', 'X': 'Pedra', 'Y': 'Papel', 'Z': 'Tesoura'}
pts_forma_jogada = {'Pedra': 1, 'Papel': 2, 'Tesoura': 3}
pts_result_partida = {'Perdeu': 0, 'Empatou': 3, 'Venceu': 6}


with open('advent-of-code-challenge-danitorelli/01-advent-of-code-challenge/02/sample.in', 'r') as f:
    linhas = f.readlines()
    rodadas = [entrada.strip() for entrada in linhas]


def pts_por_rodada(round_string):
    jogada_adversaria = entrada[round_string[0]]
    minha_jogada = entrada[round_string[2]]

    if jogada_adversaria == minha_jogada:
        return pts_result_partida['Empatou'] + pts_forma_jogada[minha_jogada]
    elif (jogada_adversaria, minha_jogada) in [('Papel', 'Pedra'), ('Pedra', 'Tesoura'), ('Tesoura', 'Papel')]:
        return pts_result_partida['Perdeu'] + pts_forma_jogada[minha_jogada]
    else:
        return pts_result_partida['Venceu'] + pts_forma_jogada[minha_jogada]


print(sum([pts_por_rodada(round_string) for round_string in rodadas]))
