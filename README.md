# Sistema de Gerenciamento de Estoque para Livraria

Sistema desenvolvido em Python para controle de estoque de livros, com cálculo automático de porcentagens por gênero e verificação de níveis mínimos de estoque.

## Como Executar

### Execução Principal
```bash
python gerenciamento_estoque.py
```

## Funcionalidades

- **Registro de Entradas**: Permite registrar exatamente 2 livros com título, gênero e quantidade
- **8 Gêneros Disponíveis**: Ficção, Não-ficção, Romance, Mistério, Fantasia, Biografia, História, Ciência
- **Estoque Mínimo**: Constantes definidas para cada gênero
- **Cálculos Automáticos**: Estoque total e porcentagens por gênero
- **Validação de Dados**: Verificação de entradas inválidas
- **Relatórios Formatados**: Exibição clara e organizada dos resultados
- **Status de Estoque**: Alertas visuais para estoque baixo

## Constantes de Estoque Mínimo

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

## 📁 Arquivos do Projeto

- `main.py` - Código principal do sistema
- `main_explicado.py` - Código principal todo comentado
- `fluxograma.svg` - Fluxograma visual da solução
- `relatorio_completo.md` - Relatório técnico completo
- `README.md` - Este arquivo de instruções


## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária (usa apenas bibliotecas padrão)

## Melhorias Futuras

Veja o arquivo `relatorio_completo.md` para uma lista detalhada de 10 melhorias sugeridas, incluindo:

- Persistência de dados
- Relatórios avançados com gráficos (CSV, PDF)
- Interface web
- Sistema de backup automático

## Desenvolvimento

Sistema desenvolvido seguindo boas práticas de programação:

- Código modular e bem documentado
- Validação robusta de entrada
- Tratamento de erros
- Interface amigável ao usuário

---