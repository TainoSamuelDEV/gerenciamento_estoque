#!/usr/bin/env python3
# Shebang: indica ao sistema operacional qual interpretador usar para executar o script
# -*- coding: utf-8 -*-
# Declaração de codificação: especifica que o arquivo usa codificação UTF-8 para caracteres especiais

"""
Docstring do módulo: descrição geral do programa
Sistema de Gerenciamento de Estoque para Livraria
Desenvolvido para controlar entradas de livros e calcular porcentagens por gênero
"""

# SEÇÃO DE CONSTANTES GLOBAIS
# Constantes são valores que não mudam durante a execução do programa
# Usamos convenção MAIÚSCULA para identificar constantes em Python

# Define o estoque mínimo necessário para o gênero Ficção (10 exemplares)
ESTOQUE_MINIMO_FICCAO = 10

# Define o estoque mínimo necessário para o gênero Não-ficção (8 exemplares)
ESTOQUE_MINIMO_NAO_FICCAO = 8

# Define o estoque mínimo necessário para o gênero Romance (12 exemplares)
ESTOQUE_MINIMO_ROMANCE = 12

# Define o estoque mínimo necessário para o gênero Mistério (6 exemplares)
ESTOQUE_MINIMO_MISTERIO = 6

# Define o estoque mínimo necessário para o gênero Fantasia (15 exemplares)
ESTOQUE_MINIMO_FANTASIA = 15

# Define o estoque mínimo necessário para o gênero Biografia (5 exemplares)
ESTOQUE_MINIMO_BIOGRAFIA = 5

# Define o estoque mínimo necessário para o gênero História (7 exemplares)
ESTOQUE_MINIMO_HISTORIA = 7

# Define o estoque mínimo necessário para o gênero Ciência (9 exemplares)
ESTOQUE_MINIMO_CIENCIA = 9

