def defineTemperatura(formalidade):
    dicionario = {
        'Alta' : 1,
        'Média' : 0.5,
        'Baixa' : 0.1
    } 

    return dicionario[formalidade]


def geraResposta(idioma, formalidade, texto):
    import google.generativeai as genai

    chave_api = ''

    GOOGLE_API_KEY=chave_api
    genai.configure(api_key=GOOGLE_API_KEY)

    generation_config = {
    'candidate_count' : 1,
    'temperature' : defineTemperatura(formalidade)
    }

    exemplo_resumo = """
Texto base: 

O que é Bitcoin?
O Bitcoin é uma forma de dinheiro eletrônico peer-to peer (ponto a ponto) que pode ser transferida sem o intermédio de instituições financeiras.

Na prática, isso significa que dois indivíduos, mesmo morando em países diferentes, podem enviar BTC um para o outro sem precisar de um banco ou de uma empresa de remessa internacional.

As transações são confirmadas na blockchain, um banco de dados enorme que registra todas as negociações dos usuários. Essa tecnologia nasceu junto com o Bitcoin, e funciona de tal forma que os próprios participantes são os auditores da rede.

Como não há uma terceira parte envolvida, mandar Bitcoin de um país para outro costuma ser mais barato e rápido do que transferir moedas fiduciárias.

O BTC é digital, descentralizado e não é controlado por governos, empresas ou pessoas. Portanto, nenhuma Casa da Moeda precisa imprimi-lo e nenhum Banco Central tem o poder de controlar o seu preço. Seu valor depende principalmente da lei de oferta e da procura.

Quando surgiu o Bitcoin
O Bitcoin surgiu em 31 de outubro de 2008. Naquele dia, o criador (ou criadores) da criptomoeda, que se esconde sob o pseudônimo de Satoshi Nakamoto, enviou um e-mail para uma lista de pessoas interessadas em criptografia. No corpo da mensagem, ele escreveu que vinha trabalhando “em um novo sistema de dinheiro eletrônico totalmente peer-to-peer, sem terceiros confiáveis”.

Ele também inseriu um link com o white paper (manual) da criptomoeda, em inglês. No documento, com nove páginas, Nakamoto descreveu resumidamente os fundamentos do Bitcoin, baseados em quatro pontos principais:

É uma rede peer-to-peer para evitar o gasto duplo (possibilidade de enviar as mesmas moedas mais de uma vez); sem intermediários, como bancos; permite o anonimato dos participantes; e usa Prova de Trabalho (um tipo de algoritmo) para gerar Bitcoin (processo que ganhou o nome de mineração) e prevenir o tal gasto duplo.

Crise financeira nos EUA e o Bitcoin
O white paper do Bitcoin foi lançado pouco mais de um mês após o anúncio da falência do Lehman Brothers, que foi o quarto maior banco de investimentos dos Estados Unidos. A quebra do conglomerado financeiro foi o episódio mais emblemático da crise financeira nos EUA, responsável por uma das piores recessões econômicas da história.

A quase simultaneidade desses dois fatos fez alguns economistas e entusiastas do mercado de criptomoedas se questionarem se o Bitcoin teria surgido como uma resposta à instabilidade financeira daquela época. Fernando Ulrich, mestre em economia e especialista em criptomoedas, falou sobre os dois eventos em seu livro “Bitcoin – A Moeda na Era digital”.

“Ainda que possa ser considerada uma mera coincidência o fato de a moeda digital ter surgido em meio à maior crise financeira desde a Grande Depressão de 1930, não podemos deixar de notar o avanço do estado interventor, as medidas sem precedentes e arbitrárias das autoridades monetárias na primeira década do novo milênio e a constante perda de privacidade que cidadãos comuns vêm enfrentando em grande parte dos países desenvolvidos e emergentes”.

Vale lembrar que a crise financeira nos Estados foi gerada, em parte, por uma desenfreada liberação de crédito fácil e pela especulação no mercado imobiliário.

Quem criou o Bitcoin?
O criador do Bitcoin se esconde atrás do pseudônimo Satoshi Nakamoto. Quem ele é, no entanto, ainda continua um mistério. Algumas pessoas vieram a público afirmando ser o personagem, mas ninguém conseguiu de fato provar nada.

O que se sabe até agora vem de vestígios de sua vida online. Em novembro de 2009, por exemplo, ele lançou o BitcoinTalk – um fórum de discussões sobre a criptomoeda. Nakamoto foi bem ativo no espaço e, ao longo de quase um ano, postou cerca de 600 mensagens. Nenhuma, no entanto, dá pistas concretas sobre sua verdadeira identidade.

Candidatos a Satoshi Nakamoto
Ninguém sabe ainda quem criou o Bitcoin. No entanto, existem alguns suspeitos. Na lista, figuram pessoas que colaboraram com o projeto, eram próximas do criador do BTC – pelo menos na vida online – ou foram citados por ele. Há também ricaços capazes de influenciar o mercado com apenas um tweet. Veja alguns dos candidatos:

Gavin Andresen, por ter ficado com o controle do código da criptomoeda e ter trocado mensagens com Nakamoto, é um deles. 
Outro suposto criador do BTC é Hal Finney, que foi a primeira pessoa a receber uma transferência de Bitcoin de Nakamoto – isso lá em 11 de janeiro de 2009. Finney, no entanto, morreu em agosto de 2014 aos 58 anos, vítima de uma doença degenerativa. A pedido dele próprio, seu corpo foi congelado para ser revivido no futuro – isso se surgir alguma tecnologia capaz de vencer a morte.
Os cientistas da computação Nick Szabo e Adam Back, ambos citados no white paper do Bitcoin, também aparecem na lista. Craig Steven Wright, cientista da computação e empresário que em 2016 disse a jornalistas que era o verdadeiro Nakamoto (sem apresentar provas convincentes), é outro suspeito.
Por fim, o CEO da Tesla e da SpaceX, Elon Musk, também está no páreo. A teoria a respeito de Musk surgiu depois que um funcionário do bilionário, conhecido por influenciar o mercado de criptomoedas com seus tweets, disse que ele poderia ter criado o BTC. O empresário nega.  

Diferença entre Bitcoin e moedas digitais
A principal diferença entre Bitcoin, demais criptomoedas e Moedas Digitais de Banco Central (CBDC, na sigla em inglês) é a forma de emissão e distribuição.

O BTC e as altcoins (termo usado para identificar qualquer criptomoeda diferente do Bitcoin) são descentralizadas. Ou seja, não há governo ou país no controle. As regras, portanto, são ditadas pelos envolvidos nos projetos, bem como pelos usuários.

As moedas digitais de bancos centrais, por outro lado, são emitidas e distribuídas por órgãos governamentais. “As CBDC são representações digitais das moedas fiduciárias dos países sendo controladas pelos bancos centrais”, explicou Ricardo Dantas, CO-CEO da corretora de criptomoedas Foxbit.




+ Este é um exemplo de resumo:

Tema: Bitcoin

Tópicos principais: O que é BitCoin, quando surgiu o BitCoin, quem criou o bitcoin, candidados a Satoshi Nakamoto, Diferença entre Bitcoin e moedas digitais.

Resumo: O Bitcoin é uma forma de dinheiro eletrônico peer-to peer (ponto a ponto) que pode ser transferida sem o intermédio de instituições financeiras. 
O Bitcoin surgiu em 31 de outubro de 2008. Naquele dia, o criador (ou criadores) da criptomoeda, que se esconde sob o pseudônimo de Satoshi Nakamoto, enviou um e-mail para uma lista de pessoas interessadas em criptografia. No corpo da mensagem, ele escreveu que vinha trabalhando “em um novo sistema de dinheiro eletrônico totalmente peer-to-peer, sem terceiros confiáveis”. 
O criador do Bitcoin se esconde atrás do pseudônimo Satoshi Nakamoto. Quem ele é, no entanto, ainda continua um mistério. Algumas pessoas vieram a público afirmando ser o personagem, mas ninguém conseguiu de fato provar nada. Ninguém sabe ainda quem criou o Bitcoin. No entanto, existem alguns suspeitos. Na lista, figuram pessoas que colaboraram com o projeto, eram próximas do criador do BTC pelo menos na vida online ou foram citados por ele. Há também ricaços capazes de influenciar o mercado com apenas um tweet. A principal diferença entre Bitcoin, demais criptomoedas e Moedas Digitais de Banco Central (CBDC, na sigla em inglês) é a forma de emissão e distribuição.


"""

    modelo = genai.GenerativeModel(model_name='gemini-1.5-pro-latest', generation_config=generation_config)

    resp = modelo.generate_content(exemplo_resumo + ", a partir desse exemplo, gere um longo resumo no idioma " + idioma + 
                                   ". Gere esse resumo com uma formalidade do nível:" + formalidade +
                                     ", do texto a seguir: \n" + texto + 
                                     "\n Além do resumo, informe o tema principal do texto, e o separe em tópicos.")

    return resp.text
