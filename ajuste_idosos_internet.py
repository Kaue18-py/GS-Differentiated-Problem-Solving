# Global Solution 2026.2 - FIAP - Differentiated Problem Solving
# Projeto: Lume (assistente virtual para idosos)
#
# Modelo: porcentagem de idosos (60+) que usam internet no Brasil e o
# custo de tokens de IA que a Lume teria para atender esse publico.
#
# Dados: IBGE - PNAD Continua TIC (2020 nao foi divulgado).
# Convencao do enunciado: 2018 = ano 1  ->  t = ano - 2017
#
# Tudo foi feito com calculo "na mao": o ajuste usa minimos quadrados
# (sistema de equacoes resolvido por eliminacao de Gauss), e a derivada,
# a integral e o limite usam as formulas que deduzimos no relatorio.
# A unica biblioteca e o matplotlib, so para desenhar o grafico.

import matplotlib.pyplot as plt

anos = [2018, 2019, 2021, 2022, 2023, 2024, 2025]
t = [ano - 2017 for ano in anos]
y = [38.7, 44.8, 57.5, 62.1, 66.0, 69.8, 74.5]

tokens_entrada = 1200
tokens_saida = 800
preco_entrada = 0.30 / 1000000
preco_saida = 2.50 / 1000000
populacao_idosos = 34100000
fatia = 0.01
custo_fixo = 6000


def br(numero, casas=2):
    texto = f"{numero:,.{casas}f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".")


def resolver_sistema(A, B):
    n = len(B)
    for i in range(n):
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            B[j] -= fator * B[i]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = B[i]
        for k in range(i + 1, n):
            soma -= A[i][k] * x[k]
        x[i] = soma / A[i][i]
    return x


def ajuste_polinomial(grau):
    A = [[sum(ti ** (i + j) for ti in t) for j in range(grau + 1)] for i in range(grau + 1)]
    B = [sum(yi * ti ** i for ti, yi in zip(t, y)) for i in range(grau + 1)]
    return resolver_sistema(A, B)


def valor(coef, x):
    return sum(c * x ** i for i, c in enumerate(coef))


def r_quadrado(coef):
    media = sum(y) / len(y)
    erro = sum((yi - valor(coef, ti)) ** 2 for ti, yi in zip(t, y))
    total = sum((yi - media) ** 2 for yi in y)
    return 1 - erro / total


print("Comparando os ajustes:")
for grau in (1, 2, 3):
    coef = ajuste_polinomial(grau)
    print(f"  grau {grau}: R^2 = {br(r_quadrado(coef), 4)}   previsao 2030: {br(valor(coef, 13), 1)}%")
print("  -> o grau 2 e o que melhor faz sentido (nao passa de 100%)\n")

c, b, a = [round(v, 4) for v in ajuste_polinomial(2)]


def p(x):
    return a * x ** 2 + b * x + c


def dp(x):
    return 2 * a * x + b


def d2p(x):
    return 2 * a


def primitiva(x):
    return a / 3 * x ** 3 + b / 2 * x ** 2 + c * x


print(f"Modelo: p(t) = {br(a, 4)}t^2 + {br(b, 4)}t + {br(c, 4)}")
print(f"R^2 = {br(r_quadrado([c, b, a]), 4)}\n")

print("Item 1 - derivada em 3 pontos (p.p. por ano)")
for x in (1, 5, 8):
    h = 0.0001
    taxa_media = (p(x + h) - p(x)) / h
    print(f"  {x + 2017}: p'({x}) = {br(dp(x))}   (pela definicao: {br(taxa_media)})")

t_critico = -b / (2 * a)
print("\nItem 2 - ponto critico")
print(f"  p'(t) = 0  ->  t = {br(t_critico, 3)}  (meados de {int(t_critico) + 2017})")
if d2p(t_critico) < 0:
    print(f"  p'' = {br(d2p(t_critico), 4)} < 0  ->  maximo de {br(p(t_critico))}%")
