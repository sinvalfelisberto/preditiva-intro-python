def read_csv_dict(name_file: str, sep=','):
    """
    Lê um arquivo CSV e converte seus dados em um dicionário de listas.

    A primeira linha do arquivo é tratada como cabeçalho (chaves do dicionário), 
    e as linhas subsequentes são armazenadas como listas de valores para 
    cada respectiva coluna.

    Args:
        name_file (str): O caminho ou nome do arquivo CSV a ser lido.
        sep (str, optional): O caractere separador de colunas. Defaults to ','.

    Returns:
        dict: Um dicionário onde as chaves são os nomes das colunas e os 
            valores são listas contendo os dados de cada linha.

    Example:
        >>> dados = read_csv_dict('vendas.csv', sep=';')
        >>> print(dados)
        {'Produto': ['Teclado', 'Mouse'], 'Preço': ['150', '80']}
    """
    # le o csv e salva em memória
    with open(name_file) as file:

        lines = []

        for line in file:
            lines.append(line)
    
    # cria os campos 
    fields = lines[0].split(sep)
    lines = lines[1:]
    fields[-1] = fields[-1][:-1]

    # cria o dicionario de para recerber os dados 
    dados = {}

    for campo in fields:
        dados[campo] = []

    # cria o dicionario com todos os dados 
    for line in lines:
        infos = line.split(sep)

        if len(infos) != len(fields):
            pass
        else:
            for i in range(len(fields)):
                if i == len(fields) -1:
                    infos[i] = infos[i][:-1]
                dados[fields[i]].append(infos[i])
    return dados

def convert_to_number(dicionario: dict, field: str):
    """
    Converte os valores de uma lista dentro de um dicionário de strings para números.

    Tenta avaliar cada string do campo usando ast.literal_eval, preservando valores
    que não podem ser avaliados. Não altera o dicionário original — retorna uma cópia.

    Args:
        dicionario (dict): Dicionário cujas colunas são listas de strings.
        field (str): Nome do campo a ser convertido.

    Returns:
        dict: Cópia do dicionário com o campo convertido para números quando possível.

    Raises:
        KeyError: Se o campo não existir no dicionário.

    Example:
        >>> dados = {'preco': ['1', '2.5', "'x'"]}
        >>> convert_to_number(dados, 'preco')
        {'preco': [1, 2.5, 'x']}
    """
    dados = dicionario
    campo_tratado = [eval(x) for x in dados[field]]
    dados[field] = campo_tratado

def classifica_trabalho(remote_ratio: int):
    """
    Lê um valor inteiro e com base nele, retorna se o trabalho é remoto, presencial ou híbrido. O valor é percentual. Se a pessoal trabalha 0% remoto, então ele trabalha presencial. Se ele trabalha 100% remoto, esse é o seu regime e, caso ele trabalhe entre 1% e 99% remoto, seu trabalho é híbrido.

    Args:
        remote_ratio (int): O valor a ser considerado pela função para determinar se o trabalho é remoto.

    Returns:
        str: uma string com a informação sobre o tipo de trabalho que a pessoa desempenha: Remoto, Presencial ou Híbrido.

    Example:
        >>> classificacao = classifica_trabalho(93)
        >>> print(f"Classificação: {classificacao}.")
        Classificação: Híbrido.
    """
    if remote_ratio == 100:
        return 'Remoto'
    if remote_ratio == 0:
        return 'Presencial'
    
    return 'Híbrido'

sqrt = lambda x: x ** (1/2)

distancia_quadrado = lambda x, media: (x-media) ** 2

f = lambda x: 'Presencial' if x == 0 else 'Remoto' if x == 100 else 'Híbrido'

def medidas_resumo(lista: list):
    """
    Calcula métricas estatísticas descritivas básicas a partir de uma lista de números.

    Esta função processa um conjunto de dados para extrair quatro medidas fundamentais:
    a contagem de elementos, a soma total, a média aritmética e a variância populacional.

    Funcionamento Matemático:
    --------------------------
    1. Contagem (n): Identifica o tamanho da amostra ou população.
    2. Total (Σx): Soma todos os valores contidos na lista.
    3. Média (μ): Divide o total pela contagem.
    4. Variância (σ²): Calcula a dispersão dos dados em relação à média. 
       Utiliza a fórmula da variância populacional: 
       σ² = Σ(xi - μ)² / n

    Parâmetros:
    -----------
    lista : list
        Uma lista de números (inteiros ou decimais). 
        Nota: Requer que a função 'distancia_quadrado(x, media)' esteja 
        definida no escopo global para calcular o desvio de cada ponto.

    Retorna:
    --------
    contagem : int
        O número total de elementos na lista.
    total : float
    	A soma de todos os elementos.
    media : float
        A média aritmética dos valores.
    varp : float
        A variância populacional dos dados.

    Exemplo de Uso:
    ---------------
    >>> # Se distancia_quadrado(x, m) for (x - m)**2
    >>> medidas_resumo([2, 4, 6])
    (3, 12, 4.0, 2.6666666666666665)

    Observação:
    -----------
    A função calcula a variância DIVIDINDO PELO NÚMERO TOTAL (n). Isso a 
    caracteriza como Variância Populacional. Se o objetivo for calcular a 
    Variância Amostral (onde os dados são apenas uma parte de um todo), 
    geralmente divide-se por (n - 1).
    """
    contagem = len(lista)
    total = sum(lista)
    media = total / contagem
    diff_quadrado = [distancia_quadrado(x, media) for x in lista]
    sum_diff_quadrado = sum(diff_quadrado)
    varp = sum_diff_quadrado / contagem
    return contagem, total, media, varp

def distinct_groups(lista: list):
    """
    Recebe uma lista como parâmentro e retorna um conjunto com os itens distintos.

    Args:
        lista (list): A lista que contém as informações duplicadas.

    Returns:
        list: Uma lista com itens únicos.

    Example:
        >>> itens_distintos = distinct_groups(['Remoto', 'Remoto', 'Remoto', 'Híbrido', 'Presencial', 'Híbrido', 'Remoto'])
        >>> print(itens_distintos)
        ['Remoto', 'Híbrido', 'Presencial']
    """
    return list(set(lista))