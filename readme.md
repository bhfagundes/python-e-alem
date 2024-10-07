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
- `db/`: Conexões e operações de banco de dados.
- `repositories/`: Repositórios de dados (mapeamento de entidades do banco de dados).
- `services/`: Regras de negócio.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.
