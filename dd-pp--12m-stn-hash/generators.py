# -*- coding: utf-8 -*-

import random


class PRNG(object):
    """
        Pseudorandom Number Generator.
        Trieda zodpovedná za obsah atribútov a metód spoločných pre PRNG

        self.seed =  seed, ktorý sa má použiť v generátore, musí mať
                skutočne náhodnú hodnotu

        self.length = veľkosť čísla, ktoré sa má vygenerovať

    """
    def __init__(self, seed, length):
        self.seed = seed
        self.length = length

    """
        Vráti zoznam prvočísel až po hodnotu „max“
        pomocou sitovej metódy Eratosthenes
    """

    def get_list_of_primes(self, max):
        primes = list()
        not_primes = list()
        for i in range(2, max + 1):
            if i not in not_primes:
                primes.append(i)
                for j in range(i * i, max + 1, i):
                    not_primes.append(j)
        return primes


    """
        Skontroluje, či sú hodnoty v1 a v2 rovnaké
    """
    def are_coprimes(self, v1, v2):
        while v2 != 0:
            v1, v2 = v2, (v1 % v2)
        return v1 == 1

class BBS(PRNG):
    """
        Algoritmus Blum Blum Shub.
        Zdedí nadradenú triedu PRNG.
    """
    def __init__(self, seed, length):
        super(BBS, self).__init__(seed, length)

    """
        Metóda použitá na generovanie n, čo je súčin
        násobenie prvočísel p a q.

        Kontroluje modulo 4 == 3, hodnota väčšia ako jedna
        prah (používa sa na generovanie veľkých čísel), okrem toho
        aby sa skontrolovalo, či p a q sú navzájom rovnaké čísla.
    """
    def get_n(self):
        # minimálna hodnota pre hodnotu p a q
        threshold = 7000
        # vráti zoznam prvočísel do 100 000
        primes = self.get_list_of_primes(10000)
        while True:
            p = random.choice(primes)
            # skontroluje zvolené číslo
            if (((p % 4) == 3) and p > threshold):
                break
        while True:
            q = random.choice(primes)
            # skontroluje zvolené číslo
            if (((q % 4) == 3) and q > threshold):
                # kontroluje co-primes
                if ((p != q) and self.are_coprimes(self.seed, p*q)):
                    break
        return p * q


    """
        Metóda používaná na efektívne generovanie čísla
        pseudonáhodný.

        is_default označuje, či sa majú použiť hodnoty
        predtým nastavené p a q, kde p = 70891 a q = 85247.
        Ak je hodnota nepravda, použie na to funkciu get_n().
        generuje hodnoty p a q, čím sa zvyšuje zložitosť algoritmu.

        Efektívny je každý krok vykonávania algoritmu

    """
    def generate_number(self, is_default=True):
        if is_default:
            p = 70891
            q = 85247
            n = p * q
        else:
            n = self.get_n()
        x = list()
        b = list()
        x.append((self.seed ** 2) % n) # priradenie x[0]
        for i in range(self.length):
            # priradenie Xi podľa algoritmu
            x.append((x[-1]**2) % n)
            # alokácia Bi podľa algoritmu
            b.append(x[-1] % 2)
        # Hodnoty skupiny Bi ako reťazec do
        # set self.generated_number, premennej kde
        # sa pseudonáhodné číslo uloží
        # koniec generovania.
        self.generated_number = ''.join(map(str, b))
        return True


class LCG(PRNG):
    """
        Algoritmus lineárneho kongruenciálneho generátora.
        Zdedí nadradenú triedu PRNG.

        Vykonáva všetky kontroly podľa pravidiel
        algoritmu pre premenné m, a, c a x0.

        dĺžka a x0 budú priradené k zdedeným atribútom
        triedy PRNG self.length a self.seed.
    """
    def __init__(self, length, m, a, c, x0):
        if m <= 0:
            raise ValueError('m must be > 0')
        if a <= 0:
            raise ValueError('a must be > 0')
        if a >= m:
            raise ValueError('a must be < m')
        if c < 0:
            raise ValueError('c must be >= 0')
        if c >= m:
            raise ValueError('c must be < m')
        if x0 < 0:
            raise ValueError('x0 must be >= 0')
        if c >= m:
            raise ValueError('x0 must be < m')
        self.m = m
        self.a = a
        self.c = c
        super(LCG, self).__init__(x0, length)


    """
        Efektívne generuje pseudonáhodné číslo
        ekvivalentného algoritmu a nakonfigurovaných atribútov
        v konštruktore triedy.
    """
    def generate_number(self):
        x = list()
        # Pridá „seed“ k počiatočnej hodnote X
        x.append(self.seed)
        # Podľa požadovanej veľkosti vygeneruje hodnoty
        # ktoré musia byť zreťazené
        for i in range(self.length):
            # Pridajte do X výpočet ((a*X(n-1) + c) mod m))
            # podľa pravidiel algoritmu
            x.append((self.a * x[-1] + self.c) % self.m)
        # uloží vygenerované pseudonáhodné číslo do premennej
        # self.generated_number
        self.generated_number = ''.join(map(str,x))



class MT(PRNG):
    """
        Algoritmus Mersenne Twister.

    """
    def __init__(self, seed):
        super(MT, self).__init__(seed)