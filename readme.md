# FIAP
## Desafio 

Quando o assunto é cultivo, a análise do solo é crucial para entender o melhor momento para cultivo, rotação e até reposição de nutrientes. Para um bom cultivo é necessário um solo fértil, com nível de nutrientes adequados.
Uma das maiores dores hoje do agronegócio, seja por custo financeiro ou temporal, é a recomendação de manutenções no solo.

## Solução
Desenvolver ferramentas de análise de solo que utilizam dados de sensores e algoritmos de aprendizado de máquina para fornecer recomendações de fertilização.
Ferramentas utilizadas: Pandas, NumPy, Scikit-learn, Matplotlib.

## Pré-requisitos

- Docker
- Docker Compose (opcional)
- Python 3.9+
- Oracle Instant Client (necessário apenas para execução local, disponível em [Oracle Instant Client Downloads](https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html))

## Configuração

1. Clone o repositório:

    ```sh
    git clone https://github.com/bhfagundes/python-e-alem.git
    cd python-e-alem
    ```

2. Crie um arquivo `.env` baseado no `.env.example`:

    ```sh
    cp .env.example .env
    ```

3. Edite o arquivo `.env` com suas configurações.

## Construção e Execução

### Usando Docker

1. Construa a imagem Docker:

    ```sh
    docker build -t nome-da-imagem .
    ```

2. Execute o container:

    ```sh
    docker run --env-file .env -p 8000:8000 nome-da-imagem
    ```

### Usando Docker Compose

1. Construa e inicie os serviços:

    ```sh
    docker-compose up --build
    ```

### Executando Localmente

1. Instale as dependências do projeto:

    ```sh
    pip install -r requirements.txt
    ```

2. Certifique-se de que o Oracle Instant Client está instalado e configurado corretamente no seu sistema. Você pode baixá-lo [aqui](https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html).

3. Execute o script principal:

    ```sh
    python main.py
    ```

## Scripts

- `main.py`: Ponto de entrada principal do projeto.
- `scripts/query_users.py`: Script para consultar usuários.

## Estrutura de Diretórios

- `config/`: Arquivos de configuração.
  - `db_config.py`: Configurações de conexão com o banco de dados.
- `db/`: Conexões e operações de banco de dados.
  - `connection.py`: Gerenciamento de conexões com o banco de dados.
- `migrations/`: Scripts de migração do banco de dados.
  - `migration.py`: Script para criar e verificar tabelas no banco de dados.
- `models/`: Modelos de dados.
  - `analise_solo.py`: Definição da classe `AnaliseSolo` que representa a estrutura dos dados de análise de solo.
- `repositories/`: Repositórios de dados (mapeamento de entidades do banco de dados).
  - `analise_solo_repository.py`: Contém a lógica para salvar e recuperar dados de análise de solo no banco de dados.
    - `salvar`: Insere um único registro de análise de solo.
    - `salvar_multiplas_analises`: Insere múltiplos registros de análise de solo em uma única operação.
    - `bulk_insert`: Insere dados em lote a partir de uma lista de tuplas.
- `services/`: Regras de negócio.
  - `analise_solo_service.py`: Contém a lógica de negócios para manipulação de dados de análise de solo.
    - `salvar_analise`: Salva uma única análise de solo.
    - `salvar_multiplas_analises`: Salva múltiplas análises de solo.
    - `salvar_analise_em_lote`: Lê dados de um arquivo CSV e salva em lote.
- `scripts/`: Scripts utilitários.
  - `query_users.py`: Script para consultar usuários no banco de dados.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.