# Livraria DTI
Este projeto é uma aplicação em Python com SQLite para gerenciar um acervo de livros. Ele permite cadastrar, listar, buscar, atualizar e remover livros via terminal, com suporte a testes automatizados e conteinerização com Docker.

## 🧩 Recurso: Livro
A aplicação trabalha com o recurso Livro, que possui as seguintes propriedades:

| Propriedade       | Tipo  | Obrigatória? | Descrição                         |
| ----------------- | ----- | ------------ | --------------------------------- |
| `titulo`          | `str` | Sim          | Título do livro                   |
| `autor`           | `str` | Sim          | Nome do autor                     |
| `editora`         | `str` | Não          | Nome da editora                   |
| `paginas`         | `int` | Sim          | Número de páginas (inteiro)       |
| `descricao`       | `str` | Não          | Breve descrição                   |
| `data_publicacao` | `str` | Sim          | Data de publicação (`YYYY-MM-DD`) |

## 🛠️ Tecnologias Utilizadas
Linguagem: Python 3.10+

Banco de dados: SQLite

Testes: Pytest

Conteinerização: Docker + Docker Compose

## ⚙️ Instalação
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/livraria-dti.git
cd livraria-dti
2. Instale as dependências:
```bash
pip install -r requirements.txt
Apenas a biblioteca pytest é necessária para os testes. As demais dependências listadas no requirements.txt são genéricas para projetos web e não são utilizadas diretamente neste CLI.

## ▶️ Como Executar a Aplicação
Execute o menu interativo com:

```bash
python menu.py
Funcionalidades disponíveis:
Cadastrar livro: Solicita os campos obrigatórios e opcionais.

Listar livros: Mostra todos os livros do banco.

Buscar por ID: Retorna os detalhes de um livro.

Atualizar livro: Permite editar os dados de um livro existente.

Deletar livro: Remove um livro pelo ID.

Sair: Fecha a conexão com o banco.

## 🧪 Testes Unitários
Os testes estão definidos no arquivo test_livro.py utilizando o framework pytest.

Para rodar os testes:
```bash
pip install pytest
pytest test_livro.py
Os testes cobrem:

Adição, busca, atualização e remoção de livros

Validação de data e número de páginas

Comportamento com dados inválidos e IDs inexistentes

## 🐳 Conteinerização com Docker
A aplicação é totalmente conteinerizável para facilitar a execução em qualquer ambiente.

1. Build da imagem:
```bash
docker build -t livraria-dti .
2. Executar com Docker Compose:
```bash
docker-compose up
Isso criará e executará o serviço livraria definido no docker-compose.yml.

Obs: A aplicação atual exige interação via terminal, portanto o container roda no modo interativo.

## 📝 Logs
A aplicação imprime mensagens informativas no terminal para as seguintes ações:

Sucesso ou erro na adição de livros

Validação de dados (por exemplo, páginas não inteiras ou data mal formatada)

Feedback sobre exclusão ou atualizações 

## 📂 Estrutura dos Arquivos
```bash
├── livro.py              # Classes Livro e Livraria (CRUD + SQLite)
├── menu.py               # Interface via terminal com menu interativo
├── test_livro.py         # Testes automatizados com pytest
├── livros.db             # Banco de dados SQLite (gerado automaticamente)
├── Dockerfile            # Instruções para criar a imagem Docker
├── docker-compose.yml    # Configuração do serviço com Docker Compose
├── requirements.txt      # Lista de dependências
