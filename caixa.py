'''O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas.
Para agilizar o cálculo de quanto cada cliente deve pagar
ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta.
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços
Você foi contratado para desenvolver o programa que monta esta tabela de preços,
que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
'''
#bibliotecas
from datetime import date #gerador de datas
hoje = date.today()

from time import sleep # faz parte  do bloco menu

from random import randint


valor_item = 1.99 # faz parte  do bloco menu
dinheiro = 0 # faz parte do bloco dos menus
quant_i = 0 #faz partge do bloco de menu master
click = 0 #faz parte do bloco de menu master
new_item = 0 #faz parte do bloco de menu master
soma_item = 0
lista_id = []
# bloco do login dos caixas
print("*"*50, "Atacadao do Manuel", "*"*50)
numero_caixa = 0
login_cad = "wembley"
senha_cad = "1234"




#bloco das  funcoes
def login (login_cad,senha_cad):
    trava = 0
    while trava != 1:
        trava = 0
        login_user = str(input("Digite o usuario:"))
        senha_user = str(input('Digite a senha:'))
        try:
         numero_caixa = int(input("Digite o numero do caixa:"))   # acessando o menu
        except ValueError:
            print("Caixas disponiveis 1 ate 8")
            continue
        if login_cad == login_user:
            if senha_user == senha_cad:
                trava = trava + 1
                print("Acessando o programa")
                return numero_caixa
        else:
         print("Usuario nao  cadastrado")
    return
def menu_opcao():
 while True:
    print('''
                    [1] Somar produtos/dinheiro :
                    [2] Somar produtos/credito + 3%:
                    [3] Somar produtos/debito + 1%
                    [4] Sair 
                    ''')
    try:
     click = int(input('Escolha uma das opcoes :'))
    except ValueError:
        print("="*40,"Digite somente numeros inteiro")
        continue
    if click == 1:
        dinheiro = soma_item * valor_item
        print("-"*40,"Valor da compra","="*20, f"R$ {dinheiro.__round__(2)}")
    if click == 2:
        sleep(1)
        print('Credito selecionado')
        dinheiro = soma_item * valor_item
        porcentagem_credito = (dinheiro * 3) / 100
        soma = dinheiro + porcentagem_credito
        print("-"*40,"Valor da compra","="*20, f"R$ {soma.__round__(2)}")
    if click == 3:
        sleep(1)
        print('Debito selecionado')
        dinheiro = soma_item * valor_item
        porcentagem_debito = (dinheiro * 1) / 100
        soma = dinheiro + porcentagem_debito
        print("-"*40,"Valor da compra","="*20, f"R$ {soma.__round__(2)}")
    if click == 4:
        break
def mudar_valor():
  while True:
    try:
     sleep(0.8)
     print("Opcao para alterar o valor dos itens foi selecionado")
     sleep(0.5)
     ask = int(input("Quantos intens teram o seu valor alterado? ->:"))
    except ValueError:
     print("=" * 40, "Somente numeros inteiros sao aceitos")
     continue
    try:
     new_valor_item = float(input("Digite o novo valor que o item recebera :"))
    except ValueError:
     print("=" * 40, "Somente numeros Reais sao aceitos (R$1.5,R$4.5....")
     continue
    print('''
                [1] Somar produtos/dinheiro :
                [2] Somar produtos/credito + 3%:
                [3] Somar produtos/debito + 1%
                ''')

    try:
     click = int(input('Escolha uma das opcoes :'))
    except ValueError:
      sleep(0.8)
      print("=" * 40, "Somente numeros inteiros sao aceitos")
      continue
    if click == 1:
        dinheiro = ask * new_valor_item
        sub = quant_i - ask
        dinheiro_2 = sub * valor_item
        soma = dinheiro + dinheiro_2
        print(f"Valor da compra {soma.__round__(3)}")
    if click == 2:
            sleep(1)
            print('Credito selecionado')
            dinheiro = ask * new_valor_item
            sub = quant_i - ask
            dinheiro_2 = sub * valor_item
            soma = dinheiro + dinheiro_2
            porcentagem_credito = soma * 3/100
            soma = soma + porcentagem_credito
            print('Valor da compra {}'.format(soma.__round__(2)))
    if click == 3:
            sleep(1)
            print('Debito selecionado')
            dinheiro = ask * new_valor_item
            sub = quant_i - ask
            dinheiro_2 = sub * valor_item
            soma = dinheiro + dinheiro_2
            porcentagem_debito = (soma * 1) / 100
            soma = soma +  porcentagem_debito
            print("Valor da compra {}".format(soma.__round__(2)))
    break
