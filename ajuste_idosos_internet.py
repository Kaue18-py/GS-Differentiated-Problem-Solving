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

# ------------------------------------------------------------------ comparacao de modelos
def r2(modelo):
    prev = modelo(t)
    return 1 - np.sum((p_dados - prev) ** 2) / np.sum((p_dados - p_dados.mean()) ** 2)


print("Comparacao de modelos (mesmo que FitPoly(list, n) no GeoGebra):")
for n in (1, 2, 3):
    m = np.poly1d(np.polyfit(t, p_dados, n))
    print(f"  grau {n}: R^2 = {fmt(r2(m), 4)}   previsao 2030 (t=13): {fmt(m(13), 1)}%")
print("  -> grau 1 passa de 100% por volta de 2030 e grau 3 tambem dispara;")
print("     o grau 2 se ajusta bem E faz sentido (crescimento que desacelera).\n")

# ------------------------------------------------------------------ modelo escolhido: grau 2
a, b, c = np.round(np.polyfit(t, p_dados, 2), 4)
p = np.poly1d([a, b, c])        # p(t)  [% de idosos na internet]
p1 = p.deriv()                  # p'(t) [pontos percentuais por ano]
p2 = p.deriv(2)                 # p''(t)

print("Modelo ajustado:")
print(f"  p(t) = {fmt(a, 4)}t^2 + {fmt(b, 4)}t + {fmt(c, 4)}   [%]")
print(f"  R^2 = {fmt(r2(p), 4)}\n")

# ------------------------------------------------------------------ item 1: derivada (taxa de variacao)
print("Item 1 - Derivada em 3 pontos: p'(t) = "
      f"{fmt(2 * a, 4)}t + {fmt(b, 4)}  [pontos percentuais por ano]")
for tv in (1, 5, 8):
    print(f"  {ano(tv)} (t={tv}): p = {fmt(p(tv))}%   p'({tv}) = {fmt(p1(tv))} p.p./ano")
print("  -> o crescimento continua positivo, mas cada vez mais lento.\n")

# ------------------------------------------------------------------ item 2: ponto critico (extremo)
t_crit = -b / (2 * a)            # p'(t) = 0  ->  2at + b = 0
tipo = "MAXIMO" if p2(t_crit) < 0 else "MINIMO"
print("Item 2 - Ponto critico (p'(t) = 0):")
print(f"  2*({fmt(a, 4)})t + {fmt(b, 4)} = 0  ->  t = {fmt(t_crit, 3)}  (meados de {ano(int(t_crit))})")
print(f"  p({fmt(t_crit, 3)}) = {fmt(p(t_crit))}%   p'' = {fmt(p2(t_crit), 4)} < 0  ->  {tipo}")
print("  -> o modelo preve que o uso entre idosos para de crescer em ~84%.")
print("     Depois disso a parabola desce, o que nao e realista: o modelo vale ate ~2031.\n")
