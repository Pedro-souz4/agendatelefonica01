# Todas váriaveis
nome1 = nome2 = nome3 = nome4 = nome5 = ""
telefone1 = telefone2 = telefone3 = telefone4 = telefone5 = ""
email1 = email2 = email3 = email4 = email5 = ""
contatos_cadastrados = 0

# Loop base do programa
while True:
    print("--- Agenda Telefônica ---")
    print("1. Cadastrar novo contato")
    print("2. Visualizar todos os contatos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1" and contatos_cadastrados < 5:
        print("Cadastro de novo contato:")

        # Cadastro do nome
        while True:
            nome = input("Nome completo: ")
            nome_valido = True
            if nome == "":
                nome_valido = False
            else:
                contador = 0
                while contador < 3 and nome[contador:contador+1] != "":
                    contador += 1
                if contador < 3:
                    nome_valido = False
            if nome_valido:
                break
            print("Nome inválido. Deve ter pelo menos 3 caracteres.")

        # Cadastro do telefone
        while True:
            telefone = input("Número de telefone: ")
            telefone_valido = True
            contador = 0
            while telefone[contador:contador+1] != "":
                if telefone[contador:contador+1] < "0" or telefone[contador:contador+1] > "9":
                    telefone_valido = False
                    break
                contador += 1
            if contador < 8 or contador > 15:
                telefone_valido = False
            if telefone_valido:
                break
            print("Telefone inválido. Deve conter entre 8 e 15 dígitos numéricos.")

        # Cadastro do email
        while True:
            email = input("Email: ")
            email_valido = False
            contador = 0
            arroba_encontrado = False
            while email[contador:contador+1] != "":
                if email[contador:contador+1] == "@":
                    arroba_encontrado = True
                    break
                contador += 1
            if arroba_encontrado:
                contador += 1
                while email[contador:contador+1] != "":
                    if email[contador:contador+1] == ".":
                        email_valido = True
                        break
                    contador += 1
            if email_valido:
                break
            print("Email inválido. Deve conter '@' e um domínio válido.")

        # Armazenamento dos dados
        if contatos_cadastrados == 0:
            nome1, telefone1, email1 = nome, telefone, email
        elif contatos_cadastrados == 1:
            nome2, telefone2, email2 = nome, telefone, email
        elif contatos_cadastrados == 2:
            nome3, telefone3, email3 = nome, telefone, email
        elif contatos_cadastrados == 3:
            nome4, telefone4, email4 = nome, telefone, email
        else:
            nome5, telefone5, email5 = nome, telefone, email

        contatos_cadastrados += 1
        print(f"Contato cadastrado com sucesso! Total de contatos: {contatos_cadastrados}")

    elif opcao == "2":
        print("Contatos cadastrados:")
        if contatos_cadastrados == 0:
            print("Nenhum contato cadastrado.")
        else:
            if nome1 != "":
                print(f"1. Nome: {nome1}, Telefone: {telefone1}, Email: {email1}")
            if nome2 != "":
                print(f"2. Nome: {nome2}, Telefone: {telefone2}, Email: {email2}")
            if nome3 != "":
                print(f"3. Nome: {nome3}, Telefone: {telefone3}, Email: {email3}")
            if nome4 != "":
                print(f"4. Nome: {nome4}, Telefone: {telefone4}, Email: {email4}")
            if nome5 != "":
                print(f"5. Nome: {nome5}, Telefone: {telefone5}, Email: {email5}")

    elif opcao == "3" or contatos_cadastrados == 5:
        print("Lista final de contatos:")
        if contatos_cadastrados == 0:
            print("Nenhum contato foi cadastrado.")
        else:
            if nome1 != "":
                print(f"1. Nome: {nome1}, Telefone: {telefone1}, Email: {email1}")
            if nome2 != "":
                print(f"2. Nome: {nome2}, Telefone: {telefone2}, Email: {email2}")
            if nome3 != "":
                print(f"3. Nome: {nome3}, Telefone: {telefone3}, Email: {email3}")
            if nome4 != "":
                print(f"4. Nome: {nome4}, Telefone: {telefone4}, Email: {email4}")
            if nome5 != "":
                print(f"5. Nome: {nome5}, Telefone: {telefone5}, Email: {email5}")
        break

    else:
        print("Opção inválida.")