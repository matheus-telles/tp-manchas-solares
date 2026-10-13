# ☀️ Manchas Solares — Análise de Ciclos Solares em Python

[![Abrir no navegador](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://matheus-telles.github.io/tp-manchas-solares/lab/index.html?path=TP_Matheus_de_Sousa.ipynb)

Trabalho prático da disciplina **DCC001 – Programação de Computadores** (UFMG, 2º semestre de 2025), cursada quando eu ainda estava em Engenharia de Minas. Professor: José de Siqueira.

**Nota do trabalho:** 116,8 · **Nota final na disciplina:** 100/100 (a soma das notas chegou a 148,5 por causa do trabalho e foi limitada ao máximo de 100)

O projeto é um notebook Jupyter interativo que lê os dados oficiais de manchas solares do [SILSO/SIDC](https://www.sidc.be/silso/) (Royal Observatory of Belgium), calcula a média suavizada de 13 meses, detecta os ciclos solares automaticamente e compara o resultado com os ciclos oficiais, usando testes estatísticos.

## Contexto

O número de manchas solares sobe e desce em ciclos de cerca de 11 anos, causados pela atividade magnética do Sol. Os registros mensais existem desde 1749 e as observações diárias passaram a ser constantes a partir de 1818. O objetivo do trabalho era usar Python como ferramenta científica: identificar quando cada ciclo solar começa e termina e comparar os ciclos calculados com os oficiais. O enunciado completo está em [`tp-manchas-solares.pdf`](tp-manchas-solares.pdf).

## Funcionalidades

A interface (feita com `ipywidgets`) tem quatro abas:

| Aba | O que faz |
|---|---|
| **Análise de Período** | Máximo diário, máximo e mínimo mensal e meses com média zero em um intervalo escolhido, com gráfico dos dados mensais e da curva suavizada |
| **Ciclos Solares** | Detecta ciclos por 4 métodos (mínimo a mínimo, máximo a máximo, cruzamento ascendente e descendente da média), aplica um teste estatístico em cada ciclo e plota os ciclos calculados junto com os oficiais |
| **Estatística** | Teste t de Welch entre dois ciclos oficiais e teste Qui-Quadrado (com Kolmogorov–Smirnov como alternativa) de um ciclo contra o histórico |
| **Consultas** | Média anual, média mensal, valor de um dia, dias sem manchas em um mês e média/desvio padrão calculados a partir dos dados diários |

## Metodologia

- **Média suavizada (SIDC):** janela de 13 meses com peso 0,5 nos meses das pontas e peso 1 nos 11 centrais. Meses sem dados ficam fora da conta e o denominador é ajustado.
- **Detecção de ciclos:** extremos locais da série suavizada dentro de uma janela de vizinhança configurável (padrão de 36 meses), com tolerância numérica e tratamento de platôs.
- **Testes estatísticos:** t de Welch para comparar médias; Qui-Quadrado para comparar a distribuição de atividade (faixas 0–50, 50–150 e 150+); KS quando o Qui-Quadrado não é aplicável (frequências esperadas menores que 5).

## Resultado

Com o método mínimo a mínimo e a janela padrão, os mínimos detectados ficam a poucos meses das datas oficiais de início de cada ciclo, do ciclo 2 (1766) ao ciclo 25 (2019). A conclusão foi que definir os ciclos pelos mínimos da média suavizada é o critério mais preciso, o mesmo adotado oficialmente. As pequenas diferenças vêm do fato de as datas oficiais terem passado por revisões manuais, enquanto o programa aplica a mesma regra a toda a série.

## Testar no navegador

**[Abrir o notebook online](https://matheus-telles.github.io/tp-manchas-solares/lab/index.html?path=TP_Matheus_de_Sousa.ipynb)**, sem instalar nada. O Python roda no próprio navegador via [JupyterLite](https://jupyterlite.readthedocs.io/).

1. Espere o kernel carregar (o primeiro acesso leva alguns segundos).
2. Vá em **Run → Run All Cells**.
3. Role até o fim da seção 3: a interface com as quatro abas aparece abaixo do código.

O site é gerado automaticamente pelo GitHub Actions a cada push em `main` (veja `.github/workflows/jupyterlite.yml`).

## Como executar localmente

```bash
git clone https://github.com/matheus-telles/tp-manchas-solares.git
cd tp-manchas-solares
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook TP_Matheus_de_Sousa.ipynb
```

Execute a célula de código. Os arquivos de dados precisam estar na mesma pasta do notebook.

## Dados

| Arquivo | Conteúdo |
|---|---|
| `SN_d_tot_V2.0.txt` | Número total de manchas solares por dia, desde 1818 ([formato](https://www.sidc.be/silso/infosndtot)) |
| `SN_m_tot_V2.0.txt` | Média mensal do número total de manchas solares, desde 1749 ([formato](https://www.sidc.be/silso/infosnmtot)) |

Fonte: WDC-SILSO, Royal Observatory of Belgium, Brussels. Os arquivos deste repositório foram baixados do SILSO em outubro de 2026 e vão até setembro de 2026.

## Tecnologias

Python · Jupyter · ipywidgets · Matplotlib · NumPy · SciPy
