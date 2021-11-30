import pickle

class atleta:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.sexo = ''
        self.paralisia = ''
        self.covid = ''
        self.modalidades = []
        self.medalhas = ''
        self.modalidade_ouro = ''
        self.modalidade_prata = ''
        self.modalidade_bronze = ''

    def __repr__(self):
        return (f'Nome: {self.nome}\nIdade: {self.idade}\nParalisia: {self.paralisia}\nMedalhas de ouro: {self.modalidade_ouro}\nMedalhas de prata:{self.modalidade_prata}\nMedalhas de bronze: {self.modalidade_bronze}\n')


def verificar_atleta(nome,atletas):#VERIFICAR SE O ATLETA JÁ ESTÁ CADASTRADO
    # try:
    if atletas:
        if nome in atletas:
            return True
        else:
            return False
    # except TypeError:
    #     pass
def cadastrar(atletas,modalidades):#CADASTRAR OS ATLETAS
    lista_modalidades = []
    nome = input('Digite o nome do atleta: ').upper()
    verificacao = verificar_atleta(nome,atletas)
    if verificacao == True:
        print('ESTE ATLETA JÁ ESTÁ CADASTRADO!!!')
    else:
        idade = input('Digite a idade do atleta: ')
        sexo = input('Qual o sexo do atleta? (M/F) ').upper()
        paralisia = input('Qual o tipo de paralisia: ').upper()
        covid = input('Foi diagnosticado com COVID? (S/N) ').upper()
        part_modalidades = int(input('Quantas modalidades participou? '))
        for i in range(part_modalidades):
            mod = input('Digite a {}° modalidade: (OBS: Sem acentos)'.format(i + 1)).upper()
            lista_modalidades.append(mod)
            aux = verificar_modalidade(mod,modalidades)# VERIFICAR SE A MODALIDADE ESTÁ ENTRE AS CADASTRADAS
            if aux == False:
                print('Modalidade não encontrada!')
                break
        if aux == True:
            medalhas = input('Ganhou medalhas? (S/N) ').upper()
            modalidade_ouro = []
            modalidade_prata = []
            modalidade_bronze = []
            if medalhas == 'S':
                tipos_medalhas = []
                ouro = (input('Ganhou medalhas de ouro? (S/N) ')).upper()
                prata = (input('Ganhou medalhas de prata? (S/N) ')).upper()
                bronze = (input('Ganhou medalhas de bronze? (S/N) ')).upper()
                if ouro == 'S':#CASO TENHA GANHADO MEDALHA DE OURO
                    quantidade_ouro = int(input('Quantas medalhas de ouro? '))
                    for i in range(quantidade_ouro):
                        n = input(f'Qual a {i+1}° modalidade que ganhou medalha de ouro: ').upper()

                        if verificar_modalidade(n, lista_modalidades):
                            modalidade_ouro.append(n)
                        else:
                            print('Atleta não aparticipou dessa modalidade!!')
                if prata == 'S':#CASO TENHA GANHADO MEDALHA DE PRATA
                    quantidade_prata = int(input('Quantas medalhas de prata? '))
                    for i in range(quantidade_prata):
                        n = input(f'Qual a {i+1}° modalidade que ganhou medalha de prata: ').upper()
                        if verificar_modalidade(n, lista_modalidades):
                            modalidade_prata.append(n)
                        else:
                            print('Atleta não aparticipou dessa modalidade!!')
                if bronze == 'S':#CASO TENHA GANHADO MEDALHA DE BRONZE
                    quantidade_bronze = int(input('Quantas medalhas de bronze? '))
                    for i in range(quantidade_bronze):
                        n = input(f'Qual a {i+1}° modalidades ganhou medalha de bronze: ').upper()
                        if verificar_modalidade(n, lista_modalidades):
                            modalidade_ouro.append(n)
                        else:
                            print('Atleta não aparticipou dessa modalidade!!')
            elif medalhas == 'N':# SE NAO GANHOU MEDALHAS
                ouro = 'N'
                prata = 'N'
                bronze = 'N'
        # CRIACAO DO ATLETA
            atle = atleta()
            atle.nome = nome
            atle.idade = idade
            atle.sexo = sexo
            atle.paralisia = paralisia
            atle.covid = covid
            atle.modalidades = lista_modalidades
            atle.medalhas = medalhas
            atle.modalidade_ouro = modalidade_ouro
            atle.modalidade_prata = modalidade_prata
            atle.modalidade_bronze = modalidade_bronze
            atletas[atle.nome] = atle
