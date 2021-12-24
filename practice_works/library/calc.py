import math
import scipy.constants as const


class Calculus1:

    # Основні формули для розрахунку
    @staticmethod
    def get_ro(sigma):
        return 1 / sigma

    @staticmethod
    def get_sigma(n, tor_n, p, tor_p):
        return const.e * (n * tor_n + p * tor_p)

    # Додаткові формули
    @staticmethod
    def get_effective_mass(mx):
        return mx * const.m_e

    # Формули для значень квадрату концентрації власних носіїв
    def get_nc(self, mn, t):
        return 2 * math.pow(2 * const.pi * self.get_effective_mass(mn) * const.k * t / (const.h ** 2), 3 / 2)

    def get_nv(self, mp, t):
        return 2 * math.pow(2 * const.pi * self.get_effective_mass(mp) * const.k * t / (const.h ** 2), 3 / 2)

    @staticmethod
    def get_ni2(nc, nv, t, delta_e):
        return nc * nv * math.exp(-delta_e * const.e / (const.k * t))

    # Компенсовані напівпровідники - концентрація електронів та дірок
    @staticmethod
    def get_self_n(ni2):
        return math.sqrt(ni2)

    @staticmethod
    def get_self_p(ni2):
        return math.sqrt(ni2)

    # Компенсовані напівпровідники - концентрація електронів та дірок
    @staticmethod
    def get_compensate_n(na, nd, ni2):
        return (nd - na)/2 + math.sqrt((nd - na)**2 + 4*ni2)/2

    @staticmethod
    def get_compensate_p(na, nd, ni2):
        return (na - nd)/2 + math.sqrt((nd - na)**2 + 4*ni2)/2
