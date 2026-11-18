# Comandos para o GeoGebra

Digite um comando por linha no campo de entrada de https://www.geogebra.org/calculator
(use **ponto** como separador decimal).

## 1. Pontos (dados reais do IBGE, 2018 = Ano 1)

```
A = (1, 38.7)
B = (2, 44.8)
C = (4, 57.5)
D = (5, 62.1)
E = (6, 66)
F = (7, 69.8)
G = (8, 74.5)
```

2020 (Ano 3) não entra porque a PNAD TIC não foi divulgada nesse ano.

## 2. Ajuste (igual ao PDF do professor)

```
n = 2
list = {A, B, C, D, E, F, G}
p(x) = FitPoly(list, n)
```

Resultado esperado: `p(x) ≈ -0.2548x² + 7.3456x + 31.5262`

Para comparar, mude `n` para 1 e depois para 3. A reta passa de 100% por volta de 2030,
e por isso o grau 2 é o que faz mais sentido.

## 3. Cálculo

```
p'(x)                                  # derivada: -0.5096x + 7.3456
p'(1)                                  # 2018: ≈ 6.84 p.p./ano
p'(5)                                  # 2022: ≈ 4.80 p.p./ano
p'(8)                                  # 2025: ≈ 3.27 p.p./ano
Extremum(p, 1, 20)                     # máximo: (14.41, 84.47) -> meados de 2031
Integral(2937.37 p(x), 1, 8)           # custo acumulado 2018-2025 (intervalo dos dados): ≈ US$ 1.200.413
Integral(2937.37 p(x), 9, 14)          # previsão extra 2026-2031: ≈ US$ 1.200.981
Limit((6000 + 0.8614x) / x, ∞)         # custo médio por usuário: 0.8614
```

O símbolo `∞` está no teclado virtual do GeoGebra (aba de símbolos).

## Fontes dos dados

IBGE, PNAD Contínua, módulo TIC. Indicador: % de pessoas de 60 anos ou mais que
utilizaram a Internet.

| Ano | t | % | Onde foi divulgado |
|---|---|---|---|
| 2018 | 1 | 38,7 | [IBGE – PNAD Contínua TIC 2018](https://agenciadenoticias.ibge.gov.br/agencia-sala-de-imprensa/27515-pnad-continua-tic-2018-internet-chega-a-79-1-dos-domicilios-do-pais.html) |
| 2019 | 2 | 44,8 | [Agência Brasil, ago/2024](https://agenciabrasil.ebc.com.br/geral/noticia/2024-08/uso-de-internet-no-pais-cresce-mais-entre-idosos-mostra-ibge) |
| 2021 | 4 | 57,5 | PNAD TIC 2022, divulgada em 09/11/2023 ([Mercado & Consumo](https://mercadoeconsumo.com.br/09/11/2023/economia/de-cada-100-brasileiros-87-usavam-internet-em-2022/)) |
| 2022 | 5 | 62,1 | PNAD TIC 2022, divulgada em 09/11/2023 ([Mercado & Consumo](https://mercadoeconsumo.com.br/09/11/2023/economia/de-cada-100-brasileiros-87-usavam-internet-em-2022/)) |
| 2023 | 6 | 66,0 | [Agência Brasil, ago/2024](https://agenciabrasil.ebc.com.br/geral/noticia/2024-08/uso-de-internet-no-pais-cresce-mais-entre-idosos-mostra-ibge) |
| 2024 | 7 | 69,8 | [IBGE – PNAD TIC 2024](https://agenciadenoticias.ibge.gov.br/pt/agencia-noticias/44033-pela-primeira-vez-mais-da-metade-da-populacao-acessa-a-internet-pela-tv.html?lang=pt-BR) |
| 2025 | 8 | 74,5 | [IBGE – PNAD TIC 2025](https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/47408-proporcao-de-usuarios-da-internet-no-pais-ultrapassou-90-da-populacao-de-10-anos-ou-mais-em-2025) |

Na divulgação de 2025, o IBGE revisou 2024 para 70,1% e 2019 para 44,9%. Usamos os valores
publicados originalmente em cada ano. Trocar pelos revisados quase não muda o ajuste.

Preço dos tokens: tabela oficial do Gemini, https://aistudio.google.com/docs/pricing
(gemini-3.5-flash-lite: US$ 0,30 / 1M tokens de entrada, US$ 2,50 / 1M de saída, nov/2026).
