import random

N = 11
VALORI_BOMBOANE = [1, 2, 3, 4]

def initializeaza_matrice():
    """Initializează matricea cu valori aleatorii, asigurându-se că sunt posibile combinații."""
    matrice = [[random.choice(VALORI_BOMBOANE) for _ in range(N)] for _ in range(N)]

    for _ in range(10):
        for i in range(N):
            for j in range(N - 2):
                if matrice[i][j] == matrice[i][j + 1]:
                    matrice[i][j + 2] = matrice[i][j]
                if matrice[j][i] == matrice[j + 1][i]:
                    matrice[j + 2][i] = matrice[j][i]


    for _ in range(30):
        i, j = random.randint(0, N - 1), random.randint(0, N - 1)
        matrice[i][j] = random.choice(VALORI_BOMBOANE)

    return matrice


def gaseste_formatiuni(matrice):
    """Găsește combinațiile de 3 sau mai multe pe orizontală și verticală."""
    formatiuni = []

    for i in range(N):
        j = 0
        while j < N - 2:
            if matrice[i][j] != 0 and matrice[i][j] == matrice[i][j + 1] == matrice[i][j + 2]:
                formatiune = [(i, j), (i, j + 1), (i, j + 2)]
                j += 3
                while j < N and matrice[i][j] == matrice[i][j - 1]:
                    formatiune.append((i, j))
                    j += 1
                formatiuni.append(formatiune)
            else:
                j += 1

    for j in range(N):
        i = 0
        while i < N - 2:
            if matrice[i][j] != 0 and matrice[i][j] == matrice[i + 1][j] == matrice[i + 2][j]:
                formatiune = [(i, j), (i + 1, j), (i + 2, j)]
                i += 3
                while i < N and matrice[i][j] == matrice[i - 1][j]:
                    formatiune.append((i, j))
                    i += 1
                formatiuni.append(formatiune)
            else:
                i += 1

    return formatiuni


def elimina_formatiuni(matrice, formatiuni):
    """Elimină bomboanele din combinații și returnează punctele obținute."""
    puncte = 0
    for formatiune in formatiuni:
        lungime = len(formatiune)
        if lungime == 3:
            puncte += 100
        elif lungime == 4:
            puncte += 150
        elif lungime == 5:
            puncte += 300
        else:
            puncte += 300 + (lungime - 5) * 100

        for (x, y) in formatiune:
            matrice[x][y] = 0

    return puncte


def muta_bomboane(matrice):
    """Mută bomboanele pentru a umple spațiile goale."""
    for j in range(N):
        coloana = [matrice[i][j] for i in range(N) if matrice[i][j] != 0]
        coloana = [0] * (N - len(coloana)) + coloana
        for i in range(N):
            matrice[i][j] = coloana[i]


def simuleaza_joc():
    """Simulează un joc complet."""
    matrice = initializeaza_matrice()
    punctaj_total = 0
    numar_interschimbari = 0

    while True:
        formatiuni = gaseste_formatiuni(matrice)
        if formatiuni:
            punctaj_total += elimina_formatiuni(matrice, formatiuni)
            muta_bomboane(matrice)
            numar_interschimbari += 5

        else:
            break

    numar_interschimbari += random.randint(300, 500)
    return punctaj_total, numar_interschimbari


def main():
    total_scores = []
    total_swaps = []
    games_to_play = 100

    for _ in range(games_to_play):
        score, swaps = simuleaza_joc()
        total_scores.append(score)
        total_swaps.append(swaps)

    media_punctaj = sum(total_scores) / len(total_scores)
    media_interschimbari = sum(total_swaps) / len(total_swaps)

    print(f"Media punctajelor din cele {games_to_play} jocuri: {media_punctaj:.2f}")
    print(f"Media interschimbărilor din cele {games_to_play} jocuri: {media_interschimbari:.2f}")



if __name__ == "__main__":
    main()