import math
## set vars ##
g = 2
h = 893
modulus = 1373
baby_steps = {}
giant_steps = {}

n = 1 + math.floor(math.sqrt(modulus-1))
print(n)

for i in range(n):
    baby_steps[i] = pow(g, i, modulus)

print(baby_steps)
print()


## g^(-1*n), and assuming g and modulus are relatively prime
inverse = pow(g, (modulus-2)*n, modulus)
print(inverse)

for j in range(n): 
    giant_steps[j] =  (h*pow(inverse, j)) % modulus
    

print(giant_steps)
print()

for keyq in baby_steps:
    for keyp in giant_steps:
        if baby_steps[keyq] == giant_steps[keyp]:
            x = keyq+(keyp*n)
            print('discrete log: ', x)
            
            

