import datetime

def menu():
    mensagem = ("Horario de da Quadra")
    print("*" * 30)
    print("Horario de da Quadra")
    print("*" * 30)

def formulario():
    while True:
        horario = input("Digite as horas de entrada na quadra no formato HH:MM: ") # Variavel que vai guardar a entrada do usuario
        try:
            horario_entrada = datetime.datetime.strptime(horario, "%H:%M").time() # Estrutura que faz a conversão da entrada para horas e minutos
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma hora válida.") # Retorna a mensagem informando que não foi convertido para hora.
    
    while True:
        saida = input("Digite as horas de saida da quadra no formato HH:MM: ") # Variavel que vai guardar a entrada do usuario
        try:
            horario_saida = datetime.datetime.strptime(saida, "%H:%M").time() # Estrutura que faz a conversão da entrada para horas e minutos
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma hora válida.") # Retorna a mensagem informando que não foi convertido para hora.
            
    while True:
        valor = input("Informe o valor da hora reservada:")  #Variavel que vai guardar o aluguel por hora
        try:
            total_pago = float(valor.replace(",",".")) # Estrutura que faz a conversão para valores fracionados
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite uma hora válida.") # Retorna a mensagem informando que não foi convertido para valores fracionados.
            
    data_entrada = datetime.datetime.now().date() # Data atual como data de entrada
    data_saida = datetime.datetime.now().date()   # Data atual como data de saída    
    
    if horario_entrada == horario_saida:
        duracao = 24 # Duração é de 24 horas
    elif horario_entrada > horario_saida:
        data_saida += datetime.timedelta(days=1) # Incrementa um dia na data de saída
        diferenca = datetime.datetime.combine(data_saida, horario_saida) - datetime.datetime.combine(data_entrada, horario_entrada)
        duracao = diferenca.total_seconds() / 3600 # transforma a duração em horas
    else:
        diferenca = datetime.datetime.combine(data_saida, horario_saida) - datetime.datetime.combine(data_entrada, horario_entrada)
        duracao = diferenca.total_seconds() / 3600 # transforma a duração em horas
        
    total = duracao * total_pago
    
    print(f"Total a pagar: R${total:.2f}")
    print(f"Você ficou {duracao:.2f} horas na quadra.")
    
while True:
    menu()
    formulario()


