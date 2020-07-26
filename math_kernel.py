from sympy import *

RHO, L, X, EA = symbols('RHO, L, X, EA')
nsi = integrate(RHO * (X - EA * L)**2, (X, 0, L))

class Structure:
    def __init__(self):
        pass

class Sbeam(Structure):
    def __init__(self, r):
        self.r = r
        self.A = 3.14 * r ** 2
        self.I1 = 3.14 / 4 * r ** 4
        self.I2 = self.I1
        self.I12 = 0.0
        self.J = self.I1 * 2

class Mass:
    def __init__(self):
        pass

class Mslab(Mass):
    def __init__(self, rho, l, ea): #L = chord length, EA = percentage of elastic axis w.r.t. L
        self.NSM = rho * l
        self.NSI = float(nsi.subs({RHO:rho, L:l, EA:ea}))

def pbeam_gen(r, rho, l, ea, Sbeam, Mslab): #generates everything including and after A(A)
    beam = Sbeam(r)
    slab = Mslab(rho, l, ea)
    AA = beam.A
    l1A = beam.I1
    l2A = beam.I2
    l12A = beam.I12
    JA = beam.J
    NSMA = slab.NSM
    C1A = 0.0
    C2A = 0.0
    D1A = 0.0
    D2A = 0.0
    E1A = 0.0
    E2A = 0.0
    F1A = 0.0
    F2A = 0.0
    SO = 'YES'
    XB = 1.0
    A = beam.A
    l1 = beam.I1
    l2 = beam.I2
    l12 = beam.I12
    J = beam.J
    NSM = slab.NSM
    C1 = 0.0
    C2 = 0.0
    D1 = 0.0
    D2 = 0.0
    E1 = 0.0
    E2 = 0.0
    F1 = 0.0
    F2 = 0.0
    K1 = 0.0
    K2 = 0.0
    S1 = 0.0
    S2 = 0.0
    NSIA = slab.NSI
    NSIB = slab.NSI
    CWA = 0.0
    CWB = 0.0
    M1A = ea*l - .5*l
    M2A = 0.0
    M1B = M1A
    M2B = M2A
    N1A = M1A
    N2A = M2A
    N1B = M1B
    N2B = M2B

    return [AA, l1A, l2A, l12A, JA, NSMA, C1A, C2A, D1A, D2A, E1A, E2A, F1A, F2A,
            SO, XB, A, l1, l2, l12, J, NSM, C1, C2, D1, D2, E1, E2, F1, F2,
            K1, K2, S1, S2, NSIA, NSIB, CWA, CWB, M1A, M2A, M1B, M2B, N1A, N2A, N1B, N2B]


