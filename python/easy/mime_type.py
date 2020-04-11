nb_asso, nb_file = [int(input()) for _ in range(2)]
dict_asso = dict()

for _ in range(nb_asso):
    asso_split = input().split()
    dict_asso[asso_split[0].lower()] = asso_split[1]

for _ in range(nb_file):
    file_split = input().split('.')
    if len(file_split) > 1:
        print(dict_asso[file_split[-1].lower()] if file_split[-1].lower() in dict_asso else "UNKNOWN")
    else:
        print("UNKNOWN")