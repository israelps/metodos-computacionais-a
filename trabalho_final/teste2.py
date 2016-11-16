from scipy.optimize import basinhopping

def V(r):
    potencial = 0
    sigma = 0.0025
    for i in range(len(r)):  # potencial da placa
        potencial += sigma  * e * r[i][0] / (80 * epsilon_0)
        for k in range(i + 1, len(r)):  # potencial entre os ions
            potencial += pow(e, 2) / (
                4 * pi * (80 * epsilon_0) * np.linalg.norm(r[i] - r[k]))
    return potencial