# DEFINIÇÃO DA PRIMEIRA FUNÇÃO: obter_dados_livro
# A palavra-chave 'def' inicia a definição de uma função
# 'numero_entrada' é o parâmetro que a função recebe
def obter_dados_livro(numero_entrada):
    """
    Docstring da função: explica o que a função faz
    Solicita e coleta os dados de um livro do usuário
    
    Args: (argumentos que a função recebe)
        numero_entrada (int): Número da entrada (1 ou 2)
    
    Returns: (o que a função retorna)
        dict: Dicionário com título, gênero e quantidade do livro
    """
    
    # Exibe um cabeçalho formatado usando f-string (formatação de string)
    # \n cria uma nova linha, === são caracteres decorativos
    print(f"\n=== ENTRADA {numero_entrada} ===")
    
    # SEÇÃO 1: COLETA E VALIDAÇÃO DO TÍTULO
    # input() solicita entrada do usuário, strip() remove espaços em branco nas extremidades
    titulo = input("Digite o título do livro: ").strip()
    
    # Loop while: continua executando enquanto a condição for verdadeira
    # 'not titulo' é True quando titulo está vazio (string vazia é considerada False)
    while not titulo:
        # Exibe mensagem de erro para o usuário
        print("Erro: O título não pode estar vazio.")
        # Solicita novamente o título até que seja válido
        titulo = input("Digite o título do livro: ").strip()
    
    # SEÇÃO 2: COLETA E VALIDAÇÃO DO GÊNERO
    # Exibe o menu de opções de gêneros disponíveis
    print("\nGêneros disponíveis:")
    print("1. Ficção")      # Opção 1
    print("2. Não-ficção")  # Opção 2
    print("3. Romance")     # Opção 3
    print("4. Mistério")    # Opção 4
    print("5. Fantasia")    # Opção 5
    print("6. Biografia")   # Opção 6
    print("7. História")    # Opção 7
    print("8. Ciência")     # Opção 8
    
    # Cria um dicionário que mapeia números (como strings) para nomes de gêneros
    # Chave: valor numérico como string, Valor: nome do gênero
    generos_validos = {
        '1': 'Ficção',      # Se usuário digitar '1', corresponde a 'Ficção'
        '2': 'Não-ficção',  # Se usuário digitar '2', corresponde a 'Não-ficção'
        '3': 'Romance',     # Se usuário digitar '3', corresponde a 'Romance'
        '4': 'Mistério',    # Se usuário digitar '4', corresponde a 'Mistério'
        '5': 'Fantasia',    # Se usuário digitar '5', corresponde a 'Fantasia'
        '6': 'Biografia',   # Se usuário digitar '6', corresponde a 'Biografia'
        '7': 'História',    # Se usuário digitar '7', corresponde a 'História'
        '8': 'Ciência'      # Se usuário digitar '8', corresponde a 'Ciência'
    }
    
    # Solicita a opção de gênero do usuário
    opcao_genero = input("Escolha o gênero (1-8): ").strip()
    
    # Loop de validação: continua até que uma opção válida seja inserida
    # 'opcao_genero not in generos_validos' verifica se a opção não existe no dicionário
    while opcao_genero not in generos_validos:
        # Exibe mensagem de erro
        print("Erro: Opção inválida. Escolha um número de 1 a 8.")
        # Solicita novamente a opção
        opcao_genero = input("Escolha o gênero (1-8): ").strip()
    
    # Converte a opção numérica para o nome do gênero usando o dicionário
    # generos_validos[opcao_genero] busca o valor correspondente à chave
    genero = generos_validos[opcao_genero]
    
    # SEÇÃO 3: COLETA E VALIDAÇÃO DA QUANTIDADE
    # Loop infinito que só termina com 'break'
    while True:
        # Bloco try-except para capturar erros de conversão
        try:
            # input() retorna string, int() converte para número inteiro
            quantidade = int(input("Digite a quantidade de exemplares: "))
            
            # Verifica se a quantidade é menor ou igual a zero
            if quantidade <= 0:
                # Exibe erro e continua o loop
                print("Erro: A quantidade deve ser um número positivo.")
                continue  # Volta para o início do loop while
            
            # Se chegou aqui, a quantidade é válida, sai do loop
            break
            
        # Captura erro quando int() não consegue converter a string
        except ValueError:
            # Exibe mensagem de erro e continua o loop
            print("Erro: Digite um número válido.")
    
    # RETORNO DA FUNÇÃO
    # Retorna um dicionário com os três dados coletados
    # As chaves são strings, os valores são as variáveis coletadas
    return {
        'titulo': titulo,        # Chave 'titulo' recebe o valor da variável titulo
        'genero': genero,        # Chave 'genero' recebe o valor da variável genero
        'quantidade': quantidade # Chave 'quantidade' recebe o valor da variável quantidade
    }

# DEFINIÇÃO DA SEGUNDA FUNÇÃO: calcular_estoque_minimo
# Esta função recebe um gênero e retorna o estoque mínimo correspondente
def calcular_estoque_minimo(genero):
    """
    Docstring: explica o propósito da função
    Calcula o estoque mínimo baseado no gênero do livro
    
    Args: (parâmetros de entrada)
        genero (str): Gênero do livro
    
    Returns: (o que a função retorna)
        int: Quantidade mínima de estoque para o gênero
    """
    
    # ESTRUTURA CONDICIONAL IF-ELIF-ELSE
    # Verifica se o gênero é exatamente igual a 'Ficção'
    if genero == 'Ficção':
        # Se verdadeiro, retorna a constante definida no início do arquivo
        return ESTOQUE_MINIMO_FICCAO  # Retorna 10
    
    # elif = "else if" - verifica outra condição se a anterior foi falsa
    elif genero == 'Não-ficção':
        # Retorna a constante para não-ficção
        return ESTOQUE_MINIMO_NAO_FICCAO  # Retorna 8
    
    # Continua verificando cada gênero possível
    elif genero == 'Romance':
        # Retorna a constante para romance
        return ESTOQUE_MINIMO_ROMANCE  # Retorna 12
    
    elif genero == 'Mistério':
        # Retorna a constante para mistério
        return ESTOQUE_MINIMO_MISTERIO  # Retorna 6
    
    elif genero == 'Fantasia':
        # Retorna a constante para fantasia
        return ESTOQUE_MINIMO_FANTASIA  # Retorna 15
    
    elif genero == 'Biografia':
        # Retorna a constante para biografia
        return ESTOQUE_MINIMO_BIOGRAFIA  # Retorna 5
    
    elif genero == 'História':
        # Retorna a constante para história
        return ESTOQUE_MINIMO_HISTORIA  # Retorna 7
    
    elif genero == 'Ciência':
        # Retorna a constante para ciência
        return ESTOQUE_MINIMO_CIENCIA  # Retorna 9
    
    # else: executado quando nenhuma das condições anteriores foi verdadeira
    else:
        # Valor padrão caso o gênero não seja reconhecido
        return 5  # Valor padrão para gêneros não mapeados

