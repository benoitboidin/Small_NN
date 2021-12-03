from copy import deepcopy


def activation(h):
    if h >= 0:
        hs = 1
    else:
        hs = 0
    return hs


def display(forme):
    for v in range(N):
        for w in range(N):
            if forme[v][w] == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print('')


N = 5
N_cell = N * N
eps = 0.2

etats = [[0 for _ in range(N)] for _ in range(N)]
newetats = [[0 for _ in range(N)] for _ in range(N)]
seuils = [[0.0 for _ in range(N)] for _ in range(N)]
poids = [[0.5 for _ in range(N_cell)] for _ in range(N_cell)]
for i in range(N_cell):
    for j in range(N_cell):
        if i == j:
            poids[i][j] = 0

test = [[0, 1, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 1]]

alphabet = \
    [[[0, 1, 1, 1, 0],  # { A }
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1]],
     [[1, 1, 1, 1, 0],  # { B }
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 0]],
     [[0, 1, 1, 1, 1],  # { C }
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [0, 1, 1, 1, 1]],
     [[1, 1, 1, 1, 0],  # { D }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 0]],
     [[1, 1, 1, 1, 1],  # { E }
      [1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1]],
     [[1, 1, 1, 1, 1],  # { F }
      [1, 0, 0, 0, 0],
      [1, 1, 1, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0]],
     [[1, 1, 1, 1, 1],  # { G }
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1]],
     [[1, 0, 0, 0, 1],  # { H }
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1]],
     [[0, 0, 1, 0, 0],  # { I }
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0]],
     [[0, 0, 1, 1, 1],  # { J }
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 1, 1, 0]],
     [[1, 0, 0, 0, 1],  # { K }
      [1, 0, 0, 1, 0],
      [1, 1, 1, 0, 0],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 0, 1]],
     [[1, 0, 0, 0, 0],  # { L }
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1]],
     [[1, 1, 0, 1, 1],  # { M }
      [1, 0, 1, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1]],
     [[1, 0, 0, 0, 1],  # { N }
      [1, 1, 0, 0, 1],
      [1, 0, 1, 0, 1],
      [1, 0, 0, 1, 1],
      [1, 0, 0, 0, 1]],
     [[0, 1, 1, 1, 0],  # { O }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [0, 1, 1, 1, 0]],
     [[1, 1, 1, 1, 0],  # { P }
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0]],
     [[1, 1, 1, 1, 1],  # { Q }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 1, 1],
      [1, 1, 1, 1, 1]],
     [[1, 1, 1, 1, 0],  # { R }
      [1, 0, 0, 0, 1],
      [1, 1, 1, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 0, 0, 0, 1]],
     [[0, 1, 1, 1, 1],  # { S }
      [1, 0, 0, 0, 0],
      [0, 1, 1, 1, 0],
      [0, 0, 0, 0, 1],
      [1, 1, 1, 1, 0]],
     [[1, 1, 1, 1, 1],  # { T }
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0]],
     [[1, 0, 0, 0, 1],  # { U }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [0, 1, 1, 1, 0]],
     [[1, 0, 0, 0, 1],  # { V }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0]],
     [[1, 0, 0, 0, 1],  # { W }
      [1, 0, 0, 0, 1],
      [1, 0, 0, 0, 1],
      [1, 0, 1, 0, 1],
      [0, 1, 0, 1, 0]],
     [[1, 0, 0, 0, 1],  # { X }
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0],
      [0, 1, 0, 1, 0],
      [1, 0, 0, 0, 1]],
     [[1, 0, 0, 0, 1],  # { Y }
      [0, 1, 0, 1, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0]],
     [[1, 1, 1, 1, 1],  # { Z }
      [0, 0, 0, 1, 0],
      [0, 0, 1, 0, 0],
      [0, 1, 0, 0, 0],
      [1, 1, 1, 1, 1]]]

l = 0
modif = 1
while modif > 0:
    modif = 0
    print('Les lettres suivantes doivent être apprises : ', end='')
    for l in range(26):
        etats = alphabet[l]
        for i1 in range(N):
            for i2 in range(N):
                somme = 0
                on = []

                # Activation de la cellule.
                for j1 in range(N):
                    for j2 in range(N):
                        if etats[j1][j2] == 1:
                            somme += poids[i1 * 5 + i2][j1 * 5 + j2]
                            # Comptage.
                            on.append([j1, j2])
                somme -= seuils[i1][i2]
                ncell = activation(somme)
                # print('On : ', on)

                if ncell != alphabet[l][i1][i2]:
                    modif += 1
                    if somme >= 0:
                        delta = (somme + eps) / (len(on) + 1)
                    if somme < 0:
                        delta = (somme - eps) / (len(on) + 1)
                    # Modification seuils.
                    seuils[i1][i2] += delta
                    # Modification poids.
                    for k in range(len(on)):
                        if [on[k][0] * 5 + on[k][1]] != [i1 * 5 + i2]:
                            poids[i1 * 5 + i2][on[k][0] * 5 + on[k][1]] -= delta
                            poids[on[k][0] * 5 + on[k][1]][i1 * 5 + i2] -= delta
                newetats[i1][i2] = ncell
        if newetats not in alphabet:
            print(chr(l + 65), end=' ')
        etats = newetats[:]
    print('\nNombre de modifications : ', modif, '\n')
    for b in range(25):
        print(poids[b])

# Vérifiation.
appris = 26
for l in range(26):
    etats = deepcopy(alphabet[l])
    for i1 in range(N):
        for i2 in range(N):
            somme = 0
            for j1 in range(N):
                for j2 in range(N):
                    if etats[j1][j2] == 1:
                        somme += poids[i1 * 5 + i2][j1 * 5 + j2]
            somme -= seuils[i1][i2]
            etats[i1][i2] = activation(somme)
    if etats != alphabet[l]:
        appris -= 1

print('Appris = ', appris)

# Reconnaissance.
print('Lettre à reconnaître :\n ')
display(test)
print('')
stop = 0
while test not in alphabet and stop < 10:
    stop += 1
    for i1 in range(N):
        for i2 in range(N):
            somme = 0
            for j1 in range(N):
                for j2 in range(N):
                    somme += poids[i1 * 5 + i2][j1 * 5 + j2] * \
                           test[j1][j2]
            somme -= seuils[i1][i2]
            test[i1][i2] = activation(somme)
    display(test)
if stop == 10:
    print('Échec de la reconnaissance.')
else:
    print('\nLe programme a reconnu un', chr(alphabet.index(test) + 65))
