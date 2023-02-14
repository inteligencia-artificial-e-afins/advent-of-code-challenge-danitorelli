from string import ascii_letters

with open(
    "advent-of-code-challenge-danitorelli/01-advent-of-code-challenge/03/sample.in", "r"
) as f:
    linhas = f.readlines()
    mochilas = [entrada.strip() for entrada in linhas]


for mochila in mochilas:
    metade_1 = set(mochila[: len(mochila) // 2])
    metade_2 = set(mochila[len(mochila) // 2 :])

soma_mochilas = 0
j = 3

for i in range(0, len(mochilas), 3):
    entrada = mochilas[i:j]
    j += 3

    for valor, caractere in enumerate(ascii_letters):
        if (
            caractere in entrada[0]
            and caractere in entrada[1]
            and caractere in entrada[2]
        ):
            soma_mochilas += valor + 1

print(soma_mochilas)
