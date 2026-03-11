# Gestor de Inventário

Sistema de gestão de estoque desenvolvido com **Django**, focado em automação de processos e inteligência de dados.

## Funcionalidades
- **Dashboard Inteligente:** Resumo financeiro e de volume de estoque calculado em tempo real.
- **Alertas de Estoque Baixo:** Identificação visual automática de produtos que precisam de reposição (estoque < 5 unidades).
- **Relatórios Profissionais:** Exportação de dados do estoque para **Excel (.xlsx)** integrada com a biblioteca **Pandas**.
- **Automação de Estoque:** Uso de **Django Signals** para baixar o estoque automaticamente após cada venda registrada.
- **Painel Administrativo:** Gestão completa de Categorias, Fornecedores, Produtos e Vendas.

## Tecnologias Utilizadas
- **Python 3.x**
- **Django Framework** (Backend & Templates)
- **Pandas** (Processamento de Dados)
- **Bootstrap 5** (Interface Responsiva)
- **SQLite** (Banco de Dados)

## Como Executar o Projeto
1. Clone o repositório: `git clone https://github.com/seu-usuario/gestor_inventario.git`
2. Crie uma venv: `python -m venv venv`
3. Ative a venv: 
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode as migrações: `python manage.py migrate`
6. Inicie o servidor: `python manage.py runserver`

---
Desenvolvido por **Diogo Paim** como projeto de portfólio para demonstração de habilidades Full-Stack com Python/Django.
