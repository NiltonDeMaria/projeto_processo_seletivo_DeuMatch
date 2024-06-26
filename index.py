candidatosLista = [[5, 10, 8, 8], [10, 7, 7, 8], [8, 5, 4, 9], [2, 2, 2, 1], [10, 10, 8, 9]]

def buscaCandidatos(e, t, p, s):
    
    tamanhoLista = len(candidatosLista)
    b = 0

    for n in range(tamanhoLista):
        if (candidatosLista[n][0] >= e and
            candidatosLista[n][1] >= t and
            candidatosLista[n][2] >= p and
            candidatosLista[n][3] >= s):

            candidato = n + 1
            print(f"   Candidato {candidato} atende o critério.")
            b += 1
    if b == 0:
        print("   Nenhuma candidato atente ao critério.")

def busca():

    buscaValor = int(input('''
    ===========================================
        1 - Busca de candidato por critério;
        2 - Busca de um candidato específico:
        3 - SAIR.
    ===========================================
                       '''))

    if buscaValor == 1:
        
        while True:
            try:
                criterioEntrevista = int(input("Digite o critério da entrevista: "))
                break
            except ValueError:
                print('Essa não é uma resposta válida\n')
        
        while True:
            try:
                criterioTesteTeorico = int(input("Digite o critério do Teste Teórico: "))
                break
            except ValueError:
                print('Essa não é uma resposta válida\n')

        while True:
            try:
                criterioTestePratico = int(input("Digite o critério do Teste Prático: "))
                break
            except ValueError:
                print('Essa não é uma resposta válida\n')
        
        while True:
            try:
                criterioSoft = int(input("Digite o critério da Avaliação de Soft Skills: "))
                break
            except ValueError:
                print('Essa não é uma resposta válida\n')

        buscaCandidatos(criterioEntrevista, criterioTesteTeorico, criterioTestePratico, criterioSoft)

        busca()

    elif buscaValor == 2:
        
        while True:
            try:
                nCandidato = int(input("Digite o número do candidato: "))
                break
            except ValueError:
                print('Essa não é uma resposta válida\n')
        
        if nCandidato < 1 or nCandidato > len(candidatosLista):
            print("Candidato inexistente, tente novamente.")
            busca()

        print(f"   Candidato {nCandidato}: e{candidatosLista[nCandidato-1][0]}_t{candidatosLista[nCandidato-1][1]}_p{candidatosLista[nCandidato-1][2]}_s{candidatosLista[nCandidato-1][3]}")

        busca()
   
    elif buscaValor == 3:
        print("   Obrigado, volte sempre!")

    else:
        busca()

busca()