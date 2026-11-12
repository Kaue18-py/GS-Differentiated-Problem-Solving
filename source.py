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
