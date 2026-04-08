print("Quantas strings começam com a letra 'a'")

menu = 1
str_list = []
str_list_lettea = []
while menu == 1:
    user_string = input("Digite uma palavra (digite 'sair' para encerrar): ")
    str_list.append(user_string)
    if user_string == 'sair':
        str_list.remove('sair')
        for str_atual in str_list:
            if str_atual[0].lower() == 'a':
                str_list_lettea.append(str_atual)
        print(f"Lista original: {str_list}.")
        print(f"Lista que começa com A: {str_list_lettea}.")