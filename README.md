## Django REST Framework API - CRUD Básico
![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)

### Descrição

Este projeto é uma API REST desenvolvida com Django REST Framework como parte do curso da Alura. O objetivo principal é o aprendizado prático dos conceitos básicos do framework, incluindo a criação de endpoints para os métodos HTTP mais comuns (GET, POST, PUT, PATCH, DELETE), definição de endpoints personalizados para filtros específicos de dados e implementação de autenticação para acesso restrito à API.

<img width="1007" alt="image" src="https://github.com/ledsouza/Django-API-Rest-Framework/assets/56280624/e7e893f2-3705-48d1-a9f7-d6ce33958202">

### Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* Postman

### Descrição Detalhada

Este projeto demonstra a construção de uma API RESTful utilizando o framework Django REST, abordando os seguintes aspectos:

**Funcionalidades:**

* **Endpoints básicos:** Implementa endpoints para os métodos HTTP GET, POST, PUT, PATCH e DELETE, permitindo operações CRUD (Criar, Ler, Atualizar e Deletar) em recursos da API.
* **Endpoints personalizados:** Implementa endpoints personalizados para fornecer filtros específicos aos dados, como:
    * Obter os cursos em que um determinado aluno está matriculado.
    * Obter os alunos que estão matriculados em um determinado curso.
* **Autenticação:** Implementa autenticação para garantir que apenas usuários autenticados acessem os recursos da API.
* **Testes:** Utiliza Postman para testar os endpoints da API, validando as requisições e respostas.

**Estrutura do Projeto:**

O projeto segue a estrutura padrão de um projeto Django, com os seguintes componentes principais:

* **`models.py`:** Define os modelos de dados da aplicação, representando as entidades e seus relacionamentos.
* **`serializers.py`:** Define os serializers, responsáveis por converter os dados dos modelos para o formato JSON e vice-versa.
* **`views.py`:** Define as views da API, que processam as requisições HTTP e retornam as respostas apropriadas.
* **`urls.py`:** Define as URLs da API, mapeando-as para as views correspondentes.

**Configurações:**

O projeto utiliza as configurações padrão do Django REST Framework, com algumas personalizações para autenticação e permissões.

**Como Executar o Projeto:**

1. Clone este repositório.
2. Crie um ambiente virtual e ative-o.
3. Instale as dependências do projeto com o comando `poetry install`.
4. Aplique as migrações do banco de dados com os comandos `python manage.py makemigrations` e `python manage.py migrate`.
5. Inicie o servidor de desenvolvimento com o comando `python manage.py runserver`.

**Observações:**

Este projeto foi desenvolvido para fins de aprendizado e pode ser utilizado como base para outros projetos. No entanto, é importante adaptá-lo às necessidades específicas de cada aplicação.
