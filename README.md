# GS Differentiated Problem Solving

Global Solution 2026.2 – FIAP – CitizenTech

## Contexto

O nosso projeto é uma assistente de IA para idosos. Esta parte do trabalho aplica cálculo
diferencial e integral (limites, derivadas, taxas de variação e integrais) para estimar
**quantos tokens a IA vai consumir e quanto isso vai custar**.

## Objetivo

- Ajustar uma função a dados **reais** de pelo menos 5 anos (2018 = Ano 1).
- Usar o modelo para analisar taxas de variação, comportamentos extremos e acumulações.
- Estimar o custo de tokens do app para atender o público idoso.

## Dados

Porcentagem de idosos (60+) que usam internet no Brasil, da PNAD Contínua TIC (IBGE),
de 2018 a 2025. 2020 fica de fora porque a pesquisa não foi divulgada nesse ano.
As fontes de cada ano estão em [geogebra_comandos.md](geogebra_comandos.md).

## Modelo

`p(t) = -0,2548t² + 7,3456t + 31,5262` (ajuste polinomial de grau 2, R² = 0,9985)

| Item | Resultado |
|---|---|
| Derivada | crescimento de 6,84 p.p./ano (2018), 4,80 (2022) e 3,27 (2025) |
| Ponto crítico | máximo de 84,5% em meados de 2031 |
| Integral | custo acumulado de tokens no período dos dados (2018–2025) ≈ US$ 1,2 milhão; previsão 2026–2031 também ≈ US$ 1,2 milhão |
| Limite | custo médio por usuário tende a US$ 0,86/ano |

## Estrutura

| Arquivo | Conteúdo |
|---|---|
| `ajuste_idosos_internet.py` | dados, ajuste, cálculos e gráficos |
| `geogebra_comandos.md` | os mesmos cálculos no GeoGebra e as fontes dos dados |
| `grafico_idosos_internet.png` | gráfico gerado pelo script |

## Como rodar

```
pip install -r requirements.txt
python ajuste_idosos_internet.py
```
