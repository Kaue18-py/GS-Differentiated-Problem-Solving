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
As fontes de cada ano estão na seção [Fontes dos dados](#fontes-dos-dados).

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
| `grafico_idosos_internet.png` | gráfico gerado pelo script |

## Como rodar

```
pip install -r requirements.txt
python ajuste_idosos_internet.py
```

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
