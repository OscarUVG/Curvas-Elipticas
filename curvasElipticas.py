import matplotlib.pyplot as plt

# Suma de dos puntos g1 y g1 en la curva eliptica sobre F_q
# con ecuacion y^2 = x^3 + ax + b.
def sum_points(g1, g2, q, a, b):
    
    # Alguno de los puntos es el neutro o los puntos son inversos entre ellos.
    if(g1 == float('inf')): g3 = g2
    elif(g2 == float('inf')): g3 = g1
    elif(g1[0] == g2[0] and g1[1] != g2[1]): g3 = float('inf')
    else:
        
        # Aplican las formulas usuales de suma de puntos
        if(g1 != g2):
            m = (g2[1] - g1[1]) * pow(g2[0] - g1[0], -1, q) % q
        else: 
            m = (3*g1[0]**2 + a) * pow(2*g1[1], -1, q) % q
            
        g3x = (m**2 - g1[0] - g2[0]) % q
        g3y = (m*(g1[0] - g3x) - g1[1]) % q
        g3 = (g3x, g3y)
    
    return g3

# Generacion del grupo dado por la curva eliptica sobre F_q
# con ecuacion y^2 = x^3 + ax + b, dado un generador g.
def construct_group(g, q, a, b):
    group = [g]
    while(group[-1] != float('inf') and len(group) <= 2*q + 1):
        g1 = sum_points(group[-1], g, q, a, b)
        group.append(g1)
    return group


#q, a, b = 37, 1, 0
#g = (2,2)

#=== Ejemplo ===
q, a, b = 29, 4, 20 # y^2 = x^3 + 4x + 20 sobre F29
g = (1,5)
group = construct_group(g, q, a, b)
print('=== Grupo E(F_%d) con E: y^2 = x^3 + %dx + %d ===' % (q, a, b))
print('Tamaño del grupo: %d\n' % len(group))
print(group)

# Grafico
x_coords = [g[0] for g in group[:-1]]
y_coords = [g[1] for g in group[:-1]]
plt.title('$y^2 = x^3 + %dx + %d $ sobre $\mathbb{F}_{%d}$' % (a, b, q))
plt.scatter(x_coords, y_coords, color='purple')
plt.plot(x_coords, y_coords, color='purple', alpha=0.5)
plt.show()