# DEFINIÇÃO DA TERCEIRA FUNÇÃO: calcular_estatisticas
# Esta é a função mais complexa, que processa todos os dados dos livros
def calcular_estatisticas(livros):
    """
    Docstring: descreve uma função complexa de análise de dados
    Calcula estatísticas do estoque de livros
    
    Args: (parâmetros de entrada)
        livros (list): Lista de dicionários com dados dos livros
    
    Returns: (o que a função retorna)
        dict: Dicionário com estatísticas calculadas
    """
    
    # CÁLCULO 1: ESTOQUE TOTAL
    # sum() soma todos os valores, generator expression itera pela lista
    # Para cada livro na lista, pega o valor da chave 'quantidade'
    estoque_total = sum(livro['quantidade'] for livro in livros)
    # Exemplo: se livros = [{'quantidade': 5}, {'quantidade': 2}]
    # Resultado: estoque_total = 7
    
    # CÁLCULO 2: AGRUPAMENTO POR GÊNERO
    # Inicializa um dicionário vazio para armazenar quantidades por gênero
    generos_quantidade = {}
    
    # Loop for: itera por cada livro na lista
    for livro in livros:
        # Extrai o gênero do livro atual
        genero = livro['genero']
        
        # Verifica se o gênero já existe no dicionário
        if genero in generos_quantidade:
            # Se existe, soma a quantidade atual à quantidade já armazenada
            generos_quantidade[genero] += livro['quantidade']
        else:
            # Se não existe, cria uma nova entrada no dicionário
            generos_quantidade[genero] = livro['quantidade']
    # Exemplo: generos_quantidade = {'Romance': 5, 'Ciência': 2}
    
    # CÁLCULO 3: PORCENTAGENS POR GÊNERO
    # Inicializa dicionário para armazenar porcentagens
    generos_porcentagem = {}
    
    # items() retorna pares chave-valor do dicionário
    for genero, quantidade in generos_quantidade.items():
        # Calcula porcentagem: (quantidade do gênero / total) * 100
        # Operador ternário: valor_se_verdadeiro if condição else valor_se_falso
        porcentagem = (quantidade / estoque_total) * 100 if estoque_total > 0 else 0
        
        # round() arredonda o número para 1 casa decimal
        generos_porcentagem[genero] = round(porcentagem, 1)
    # Exemplo: generos_porcentagem = {'Romance': 71.4, 'Ciência': 28.6}
    
    # CÁLCULO 4: STATUS DO ESTOQUE (BAIXO OU ADEQUADO)
    # Inicializa dicionário para armazenar status de cada gênero
    status_estoque = {}
    
    # Para cada gênero e sua quantidade
    for genero, quantidade in generos_quantidade.items():
        # Chama a função calcular_estoque_minimo para obter o mínimo necessário
        estoque_minimo = calcular_estoque_minimo(genero)
        
        # Compara quantidade atual com estoque mínimo
        if quantidade < estoque_minimo:
            # Se quantidade é menor que o mínimo, status é 'Baixo'
            status_estoque[genero] = 'Baixo'
        else:
            # Caso contrário, status é 'Adequado'
            status_estoque[genero] = 'Adequado'
    # Exemplo: status_estoque = {'Romance': 'Baixo', 'Ciência': 'Baixo'}
    
    # RETORNO DA FUNÇÃO
    # Retorna um dicionário com todas as estatísticas calculadas
    return {
        'estoque_total': estoque_total,              # Total de exemplares
        'generos_quantidade': generos_quantidade,    # Quantidade por gênero
        'generos_porcentagem': generos_porcentagem,  # Porcentagem por gênero
        'status_estoque': status_estoque             # Status por gênero
    }