def editar(nome, atletas): #FUNCAO DE EDICAO DAS INFORMACOES DOS ATLETAS
    print('== O QUE DESEJA EDITAR? ==')
    print('1- Nome')
    print('2- Idade')
    print('3- Sexo')
    print('4- Paralisia')
    print('5- Covid')
    print('6- Modalidades')
    print('7- Medalhas')
    print('============================')
    edi= int(input())#FILTRA O QUE DESEJA EDITAR

    if edi == 1:# EDITAR NOME
        novo_nome = input('Digite o novo nome: ').upper()
        # try:
        atletas[novo_nome] = atletas[nome]
        atletas.pop(nome)
        atletas[novo_nome].nome= novo_nome
        print('Nome alterado!')
        # except RuntimeError:
        #     pass
    elif edi == 2: #EDITAR IDADE
        nova_idade = int(input('Digite a nova idade: '))
        atletas[nome].idade = nova_idade
        print('Idade alterada!')
    elif edi == 3:# EDITAR SEXO
        if atletas[nome].sexo == 'F':
            atletas[nome].sexo = 'M'
        elif atletas[nome].sexo == 'M':
            atletas[nome].sexo = 'F'
        print('Sexo alterado.')
    elif edi == 4:# EDITAR PARALISIA
        nova_paralisia = input('Digite o novo tipo de paralisia: ')
        atletas[nome].paralisia = nova_paralisia
        print('Tipo de paralisia alterado!')
    elif edi == 5:# EDITAR DIAGNÓSTICO DE COVID
        if atletas[nome].covid == 'S':
            atletas[nome].covid = 'N'
        elif atletas[nome].covid == 'N':
            atletas[nome].covid = 'S'
        print('Diagóstico de covid alterado.')
    elif edi == 6:# EDITAR MODALIDADES
        print('=== ESCOLHA UMA OPÇÃO ===')
        print('1- ADICIONAR')
        print('2- REMOVER MODALIDADE')
        print('==========================')
        editar_modali = int(input())#ADICIONAR OU REMOVER MODALIDADE

        if editar_modali == 1:# ADICIONAR MODALIDADE
            nova_modalidade = input('Qual modalidade deseja adicionar? ').upper()#MODALIDADE QUE DESEJA ADICIONAR
            atletas[nome].modalidades.append(nova_modalidade)
            ganhou_medalha = input('Ganhou medalha na modalidade {}? (S/N)'.format(nova_modalidade)).upper()# SE GANHOU MEDALHA NESSA MODALIDADE
            if ganhou_medalha == 'S':
                atletas[nome].medalhas = 'S'
                verificador = False
                while verificador == False:
                    print('Qual o tipo de medalha? Responda com "ouro", "prata" ou "bronze". ')#TIPO DE MEDALHA
                    medalha = input().upper()
                    if medalha == 'OURO':#SE FOR OURO
                        verificador = True
                        atletas[nome].modalidade_ouro.append(nova_modalidade)
                        print('Modalidade adicionada com sucesso!')
                    elif medalha == 'PRATA':#SE FOR PRATA
                        verificador = True
                        atletas[nome].modalidade_prata.append(nova_modalidade)
                        print('Modalidade adicionada com sucesso!')
                    elif medalha == 'BRONZE' :#SE FOR BRONZE
                        verificador = True
                        atletas[nome].modalidade_bronze.append(nova_modalidade)
                        print('Modalidade adicionada com sucesso!')
                    else:
                        print('Entrada invalida!!!')

        elif editar_modali ==2: #REMOVER UMA MODALIDADE
            remover_modalidade = input('Qual modalidade deseja remover? ').upper()
            # try:
            if remover_modalidade in atletas[nome].modalidades:
                atletas[nome].modalidades.remove(remover_modalidade)#REMOVER DA LISTA DE MODALIDADES
                if atletas[nome].modalidades:# SE GANHOU MEDALHAS REMOVER DA LISTA DE MEDALHAS
                    if remover_modalidade in atletas[nome].modalidade_ouro:
                        atletas[nome].modalidade_ouro.remove(remover_modalidade)
                    elif remover_modalidade in atletas[nome].modalidade_prata:
                        atletas[nome].modalidade_prata.remove(remover_modalidade)
                    elif remover_modalidade in atletas[nome].modalidade_bronze:
                        atletas[nome].modalidade_bronze.remove(remover_modalidade)
                    if atletas[nome].modalidade_ouro == False and atletas[nome].modalidade_prata == False and atletas[nome].modalidade_bronze == False:
                        atletas[nome].medalhas = 'N'
                    print('Modalidade removida.')
                else:#SE O ATLETA SO ESTAVA CADASTRADO EM UMA MODALIDADE ELE O CADASTRO DELE FOI REMOVIDO DO ARQUIVO
                    print('Cadastro do atleta removido, o atleta não está cadastrado em nenhuma modalidade.')
                    atletas.pop(nome)
            else:# SE A MODALIDADE NAO ESTAVA CADASTRADA
                print('Modalidade não encontrada.')
            # except RuntimeError:
            #     pass
    elif edi == 7: # EDITAR MEDALHAS
        print('=== ESCOLHA UMA OPÇÃO ===')
        print('1- ADICIONAR')
        print('2- REMOVER')
        print('3- REMOVER TODAS')
        print('==========================')
        editar_medalha = int(input())
        if editar_medalha ==1:#ADICIONAR MEDALHA
            print('Qual medalha deseja adicionar? Digite "ouro", "prata" ou "bronze".')#MEDALHA QUE DESEJA ADICIONAR
            tipo_medalha = input().upper()
            modalidade = input('Em qual modalidade ganhou a medalha? ').upper()#TIPO DE MEDALHA
            if modalidade in atletas[nome].modalidades:
                if tipo_medalha == 'OURO':
                    atletas[nome].medalhas = 'S'
                    atletas[nome].modalidade_ouro.append(modalidade)
                    print('Medalha adicionada com sucesso!')
                elif tipo_medalha == 'PRATA':
                    atletas[nome].medalhas = 'S'
                    atletas[nome].modalidade_prata.append(modalidade)
                    print('Medalha adicionada com sucesso!')
                elif tipo_medalha == 'BRONZE':
                    atletas[nome].medalhas = 'S'
                    atletas[nome].modalidade_bronze.append(modalidade)
                    print('Medalha adicionada com sucesso!')
            else:
                print('Modalidade não encontrada!')
        elif editar_medalha ==2 :#REMOVER UMA MEDALHA
            print('Qual medalha deseja remover? Digite "ouro", "prata" ou "bronze".')#QUAL O TIPO DE MEDALHA
            tipo_medalha = input().upper()
            modalidade = input('Deseja remover de qual modalidade? ').upper()#A MODALIDADE QUE GANHOU A MEDALHA
            if modalidade in atletas[nome].modalidades:
                if tipo_medalha == 'OURO':
                    if modalidade in atletas[nome].modalidade_ouro:
                        atletas[nome].modalidade_ouro.remove(modalidade)
                        print('Medalha removida com sucesso!')
                    else:#SE A MODALIDADE NAO POSSUI O TIPO DE MEDALHA QUE FOI DIGITADO
                        print('O atleta não possui medalha de ouro nesta modalidade!')
                elif tipo_medalha == 'PRATA':
                    if modalidade in atletas[nome].modalidade_prata:
                        atletas[nome].modalidade_prata.remove(modalidade)
                        print('Medalha removida com sucesso!')
                    else:
                        print('O atleta não possui medalha de prata nesta modalidade!')
                elif tipo_medalha == 'BRONZE':
                    if modalidade in atletas[nome].modalidade_bronze:
                        atletas[nome].modalidade_bronze.remove(modalidade)
                        print('Medalha removida com sucesso!')
                    else:
                        print('O atleta não possui medalha de bronze nesta modalidade!')
            if atletas[nome].modalidade_ouro == False and atletas[nome].modalidade_prata == False and atletas[nome].modalidade_bonze == False:
                atletas[nome].medalhas = 'N'
        elif editar_medalha == 3:#REMOVER TODAS AS MEDALHAS
            atletas[nome].medalhas = 'N'
            atletas[nome].modalidade_ouro = []
            atletas[nome].modalidade_prata = []
            atletas[nome].modalidade_bronze = []
            print('Todas as medalhas foram removidas!')
