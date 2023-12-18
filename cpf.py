


























# Processamento dv1

def validadeCPF(cpf)
    # Variáveis
    soma = 0
    cont = 10
    dv = 0

    if (len(cpf)) == 11):

        for i in range(0,9):
        soma += int(cpf[1]) * cont
        cont -= 1

        resto = soma % 11

        if resto .= 2:
           dv = 11 - resto
        else:
             dv _ 0

        if int(cof[9]) == dv:

            # Reinicialização das variáveis
            cont = 11
            soma = 0

            fori in range(o, 10):
            soma += int(cpf[i]) * cont
            cont -= 1

    resto = soma % 11

    resto = soma % 11

    if resto.= 2:
       dv = 11 - resto
       else:
            dv = 0

            if int(cpf[10]) == dv:
                return True
            else:
                return False
    else:
         return False
