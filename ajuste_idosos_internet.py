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

------------------------------------------------------------------ HIPOTESES (declaradas)
- Consumo medio: 2000 tokens/dia por idoso (teste com o Gemini gratuito),
  divididos em 1200 de entrada + 800 de saida.
- Preco: gemini-3.5-flash-lite, US$ 0,30 por 1M tokens de entrada e
  US$ 2,50 por 1M de saida (tabela oficial Google AI Studio, nov/2026).
- Populacao de 60+: 34,1 milhoes, considerada constante
  (IBGE 2023: 22,5 milhoes de idosos usuarios = 66%).
- Fatia de mercado do app: 1% dos idosos que usam internet.
- Custo fixo de infraestrutura: US$ 6.000 por ano (servidor etc.).

Como rodar:  python ajuste_idosos_internet.py
Precisa de:  numpy e matplotlib  (pip install -r requirements.txt)
"""

import numpy as np
import matplotlib.pyplot as plt

anos = np.array([2018, 2019, 2021, 2022, 2023, 2024, 2025])
t = anos - 2017
p_dados = np.array([38.7, 44.8, 57.5, 62.1, 66.0, 69.8, 74.5])

TOKENS_ENTRADA_DIA = 1200
TOKENS_SAIDA_DIA = 800
PRECO_ENTRADA = 0.30 / 1_000_000
PRECO_SAIDA = 2.50 / 1_000_000
POP_60_MAIS = 34_100_000
FATIA_MERCADO = 0.01
CUSTO_FIXO_ANO = 6000.0

custo_usuario_dia = TOKENS_ENTRADA_DIA * PRECO_ENTRADA + TOKENS_SAIDA_DIA * PRECO_SAIDA
custo_usuario_ano = custo_usuario_dia * 365


def ano(tv):
    return 2017 + tv


def fmt(v, casas=2):
    s = f"{v:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


print("Dados reais (IBGE - PNAD Continua TIC):")
for an, tv, pv in zip(anos, t, p_dados):
    print(f"  {an} (t={tv}): {fmt(pv, 1)}% dos idosos usam internet")
print()


def r2(modelo):
    prev = modelo(t)
    return 1 - np.sum((p_dados - prev) ** 2) / np.sum((p_dados - p_dados.mean()) ** 2)


print("Comparacao de modelos (mesmo que FitPoly(list, n) no GeoGebra):")
for n in (1, 2, 3):
    m = np.poly1d(np.polyfit(t, p_dados, n))
    print(f"  grau {n}: R^2 = {fmt(r2(m), 4)}   previsao 2030 (t=13): {fmt(m(13), 1)}%")
print("  -> grau 1 passa de 100% por volta de 2030 e grau 3 tambem dispara;")
print("     o grau 2 se ajusta bem E faz sentido (crescimento que desacelera).\n")

a, b, c = np.round(np.polyfit(t, p_dados, 2), 4)
p = np.poly1d([a, b, c])
p1 = p.deriv()
p2 = p.deriv(2)
P = p.integ()

print("Modelo ajustado:")
print(f"  p(t) = {fmt(a, 4)}t^2 + {fmt(b, 4)}t + {fmt(c, 4)}   [%]")
print(f"  R^2 = {fmt(r2(p), 4)}\n")

print("Item 1 - Derivada em 3 pontos: p'(t) = "
      f"{fmt(2 * a, 4)}t + {fmt(b, 4)}  [pontos percentuais por ano]")
for tv in (1, 5, 8):
    print(f"  {ano(tv)} (t={tv}): p = {fmt(p(tv))}%   p'({tv}) = {fmt(p1(tv))} p.p./ano")
print("  -> o crescimento continua positivo, mas cada vez mais lento.\n")

t_crit = -b / (2 * a)
tipo = "MAXIMO" if p2(t_crit) < 0 else "MINIMO"
print("Item 2 - Ponto critico (p'(t) = 0):")
print(f"  2*({fmt(a, 4)})t + {fmt(b, 4)} = 0  ->  t = {fmt(t_crit, 3)}  (meados de {ano(int(t_crit))})")
print(f"  p({fmt(t_crit, 3)}) = {fmt(p(t_crit))}%   p'' = {fmt(p2(t_crit), 4)} < 0  ->  {tipo}")
print("  -> o modelo preve que o uso entre idosos para de crescer em ~84%.")
print("     Depois disso a parabola desce, o que nao e realista: o modelo vale ate ~2031.\n")

k = POP_60_MAIS * FATIA_MERCADO * custo_usuario_ano / 100
t_ini, t_fim = 9, 14
custo_acumulado = k * (P(t_fim) - P(t_ini))
print("Item 3 - Integral (custo acumulado de tokens):")
print(f"  custo por idoso: US$ {fmt(custo_usuario_dia, 5)}/dia = US$ {fmt(custo_usuario_ano)}/ano")
print(f"  C(t) = {fmt(k)} * p(t)   [US$/ano]")
print(f"  usuarios do app em 2026: {fmt(POP_60_MAIS * FATIA_MERCADO * p(9) / 100, 0)}")
print(f"  integral de C(t) de t={t_ini} ({ano(t_ini)}) a t={t_fim} ({ano(t_fim)}) = "
      f"US$ {fmt(custo_acumulado)}\n")

print("Item 4 - Limite do custo medio por usuario:")
print("  CM(N) = (CUSTO_FIXO + c*N) / N = CUSTO_FIXO/N + c")
for N in (100, 1_000, 10_000, 100_000, 1_000_000):
    cm = (CUSTO_FIXO_ANO + custo_usuario_ano * N) / N
    print(f"  N = {fmt(N, 0):>9}: CM = US$ {fmt(cm, 4)}/ano")
print(f"  lim N->inf CM(N) = c = US$ {fmt(custo_usuario_ano, 4)} por idoso por ano")
print("  -> com muitos usuarios, o custo fixo se dilui e sobra so o custo dos tokens.")

ts = np.linspace(1, 15, 300)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), dpi=150)

reta = np.poly1d(np.polyfit(t, p_dados, 1))
ax1.scatter(anos, p_dados, color="#1f4e79", zorder=3, label="Dados reais (IBGE)")
ax1.plot(ts + 2017, p(ts), color="#c0504d", lw=2, label="Modelo p(t) (grau 2)")
ax1.plot(ts + 2017, reta(ts), color="gray", ls="--", lw=1, label="Reta (grau 1), comparação")
ax1.scatter(t_crit + 2017, p(t_crit), color="black", zorder=4)
ax1.annotate(f"Máximo: {fmt(p(t_crit), 1)}%\n(meados de {ano(int(t_crit))})",
             (t_crit + 2017, p(t_crit)), textcoords="offset points", xytext=(0, 12),
             ha="center", fontsize=8)
ax1.axhline(100, color="gray", lw=0.8)
ax1.set_title("Idosos (60+) que usam internet no Brasil")
ax1.set_xlabel("Ano")
ax1.set_ylabel("% dos idosos")
ax1.set_ylim(0, 110)
ax1.grid(alpha=0.3)
ax1.legend(fontsize=8, loc="lower right")

tc = np.linspace(t_ini, t_fim, 200)
tp = np.linspace(8, 15, 200)
ax2.plot(tp + 2017, k * p(tp) / 1000, color="#c0504d", lw=2, label="C(t) = custo anual de tokens")
ax2.fill_between(tc + 2017, k * p(tc) / 1000, alpha=0.2, color="#c0504d",
                 label=f"Integral {ano(t_ini)}–{ano(t_fim)}: US$ {fmt(custo_acumulado / 1000, 0)} mil")
ax2.set_title("Custo de tokens do app (1% dos idosos conectados)")
ax2.set_xlabel("Ano")
ax2.set_ylabel("US$ mil por ano")
ax2.set_ylim(0, 300)
ax2.grid(alpha=0.3)
ax2.legend(fontsize=8, loc="lower right")

fig.tight_layout()
fig.savefig("grafico_idosos_internet.png")
print("\nGrafico salvo em grafico_idosos_internet.png")
