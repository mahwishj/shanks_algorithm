import math
## set vars ##
g = 2
h = 974
modulus = 1373
g_powers = {}
h_inverses = {}

n = 1 + math.floor(math.sqrt(modulus-1))
print(n)

for i in range(n):
    g_powers[i] = pow(g, i, modulus)

print(g_powers)
print()


## g^(-1*n), and assuming g and modulus are relatively prime
inverse = pow(g, (modulus-2)*n, modulus)

for j in range(n): 
    h_inverses[j] =  (h*pow(inverse, j)) % modulus
    

print(h_inverses)
print()

for keyq in g_powers:
    for keyp in h_inverses:
        if g_powers[keyq] == h_inverses[keyp]:
            x = keyq+(keyp*n)
            print('discrete log: ', x)
            
            