else:
    print(f"  p'' = {br(d2p(t_critico), 4)} > 0  ->  minimo de {br(p(t_critico))}%")

custo_dia = tokens_entrada * preco_entrada + tokens_saida * preco_saida
custo_ano = custo_dia * 365
k = populacao_idosos * fatia * custo_ano / 100

integral_dados = primitiva(8) - primitiva(1)
custo_dados = k * integral_dados
custo_previsao = k * (primitiva(14) - primitiva(9))

print("\nItem 3 - integral")
print(f"  custo por idoso: US$ {br(custo_dia, 5)}/dia = US$ {br(custo_ano, 4)}/ano")
print(f"  C(t) = {br(k)} * p(t)")
print(f"  integral de p de 1 a 8 = {br(integral_dados, 3)}")
print(f"  custo 2018-2025 = US$ {br(custo_dados)}")
print(f"  previsao 2026-2031 = US$ {br(custo_previsao)}  (US$ {br(custo_previsao / 5)} por ano)")

print("\nItem 4 - limite do custo medio por idoso: CM(N) = 6000/N + c")
for N in (100, 1000, 10000, 100000, 1000000):
    print(f"  N = {N:>9}: CM = US$ {br(custo_fixo / N + custo_ano, 4)}")
print(f"  quando N -> infinito, 6000/N -> 0, entao CM -> US$ {br(custo_ano, 4)} por ano")

xs = [1 + i * 0.05 for i in range(281)]
reta = ajuste_polinomial(1)

fig, (g1, g2) = plt.subplots(1, 2, figsize=(12, 4.5), dpi=150)

g1.scatter(anos, y, color="#1f4e79", zorder=3, label="Dados reais (IBGE)")
g1.plot([x + 2017 for x in xs], [p(x) for x in xs], color="#c0504d", lw=2, label="Modelo p(t) (grau 2)")
g1.plot([x + 2017 for x in xs], [valor(reta, x) for x in xs], color="gray", ls="--", lw=1,
        label="Reta (grau 1), comparação")
g1.scatter(t_critico + 2017, p(t_critico), color="black", zorder=4)
g1.annotate(f"Máximo: {br(p(t_critico), 1)}%\n(meados de {int(t_critico) + 2017})",
            (t_critico + 2017, p(t_critico)), textcoords="offset points", xytext=(0, 12),
            ha="center", fontsize=8)
g1.axhline(100, color="gray", lw=0.8)
g1.set_title("Idosos (60+) que usam internet no Brasil")
g1.set_xlabel("Ano")
g1.set_ylabel("% dos idosos")
g1.set_ylim(0, 110)
g1.grid(alpha=0.3)
g1.legend(fontsize=8, loc="lower right")

x_dados = [1 + i * 0.05 for i in range(141)]
x_prev = [9 + i * 0.05 for i in range(101)]
g2.plot([x + 2017 for x in xs], [k * p(x) / 1000 for x in xs], color="#c0504d", lw=2,
        label="C(t) = custo anual de tokens")
g2.fill_between([x + 2017 for x in x_dados], [k * p(x) / 1000 for x in x_dados], alpha=0.25,
                color="#1f4e79", label=f"Integral 2018–2025: US$ {br(custo_dados / 1000, 0)} mil")
g2.fill_between([x + 2017 for x in x_prev], [k * p(x) / 1000 for x in x_prev], alpha=0.15,
                color="#c0504d", hatch="//", label=f"Previsão 2026–2031: US$ {br(custo_previsao / 1000, 0)} mil")
g2.set_title("Custo de tokens da Lume (1% dos idosos conectados)")
g2.set_xlabel("Ano")
g2.set_ylabel("US$ mil por ano")
g2.set_ylim(0, 300)
g2.grid(alpha=0.3)
g2.legend(fontsize=8, loc="lower right")

fig.tight_layout()
fig.savefig("grafico_idosos_internet.png")
print("\nGrafico salvo em grafico_idosos_internet.png")