def caixa_sem_prioridades():
    while True:
        sleep(1.5)
        print('-'*50, f'{hoje.day}/{hoje.month}/{hoje.year}')
        print(' '*50, 'Caixa logado', f'{n_caixa}')
        print(
        '''         MENU
        [1] Somar produtos/dinheiro :
        [2] Somar produtos/debito + 1%
        [3] Adicionmar mais itens
        [4] Sair        
        '''
            )
        try:
         quant_i = int(input("Digite a quantidade de intem comprado:"))
         click = int(input("Digite o numero da opcao desejada: "))
        except ValueError:
         print("=" * 40, "Somente numeros inteiros sao aceitos")
         continue

        if click == 1:
            dinheiro = quant_i * valor_item
            sleep(1)
            print("="*20, 'Sua compra ficou em {}'.format(dinheiro.__round__(2)))
        if click == 2:
            sleep(1)
            print('Compra no debito selecionada')
            dinheiro  = quant_i * valor_item
            porcentagem_debito = (dinheiro*1)/100
            soma = dinheiro + porcentagem_debito
            print("="*20, "Valor total da  compra {}".format(soma.__round__(2)))
        if click == 4:
            print("Encerrando caixa")
            break
        if click == 3:
            print('Opcao para adicionar mais intem foi selecionada')
            new_item = int(input("Quantos intem a mais serao adicionados em sua lista:"))
            soma_item = (quant_i + new_item) * valor_item
            print("="*20, "Valor total da  compra {}".format(soma_item.__round__(2)))
        continue

def cadastrar_usuario():
 idi = (randint(1, 1000), randint(1, 1000))
 count = 0
 with open(f"{idi}.txt", "w") as arquivo:
    while True:
        a = str(input("Crie um nome de usuario:"))
        b = str(input("Crie uma senha numerica:"))
        arquivo.write(a)
        arquivo.write(b)
        arquivo.close()
        count = count + 1
        if count == 1:
         break
    sleep(1.2)
    print("="*30, ">", "Cadastro realizado com sucesso")
    pagina_inicial()

def pagina_inicial():
    print("="*40)
    print('''
    [1] Cadastrar usuarios
    [2] Fazer login
     ''')
    abrir = int(input("Escolha uma das opcoes :"))
    return abrir

a = pagina_inicial()
if a == 1:
     cadastrar_usuario()

elif a == 2:
    n_caixa = login(login_cad, senha_cad)
    if n_caixa == 1:
         while True:
            sleep(1.5)
            print('-'*50, f'{hoje.day}/{hoje.month}/{hoje.year}')
            print(' '*50, 'Usuario Master')
            print(
            '''         MENU
            [1] Somar produtos/dinheiro :
            [2] Somar produtos/credito + 3%:
            [3] Somar produtos/debito + 1%
            [4] Adicionar mais itens 
            [5] Mudar valor do produto      
            ''')
            try:
             quant_i = int(input("Digite a quantidade de intem comprado:"))
             click = int(input("Digite o numero da opcao desejada: "))
            except ValueError:
                print("Somente numeros inteiros sao aceitos")
            if click == 1:
                dinheiro = quant_i * valor_item
                sleep(1)
                print('Sua compra ficou em {}'.format(dinheiro.__round__(2)))
                break
            if click == 2:
                sleep(1)
                print("Compra no credito selecionada")
                dinheiro = quant_i * valor_item
                porcentagem_credito = (dinheiro*3)/100
                soma = dinheiro + porcentagem_credito
                print('Valor total da compra {}'.format(soma.__round__(2)))
                break
            if click == 3:
                sleep(1)
                print('Compra no debito selecionada')
                dinheiro = quant_i * valor_item
                porcentagem_debito = (dinheiro*1)/100
                soma = dinheiro + porcentagem_debito
                print("Valor total da  compra {}".format(soma.__round__(2)))
                break
            if click == 4:
                while True:
                    sleep(0.5)
                    print('Opcao para adicionar mais intem foi selecionada')
                    try:
                        sleep(0.5)
                        new_item = int(input("Quantos intem a mais serao adicionados em sua lista:"))
                    except ValueError:
                        sleep(0.5)
                        print("="*40, "Letras ou numeros reais (1.0, 2.0, 3.0 e etc...) nao sao acietos na operacao")
                        continue
                    soma_item = quant_i + new_item
                    sleep(1)
                    menu_opcao()
                    break
            if click == 5:
                sleep(0.5)
                mudar_valor()
                break
            elif n_caixa < 8:
                caixa_sem_prioridades()
            else:
             print('Quantidade de caixa nao existente na loja ')









