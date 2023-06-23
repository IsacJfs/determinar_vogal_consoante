print("\nIdentificador de vogal e consoante!\n")


def e_letra(letra: str) -> tuple:
    """
    Determina se é uma letra e sendo se é uma vogal ou consoante.
    :arg:
        letra (str): Qualquer letra do alfabeto.
    :returns
        tuple: retorna uma tupla contendo a letra digitada e o tipo.
    :raise
        ValueError: quantidade de caracteres maior que um.
        TypeError: caractere digitado não é uma letra
    Exemplo:
    #   >>> e_letra('a')
         ('a', 'vogal')
    """
    tipo = ""
    try:
        if len(letra) > 1:
            # Conta a quantidade de caracteres digitados, caso maior do que um, informa que foi incorreto
            raise ValueError
        if letra.isalpha():
            # isalpha confere se o caractere é uma letra
            if letra in ['a', 'e', 'i', 'o', 'u']:
                # Confere se a letra é uma vogal, else: consoante
                tipo += "vogal"
            else:
                tipo += "consoante"
        else:
            raise TypeError
    except ValueError:
        print("Digite apenas um caractere.")
    except TypeError:
        print("O caractere digitado não é uma letra.")
    else:
        return letra, tipo


print(e_letra(input("digite uma letra: ")))  # Coleta o caractere que vai ser analisado.
