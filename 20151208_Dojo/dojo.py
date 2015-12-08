#!/usr/share/python
# _*_ coding UTF-8 _*_
def suicidio(pessoas, primeiro, intervalo):
    sobrevivente = 0
    contaPessoas = 0
    

    for i in range(0, pessoas):
        if contaPessoas < intervalo:
            contaPessoas = contaPessoas + 1
            print "escapou!! xuxu %s" % i

        if contaPessoas == intervalo:
            print "morreu %s" % i
            contaPessoas = 0

    return

def testaargumentos():
    if argumentos() > 0:
        print "OK"
    else:
        print "NOK"

def argumentos():
    pessoas = raw_input("Defina o numero de pessoas")
    primeiro = raw_input("Quem sera o primeiro a morrer?")
    intervalo = raw_input("Defina o numero de intervalo do suicidio")

    pessoas = int(pessoas)
    primeiro = int(primeiro)
    intervalo = int(intervalo)

    if pessoas <= 0:
        print "O numero de pessoas deve ser maior que 0"
    elif pessoas <= 0:
        print "Valor invalido"
    elif primeiro > pessoas:
        print "Valor invalido"
    elif intervalo <= 0:
        print "O intervalo precisa ser maior que 0"
    else:
        suicidio(pessoas, primeiro, intervalo)


    return False

testaargumentos()





