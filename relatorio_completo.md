# RELATÓRIO FINAL - SISTEMA DE GERENCIAMENTO DE ESTOQUE PARA LIVRARIA

---

## 1. REQUISITOS DE NEGÓCIO

### Contexto do Problema

A livraria enfrenta desafios significativos no controle e gerenciamento de seu estoque de livros. Atualmente, a empresa não possui um sistema automatizado para:

- **Registrar entradas de novos livros** de forma organizada e sistemática
- **Controlar quantidades por gênero literário** para otimizar o mix de produtos
- **Monitorar níveis mínimos de estoque** para evitar rupturas e perdas de vendas
- **Analisar a distribuição percentual** dos gêneros no estoque total
- **Gerar relatórios gerenciais** para tomada de decisões estratégicas

### Necessidades Identificadas

O software desenvolvido visa solucionar as seguintes necessidades críticas:

1. **Automatização do Registro**: Permitir o cadastro rápido e padronizado de entradas de livros
2. **Controle de Estoque Mínimo**: Estabelecer parâmetros mínimos por gênero para evitar desabastecimento
3. **Análise Estatística**: Calcular automaticamente porcentagens de distribuição por gênero
4. **Relatórios Gerenciais**: Gerar informações consolidadas para apoio à gestão
5. **Validação de Dados**: Garantir a integridade das informações inseridas no sistema

### Benefícios Esperados

- Redução de erros manuais no controle de estoque
- Melhoria na tomada de decisões baseada em dados
- Otimização do mix de produtos por gênero
- Prevenção de rupturas de estoque
- Aumento da eficiência operacional

---

## 2. FLUXOGRAMA DA SOLUÇÃO

O fluxograma visual da solução está disponível no arquivo `fluxograma.svg` que acompanha este relatório. O diagrama representa a lógica completa do algoritmo, incluindo:

- **Processo de inicialização** do sistema
- **Loop de entrada de dados** para os dois livros
- **Validações** de título, gênero e quantidade
- **Cálculos estatísticos** de estoque total e porcentagens
- **Verificação de estoque mínimo** por gênero
- **Geração do relatório final**

### Principais Fluxos do Sistema:

1. **Fluxo Principal**: Entrada → Validação → Armazenamento → Cálculos → Relatório
2. **Fluxos de Validação**: Verificações de dados com retorno para correção
3. **Fluxo de Loop**: Repetição controlada para duas entradas obrigatórias
4. **Fluxo de Saída**: Geração e exibição do relatório consolidado

---

## 3. PSEUDOCÓDIGO

