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

## Fluxo de Uso

1. Ao iniciar o programa, você verá um menu com as seguintes opções:
   - Inserir dados manualmente
   - Ler arquivo CSV
   - Estimar fertilidade do solo
   - Treinar modelo
   - Sair

2. Para começar, você deve inserir alguns dados de treinamento:
   - Use a opção "Inserir dados manualmente" para adicionar entradas individuais
   - Ou use a opção "Ler arquivo CSV" para importar múltiplas entradas de uma vez

3. Após inserir dados suficientes, use a opção "Treinar modelo" para criar um modelo de previsão

4. Com o modelo treinado, você pode usar a opção "Estimar fertilidade do solo" para fazer previsões baseadas em novos dados

## Exemplo de Arquivo CSV

O arquivo CSV para importação deve seguir este formato:

```csv
pH,umidade,temperatura,N,P,K,fertilidade
6.5,60,25,120,45,80,1
5.8,45,22,80,30,60,0
7.2,55,28,150,55,90,1
```

Um arquivo de exemplo `example.csv` está disponível na pasta `data/` do projeto.

## Estrutura de Diretórios

- `config/`: Arquivos de configuração.
- `db/`: Conexões e operações de banco de dados.
- `migrations/`: Scripts de migração do banco de dados.
- `models/`: Modelos de dados.
- `repositories/`: Repositórios de dados.
- `services/`: Regras de negócio.
- `data/`: Arquivos de dados, incluindo o exemplo CSV.

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.