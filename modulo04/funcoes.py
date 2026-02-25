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


print