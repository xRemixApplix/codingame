n = int(input())
tab = []

def oper(operation, arg1, arg2):
    args = [arg1, arg2]

    for i in range(len(args)):
        if len(args[i].split('$')) > 1:
            if tab[int(args[i].split('$')[-1])]['RESULT'] == "":
                tab[int(args[i].split('$')[-1])]['RESULT'] = oper(tab[int(args[i].split('$')[-1])]['OPERATION'], tab[int(args[i].split('$')[-1])]['ARG1'], tab[int(args[i].split('$')[-1])]['ARG2'])
            args[i] = tab[int(args[i].split('$')[-1])]['RESULT']

    if operation == 'VALUE': return int(args[0])
    if operation == 'ADD': return int(args[0]) + int(args[1])
    if operation == 'SUB': return int(args[0]) - int(args[1])
    if operation == 'MULT': return int(args[0]) * int(args[1])

for i in range(n):
    dictio = dict()
    dictio['OPERATION'], dictio['ARG1'], dictio['ARG2'] = input().split()
    dictio['RESULT'] = ''

    tab.append(dictio)

for i in range(n):
    if tab[i]['RESULT'] == '': tab[i]['RESULT'] = oper(tab[i]['OPERATION'], tab[i]['ARG1'], tab[i]['ARG2'])
    print(tab[i]['RESULT'])