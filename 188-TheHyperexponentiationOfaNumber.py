#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=188

a = 1
for i in range(1855):
    b = pow(1777,a,10**8)
    a = b
print(a)
