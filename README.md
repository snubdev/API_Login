# API_Login

### Instalando as dependências
```
pip install fastapi
```
```
pip install "uvicorn[standard]"
```
```
pip install aiosqlite
```
```
pip install python-jose[cryptography]
```
```
pip install python-multipart
```
### Execução
Para gerar um arquivo SQLite com as tabelas do banco de dados do projeto

```
create_table.py
```
Para rodar o projeto, utilize o comando abaixo no terminal
```
uvicorn main:app --reload
```
