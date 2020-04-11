width, height = [int(i) for i in input().split()]
tab = []

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(height):
    ligne = input()
    ligne_tab = []

    for i in range(len(ligne)):
        ligne_tab.append(ligne[i])

    tab.append(ligne_tab)

for i in range(height):
    for j in range(width):
        for dir in directions:
            if 0<=i+dir[0]<height and 0<=j+dir[1]<width and tab[i][j] != '#':
                if tab[i+dir[0]][j+dir[1]] != '#':
                    tab[i][j] = int(tab[i][j]) + 1

for lig in tab:
    print(*lig, sep='')