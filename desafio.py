# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Utilizando o cache do sistema
@st.cache_resource

# Criando uma função para a introdução
def intro():
    """
    Função para exibir a introdução do desafio Enacom usando Streamlit.
    """

    # Título
    st.write("# Bem-vindo ao Desafio!")

    # Obtendo o menu no sidebar
    st.sidebar.success("Selecione a janela a seguir.")

    # Inserindo a imagem
    st.image("Enacom.png", use_column_width=True)

   # Introdução
    st.markdown(
        """

        **👈 Escolha uma opção no menu lateral à esquerda**

        Candidato: Clériston Cláudio Carneiro Pereira de Albuquerque
    """
    )

# Criando a função para apresentação
def apresentacao():
    # Inserindo uma imagem no sidebar
    st.sidebar.image("Enacom.png", use_column_width=True)

    # Título
    st.write("# 1. Apresentação")

    # Nome
    st.write('#### Clériston Cláudio Carneiro Pereira de Albuquerque')
    
     # Dividindo a tela em duas colunas
    col1, col2 = st.columns(2)

    # Inserindo a imagem
    with col1:
        st.image("cleriston.png", width=300, use_column_width=False)

    # Informação
    with col2:
        st.markdown(
        """
        **Formação Acadêmica:**

        - **Graduação:** Engenharia de Produção - FBV.
        - **Mestrado:** Engenharia de Produção - UFPE.
        - **MBA:** Investimento em Ações e Mercado de Capitais - UNICAP.
        - **MBA:** Ciência de Dados para o mercado financeiro - XP Educação.
        - **Graduando:** Ciência de Dados - Wyden.
        - **Certificação:** CEA (Especialista em Investimentos) ANBIMA.
        \n\n
        Atualmente sou Coordenador de Polo EAD na ETEPAC (Escola Técnica Estadual Professor Antônio Carlos Gomes da Costa).

    """
    )
    
    # Alinhando o texto à esquerda e à direita
    st.markdown("""
    <style>
    .left-right-aligned-text {
    text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

    # Aobrdando o objetivo
    st.markdown(
        """
        <p class='left-right-aligned-text'> <b>Objetivo:</b> Estou buscando uma transição para áreas como logística, produção, planejamento e finanças quantitativas, 
        onde posso aplicar meu conhecimento em ciência de dados para impulsionar resultados significativos. Meu objetivo é utilizar análises para otimizar processos, 
        identificar oportunidades estratégicas e contribuir para o crescimento sustentável das organizações. Estou comprometido em enfrentar desafios com criatividade 
        e dedicação, sempre buscando maneiras inovadoras de agregar valor.</p>

    """
    , unsafe_allow_html=True)

# Criando a função para metodologia
def metodologia():
    # Inserindo uma imagem no sidebar
    st.sidebar.image("Enacom.png", use_column_width=True)

    # Título
    st.write("# 2. Metodologia")

    # Alinhando o texto à esquerda e à direita
    st.markdown("""
    <style>
    .left-right-aligned-text {
    text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

    # Argumentando sobre a metodologia
    st.markdown(
        """
     <p class='left-right-aligned-text'> <b>Definição do Problema:</b> Desenvolver um modelo de preditivo para prever a geração de energia hidroelétrica pelos próximos anos com base nos dados fornecidos pelo Operador Nacional do Sistema Elétrico (ONS).</p>

     <p class='left-right-aligned-text'> <b>Análise de Dados:</b> Foram utilizados dados de geração de energia e dados hidrológicos dos reservatórios do ONS. Realizou-se uma análise exploratória para entender a distribuição dos dados, identificar padrões e visualizar o comportamento ao longo do tempo.</p>

     <p class='left-right-aligned-text'> <b>Pré-processamento de dados:</b> foi realizada a limpeza, normalização e tratamento de valores ausentes para garantir a qualidade dos dados utilizados no treinamento dos modelos.</p>

     <p class='left-right-aligned-text'> <b>Divisão de dados:</b> Os dados foram divididos em conjuntos de treinamento (2000-2018) e teste (2019-2020) para avaliar o desempenho dos modelos.</p>

     <p class='left-right-aligned-text'> <b>Seleção de modelos:</b> Foram testados cinco modelos diferentes: Regressão Linear, Árvore de Decisão, Floresta Aleatória, Rede Neural e XGBoost, para determinar qual melhor se adequava ao problema.</p>

     <p class='left-right-aligned-text'> <b>Avaliação de modelos:</b> Utilizou-se a métrica MSE (Mean Square Error) e Validação Cruzada para avaliar a precisão e a capacidade de generalização dos modelos.</p>

     <p class='left-right-aligned-text'> <b>Otimização de hiperparâmetros:</b> Foi utilizada a técnica Grid Search para ajustar os hiperparâmetros do modelo selecionado e melhorar ainda mais seu desempenho.</p>

    """
    , unsafe_allow_html=True)

# Criando a função para resultados
def insights():
    # Inserindo uma imagem no sidebar
    st.sidebar.image("Enacom.png", use_column_width=True)

    # Título
    st.write("# 3. Insights")

    # Obtendo os dados
    df_hidreletrica = pd.read_csv('hidreletrica.csv')
    df_geracao = pd.read_csv('dado_df.csv')

    # Alinhando o texto à esquerda e à direita
    st.markdown("""
    <style>
    .left-right-aligned-text {
    text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

    # titulo sobre a evolução da geração de energia no Brasil
    st.title('Evolução da Geração de Energia no Brasil (2000-2020)')

    # Texto falando sobre a geração de energia no país
    st.markdown("""
    <p class='left-right-aligned-text'>O gráfico a seguir retrata a evolução da geração de energia no Brasil ao longo do período de 2000 a 2020. 
                É evidente que a região Sudeste se destaca como a principal responsável pela geração de energia no país.</p>
    """, unsafe_allow_html=True)

    # Visualizar graficamente os dados (VISÃO GERAL)
    # Agrupar por região para facilitar a visualização do gráfico
    plot_fonte = df_geracao.groupby(['ano', 'id_subsistema'])['val_geracao'].sum().reset_index()

    # Converter a columa mes_ano em strings
    plot_fonte['ano'] = plot_fonte['ano'].astype(str)

    # Plotar o gráfico
    fig = px.bar(plot_fonte, x='ano', y='val_geracao', color='id_subsistema',
             title='Evolução da Geração de Energia por Região (Visão Geral)',
             labels={'val_geracao': 'Geração de Energia (MW med)', 'mes_ano': 'Data'},
             color_discrete_map={'N': 'blue', 'NE': 'black', 'SE': 'purple','S':'orange'})

    fig.update_xaxes(title_text='Data')
    fig.update_yaxes(title_text='Geração de Energia (MW med)')
    fig.update_layout(legend_title_text='Regiões')
    st.plotly_chart(fig)

    # Texto sobre a média e o desvio padrão
    st.markdown("""
    <p class='left-right-aligned-text'>A quantidade média de energia gerada no país é de cerca de 43.119.230 megawatts médios (MW med). 
                Isso é o quanto de energia geralmente é produzida. O desvio padrão, que é uma medida de quanto os números variam, é de aproximadamente 68.583.910 MW med.
                Isso significa que a quantidade de energia produzida pode variar bastante em relação à média.</p>
    """, unsafe_allow_html=True)

    # título sobre a correlação entre as regiões
    st.title('Análise de Correlação entre Regiões')

     # Texto sobre a correlação entre regiões
    st.markdown("""
    <p class='left-right-aligned-text'>A análise de correlação foi conduzida para investigar se existe alguma relação entre a geração de energia de cada região.
                 A matriz de correlação apresentada abaixo ilustra o cenário, seguida de comentários sobre os resultados obtidos..</p>
    """, unsafe_allow_html=True)

    # Calcular a matriz de correlação entre as regiões
    matriz_correlacao = df_geracao.pivot_table(index='ano', columns='id_subsistema', values='val_geracao', aggfunc='sum').corr()

    # Exibir a matriz de correlação
    st.markdown("Matriz de Correlação entre as Regiões:")
    st.table(matriz_correlacao)

    # Explciando a correlação entre as regiões
    st.markdown(
        """
    <p class='left-right-aligned-text'> ● <b>Região Norte:</b> Possui uma correlação forte com a região Nordeste e uma correlação moderada em relação às 
    regiões Sul e Sudeste.</p>
    <p class='left-right-aligned-text'> ● <b>Região Nordeste:</b> Apresenta uma correlação fraca com a região Sul do país, mas uma correlação moderada a 
    forte com a região Sudeste.</p>
    <p class='left-right-aligned-text'> ● <b>Região Sudeste:</b> Demonstrou uma correlação moderada com as regiões Norte e Nordeste, enquanto exibiu uma correlação 
    moderada com a região Sul.</p>
    <p class='left-right-aligned-text'> ● <b>Região Sul:</b> Exibiu correlações moderadas com as demais regiões, sugerindo uma menor interdependência em termos de geração 
    de energia.</p>
    """, unsafe_allow_html=True
    )

    # título sobre o Panorama das Fontes de Energia no Brasil
    st.title('Panorama das Fontes de Energia no Brasil')

    # Texto falando sobre a geração de energia por fonte de energia
    st.markdown("""
    <p class='left-right-aligned-text'>No próximo gráfico, é evidenciado o panorama das fontes de geração de energia no país. Fica claro que a geração hidrelétrica 
                predomina, seguida pela Termelétrica. Notavelmente, a energia eólica tem ganhado espaço ao longo do tempo.</p>
    """, unsafe_allow_html=True)

    # Visualizar graficamente os dados por fonte de energia (VISÃO GERAL)
    # Agrupar por região para facilitar a visualização do gráfico
    plot_fonte_1 = df_geracao.groupby(['ano', 'nom_tipousina'])['val_geracao'].sum().reset_index()

    # Converter a columa mes_ano em strings
    plot_fonte_1['ano'] = plot_fonte_1['ano'].astype(str)

    # Plotar o gráfico
    fig = px.bar(plot_fonte_1, x='ano', y='val_geracao', color='nom_tipousina',
             title='Evolução da Geração de Energia por Fonte de Geração (Visão Geral)',
             labels={'val_geracao': 'Geração de Energia (MW med)', 'mes_ano': 'Data'},
             color_discrete_map={'EOLIELÉTRICA': 'blue', 'NUCLEAR': 'black', 'TÉRMICA': 'orange', 'HIDROELÉTRICA': 'purple','BOMBEAMENTO':'red', 'FOTOVOLTAICA':'brown'})

    fig.update_xaxes(title_text='Data')
    fig.update_yaxes(title_text='Geração de Energia (MW med)')
    fig.update_layout(legend_title_text='Fontes de energia')
    st.plotly_chart(fig)

    # título sobre correlação entre as fontes de energia
    st.title('Correlações entre diferentes Fontes de Energia')

    # Texto falando sobre a geração de energia por fonte de energia
    st.markdown("""
    <p class='left-right-aligned-text'>Foi utilizada uma matriz de correlação para determinar a existência de correlações entre diferentes fontes de geração de energia.
                 Os resultados são surpreendentes, como ilustrado na matriz abaixo.</p>
    """, unsafe_allow_html=True)

    # Calcular a matriz de correlação entre as fontes de geração
    matriz_correlacao = df_geracao.pivot_table(index='ano', columns='nom_tipousina', values='val_geracao', aggfunc='sum').corr()

    # Exibir a matriz de correlação
    st.markdown("Matriz de Correlação entre as Fontes de geração:")
    st.table(matriz_correlacao['HIDROELÉTRICA'])    

    # Comentando sobre a correlação entre as fontes de energia
    st.markdown("""
    <p class='left-right-aligned-text'> ● <b>Hidroelétrica e Bombeamento:</b> Correlação positiva forte.</p>
    <p class='left-right-aligned-text'> ● <b>Hidroelétrica e Eólica:</b> Correlação negativa.</p>
    <p class='left-right-aligned-text'> ● <b>Hidroelétrica e Fotovoltaica:</b> Correlação positiva e robusta.</p>
    <p class='left-right-aligned-text'> ● <b>Hidroelétrica e Energia Nuclear:</b> Correlação moderadamente positiva.</p>
   <p class='left-right-aligned-text'>  ● <b>Hidroelétrica e Térmica:</b> Correlação positiva, porém menos pronunciada.</p>
    """, unsafe_allow_html=True)

    # título sobre Geração de Energia Hidrelétrica por Região
    st.title('Geração de Energia Hidrelétrica por Região')

    # Texto falando sobre a geração de energia hidrelétrica
    st.markdown("""
    <p class='left-right-aligned-text'>Em relação à geração de energia hidrelétrica, a região Sudeste lidera o setor, como evidenciado no panorama a seguir.</p>
    """, unsafe_allow_html=True)

    # Visualizar graficamente os dados das hidrelétrica por região (VISÃO GERAL)
    # Agrupar por região para facilitar a visualização do gráfico
    df_plot_hidreletrica = df_geracao[df_geracao['nom_tipousina']=='HIDROELÉTRICA']

    # Converter a columa mes_ano em strings
    df_plot_hidreletrica['ano'] = df_plot_hidreletrica['ano'].astype(str)

    # Plotar o gráfico
    fig = px.bar(df_plot_hidreletrica, x='ano', y='val_geracao', color='id_subsistema',
             title='Evolução da Geração de Energia Hídrica por Região (Visão Geral)',
             labels={'val_geracao': 'Geração de Energia (MW med)', 'mes_ano': 'Data'},
             color_discrete_map={'N': 'blue', 'NE': 'black', 'S': 'orange', 'SE': 'purple'})

    fig.update_xaxes(title_text='Data')
    fig.update_yaxes(title_text='Geração de Energia (MW med)')
    fig.update_layout(legend_title_text='Regiões')
    st.plotly_chart(fig)

    # Texto falando sobre cada região
    st.markdown("""
    <p class='left-right-aligned-text'>No campo abaixo, selecione a região para visualizar a evolução das fontes de energia hídrica de cada região do Brasil.
     Na visualização, a linha vermelha representa a média de geração de energia por região.</p>
    """, unsafe_allow_html=True)


    # Criar Função para plotar o gráfico por Região
    # Agrupar os dados por tipo de geração e
    plot_por_regiao = df_geracao.groupby(['ano', 'nom_tipousina','id_subsistema'])['val_geracao'].sum().reset_index()

    # Convertendo a coluna 'mes_ano' para string
    plot_por_regiao['ano'] = plot_por_regiao['ano'].astype(str)

    # Criar função para plotar gráfico
    def plotar_grafico(nome, sigla):
        fig = px.bar(plot_por_regiao[(plot_por_regiao['id_subsistema'] == f'{sigla}') & (plot_por_regiao['nom_tipousina'] == 'HIDROELÉTRICA')], x='ano', y='val_geracao', color='id_subsistema',
                 title=f'Evolução da Geração de Energia Hidrelétrica na Região {nome.upper()}',
                 labels={'val_geracao': 'Geração de Energia (MW med)', 'ano': 'Data'},
                 color_discrete_map={'N': 'blue', 'NE': 'black', 'S': 'orange', 'SE': 'purple'})

        # Calculando a média da região
        media_regiao = plot_por_regiao[plot_por_regiao['id_subsistema'] == f'{sigla}']['val_geracao'].mean()

        # Adicionando a média como uma linha horizontal
        fig.add_hline(y=media_regiao, line_color="red", annotation_text=f'Média: {media_regiao:.2f} MW med', annotation_position="bottom right")

        fig.update_xaxes(title_text='Data')
        fig.update_yaxes(title_text='Geração de Energia (MW med)')
        fig.update_layout(legend_title_text='Formas de geração')
        st.plotly_chart(fig)

    # Criar a função para mostrar a área
    def mostrar_resultados(area_selecionada):
        # Mostrar o gráfico com base na área selecionada
        if area_selecionada == "Norte":
            # Plotando o gráfico da região Norte
            plotar_grafico('norte', 'N')

            # Texto sobre a região 
            st.write("""<p class='left-right-aligned-text'>Na região Norte, a média de geração de energia é de 27.258.360 MW med, com um 
                    desvio padrão de 18.903.600 MW med. Notavelmente, essa região demonstra uma geração de 
                    energia hidrelétrica acima da média, revelando uma forte dependência desse tipo de energia 
                    com uma diversidade limitada de fontes na região. É interessante observar que a geração de 
                    energia hidrelétrica quase dobrou desde o início do ano 2000 até os dias atuais. Esse aumento 
                    substancial destaca a importância contínua da energia hídrica como principal fonte de energia 
                    na região Norte.</p>""", unsafe_allow_html=True)
            

        elif area_selecionada == "Nordeste":
            # Plotando o gráfico da região Nordeste
            plotar_grafico('nordeste', 'NE')

            # Texto sobre a região 
            st.write("""<p class='left-right-aligned-text'>Na região Nordeste, a geração de energia hidrelétrica está gradualmente cedendo lugar para outras fontes de
                      energia elétrica. Durante o período de 2013 a 2018, houve um declínio notável na produção hidrelétrica, sendo que nos anos de 2017 e 2018 os 
                     valores ficaram abaixo da média regional. A média de geração de energia durante esse período foi de 20.313.570 MW med, com um desvio padrão 
                     de 19.118.230 MW med. Esses números evidenciam uma produção média de energia inferior em comparação com outras regiões do país, acompanhada por
                      uma variação considerável. Esse cenário pode ser atribuído à crescente dependência de outras fontes de energia na região, como a eólica, que é
                      mais suscetível a variações sazonais e climáticas.</p>"""
                     , unsafe_allow_html=True)
    
        elif area_selecionada == "Sudeste":
            # Plotando o gráfico da região Sudeste
            plotar_grafico('Sudeste', 'SE')

            # Texto sobre a região 
            st.write("""<p class='left-right-aligned-text'>Na região Sudeste do Brasil, a média de geração de energia é de 85.130.530 MW med, 
                    com um desvio padrão de 107.336.300 MW med. Esta região se destaca por apresentar a maior 
                    média de geração de energia entre todas as regiões do país, acompanhada também pelo maior 
                    desvio padrão, o que indica uma considerável variabilidade nos níveis de geração ao longo do 
                    tempo.</p>
                    <p class='left-right-aligned-text'>Essa variabilidade pode ser atribuída à complexidade da infraestrutura energética da 
                    região, que engloba uma diversidade de fontes, incluindo hidrelétricas, termelétricas, eólicas e 
                    nucleares. Essas fontes estão sujeitas a diversas influências, como demanda, condições 
                    climáticas e disponibilidade de recursos.</p>
                    """, unsafe_allow_html=True)
    
        elif area_selecionada == "Sul":
            # Plotando o gráfico da região Norte
            plotar_grafico('Sul', 'S')

            # Texto sobre a região 
            st.write("""<p class='left-right-aligned-text'>Na região Sul, a média de geração de energia é de aproximadamente 26.750.050 MW med, 
                     com um desvio padrão considerável de cerca de 29.148.710 MW med. Esses valores indicam uma variação significativa nos níveis de geração 
                     ao longo do tempo, refletindo a complexidade do sistema de geração de energia na região.</p>
                    <p class='left-right-aligned-text'>Entretanto, a geração de energia hidroelétrica nesta região enfrenta desafios significativos devido à notável 
                     variação em sua produção ao longo do tempo, o que aponta para uma instabilidade considerável nesse aspecto. Essa instabilidade é atribuída não 
                     apenas à predominância de fontes de energia hidrelétrica, mas também a outras fontes, como a termelétrica, que estão sujeitas a fatores sazonais 
                     e de demanda. Isso torna o panorama energético da região Sul suscetível a flutuações significativas.</p>""", unsafe_allow_html=True)
    
    # Campo para selecionar a região
    area = st.selectbox("Selecione uma região:", ["Norte", "Nordeste", "Sudeste", "Sul"])

    if area:
        mostrar_resultados(area)
    
    # título sobre correlação com outras variáveis
    st.title('Correlação da geração de energia hidrelétrica e os dados dos reservatórios hidrológicos')

    # Texto falando sobre a correlação entre a geração de energia elétrica e as variáveis dos reservatórios
    st.markdown("""
    <p class='left-right-aligned-text'>Outras variáveis foram incluídas no modelo para prever a geração de energia 
                                        hidrelétrica, incluindo os dados hidrológicos dos reservatórios. Para manter a concisão, 
                                        apresento a correlação dessas variáveis com a geração de energia hidrelétrica</p>
    """, unsafe_allow_html=True)

    st.write('A correlação entre a geração de energia Hidroelétrica e as variáveis:\n')
    correlacao = df_hidreletrica.corr().iloc[1:, 1:]
    st.table(correlacao.iloc[:, 0])

    # Texto fcomentando sobre a correlação
    st.markdown("""
    <p class='left-right-aligned-text'>Observa-se que as correlações são bastante significativas, exceto pela variável 
    "vazãotransferida", que apresenta uma correlação próxima de zero.</p>""", unsafe_allow_html=True)

# Criando a função para Modelos e avaliação de modelos
def modelos():
    # Inserindo uma imagem no sidebar
    st.sidebar.image("Enacom.png", use_column_width=True)

    # Título
    st.write("# 4. Modelos e avaliação de modelos")

    # Comentando sobre os dados
    st.header('Dados')

    st.write('Os dados foram divididos em conjuntos de treinamento e teste, utilizando as variáveis de região e dados hidrológicos como variáveis dependentes. Para essa divisão, foi empregada a função `train_test_split`.')

    # Apresentando os modelos
    st.header('Modelos Aplicados')

    st.write('Foram aplicados os seguintes modelos de aprendizagem de máquina aos dados:')
    st.write('1. Regressão Linear')
    st.write('2. Árvore de Decisão')
    st.write('3. Floresta Aleatória')
    st.write('4. Rede Neural')
    st.write('5. XGBoost')

    # Argumentando sobre a métrica utilizadas
    st.header('Métrica de Avaliação')

    st.write('A métrica utilizada para avaliar o desempenho dos modelos foi o Erro Quadrático Médio (MSE), que mensura a média dos quadrados das diferenças entre os valores previstos e os valores reais.')

    # Resultado da métrica
    st.header('Resultados Obtidos')

    results_data = {
        'Modelo': ['Regressão Linear', 'Floresta Aleatória', 'Árvore de Decisão', 'Rede Neural', 'XGBoost'],
        'MSE': ['0,000000023', '3.517.183,06', '7.284.903,20', '5.800.716,82', '2.322.597,80']
    }
    results_df = pd.DataFrame(results_data)
    st.write(results_df)

    st.write('Observa-se que a Regressão Linear alcançou o menor valor de MSE em comparação com os outros modelos, sugerindo melhor capacidade de previsão em relação aos valores reais de geração de energia.')

    # Abordando a validação cruzada
    st.header('Validação Cruzada')

    cross_val_data = {
        'Modelo': ['Regressão Linear', 'Floresta Aleatória', 'Árvore de Decisão', 'Rede Neural', 'XGBoost'],
        'Média': ['0,00000004', '7.491.811,65', '9.464.323,96', '6.063.382,26', '10.460.246,20'],
        'Desvio Padrão': ['0,00000003', '6.265.518,17', '10.743.881,57', '4.468.835,96', '8.698.803,37']
    }
    cross_val_df = pd.DataFrame(cross_val_data)
    st.write(cross_val_df)

    st.write('Observa-se que o modelo de Regressão Linear obteve excelente desempenho, com pontuações consistentes em diferentes execuções da validação cruzada.')

# Criando a função para Conclusão
def conslusao():
    # Inserindo uma imagem no sidebar
    st.sidebar.image("Enacom.png", use_column_width=True)

    # Alinhando o texto à esquerda e à direita
    st.markdown("""
    <style>
    .left-right-aligned-text {
    text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

    # Título
    st.write("# 5. Resultados e Conclusão")

    # Resultado
    st.header('Resultado')

    # Lendo os dados
    y_test = pd.read_csv('y_test.csv')
    y_pred = pd.read_csv('y_pred_linear.csv')

    # Renomeando a coluna
    y_test.rename(columns={'val_geracao':'Real'}, inplace=True)
    y_pred.rename(columns={'val_geracao':'Previsto'}, inplace=True)

    # Cria o gráfico
    # Cria uma figura contendo dois gráficos de linhas: um para os valores reais e outro para as previsões do modelo final
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_test.index, y=y_test['Real'], mode='lines', name='Real', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=y_pred.index, y=y_pred['Previsto'], mode='lines', name='Previsões', line=dict(color='red')))

    # Atualiza os nomes dos eixos x e y
    fig.update_xaxes(title_text='Amostras')
    fig.update_yaxes(title_text='Valor')

    # Adiciona título
    fig.update_layout(title='Real x Previsto')

    st.plotly_chart(fig)

    # adiconando o comentário
    st.write('''<p class='left-right-aligned-text'>O gráfico acima compara os valores reais (y_test) com os valores previstos (y_pred) pelo modelo de Regressão Linear. 
             Observamos uma boa correspondência entre os valores previstos e reais, indicando um bom desempenho do modelo. Essa proximidade
              sugere que a Regressão Linear é capaz de fazer previsões precisas para este conjunto de dados.</p>''', unsafe_allow_html=True)

    # falando da conclusão
    st.header('Conclusão')

    st.write('''<p class='left-right-aligned-text'>A Regressão Linear demonstrou ser uma escolha sólida para esse conjunto de dados, oferecendo simplicidade, 
             eficácia e boa capacidade de generalização. Sua capacidade de previsão superior, juntamente com o menor tempo computacional
              necessário para ajustar o modelo, destaca sua viabilidade em determinados cenários de modelagem.</p>''', unsafe_allow_html=True)


page_names_to_funcs = {
    "Início": intro,
    "Apresentação": apresentacao,
    "Metodologia": metodologia,
   'Insights': insights,
   "Modelos e avaliação de modelos": modelos,
   'Resultados e Conclusão' : conslusao
}

demo_name = st.sidebar.selectbox("Selecione o item", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()