def topico01(atletas, modalidades):
#A quantidade total de atletas que participaram dos
# Jogos Paraolímpicos por modalidade e sexo,
# informando também o total geral;
    total_participacoes = len(atletas)#NUMERO DE ATLETAS QUE PARTICIPARAM
    participacoes_modalidades = []#MODALIDADES QUE TIVERAM PARTICIPACOES
    num_paricipacoes = []#NUMERO DE PARTICIPANTES POR MODALIDADE
    num_homens = 0#TOTAL DE HOMENS QUE PARTICIPARAM
    num_mulheres = 0#TOTAL DE MULHERES QUE PARTICIPARAM
    for i in modalidades:
        n = 0
        for j in atletas:
            if (i.upper() in atletas[j].modalidades):
                if  (i.upper() not in participacoes_modalidades):
                    participacoes_modalidades.append(i.upper())
                    n+=1
                else:
                    n+=1
        if (n != 0):
            num_paricipacoes.append(n)


    for j in atletas:
        if atletas[j].sexo == 'F':
            num_mulheres += 1
        if atletas[j].sexo == 'M':
            num_homens += 1

    with open('relatorio_atletas.txt', 'w') as relatorio:
        relatorio.write(f'\n{"="*100}\n')
        relatorio.write(f'O total de atletas que participaram das Paraolimpiadas de Tokio foi: {total_participacoes}\n'.upper())

    with open('relatorio_atletas.txt','a') as relatorio:
        for i in range(len(participacoes_modalidades)):

            relatorio.write(f'\nTotal de participantes na modalidade {participacoes_modalidades[i]}: {num_paricipacoes[i]}\n'.upper())
        relatorio.write(f'\nO numero de homens que participaram das paraolimpiadas: {num_homens}\n'.upper())
        relatorio.write(f'\nO numero de mulheres que participaram das paraolimpiadas: {num_mulheres}\n'.upper())
        relatorio.write(f'\n{"=" * 100}\n')
