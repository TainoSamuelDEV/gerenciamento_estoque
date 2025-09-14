# 📚 Sistema de Gerenciamento de Estoque para Livraria

Sistema desenvolvido em Python para controle de estoque de livros, com cálculo automático de porcentagens por gênero e verificação de níveis mínimos de estoque.

## 🚀 Como Executar

### Execução Principal
```bash
python gerenciamento_estoque.py
```

### Execução dos Testes Automatizados
```bash
python teste_automatizado.py
```

## 📋 Funcionalidades

- ✅ **Registro de Entradas**: Permite registrar exatamente 2 livros com título, gênero e quantidade
- ✅ **8 Gêneros Disponíveis**: Ficção, Não-ficção, Romance, Mistério, Fantasia, Biografia, História, Ciência
- ✅ **Estoque Mínimo**: Constantes definidas para cada gênero
- ✅ **Cálculos Automáticos**: Estoque total e porcentagens por gênero
- ✅ **Validação de Dados**: Verificação de entradas inválidas
- ✅ **Relatórios Formatados**: Exibição clara e organizada dos resultados
- ✅ **Status de Estoque**: Alertas visuais para estoque baixo

## 📊 Constantes de Estoque Mínimo

| Gênero | Estoque Mínimo |
|--------|----------------|
| Ficção | 10 exemplares |
| Não-ficção | 8 exemplares |
| Romance | 12 exemplares |
| Mistério | 6 exemplares |
| Fantasia | 15 exemplares |
| Biografia | 5 exemplares |
| História | 7 exemplares |
| Ciência | 9 exemplares |

## 🧪 Cenários de Teste

O sistema foi testado com 3 cenários diferentes:

1. **Cenário Padrão**: Dois gêneros diferentes com estoque adequado
2. **Estoque Baixo**: Teste de alertas para estoque abaixo do mínimo
3. **Mesmo Gênero**: Agregação de livros do mesmo gênero

## 📁 Arquivos do Projeto

- `gerenciamento_estoque.py` - Código principal do sistema
- `teste_automatizado.py` - Testes funcionais automatizados
- `fluxograma.svg` - Fluxograma visual da solução
- `relatorio_completo.md` - Relatório técnico completo
- `README.md` - Este arquivo de instruções

## 🎯 Exemplo de Uso

```
🏪 SISTEMA DE GERENCIAMENTO DE ESTOQUE - LIVRARIA
=======================================================

=== ENTRADA 1 ===
Digite o título do livro: O Senhor dos Anéis
Escolha o gênero (1-8): 5
Digite a quantidade de exemplares: 25
✅ Livro 'O Senhor dos Anéis' registrado com sucesso!

=== ENTRADA 2 ===
Digite o título do livro: 1984
Escolha o gênero (1-8): 1
Digite a quantidade de exemplares: 15
✅ Livro '1984' registrado com sucesso!

📊 ESTOQUE TOTAL: 40 exemplares

📈 DISTRIBUIÇÃO POR GÊNERO:
• Fantasia: 62.5% (25 exemplares) - ✅ Adequado
• Ficção: 37.5% (15 exemplares) - ✅ Adequado
```

## 🔧 Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

## 📈 Melhorias Futuras

Veja o arquivo `relatorio_completo.md` para uma lista detalhada de 10 melhorias sugeridas, incluindo:

- Interface gráfica (GUI)
- Persistência de dados
- Relatórios avançados com gráficos
- Interface web
- Integração com APIs
- Sistema de backup automático

## 👨‍💻 Desenvolvimento

Sistema desenvolvido seguindo boas práticas de programação:

- Código modular e bem documentado
- Validação robusta de entrada
- Tratamento de erros
- Testes automatizados
- Interface amigável ao usuário

---

**Desenvolvido para atender aos requisitos de gerenciamento de estoque de livrarias** 📖