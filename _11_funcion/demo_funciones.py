'''
Created on 29/03/2013

@author: voval
'''

import primos

primos.ListarPrimos(2, 150)


num=193
print(num, ' es primo' if primos.EsPrimo(num) else 'no es primo')
