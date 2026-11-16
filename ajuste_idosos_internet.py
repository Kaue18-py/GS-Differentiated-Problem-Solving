"""
Global Solution 2026.2 - FIAP - Differentiated Problem Solving

Fenomeno modelado: porcentagem de idosos (60 anos ou mais) que usam a
internet no Brasil, ano a ano, e o custo de tokens de IA que o nosso
app teria para atender esse publico.

------------------------------------------------------------------ DADOS
Dados REAIS: IBGE - PNAD Continua, modulo TIC (Tecnologia da Informacao
e Comunicacao). Indicador: % de pessoas com 60 anos ou mais que
utilizaram a Internet no periodo de referencia.
    2018: 38,7%   2019: 44,8%   2021: 57,5%   2022: 62,1%
    2023: 66,0%   2024: 69,8%   2025: 74,5%
Nao ha divulgacao da PNAD TIC para 2020 (pandemia), entao esse ano
fica de fora. Nenhum dado foi inventado.

Convencao do enunciado: 2018 = Ano 1, 2019 = Ano 2, ...  (t = ano - 2017)

Como rodar:  python ajuste_idosos_internet.py
Precisa de:  numpy  (pip install -r requirements.txt)
"""

import numpy as np

# ------------------------------------------------------------------ dados reais (IBGE)
anos = np.array([2018, 2019, 2021, 2022, 2023, 2024, 2025])
t = anos - 2017                                   # Ano 1 = 2018
p_dados = np.array([38.7, 44.8, 57.5, 62.1, 66.0, 69.8, 74.5])   # % de idosos na internet


def ano(tv):
    return 2017 + tv


def fmt(v, casas=2):
    """Numero no formato brasileiro (1.234,56)."""
    s = f"{v:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


print("Dados reais (IBGE - PNAD Continua TIC):")
for an, tv, pv in zip(anos, t, p_dados):
    print(f"  {an} (t={tv}): {fmt(pv, 1)}% dos idosos usam internet")
print()
