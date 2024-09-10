def adicionar_contatos(contato, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        favorito = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{favorito}] {nome} - {telefone} - {email}")
    return

def atualizar_nome_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):    
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone_contato
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
        print(f"Contato {indice_contato} atualizada para {novo_nome_contato} - {novo_telefone_contato}, {novo_email_contato}")
    else:
        print("Indice do contato invalido.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} favoritado")
    return

def visualizar_favoritos(contatos):
    print("Contatos favoritos.")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            favorito = "✓"
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. [{favorito}] {nome} - {telefone} - {email}")    
    return

def deletar_contatos(contatos, indice_contato):  
    indice_contato_ajustado = int(indice_contato) - 1
    del contatos[indice_contato_ajustado]   
    print("Contato apagado com sucesso.")
    return


contatos = []

while True:
    print("\nMenu do Lista de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar Contato")
    print("4. Favoritar Contato")
    print("5. Deletar Contato")
    print("6. Ver Contatos Favoritos")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome da contato que deseja adicionar: ")
        telefone = input("Digite o número de telefone do contato que deseja adicionar: ")
        email = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contatos(contatos, nome, telefone, email)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        atualizar_nome_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar: ")
        favoritar_contato(contatos, indice_contato)
    elif escolha == "5":        
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        deletar_contatos(contatos, indice_contato)
    elif escolha == "6":
        visualizar_favoritos(contatos)
    elif escolha == "7":
        break

print("Programa finalizado")