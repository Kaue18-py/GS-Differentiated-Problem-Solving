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

# ---------------------------------------------------------------- ajuste (grau 3)
coef_bruto = np.polyfit(x, tokens, 3)
a, b, c, d = np.round(coef_bruto, 3)   # coeficientes arredondados usados no relatorio
r = np.poly1d([a, b, c, d])
r1 = r.deriv()       # r'(x)
r2 = r.deriv(2)      # r''(x)
R = r.integ()        # primitiva


def hora(xv):
    """Converte x (horas desde as 7h) em texto de horario, ex.: 2.98 -> '9h59'."""
    total_min = round((7 + xv) * 60)
    return f"{total_min // 60}h{total_min % 60:02d}"


previsto = r(x)
ss_res = np.sum((tokens - previsto) ** 2)
ss_tot = np.sum((tokens - tokens.mean()) ** 2)
r_quadrado = 1 - ss_res / ss_tot

print("Modelo ajustado:")
print(f"r(x) = {a}x^3 + ({b})x^2 + {c}x + {d}   [mil tokens/h]")
print(f"R^2 = {r_quadrado:.4f}\n")

# ---------------------------------------------------------------- item 1: derivada em 3 pontos
# Unidade de r'(x): (mil tokens/h) por hora
print("Item 1 - derivada em 3 pontos  [mil tokens/h por hora]")
for xv in (1, 6, 10):
    v = r1(xv)
    sentido = "sobe" if v > 0 else "cai"
    print(f"  {hora(xv)} (x={xv}): r'({xv}) = {v:.3f}")
    print(f"    -> As {hora(xv)} o uso de tokens {sentido} com uma velocidade de "
          f"{br(abs(v))} mil tokens/h por hora.")

# ---------------------------------------------------------------- item 2: pontos criticos
print("\nItem 2 - pontos criticos (r'(x) = 0)")
criticos = sorted(xc.real for xc in r1.roots if abs(xc.imag) < 1e-9)
for xc in criticos:
    tipo = "MAXIMO local" if r2(xc) < 0 else "MINIMO local"
    print(f"  x = {xc:.3f} ({hora(xc)}): r = {r(xc):.3f} mil tokens/h, "
          f"r'' = {r2(xc):.3f} -> {tipo}")

# ---------------------------------------------------------------- item 3: integral
integral = R(12) - R(0)
print(f"\nItem 3 - integral de 0 a 12: {integral:.3f} mil tokens no dia")
print(f"  (media: {integral / 12:.3f} mil tokens por hora)")
print(f"  conferencia com trapezios nos dados: {np.trapezoid(tokens, x):.3f} mil tokens")

# ---------------------------------------------------------------- item 4: limite
# Adocao ao longo dos dias: U(n) = L * (1 - e^(-k n)), L = consumo de um dia tipico
k = 0.3
L = round(integral, 1)
print(f"\nItem 4 - limite do modelo de adocao U(n) = {L}(1 - e^(-{k}n))")
for n in (1, 7, 14, 30, 60):
    print(f"  n = {n:>2} dias: U = {L * (1 - math.exp(-k * n)):.2f} mil tokens/dia")
print(f"  lim n->inf U(n) = {L} mil tokens/dia")

# ---------------------------------------------------------------- grafico
xs = np.linspace(0, 12, 400)
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=160)
ax.plot(xs + 7, r(xs), color="#185FA5", lw=2, label="modelo r(x)")
ax.fill_between(xs + 7, r(xs), color="#185FA5", alpha=0.10, label="integral (tokens do dia)")
ax.scatter(horas, tokens, color="#D85A30", zorder=3, s=22, label="dados simulados")
for xc in criticos:
    ax.scatter(xc + 7, r(xc), color="black", zorder=4, s=40)
    rotulo = "máximo" if r2(xc) < 0 else "mínimo"
    ax.annotate(f"{rotulo}\n{hora(xc)}: {br(r(xc), 1)}", (xc + 7, r(xc)),
                textcoords="offset points", xytext=(0, 12 if r2(xc) < 0 else -30),
                ha="center", fontsize=8)
ax.set_xlabel("hora do dia")
ax.set_ylabel("mil tokens por hora")
ax.set_xticks(range(7, 20))
ax.set_ylim(0, 32)
ax.grid(alpha=0.25)
ax.legend(fontsize=8, loc="upper center", ncol=3, frameon=False)
fig.tight_layout()
fig.savefig("grafico_tokens.png")
print("\nGrafico salvo em grafico_tokens.png")

# ---------------------------------------------------------------- item 5: regra de alerta
# Resultado escolhido: a INTEGRAL (consumo esperado de um dia tipico).
# Pouca conversa com a assistente e sinal de isolamento ou mal-estar.
# Regra: se o consumo do dia ficar abaixo de 50% do esperado, o painel
# da familia mostra um alerta.
FRACAO_ALERTA = 0.5
limiar_alerta = FRACAO_ALERTA * integral


def verificar_alerta(consumo_dia):
    """Retorna a mensagem que aparece no painel da familia para o consumo do dia."""
    if consumo_dia < limiar_alerta:
        return (f"ALERTA: uso de {br(consumo_dia, 1)} mil tokens hoje, abaixo de "
                f"{br(limiar_alerta, 1)} mil. Vale ligar para ver se esta tudo bem.")
    return f"OK: uso de {br(consumo_dia, 1)} mil tokens hoje, dentro do esperado."


print(f"\nItem 5 - regra de alerta: limiar = {FRACAO_ALERTA:.0%} da integral "
      f"= {limiar_alerta:.1f} mil tokens/dia")
for exemplo in (170.0, 60.0):
    print(f"  consumo {exemplo:.1f} -> {verificar_alerta(exemplo)}")

# Limitacao: o modelo e um polinomio de grau 3, entao lim x->inf r(x) = +inf.
# Fora do intervalo 7h-19h ele preve uso crescendo sem parar, o que nao faz
# sentido (o idoso dorme). So vale dentro do intervalo dos dados.
print("\nLimitacao - fora do intervalo dos dados o modelo explode:")
for xv in (12, 14, 16):
    print(f"  r({xv}) = {r(xv):.1f} mil tokens/h ({hora(xv)})")
print("  lim x->inf r(x) = +inf  (coeficiente de x^3 positivo)")