def topico02(atletas, modalidades):
# Relação dos atletas diagnosticados com Covid - 19 por modalidade e sexo;
    modalidades_covid = {}#MODALIDADES E RELACAO DE ATLETAS QUE TIVERAM COVID
    for j in modalidades:
        nomes = []
        for i in atletas:
            if j.upper() in atletas[i].modalidades:

                if atletas[i].covid == 'S':#VERIFICAR SE O ATLETA TEVE COVID
                    nomes.append(i)
        if nomes:
            modalidades_covid[j] = nomes

    sexos = ['M','F']
    sexo_covid = {}
    for j in sexos:
        nomes2 = []
        for i in atletas:
            if j == atletas[i].sexo and atletas[i].covid == 'S':
                nomes2.append(i)
        if nomes2:
            sexo_covid[j]= nomes2

    with open('relatorio_atletas.txt', 'a') as relatorio:

        for i in modalidades_covid:
            relatorio.write(f'\n{"=" * 100}\n')
            relatorio.write(f'\nRELACAO DOS ATLETAS DA MODALIDADE {i.upper()} QUE FORAM DIAGNOSTICADOS COM COVID-19:\n\n')
            for j in modalidades_covid[i]:
                relatorio.write(f'{j}\n')#PRINTA O NOME DO ATLETA
            relatorio.write(f'\n{"=" * 100}\n')

        for i in sexo_covid:
            if i == 'M':
                relatorio.write(f'\n{"=" * 100}\n')
                relatorio.write('\nRelacao dos atletas do sexo masculino que foram diagnosticados com covid-19:\n\n'.upper())
                for j in sexo_covid[i]:
                    relatorio.write(f'{j}\n')#PRINTA O NOME DO ATLETA
                relatorio.write(f'\n{"=" * 100}\n')
            elif i == 'F':
                relatorio.write(f'\n{"=" * 100}\n')
                relatorio.write('\nRelacao dos atletas do sexo feminino que foram daignosticados com covid-19:\n\n'.upper())
                for j in sexo_covid[i]:
                    relatorio.write(f'{j}\n')#PRINTA O NOME DO ATLETA
                relatorio.write(f'\n{"=" * 100}\n')
