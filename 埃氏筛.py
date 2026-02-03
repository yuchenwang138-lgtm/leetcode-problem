#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 15:56:02 2025

@author: macbook
"""

def sieve(n: int):
    if n < 1:
        return bytearray(b"\x00") * (n+1)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"         
    r = int(math.isqrt(n))
    for p in range(2, r + 1):
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)
    return is_prime