# DEFINIÇÃO DA QUARTA FUNÇÃO: exibir_relatorio
# Esta função é responsável por formatar e exibir todas as informações na tela
def exibir_relatorio(livros, estatisticas):
    """
    Docstring: descreve uma função de apresentação de dados
    Exibe o relatório completo do sistema de gerenciamento de estoque
    
    Args: (parâmetros de entrada)
        livros (list): Lista de livros registrados
        estatisticas (dict): Dicionário com todas as estatísticas calculadas
    """
    
    # CABEÇALHO DO RELATÓRIO
    # \n cria uma nova linha, "="*60 repete o caractere "=" 60 vezes
    print("\n" + "="*60)
    # Título centralizado do relatório
    print("           RELATÓRIO DE GERENCIAMENTO DE ESTOQUE")
    # Linha de separação
    print("="*60)
    
    # SEÇÃO 1: LIVROS REGISTRADOS
    print("\n1. LIVROS REGISTRADOS:")
    # Linha de separação menor
    print("-" * 30)
    
    # enumerate() adiciona um contador automático começando em 1
    # Para cada livro na lista, i será o número sequencial
    for i, livro in enumerate(livros, 1):
        # f-string para formatar a saída com o número do livro
        print(f"   {i}. Título: {livro['titulo']}")
        # Acessa a chave 'genero' do dicionário livro
        print(f"      Gênero: {livro['genero']}")
        # Acessa a chave 'quantidade' do dicionário livro
        print(f"      Quantidade: {livro['quantidade']} exemplares")
        # Linha em branco para separar os livros
        print()
    
    # SEÇÃO 2: ESTOQUE TOTAL
    print("2. ESTOQUE TOTAL:")
    print("-" * 20)
    # Acessa o valor 'estoque_total' do dicionário estatisticas
    print(f"   Total de exemplares em estoque: {estatisticas['estoque_total']}")
    print()
    
    # SEÇÃO 3: DISTRIBUIÇÃO POR GÊNERO
    print("3. DISTRIBUIÇÃO POR GÊNERO:")
    print("-" * 35)
    
    # Itera pelos gêneros e suas quantidades
    for genero, quantidade in estatisticas['generos_quantidade'].items():
        # Exibe o nome do gênero
        print(f"   {genero}:")
        # Exibe a quantidade de exemplares deste gênero
        print(f"      • Quantidade: {quantidade} exemplares")
        
        # Busca a porcentagem correspondente no dicionário de porcentagens
        porcentagem = estatisticas['generos_porcentagem'][genero]
        print(f"      • Porcentagem: {porcentagem}%")
        
        # Chama a função para obter o estoque mínimo deste gênero
        estoque_minimo = calcular_estoque_minimo(genero)
        print(f"      • Estoque mínimo: {estoque_minimo} exemplares")
        
        # Busca o status no dicionário de status
        status = estatisticas['status_estoque'][genero]
        
        # Estrutura condicional para exibir status com ícones
        if status == 'Adequado':
            # ✓ é um caractere Unicode para check mark
            print(f"      • Status: ✓ Estoque adequado")
        else:
            # ⚠ é um caractere Unicode para aviso
            print(f"      • Status: ⚠ Estoque baixo")
        # Linha em branco para separar os gêneros
        print()
    
    # SEÇÃO 4: ALERTAS DE ESTOQUE
    print("4. ALERTAS DE ESTOQUE:")
    print("-" * 25)
    
    # Variável de controle para verificar se há alertas
    alertas_encontrados = False
    
    # Verifica cada gênero para alertas de estoque baixo
    for genero, status in estatisticas['status_estoque'].items():
        # Se o status for 'Baixo', exibe alerta
        if status == 'Baixo':
            print(f"   ⚠ ATENÇÃO: {genero} está com estoque baixo!")
            
            # Busca quantidade atual e estoque mínimo para comparação
            quantidade_atual = estatisticas['generos_quantidade'][genero]
            estoque_minimo = calcular_estoque_minimo(genero)
            print(f"     Atual: {quantidade_atual} | Mínimo: {estoque_minimo}")
            
            # Marca que pelo menos um alerta foi encontrado
            alertas_encontrados = True
    
    # Se nenhum alerta foi encontrado, exibe mensagem positiva
    if not alertas_encontrados:
        print("   ✓ Nenhum alerta de estoque encontrado.")
    
    # RODAPÉ DO RELATÓRIO
    print("\n" + "="*60)
    print("                    FIM DO RELATÓRIO")
    print("="*60)

