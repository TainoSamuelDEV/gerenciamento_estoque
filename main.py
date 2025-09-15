# Constantes - Estoque mínimo por gênero
ESTOQUE_MINIMO_FICCAO = 10
ESTOQUE_MINIMO_NAO_FICCAO = 8
ESTOQUE_MINIMO_ROMANCE = 12
ESTOQUE_MINIMO_MISTERIO = 6
ESTOQUE_MINIMO_FANTASIA = 15
ESTOQUE_MINIMO_BIOGRAFIA = 5
ESTOQUE_MINIMO_HISTORIA = 7
ESTOQUE_MINIMO_CIENCIA = 9

def obter_dados_livro(numero_entrada):
    """
    Solicita e coleta os dados de um livro do usuário
    
    Args:
        numero_entrada (int): Número da entrada (1 ou 2)
    
    Returns:
        dict: Dicionário com título, gênero e quantidade do livro
    """
    print(f"\n=== ENTRADA {numero_entrada} ===")
    
    # Solicita título do livro
    titulo = input("Digite o título do livro: ").strip()
    while not titulo:
        print("Erro: O título não pode estar vazio.")
        titulo = input("Digite o título do livro: ").strip()
    
    # Solicita gênero do livro
    print("\nGêneros disponíveis:")
    print("1. Ficção")
    print("2. Não-ficção")
    print("3. Romance")
    print("4. Mistério")
    print("5. Fantasia")
    print("6. Biografia")
    print("7. História")
    print("8. Ciência")
    
    generos_validos = {
        '1': 'Ficção',
        '2': 'Não-ficção',
        '3': 'Romance',
        '4': 'Mistério',
        '5': 'Fantasia',
        '6': 'Biografia',
        '7': 'História',
        '8': 'Ciência'
    }
    
    opcao_genero = input("Escolha o gênero (1-8): ").strip()
    while opcao_genero not in generos_validos:
        print("Erro: Opção inválida. Escolha um número de 1 a 8.")
        opcao_genero = input("Escolha o gênero (1-8): ").strip()
    
    genero = generos_validos[opcao_genero]
    
    # Solicita quantidade de exemplares
    while True:
        try:
            quantidade = int(input("Digite a quantidade de exemplares: "))
            if quantidade <= 0:
                print("Erro: A quantidade deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Erro: Digite um número válido.")
    
    return {
        'titulo': titulo,
        'genero': genero,
        'quantidade': quantidade
    }

def obter_estoque_minimo(genero):
    """
    Retorna o estoque mínimo definido para um gênero específico
    
    Args:
        genero (str): Nome do gênero
    
    Returns:
        int: Quantidade mínima de estoque para o gênero
    """
    estoques_minimos = {
        'Ficção': ESTOQUE_MINIMO_FICCAO,
        'Não-ficção': ESTOQUE_MINIMO_NAO_FICCAO,
        'Romance': ESTOQUE_MINIMO_ROMANCE,
        'Mistério': ESTOQUE_MINIMO_MISTERIO,
        'Fantasia': ESTOQUE_MINIMO_FANTASIA,
        'Biografia': ESTOQUE_MINIMO_BIOGRAFIA,
        'História': ESTOQUE_MINIMO_HISTORIA,
        'Ciência': ESTOQUE_MINIMO_CIENCIA
    }
    
    return estoques_minimos.get(genero, 5)  # Valor padrão caso gênero não encontrado

def calcular_estatisticas(livros):
    """
    Calcula estatísticas do estoque de livros
    
    Args:
        livros (list): Lista de dicionários com dados dos livros
    
    Returns:
        tuple: (estoque_total, estatisticas_por_genero)
    """
    # Calcula estoque total
    estoque_total = sum(livro['quantidade'] for livro in livros)
    
    # Agrupa por gênero
    generos = {}
    for livro in livros:
        genero = livro['genero']
        if genero in generos:
            generos[genero] += livro['quantidade']
        else:
            generos[genero] = livro['quantidade']
    
    # Calcula porcentagens
    estatisticas_por_genero = {}
    for genero, quantidade in generos.items():
        porcentagem = (quantidade / estoque_total) * 100
        estoque_minimo = obter_estoque_minimo(genero)
        
        estatisticas_por_genero[genero] = {
            'quantidade': quantidade,
            'porcentagem': porcentagem,
            'estoque_minimo': estoque_minimo,
            'acima_minimo': quantidade >= estoque_minimo
        }
    
    return estoque_total, estatisticas_por_genero

def exibir_relatorio(livros, estoque_total, estatisticas_por_genero):
    """
    Exibe o relatório completo do estoque
    
    Args:
        livros (list): Lista de livros registrados
        estoque_total (int): Total de livros em estoque
        estatisticas_por_genero (dict): Estatísticas por gênero
    """
    print("\n" + "="*60)
    print("           RELATÓRIO DE ESTOQUE - LIVRARIA")
    print("="*60)
    
    # Exibe livros registrados
    print("\n📚 LIVROS REGISTRADOS:")
    print("-" * 40)
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']}")
        print(f"   Gênero: {livro['genero']}")
        print(f"   Quantidade: {livro['quantidade']} exemplares")
        print()
    
    # Exibe estoque total
    print(f"📊 ESTOQUE TOTAL: {estoque_total} exemplares")
    
    # Exibe porcentagens por gênero
    print("\n📈 DISTRIBUIÇÃO POR GÊNERO:")
    print("-" * 50)
    for genero, stats in estatisticas_por_genero.items():
        status = "✅ Adequado" if stats['acima_minimo'] else "⚠️  Baixo"
        print(f"• {genero}:")
        print(f"  - Quantidade: {stats['quantidade']} exemplares")
        print(f"  - Porcentagem: {stats['porcentagem']:.1f}% do estoque total")
        print(f"  - Estoque mínimo: {stats['estoque_minimo']} exemplares")
        print(f"  - Status: {status}")
        print()

def main():
    """
    Função principal do programa
    """
    print("🏪 SISTEMA DE GERENCIAMENTO DE ESTOQUE - LIVRARIA")
    print("=" * 55)
    print("Este sistema permite registrar entradas de livros e")
    print("calcular estatísticas de distribuição por gênero.")
    print("\nVocê deverá registrar exatamente 2 entradas de livros.")
    
    # Lista para armazenar os livros
    livros = []
    
    # Registra duas entradas de livros
    for i in range(1, 3):
        livro = obter_dados_livro(i)
        livros.append(livro)
        print(f"✅ Livro '{livro['titulo']}' registrado com sucesso!")
    
    # Calcula estatísticas
    estoque_total, estatisticas_por_genero = calcular_estatisticas(livros)
    
    # Exibe relatório final
    exibir_relatorio(livros, estoque_total, estatisticas_por_genero)
    
    print("\n" + "="*60)
    print("           PROCESSAMENTO CONCLUÍDO")
    print("="*60)

if __name__ == "__main__":
    main()