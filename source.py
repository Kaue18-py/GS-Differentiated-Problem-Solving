"""
GS 2026.2 - Differentiated Problem Solving
Modelo: uso de tokens por hora da assistente virtual ao longo do dia.

x = horas desde as 7h (x = 0 -> 7h, x = 12 -> 19h)
r(x) = mil tokens por hora

ATENCAO: os dados abaixo sao SIMULADOS a partir de uma rotina tipica de idoso.
Troque a lista `tokens` pelos dados reais do grupo e rode de novo.
"""

import math

import numpy as np
import matplotlib.pyplot as plt


def br(valor, casas=2):
    """Formata um numero no padrao brasileiro (virgula decimal)."""
    return f"{valor:.{casas}f}".replace(".", ",")


# ---------------------------------------------------------------- dados
horas = np.arange(7, 20)          # 7h ate 19h
x = horas - 7                     # horas desde as 7h
tokens = np.array([5.2, 15.9, 24.3, 26.1, 23.2, 19.4, 15.6,
                   9.1, 6.2, 3.8, 6.7, 12.1, 24.8])  # mil tokens/h
