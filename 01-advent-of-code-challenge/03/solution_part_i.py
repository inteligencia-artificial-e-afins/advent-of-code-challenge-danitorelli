from string import ascii_letters

with open(
    "advent-of-code-challenge-danitorelli/01-advent-of-code-challenge/03/sample.in", "r"
) as f:
    linhas = f.readlines()
    mochilas = [entrada.strip() for entrada in linhas]


soma_mochilas = 0

for mochila in mochilas:
    metade_1 = set(mochila[: len(mochila) // 2])
    metade_2 = set(mochila[len(mochila) // 2 :])

    for valor, caractere in enumerate(ascii_letters):
        if caractere in metade_1 and caractere in metade_2:
            soma_mochilas += valor + 1

print(soma_mochilas)
