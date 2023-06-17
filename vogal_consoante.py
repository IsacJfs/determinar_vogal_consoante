print("Identificador de vogal e consoante!")


def e_letra(letra):
    # Função criada para determinar se um caractere digitado é ou não uma lentra.
    if len(letra) > 1:
        # Conta a quantidade de caracteres digitados, caso maior do que um, informa que foi incorreto
        # N]ao foi utilizado raise, para que o programa não finalize.
        return "Erro, digite apenas uma"
    if letra.isalpha():
        # isalpha confere se o caractere é uma letra
        if letra in ['a', 'e', 'i', 'o', 'u']:
            # Confere se a letra é uma vogal, else: é uma consoante
            return f"Você digitou a vogal '{letra}'."
        else:
            return f"Você digitou a consoante '{letra}'."
    else:
        return f"O caractere digitado '{letra}' não é uma letra."


print(e_letra(input("digite uma letra: ")))  # Coleta o caractere que vai ser analisado.
