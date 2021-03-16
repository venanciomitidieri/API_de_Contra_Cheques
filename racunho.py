# API de Contracheques

import os
from os import makedirs
from os import mkdir
import random


def Id(diretorio):
    ident = ""
    for i in range(11):
        b = random.randint(0, 9)
        ident += str(b)

    arq = open(diretorio, "a")
    arq.write(ident + "\n")
    l = arq.read()
    arq.close()
    lista = l.split("\n")

    return ident, lista


class API:
    def __init__(self, ident, nom, sob, doc, se, bruto, admissao, saude, dental, vale_trans, dive):
        self.Id = ident
        self.nome = nom
        self.sobrenome = sob
        self.CPF = doc
        self.setor = se
        self.salario_bruto = bruto
        self.salario_liquido = self.salario_bruto
        self.data_admissao = admissao
        self.op_saude = saude
        self.op_dental = dental
        self.vale_transporte = vale_trans
        self.lista = [self.Id]
        self.diretorio = dive
        self.data_mês = ""
        self.dicionario = None


    def Verifica_cpf(self):
        nove_digitos = self.CPF[:-2]
        soma = 0
        st = ""
        for i, n in enumerate(nove_digitos):
            soma = soma + (int(n)) * (10 - i)
        divid = (soma * 10) % 11
        dois_digitos = self.CPF[-2:]
        if (divid == 10):
            divid = 0
        string = str(divid)
        st += string
        nove_digitos = nove_digitos + string
        soma2 = 0

        for k, l in enumerate(nove_digitos):
            soma2 = soma2 + (int(l)) * (11 - k)
        divid2 = (soma2 * 10) % 11
        if (divid2 == 10):
            divid2 = 0
        string2 = str(divid2)
        st += string2

        verifica = st in dois_digitos

        sinal = 0
        numer = 0
        while (sinal == 0) and (numer < 9):
            conta = self.CPF.count(str(numer))
            if (conta >= 11):
                sinal = 1
            numer = numer + 1

        sinaliza = sinal in range(1)

        if (verifica == True) and (sinaliza == True):
            return True
        else:
            return False


    def Descontos(self):
        descont = 0
        descont2 = 0
        if (self.salario_bruto <= 1045):
            descont = (self.salario_bruto * 7.5) / 100
            self.salario_liquido = self.salario_liquido - descont
        elif (self.salario_bruto > 1045) and (self.salario_bruto <= 2089.6):
            descont = (self.salario_bruto * 9) / 100
            self.salario_liquido = self.salario_liquido - descont
        elif (self.salario_bruto > 2089.6) and (self.salario_bruto <= 3134.4):
            descont = (self.salario_bruto * 12) / 100
            self.salario_liquido = self.salario - liquido - descont
        elif (self.salario_bruto > 3134.4) and (self.salario_bruto <= 6101.06):
            descont = (self.salario_bruto * 14) / 100
            self.salario_liquido = self.salario_liquido - descont

        self.lista.append(descont)

        if (self.salario_bruto >= 1903.99) and (self.salario_bruto < 2826.66):
            descont2 = (self.salario_bruto * 7.5) / 100
        elif (self.salario_bruto >= 2826.66) and (self.salario_bruto < 3751.06):
            descont2 = (self.salario_bruto * 15) / 100
        elif (self.salario_bruto >= 3751.06) and (self.salario_bruto <= 4664.68):
            descont2 = (self.salario_bruto * 22.5) / 100
        elif (self.salario_bruto > 4664.68):
            descont2 = (self.salario_bruto * 27.5) / 100

        if ((self.salario_bruto >= 1903.99) and (self.salario_bruto < 2826.66)) and (descont2 > 142.8):
            descont2 = 142.8
        elif ((self.salario_bruto >= 2826.66) and (self.salario_bruto < 3751.06)) and (descont2 > 354.8):
            descont2 = 354.8
        elif ((self.salario_bruto >= 3751.06) and (self.salario_bruto <= 4664.68)) and (descont2 > 636.13):
            descont2 = 636.13
        elif (self.salario_bruto > 4664.68) and (descont2 > 869.36):
            descont2 = 869.36

        self.salario_liquido = self.salario_liquido - descont2
        self.lista.append(descont2)

        if (self.op_saude == True):
            self.salario_liquido = self.salario_liquido - 10
            self.lista.append(10)
        else:
            self.lista.append(0)

        if (self.op_dental == True):
            self.salario_liquido = self.liquido_liquido - 5
            self.lista.append(5)
        else:
            self.lista.append(0)

        if (self.vale_transporte == True) and (self.salario_bruto >= 1500):
            des = (self.salario_bruto * 6) / 100
            self.salario_liquido = self.salario_liquido - des
            self.lista.append(des)
        else:
            self.lista.append(0)

        FGTS = (self.salario_bruto * 8) / 100
        self.salario_liquido = self.salario_liquido - FGTS
        self.lista.append(FGTS)

    def Arquivos(self):
        endereco = self.diretorio + "/" + self.Id
        d = mkdir(endereco)
        l = ["INSS", "IRRF", "Plano de saúde", "Plano dental", "Vale transporte", "FGTS"]

        arq = open(endereco + "/" + self.Id + ".txt", "w")
        arq.write(self.data_mês + "\n")
        arq.write("\n")
        arq.write("Tipo\tValor\tDescrição\n")
        arq.write("\n")
        bruto = "%0.2f" % self.salario_bruto
        arq.write("Remuneracao\t" + bruto + "\tSalário\n")
        arq.write("\n")

        soma = 0
        for i, n in enumerate(self.lista):
            if (n > 0):
                c = "%0.2f" % n
                arq.write("Desconto\t" + c + "\t" + l[i] + "\n")
            soma = soma + n
        arq.write("\n")
        som = "%0.2f" % soma
        som = "-" + som

        arq.write("Salario bruto\t" + bruto + "\n")
        arq.write("\n")
        arq.write("Total de descontos\t" + som + "\n")
        arq.write("\n")
        converte = "%0.2f" % self.salario_liquido
        arq.write("Salario liquido\t" + converte + "\n")
        arq.close()

        def Dicionario(self):
            ident, lista = Id(self.diretorio)

        # Importar biblioteca que gera números aleatóriamente-Ok!
        # Estudar comandos que criam pasta, pasta dentro de pasta, e arquivo dentro de subpasta-Ok!
        ##Criar uma única pasta, e criar uma subpasta para cada funcionário-Ok!
        # Criar os comandos de desconto, armazenar cada desconto em uma lista e escrever em um arquivo-Ok!
        # O nome do arquivo será o id do funcionário-Ok!
        # Criar função que gera Id para ser guardado e processado (os Ids serão usados como chave)
        # Criar método que cria data e mês para recebimento do primeiro sálario
        # Criar um método para fazer GET dos dados de cada funcionário