```
ALGORITMO GerenciamentoEstoqueLivraria

INÍCIO
    // Definir constantes de estoque mínimo por gênero
    CONSTANTE ESTOQUE_MINIMO_FICCAO = 10
    CONSTANTE ESTOQUE_MINIMO_NAO_FICCAO = 8
    CONSTANTE ESTOQUE_MINIMO_ROMANCE = 12
    CONSTANTE ESTOQUE_MINIMO_MISTERIO = 6
    CONSTANTE ESTOQUE_MINIMO_FANTASIA = 15
    CONSTANTE ESTOQUE_MINIMO_BIOGRAFIA = 5
    CONSTANTE ESTOQUE_MINIMO_HISTORIA = 7
    CONSTANTE ESTOQUE_MINIMO_CIENCIA = 9
    
    // Inicializar variáveis
    DECLARAR lista_livros COMO LISTA VAZIA
    DECLARAR contador_entrada COMO INTEIRO = 1
    
    // Exibir instruções do sistema
    ESCREVER "Sistema de Gerenciamento de Estoque - Livraria"
    ESCREVER "Você deverá registrar exatamente 2 entradas de livros"
    
    // Loop para registrar duas entradas
    ENQUANTO contador_entrada <= 2 FAÇA
        ESCREVER "=== ENTRADA", contador_entrada, "==="
        
        // Solicitar e validar título
        REPETIR
            ESCREVER "Digite o título do livro:"
            LER titulo
            SE titulo VAZIO ENTÃO
                ESCREVER "Erro: O título não pode estar vazio"
            FIM SE
        ATÉ titulo NÃO VAZIO
        
        // Solicitar e validar gênero
        ESCREVER "Gêneros disponíveis:"
        ESCREVER "1. Ficção, 2. Não-ficção, 3. Romance, 4. Mistério"
        ESCREVER "5. Fantasia, 6. Biografia, 7. História, 8. Ciência"
        
        REPETIR
            ESCREVER "Escolha o gênero (1-8):"
            LER opcao_genero
            SE opcao_genero NÃO ESTÁ EM [1,2,3,4,5,6,7,8] ENTÃO
                ESCREVER "Erro: Opção inválida"
            FIM SE
        ATÉ opcao_genero VÁLIDA
        
        // Converter opção para nome do gênero
        genero = CONVERTER_OPCAO_PARA_GENERO(opcao_genero)
        
        // Solicitar e validar quantidade
        REPETIR
            ESCREVER "Digite a quantidade de exemplares:"
            LER quantidade
            SE quantidade <= 0 OU NÃO É NÚMERO ENTÃO
                ESCREVER "Erro: Digite um número positivo válido"
            FIM SE
        ATÉ quantidade VÁLIDA
        
        // Armazenar dados do livro
        livro = CRIAR_REGISTRO(titulo, genero, quantidade)
        ADICIONAR livro À lista_livros
        
        ESCREVER "Livro registrado com sucesso!"
        contador_entrada = contador_entrada + 1
    FIM ENQUANTO
    
    // Calcular estoque total
    estoque_total = 0
    PARA CADA livro EM lista_livros FAÇA
        estoque_total = estoque_total + livro.quantidade
    FIM PARA
    
    // Agrupar por gênero e calcular estatísticas
    DECLARAR generos COMO DICIONÁRIO VAZIO
    PARA CADA livro EM lista_livros FAÇA
        SE livro.genero EXISTE EM generos ENTÃO
            generos[livro.genero] = generos[livro.genero] + livro.quantidade
        SENÃO
            generos[livro.genero] = livro.quantidade
        FIM SE
    FIM PARA
    
    // Calcular porcentagens e verificar estoque mínimo
    DECLARAR estatisticas COMO DICIONÁRIO VAZIO
    PARA CADA genero, quantidade EM generos FAÇA
        porcentagem = (quantidade / estoque_total) * 100
        estoque_minimo = OBTER_ESTOQUE_MINIMO(genero)
        acima_minimo = quantidade >= estoque_minimo
        
        estatisticas[genero] = CRIAR_ESTATISTICA(
            quantidade, porcentagem, estoque_minimo, acima_minimo
        )
    FIM PARA
    
    // Exibir relatório final
    ESCREVER "=== RELATÓRIO DE ESTOQUE - LIVRARIA ==="
    
    ESCREVER "LIVROS REGISTRADOS:"
    PARA CADA livro EM lista_livros FAÇA
        ESCREVER livro.titulo, "(", livro.genero, ") -", livro.quantidade, "exemplares"
    FIM PARA
    
    ESCREVER "ESTOQUE TOTAL:", estoque_total, "exemplares"
    
    ESCREVER "DISTRIBUIÇÃO POR GÊNERO:"
    PARA CADA genero, stats EM estatisticas FAÇA
        ESCREVER genero, ":"
        ESCREVER "  - Quantidade:", stats.quantidade, "exemplares"
        ESCREVER "  - Porcentagem:", stats.porcentagem, "% do estoque total"
        ESCREVER "  - Estoque mínimo:", stats.estoque_minimo, "exemplares"
        SE stats.acima_minimo ENTÃO
            ESCREVER "  - Status: Adequado"
        SENÃO
            ESCREVER "  - Status: Baixo"
        FIM SE
    FIM PARA
    
    ESCREVER "PROCESSAMENTO CONCLUÍDO"
FIM
```

---

## 4. ALGORITMO DESENVOLVIDO

O código-fonte completo da solução está disponível no arquivo `gerenciamento_estoque.py`. O algoritmo foi desenvolvido em Python seguindo as melhores práticas de programação:

### Principais Características do Código:

1. **Estrutura Modular**: Funções bem definidas para cada responsabilidade
2. **Validação Robusta**: Verificações completas de entrada de dados
3. **Constantes Bem Definidas**: Estoques mínimos configuráveis por gênero
4. **Tratamento de Erros**: Loops de validação para entradas inválidas
5. **Interface Amigável**: Mensagens claras e formatação organizada
6. **Documentação Completa**: Docstrings e comentários explicativos

### Principais Funções Implementadas:

- `obter_dados_livro()`: Coleta e valida dados de entrada
- `obter_estoque_minimo()`: Retorna estoque mínimo por gênero
- `calcular_estatisticas()`: Processa cálculos de estoque e porcentagens
- `exibir_relatorio()`: Gera relatório formatado
- `main()`: Função principal que coordena o fluxo

### Constantes Definidas:

```python
ESTOQUE_MINIMO_FICCAO = 10
ESTOQUE_MINIMO_NAO_FICCAO = 8
ESTOQUE_MINIMO_ROMANCE = 12
ESTOQUE_MINIMO_MISTERIO = 6
ESTOQUE_MINIMO_FANTASIA = 15
ESTOQUE_MINIMO_BIOGRAFIA = 5
ESTOQUE_MINIMO_HISTORIA = 7
ESTOQUE_MINIMO_CIENCIA = 9
```

---

## 5. COMPROVAÇÃO DE TESTES FUNCIONAIS

### Cenário de Teste 1: Entrada Padrão

**Dados de Entrada:**
- **Livro 1:**
  - Título: "O Senhor dos Anéis"
  - Gênero: Fantasia (opção 5)
  - Quantidade: 25 exemplares

- **Livro 2:**
  - Título: "1984"
  - Gênero: Ficção (opção 1)
  - Quantidade: 15 exemplares