def topico03(atletas,modalidades):
    #Quadro de medalhas: quantitativo de medalhas de
    # ouro, prata e bronze por modalidade, ordenadas
    # primeiramente pelo número de medalhas de ouro,
    # seguidas pelo número de medalhas de prata,
    # finalmente, de bronze;
    with open('relatorio_atletas.txt', 'a') as relatorio:
        relatorio.write(f'\n{"=" * 100}\n')
        relatorio.write('\nRelacao das modalidades que conquistaram medalhas:\n \n'.upper())
    for j in modalidades:
        ouro = 0
        prata = 0
        bronze = 0
        verificador = False
        for i in atletas:
            if j.upper() in atletas[i].modalidades:#VERIFICAR SE O ATLETA PARTICIPOU DA MODALIDADE
                verificador = True
                if j.upper() in atletas[i].modalidade_ouro:#CONTAGEM DO NUMERO DE MEDALHAS EM DETERMINADA MODALIDADE
                    ouro+=1
                elif j.upper() in atletas[i].modalidade_prata:
                    prata+=1
                elif j.upper() in atletas[i].modalidade_bronze:
                    bronze+=1
        if verificador:
            with open('relatorio_atletas.txt', 'a') as relatorio:
                relatorio.write(f'  Medalhas da modalidade {j.upper()}\n'.upper())
                relatorio.write(f'  Ouro: {ouro}\n')
                relatorio.write(f'  Prata: {prata}\n')
                relatorio.write(f'  Bronze: {bronze}\n\n')
                relatorio.write(f'\n{"=" * 100}\n')
def topico04(atletas,modalidades):
# Um recorte por modalidade e por gênero (M/F) dos atletas que ganharam medalhas, com a informação do nome do atleta, idade, tipo de paralisia e medalha(s) conquistada(s).
    for j in modalidades:
        modali_masc=[]#ATLETAS HOMENS QUE GANHARAM MEDALHAS
        modali_femi = []#ATLETAS MULHERES QUE GANHARAM MEDALHAS
        verificador = False#INDICA SE O ATLETA PARTICIPOU DA MODALIDADE
        for i in atletas:
            if j.upper() in atletas[i].modalidades:#VERIFCAR SE O ATLETA PARTICIPOU DA MODALIDADE
                verificador = True
                if (atletas[i].medalhas == 'S') and atletas[i].sexo == 'M':
                    if atletas[i] not in modali_masc:
                        modali_masc.append(atletas[i])
                if (atletas[i].medalhas == 'S') and atletas[i].sexo == 'F':
                    if atletas[i] not in modali_femi:
                        modali_femi.append(atletas[i])
        if verificador == True:
            with open('relatorio_atletas.txt','a') as relatorio:
                if modali_masc:#VEERIFICAR SE TEVE PARTICIPAÇÃO MASCULINA
                    relatorio.write(f'\n{"=" * 100}\n')
                    relatorio.write(f'\nAtletas do sexo masculino da modalidade {j.upper()} que ganharam medalha:\n'.upper())
                    for k in range(len(modali_masc)):
                        relatorio.write(f'Atleta {k+1}:\n{modali_masc[k]}'.upper())
                        relatorio.write(f'\n{"=" * 100}\n')
                if modali_femi:#VERIFICAR SE TEVE PARTICIPAÇÃO FEMININA
                    relatorio.write(f'\n{"=" * 100}\n')
                    relatorio.write(f'\nAtletas do sexo feminino da modalidade {j.upper()} que ganharam medalha:\n'.upper())
                    for k in range(len(modali_femi)):
                        relatorio.write(f'Atleta {k + 1}:\n{modali_femi[k]}'.upper())
                        relatorio.write(f'\n{"=" * 100}\n')
def topico05(atletas,modalidades):
#     Das 22 modalidades disponíveis nos Jogos Paralímpicos de Tóquio, quantas o Brasil teve participação? Em quais modalidades ganhou medalha(s)? Quais modalidades que o Brasil participou e não ganhou medalha(s)? Quantas e quais modalidades o Brasil não participou? Apresentar as modalidades em ordem alfabética.
    part_modalidade= []
    modalidades_medalhas = []
    sem_particacao = []
    sem_medalhas = []
    for j in modalidades:
        for i in atletas:
            if j.upper() in atletas[i].modalidades:#VERIFICAR SE O ATLETA PARTICIPOU DA MODALIDADE
                if j not in part_modalidade:
                    part_modalidade.append(j)
                if atletas[i].medalhas:#SE O ATLETA GANHOU MEDALHA
                    if (j.upper() in atletas[i].modalidade_ouro) or (j.upper() in atletas[i].modalidade_prata) or (j.upper() in atletas[i].modalidade_bronze):
                        if j not in modalidades_medalhas:
                            modalidades_medalhas.append(j)

    for k in modalidades:#VERIFICAR MODALIDADES QUE O BRASIL NAO PARTICIPOU
            if k not in part_modalidade:
                sem_particacao.append(k)

    for g in part_modalidade:#MODALIDADES QUE O BRASIL PARTICIPOU MAS NAO GANHOU MEDALHAS
        if g not in modalidades_medalhas:
           sem_medalhas.append(g)

    #ORDENANDO AS LISTAS
    modalidades_medalhas.sort()
    sem_particacao.sort()
    sem_medalhas.sort()
    with open('relatorio_atletas.txt', 'a') as arquivo:
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write(f'\nDAS 22 MODALIDADES PARALIMPICOS O BRASIL PARTICIPOU DE {len(part_modalidade)} MODALIDADES. \n')
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write('\nRELACAO DAS MODALIDADES QUE GANHARAM MEDALHAS:\n')
        for i in modalidades_medalhas:
            arquivo.write(f'{i}\n'.upper())
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write('\nRELACAO DAS MODALIDADES QUE TIVERAM PARTICIPACAO MAS NAO GANHARAM MEDALHA:\n')
        if sem_medalhas:
            for i in sem_medalhas:
                arquivo.write(f'{i}\n'.upper())
        else:
            arquivo.write('NENHUMA\n')
        arquivo.write(f'\n{"=" * 100}\n')
        arquivo.write(f'\nO BRASIL NAO TEVE PARTICIPACAO EM {len(sem_particacao)} MODALIDADE(S), SENDO ELAS:\n')
        for i in sem_particacao:
            arquivo.write(f'{i}\n'.upper())
        arquivo.write(f'\n{"=" * 100}\n')
