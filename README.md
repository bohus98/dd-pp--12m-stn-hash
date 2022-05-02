# dd-pp--12m-stn-hash
# generators
## PRNG
Trieda zodpovedná za obsah atribútov a metód spoločných pre PRNG
### get_list_of_primes
Funkcia, ktorá vráti zoznam prvočísel až po hodnotu „max“ pomocou sitovej metódy Eratosthenes
### are_coprimes
Skontroluje, či sú hodnoty v1 a v2 rovnaké
## BBS
Algoritmus Blum Blum Shub.
Zdedí nadradenú triedu PRNG
### get_n
Metóda použitá na generovanie n, čo je súčin násobenia prvočísel p a q.
Kontroluje modulo 4 == 3, hodnota väčšia ako jedna 
prah (používa sa na generovanie veľkých čísel), okrem toho 
aby sa skontrolovalo, či p a q sú navzájom rovnaké čísla.
### generate_number
Metóda používaná na efektívne generovanie pseudonáhodných čísel.
is_default označuje, či sa majú použiť hodnoty
predtým nastavené p a q, kde p = 70891 a q = 85247.
Ak je hodnota nepravda, použie na to funkciu get_n().
generuje hodnoty p a q, čím sa zvyšuje zložitosť algoritmu.

Efektívny je každý krok vykonávania algoritmu
## LCG
Algoritmus lineárneho kongruenciálneho generátora.
Zdedí nadradenú triedu PRNG.

Vykonáva všetky kontroly podľa pravidiel
algoritmu pre premenné m, a, c a x0.

dĺžka a x0 budú priradené k zdedeným atribútom
triedy PRNG self.length a self.seed.
### generate_number
Efektívne generuje pseudonáhodné číslo
ekvivalentného algoritmu a nakonfigurovaných atribútov
v konštruktore triedy.
## MT
Algoritmus Mersenne Twister.
# main
Pomocou náhodne vybraného seedu generujem pseudonáhodné čísla pococou funkcii z generators
### all_lengths
List definujúci bitovú dĺžku čísel generovaných funkciou BBS.
Pre náš prípad nastavené na dĺžku 2
### BBS 
Vráti bitstring o dĺžke 2.
### LCG
Pomocou bitovej dĺžky a ďalších atribútov vygeneruje pseudo náhodné číslo.
Pre dĺžku = 2, bude dĺžka LCG 12
### MD5 Hash
Zahashovanie samostatného LCG pomocou MD5 hashu.
Bohužiaľ sa zmení dĺžka výsledného stringu.