**Saída Esperada:**
```
📊 ESTOQUE TOTAL: 40 exemplares

📈 DISTRIBUIÇÃO POR GÊNERO:
• Fantasia:
  - Quantidade: 25 exemplares
  - Porcentagem: 62.5% do estoque total
  - Estoque mínimo: 15 exemplares
  - Status: ✅ Adequado

• Ficção:
  - Quantidade: 15 exemplares
  - Porcentagem: 37.5% do estoque total
  - Estoque mínimo: 10 exemplares
  - Status: ✅ Adequado
```

### Cenário de Teste 2: Estoque Baixo

**Dados de Entrada:**
- **Livro 1:**
  - Título: "Steve Jobs"
  - Gênero: Biografia (opção 6)
  - Quantidade: 3 exemplares

- **Livro 2:**
  - Título: "Sherlock Holmes"
  - Gênero: Mistério (opção 4)
  - Quantidade: 7 exemplares

**Saída Esperada:**
```
📊 ESTOQUE TOTAL: 10 exemplares

📈 DISTRIBUIÇÃO POR GÊNERO:
• Biografia:
  - Quantidade: 3 exemplares
  - Porcentagem: 30.0% do estoque total
  - Estoque mínimo: 5 exemplares
  - Status: ⚠️ Baixo

• Mistério:
  - Quantidade: 7 exemplares
  - Porcentagem: 70.0% do estoque total
  - Estoque mínimo: 6 exemplares
  - Status: ✅ Adequado
```

### Validação dos Requisitos:

✅ **Registro de Entradas**: Sistema registra exatamente 2 entradas com título, gênero e quantidade

✅ **Estoque Mínimo por Gênero**: Constantes definidas para todos os 8 gêneros disponíveis

✅ **Cálculo do Estoque Total**: Soma automática de todas as quantidades registradas

✅ **Exibição de Dados**: Porcentagens calculadas e exibidas corretamente para cada gênero

✅ **Validação de Entrada**: Sistema rejeita entradas inválidas e solicita correção

---

## 6. SUGESTÕES DE MELHORIAS FUTURAS

### Melhorias de Funcionalidade:

1. **Expansão do Número de Entradas**
   - Permitir registro de quantidade ilimitada de livros
   - Implementar menu para adicionar/remover entradas dinamicamente
   - Adicionar funcionalidade de edição de registros existentes

2. **Persistência de Dados**
   - Implementar salvamento em arquivo (JSON, CSV ou banco de dados)
   - Adicionar funcionalidade de carregamento de dados salvos
   - Criar sistema de backup automático dos registros

3. **Relatórios Avançados**
   - Gerar gráficos visuais de distribuição por gênero
   - Implementar relatórios de tendências temporais
   - Adicionar exportação para PDF e Excel
   - Criar alertas automáticos para estoque baixo

### Melhorias de Interface:

4. **Interface Gráfica (GUI)**
   - Desenvolver interface usando Tkinter ou PyQt
   - Implementar formulários visuais para entrada de dados
   - Adicionar botões, menus e janelas interativas

5. **Interface Web**
   - Criar aplicação web usando Flask ou Django
   - Implementar dashboard interativo com gráficos
   - Adicionar acesso multi-usuário e controle de permissões

### Melhorias Técnicas:

6. **Validações Avançadas**
   - Implementar validação de ISBN para livros
   - Adicionar verificação de duplicatas por título/autor
   - Criar sistema de categorização automática por palavras-chave

7. **Integração com APIs**
   - Conectar com APIs de livrarias para busca automática de informações
   - Implementar integração com sistemas de vendas
   - Adicionar sincronização com fornecedores

8. **Análise de Dados**
   - Implementar algoritmos de machine learning para previsão de demanda
   - Adicionar análise de sazonalidade por gênero
   - Criar sistema de recomendação de compras baseado em histórico

### Melhorias de Segurança:

9. **Controle de Acesso**
   - Implementar sistema de login e autenticação
   - Adicionar diferentes níveis de permissão (admin, operador, consulta)
   - Criar logs de auditoria para todas as operações

10. **Backup e Recuperação**
    - Implementar sistema automático de backup
    - Adicionar funcionalidade de recuperação de dados
    - Criar redundância e sincronização em nuvem

---

## CONCLUSÃO

O sistema desenvolvido atende completamente aos requisitos funcionais especificados, fornecendo uma solução robusta e eficiente para o gerenciamento básico de estoque de uma livraria. A implementação seguiu boas práticas de programação, incluindo validação de dados, estruturação modular e documentação adequada.

O algoritmo demonstra funcionalidade completa através dos testes realizados, calculando corretamente as porcentagens de distribuição por gênero e verificando os níveis de estoque mínimo estabelecidos.

As sugestões de melhorias futuras apresentadas oferecem um roadmap claro para evolução do sistema, permitindo sua expansão gradual conforme as necessidades da livraria crescem e se tornam mais complexas.

---

**Data do Relatório:** $(Get-Date -Format "dd/MM/yyyy")

**Arquivos do Projeto:**
- `gerenciamento_estoque.py` - Código-fonte principal
- `fluxograma.svg` - Fluxograma visual da solução
- `relatorio_completo.md` - Este relatório completo