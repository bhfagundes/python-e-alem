FROM python:3.9-slim

# Instalar dependências
RUN apt-get update && apt-get install -y libaio1 libaio-dev wget unzip gcc python3-dev

# Baixar e instalar o Oracle Instant Client
RUN wget https://download.oracle.com/otn_software/linux/instantclient/2350000/instantclient-basic-linux.x64-23.5.0.24.07.zip && \
    unzip instantclient-basic-linux.x64-23.5.0.24.07.zip -d /opt/oracle && \
    rm instantclient-basic-linux.x64-23.5.0.24.07.zip

# Configurar variáveis de ambiente
ENV ORACLE_HOME=/opt/oracle/instantclient_23_5
ENV LD_LIBRARY_PATH=$ORACLE_HOME:$ORACLE_HOME/lib
ENV PATH=$ORACLE_HOME:$PATH

# Copiar arquivos do projeto
COPY . /app
WORKDIR /app

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o script Python
CMD ["python", "main.py"]