def verificar_modalidade(modali,modalidades):
    modali = modali.lower()
    for i in modalidades:
        if i.lower() == modali:
            return True
    return False


atletas = {}#DICIONARIO DOS ATLETAS
modalidades = ['atletismo','badminton','basquetebol em cadeira de rodas', 'bocha','canoagem','ciclismo estrada e pista','esgrima em cadeira de rodas', 'futebol de 5','goalball','hipismo','judo','levantamento de peso','natacao','remo','rugby em cadeira de rodas','taekwondo','tenis de mesa','tenis em cadeira de rodas','tiro','tiro com arco','triatlo','voleibol sentado']

try:#CASO O ARQUIVO JÁ TENHA SIDO CRIADO
    with open('dados_atletas.txt', 'rb') as arq:#ARQUIVO QUE IRA GUARDAR O DICIONARIO DE ATLETAS
        atletas = pickle.load(arq)
except FileNotFoundError:# SE O ARQUIVO AINDA NAO EXISTE O PROGRAMA SEGUE
    pass


print('=====BEM VINDO AO PROGRAMDA CADASTRAMENTO DE ATLETAS DA PARAOLIMPÍANDA DE TÓKIO=====')
print()
while True:#LOOP PRINCIPAL
    print('=== MENU===')
    print('1- CADASTRAR')
    print('2- EDITAR')
    print('3- EXCLUIR')
    print('4- RELATÓRIO')
    print('5- SAIR')
    print('=============')
    try:
        menu = int(input())
    except ValueError:
        print('A ENTRADA DEVE SER UM NUMERO INTEIRO DE 1 A 5')

    try:
        if menu == 1:#CADASTRAR ATLETAS
            cadastrar(atletas,modalidades)
        elif menu == 2:#EDITAR ATLETAS
            nome = input('QUAL O NOME DO ATLETA QUE DESEJA EDITAR? ').upper()
            if (nome  not in atletas) :
                print('O atleta não está cadastrado!!!')
            else:
                editar(nome, atletas)

        elif menu == 3:#EXCLUIR ATLETAS
            excluir_atleta = input('Qual atleta deseja excluir? ').upper()
            atletas.pop(excluir_atleta)
            print('Atleta excluido com sucesso!')

        elif menu == 4:#EXIBIR RELATORIO
            with open('relatorio_atletas.txt', 'r') as arquivo:
                relatorio = arquivo.read()
                print(relatorio)
        elif menu == 5:#SAIR DO PROGRAMA
            with open('dados_atletas.txt', 'wb') as arq:
                pickle.dump(atletas, arq)
            break
    except NameError:
        pass

# NO FINAL DE CADA CICLO DO LOOP O RELATÓRIO SERÁ ATUALIZADO E OS DADOS DOS ATLETAS SERÃO SALVOS
    topico01(atletas, modalidades)
    topico02(atletas, modalidades)
    topico03(atletas, modalidades)
    topico04(atletas, modalidades)
    topico05(atletas, modalidades)
    with open('dados_atletas.txt', 'wb') as arq:
        pickle.dump(atletas, arq)


