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
        return (nd - na) / 2 + math.sqrt((nd - na) ** 2 + 4 * ni2) / 2

    @staticmethod
    def get_compensate_p(na, nd, ni2):
        return (na - nd) / 2 + math.sqrt((nd - na) ** 2 + 4 * ni2) / 2


class Calculus2:

    # кількість електронів в р-типі НП
    @staticmethod
    def get_n_ptype(na, ni2):
        return -na / 2 + math.sqrt(na * na + 4 * ni2) / 2

    # кількість дірок в р-типі НП
    @staticmethod
    def get_p_ptype(na, ni2):
        return na / 2 + math.sqrt(na * na + 4 * ni2) / 2

    # кількість електронів в n-типі НП
    @staticmethod
    def get_n_ntype(nd, ni2):
        return nd / 2 + math.sqrt(nd * nd + 4 * ni2) / 2

    # кількість дірок в n-типі НП
    @staticmethod
    def get_p_ntype(nd, ni2):
        return -nd / 2 + math.sqrt(nd * nd + 4 * ni2) / 2

    # кількість електронів в власному НП
    @staticmethod
    def get_n_self(ni2):
        return math.sqrt(ni2)

    # кількість дірок в власному НП
    @staticmethod
    def get_p_self(ni2):
        return math.sqrt(ni2)

    @staticmethod
    def get_phiT(T):
        return const.k * T / const.e

    @staticmethod
    def get_phi0(phiT, na, nd, ni2):
        return phiT * math.log(na * nd / ni2, math.e)

    @staticmethod
    def get_junction_width(epsilon, na, nd, phi0):
        print(na, nd)
        return math.sqrt(2*const.epsilon_0*epsilon*(1/na + 1/nd)*phi0/const.e)

    @staticmethod
    def get_junction_n_width(junction_width, na, nd):
        return junction_width*nd/(na+nd)

    @staticmethod
    def get_junction_p_width(junction_width, na, nd):
        return junction_width*na/(na+nd)


class Calculus3:

    @staticmethod
    def get_n_p0(ni2, na):
        return ni2 / na

    @staticmethod
    def get_p_n0(ni2, nd):
        return ni2 / nd

    # тепловий струм
    def get_heat_current(self, S, Lp, ni2, Nd, t_p):
        return const.e * S * Lp * self.get_p_n0(ni2, Nd) / t_p

    # струм термогенерації
    def get_thermal_generation_current(self, S, l, ni2, t_ef):
        return 0.5 * const.e * S * l * math.sqrt(ni2) / t_ef
