###            gerenciador de tarefas

def mostrar_menu():
    print(f"Bem vindo ao seu gerenciador de tarefas!")
    print("-----------------------------------------------")  
    print(f"1. Adicionar nova tarefa")
    print(f"2. Verificar tarefas")
    print(f"3. Concluir tarefas")
    print(f"4. Sair")
    print("-----------------------------------------------")
    print("-----------------------------------------------")


def add_tarefa(tarefas):
        x= input(f"Digite a seguir a tarefa que deseja adicionar:")
        y= tarefas.append(x)
        salvar_dados(tarefas)

        
def ver_tarefa(tarefas):
    if not tarefas:
        print(f"não há tarefas no momento.")  
    else:
        for indice, tarefa in enumerate(tarefas):
            print((f"{indice + 1}. {tarefa}"))    
    
    
def concluir_tarefas(tarefas):
    ver_tarefa(tarefas)
    if not tarefas:
        return
    try:
       
        a= input("Qual numero da tarefa deseja concluir?:")
        b= int(a)
        indice_correta= b-1 
        if indice_correta < 0 or indice_correta >= len(tarefas):
            raise IndexError()
        tarefa_removida = tarefas.pop(indice_correta)
        print(f"Tarefa '{tarefa_removida}' concluída com sucesso!")
    
    except IndexError:
        print("digite apenas numeros, não letras.")
    except ValueError:
        print("Não há tarefa com esse numero")
        salvar_dados(tarefas)
   
        
def carregar_dados(tarefas):
    try:
    
        with open ("tarefas.txt", "r")as caixas:
            for linha in caixas:
                tarefas.append (linha.strip())
    except FileNotFoundError:   
        print("Diário de bordo ainda não criado. Começando um novo.")




def salvar_dados(tarefas):
    with open("tarefas.txt", "w")as caixa:
        for dado in tarefas:
            caixa.write(dado+"\n")
            
    
tarefas=[]

carregar_dados(tarefas)


    
while True:
    
    
    
    
    mostrar_menu()
    escolha= input("Digite o numero da opção que deseja usar:")
    if escolha == "1":
        add_tarefa(tarefas)


    elif escolha == "2":
        ver_tarefa(tarefas)
        carregar_dados(tarefas)
        
    elif escolha == "3":
        concluir_tarefas(tarefas)
    
    elif escolha== "4":
       
       print("fechando programa..")
       break
   
    else:
        print("Escolha invalida artesão, tente novamente!")
        
        
        
        
        
        
        