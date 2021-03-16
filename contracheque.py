# API de Contra Cheques

import os
import random


def Id(diretorio):
    ident = ''
    for i in range(11):
        b = random.randint(0, 9)
        ident = ident + str(b)

    arq = open(diretorio, 'a')
    arq.write(ident + '\n')
    l = arq.read()
    arq.close()
    lista = l.split('\n')

    return ident, lista


class API:
    def __init__(self, ident, nome, sobre, doc, setor, bruto, admissao, saude, dental, vale_trans, dive):
        self.Id = ident
        self.nome = nome
        self.sobrenome = sobre
        self.CPF = doc
        self.setor = setor
        self.salario_bruto = bruto
        self.salario_liquido = self.salario_bruto
        self.data_admissao = admissao
        self.op_saude = saude
        self.op_dental = dental
        self.vale_transporte = vale_trans
        self.list = [self.Id]
        self.diretorio = dive
        self.data_mes = ''
        self.dicionario = None

