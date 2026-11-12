# GS 2026.2 — Differentiated Problem Solving

**CitizenTech:** _(nome a definir)_

**Problema:** idosos sofrem com isolamento e sedentarismo. Uma assistente de voz num tablet conversa com eles, guia exercícios e faz um check-up de mobilidade pela câmera. Os resultados vão para um painel que a família acompanha.

**Modelo:** `r(x)` = uso de tokens da assistente (mil tokens por hora), com `x` = horas desde as 7h (de 7h a 19h).

> Os dados em `source.py` são **simulados** a partir de uma rotina típica de idoso. Para usar dados reais, troque a lista `tokens` e rode de novo. Todos os resultados e o gráfico são recalculados.

## Integrantes

| Nome completo | RM |
|---|---|
| _a preencher_ | |
| _a preencher_ | |
| _a preencher_ | |
| _a preencher_ | |

## Como rodar

```bash
pip install -r requirements.txt
python source.py
```

O script imprime os resultados de cada item e salva o gráfico em `grafico_tokens.png`.

## Resultados (dados simulados)

Modelo ajustado (grau 3, R² = 0,993):

```
r(x) = 0,192x³ − 3,462x² + 15,515x + 4,821
```

| Item | Resultado |
|---|---|
| 1. Derivada | r'(1) = 9,17 (8h, subindo) · r'(6) = −5,29 (13h, caindo) · r'(10) = 3,88 (17h, subindo) — em mil tokens/h por hora |
| 2. Pontos críticos | máximo às 9h59 (25,4 mil tokens/h) · mínimo às 16h03 (4,0 mil tokens/h) |
| 3. Integral de 0 a 12 | 176,1 mil tokens no dia (média de 14,7 mil tokens/h) |
| 4. Limite | U(n) = 176,1(1 − e^(−0,3n)) → lim n→∞ U(n) = 176,1 mil tokens/dia |
| 5. Decisão | a integral vira o limiar de alerta: consumo do dia abaixo de 50% (88,1 mil tokens) gera alerta no painel da família |

**Limitação:** o modelo é um polinômio de grau 3, então lim x→∞ r(x) = +∞. Fora do intervalo de 7h a 19h ele prevê um uso que cresce sem parar (às 23h daria 153 mil tokens/h), o que não acontece porque o idoso dorme. Ele só vale dentro do intervalo dos dados.

## GeoGebra

Comandos para colar no GeoGebra online (em português, entre parênteses):

```
pontos = {(0, 5.2), (1, 15.9), (2, 24.3), (3, 26.1), (4, 23.2), (5, 19.4), (6, 15.6), (7, 9.1), (8, 6.2), (9, 3.8), (10, 6.7), (11, 12.1), (12, 24.8)}
FitPoly(pontos, 3)                      (AjustePolinomial)
r(x) = 0.192x^3 - 3.462x^2 + 15.515x + 4.821
r'(1)
r'(6)
r'(10)
Extremum(r, 0, 12)                      (Extremo)
Integral(r, 0, 12)
U(n) = 176.1 (1 - exp(-0.3 n))
Limit(U, ∞)                             (Limite)
```

Link público: _a preencher_