# DEFINIÇÃO DA FUNÇÃO PRINCIPAL: main
# Esta é a função que coordena todo o fluxo do programa
def main():
    """
    Docstring: descreve a função principal do programa
    Função principal que executa o sistema de gerenciamento de estoque
    """
    
    # APRESENTAÇÃO DO SISTEMA
    # Exibe o título do sistema
    print("🏪 SISTEMA DE GERENCIAMENTO DE ESTOQUE - LIVRARIA")
    # Cria uma linha decorativa com 55 caracteres "="
    print("=" * 55)
    print("Este sistema permite registrar entradas de livros e")
    print("calcular estatísticas de distribuição por gênero.")
    print("\nVocê deverá registrar exatamente 2 entradas de livros.")
    
    # INICIALIZAÇÃO DA ESTRUTURA DE DADOS
    # Cria uma lista vazia para armazenar os dicionários dos livros
    livros = []
    
    # COLETA DE DADOS DOS LIVROS
    # Loop for com range(1, 3): executa para i=1 e i=2 (2 iterações)
    for i in range(1, 3):
        # Chama a função obter_dados_livro passando o número da entrada
        # A função retorna um dicionário com os dados do livro
        livro = obter_dados_livro(i)
        
        # append() adiciona o dicionário livro ao final da lista livros
        livros.append(livro)
        
        # Exibe mensagem de confirmação usando f-string
        # Acessa a chave 'titulo' do dicionário livro
        print(f"✅ Livro '{livro['titulo']}' registrado com sucesso!")
    
    # PROCESSAMENTO DOS DADOS
    # Chama a função calcular_estatisticas passando a lista de livros
    # A função retorna um dicionário com todas as estatísticas
    estatisticas = calcular_estatisticas(livros)
    
    # EXIBIÇÃO DO RELATÓRIO FINAL
    # Chama a função exibir_relatorio passando os livros e as estatísticas
    # Esta função não retorna nada, apenas exibe informações na tela
    exibir_relatorio(livros, estatisticas)
    
    # MENSAGEM DE FINALIZAÇÃO
    print("\n" + "="*60)
    print("           PROCESSAMENTO CONCLUÍDO")
    print("="*60)

# PONTO DE ENTRADA DO PROGRAMA
# Esta é uma estrutura padrão em Python para executar código apenas quando
# o arquivo é executado diretamente (não quando é importado como módulo)
if __name__ == "__main__":
    # __name__ é uma variável especial do Python
    # Quando o arquivo é executado diretamente, __name__ == "__main__"
    # Quando o arquivo é importado, __name__ == nome_do_arquivo
    
    # Chama a função principal para iniciar o programa
    main()
    # Após main() terminar, o programa encerra