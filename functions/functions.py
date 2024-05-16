def definirTemperatura(formalidade):
    dicionario = {
        'Alta' : 1,
        'Média' : 0.5,
        'Baixa' : 0.1
    } 

    return dicionario[formalidade]


def gerarResposta(idioma, formalidade, texto):
    import google.generativeai as genai

    chave_api = ''

    GOOGLE_API_KEY=chave_api
    genai.configure(api_key=GOOGLE_API_KEY)

    generation_config = {
    'candidate_count' : 1,
    'temperature' : definirTemperatura(formalidade)
    }

    exemplo_resumo = """
Texto 1: 
Essa é a pior colheita de laranja no Brasil desde 1988
As plantações de laranjeiras do agro brasileiro devem ter sua pior colheita em nada menos que 36 anos, com uma queda de 24% na produção em relação a 2023.

Há dois principais motivos para isso:
Mudanças climáticas. Aliás, esse é o segundo ano consecutivo que elas afetam a safra de laranjas.
Greening. Antes que você pergunte, essa é uma doença que se espalha nos pomares. Ao que parece, ela foi mais hard nesta safra.

A relevância disso é simples. Pense que somos responsáveis por 75% do comércio mundial de suco de laranja, sendo o maior exportador do produto. A cada 4 copos de orange juice pelo mundo, 3 são brasileiros.
Para se ter uma ideia, historicamente, nos últimos anos, só de exportação, o mercado de laranja gerou R$ 2 bilhões ao PIB brasileiro.
Sofre em uma ponta, impacta na outra. Assim como a economia, nós — consumidores — também devemos ser impactados, uma vez que a safra menor tende a aumentar o preço do produto. Lei da oferta e demanda.
Isso porque, atualmente, o preço da caixa de 40kg já chegou perto de R$ 90, o maior valor em 30 anos. A tendência é subir ainda mais…



Resposta 1:

Tema: Colheita de laranjas no Brasil.

Tópicos: Previsão de pior colheita de laranjas desde 1988. Greening e mudanças climáticas são os principais causadores da queda na produção de laranjas. Impacto da colheita de laranjas na economia do Brasil.

Resumo: Essa é a pior colheita de laranja no Brasil em muitos anos, com uma queda de 24% na produção em relação a 2023. Os principais motivos pra isso: Mudanças climáticas e Greening(uma doença que se espalha nos pomares). Somos responsáveis por 75% do comércio mundial de suco de laranja, sendo o maior exportador do produto. A cada 4 copos de orange juice pelo mundo, 3 são brasileiros. Historicamente, nos últimos anos, só de exportação, o mercado de laranja gerou R$ 2 bilhões ao PIB brasileiro. Tanto a economia quanto os consumidores devem ser impactados, uma vez que a safra menor tende a aumentar o preço do produto. Lei da oferta e demanda.




Texto 2:
Um dos melhores jogadores formados pelo Vasco nos últimos 30 anos, Philippe Coutinho deve procurar novo clube no meio do ano, quando acaba seu empréstimo ao Al-Duhail, do Catar. O Aston Villa, dono dos direitos do atleta, está disposto a abrir mão dele, o que empolga os torcedores vascaínos. Mas, afinal, o que há de concreto na possível volta do craque a São Januário? 
Nas últimas horas, os vascaínos levantaram a campanha "Volta, Coutinho" no X, antigo Twitter, e o assunto está entre os mais comentados do país. A informação do interesse do Vasco foi publicada primeiramente pelo perfil "Mídia Vascaína".
Coutinho, de 31 anos, tem contrato com o Aston Villa até 2026. No entanto, o clube inglês faz ótima campanha na Premier League - ocupa o 4º lugar, perto de garantir uma vaga na Champions - e inicialmente não tem interesse na volta do meia para a próxima temporada.

É aí que o Vasco entra na história. O clube sondou Coutinho algumas vezes nos últimos anos, mas até então o jogador não tinha interesse em voltar ao Brasil. Agora, o meia vê com bons olhos o retorno ao país e dá preferência ao clube que o revelou.

A SAF vascaína fez contato informal com o estafe do jogador para entender o cenário e estuda uma investida para ter Coutinho por empréstimo. É provável que o Aston Villa peça uma compensação financeira. Por outro lado, o meia de 31 anos está disposto a reduzir seu salário para fechar com o Vasco. Hoje, o maior salário pago pelo clube é o de Payet, que recebe cerca de R$ 1,5 milhão por mês.

Para avançar na contratação, o Vasco precisa ter o aval da 777 Partners, que não tem intenção de investir alto na segunda janela - até porque a SAF gastou R$ 130 milhões em reforços no início do ano. Por isso, a preferência é por uma negociação por empréstimo, sem o custo de compra de direitos. O clube também estuda possíveis saídas no meio do ano, que poderiam aliviar a folha salarial e abrir espaço para Coutinho.



Resposta 2:

Tema: Possível chegada do Philippe Coutinho ao Vasco da Gama.

Tópicos: Philippe Coutinho deve procurar novo clube no meio do ano. O meia vê com bons olhos o retorno ao país e dá preferência ao clube que o revelou. A SAF vascaína fez contato com o estafe do jogador para entender o cenário e estuda uma investida. A preferência é por uma negociação por empréstimo, sem o custo de compra de direitos.

Resumo: Philippe Coutinho deve procurar novo clube no meio do ano, quando acaba seu empréstimo ao Al-Duhail, do Catar. Coutinho pertence ao Aston Villa, mas o clube inglês inicialmente não tem interesse na volta do meia para a próxima temporada. O meia vê com bons olhos o retorno ao país e dá preferência ao clube que o revelou. A SAF vascaína já fez contato informal com o estafe do jogador para entender o cenário e estuda uma investida para ter Coutinho por empréstimo. É provável que o Aston Villa peça uma compensação financeira. O meia de 31 anos está disposto a reduzir seu salário para fechar com o Vasco. Para avançar na contratação, o Vasco precisa ter o aval da 777 Partners.




Texto 3:
Banco Central divulgou a ata da sua última reunião que decidiu a nova taxa de juros do país, mostrando a opinião e os votos de cada um dos 9 diretores.

Se você já se esqueceu… O BC segurou o ritmo dos cortes na Selic e diminuiu a taxa em 0,25%, deixando ela em 10,50% ao ano — interrompendo o ciclo de seis cortes seguidos de 0,5%.

Aí rachou. Os diretores do BC se dividiram entre aqueles que queriam seguir com as reduções de meio ponto e os que preferiam pisar no freio. Com a ata divulgada, isso ficou bem claro:

Os quatro indicados no atual governo por Lula votaram por reduzir a Selic em 0,5%;

Já os cinco nomeados por Bolsonaro votaram por corte de 0,25%.

O que todos concordaram foi não dar pistas sobre a próxima decisão dos juros, deixando claro que o momento é de cautela com o cenário internacional e o aumento das projeções de inflação.

O que está por trás disso: Desde que assumiu, Lula tem criticado a política de juros, argumentando que a taxa está alta demais e “atrasa o crescimento econômico do país”.

O principal alvo é o presidente do BC, Campos Neto, que foi indicado por Bolsonaro. O mandato dele vai até o fim do ano, e, depois disso, Lula vai indicar um substituto. Ou seja, os indicados do atual governo vão ser maioria.

Enquanto a previsão da inflação para este ano aumenta, as decisões dos diretores vão impactar o bolso dos brasileiros, já que a Selic dita o preço do crédito e dos empréstimos.



Resposta 3:

Tema: Divergências na decisão da taxa básica de juros (Selic).

Tópicos: Divulgação da ata da última reunião do Comitê de Política Monetária (Copom) do Banco Central (BC). Manutenção da taxa Selic em 10,50% ao ano, com redução de 0,25%. Divisão entre os diretores do BC quanto à intensidade do corte da Selic. Posição favorável à redução de 0,5% por parte dos diretores indicados pelo presidente Lula. Voto pela redução de 0,25% pelos diretores indicados pelo ex-presidente Bolsonaro. Cautela em relação ao cenário internacional e às projeções de inflação. Críticas do presidente Lula à política de juros adotada pelo BC.

Resumo: A ata da última reunião do Copom, divulgada pelo Banco Central, revelou divergências entre seus membros acerca da definição da taxa básica de juros. Enquanto os diretores indicados pelo presidente Lula defenderam uma redução mais expressiva, de 0,5%, os indicados pelo ex-presidente Bolsonaro votaram por uma diminuição de 0,25%, o que prevaleceu, interrompendo o ciclo de seis cortes consecutivos de 0,5%. A decisão final, contudo, reflete a preocupação de todos os membros do Copom com a conjuntura internacional e o aumento das projeções de inflação. A ata também evidencia a tensão entre o governo Lula e o presidente do BC, Roberto Campos Neto, em relação à condução da política monetária do país. As decisões tomadas pelo BC, em um contexto de inflação crescente, impactam diretamente a vida dos brasileiros, influenciando o custo do crédito e dos empréstimos.

"""


    modelo = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', generation_config=generation_config)

    resposta = modelo.generate_content("Seguindo os exemplos a seguir: \n\n" + exemplo_resumo + 
                                   "\n\n\nInforme o tema principal, os tópicos, e com uma formalidade " + formalidade + ", faça um resumo no idioma: " + idioma + ", do seguinte texto: \n\n" + texto)
    return resposta.text