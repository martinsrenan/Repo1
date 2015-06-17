#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""		Exercicio 1
	Prints all the numbers from 1 to 100,
	except the ones that are divisible by 3.
"""

def numeros():
	for i in range(1,101):
		if i % 3 != 0:
			print i
numeros()
