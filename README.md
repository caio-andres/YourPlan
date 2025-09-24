# Your Plan

1.0 Crie o arquivo .env para armazenar variáveis sensíveis e/ou reutilizáveis

```bash
type nul > .env # Create environment file
```

1.1 Adicione as variáveis + valores contidos no arquivo .env.example para o novo arquivo .env

2.0 Crie o ambiente virtual para o projeto

```bash
python -m venv .venv # Create virtual environment
.venv\Scripts\activate # Windows
```

3.0 Instale as dependências contidas dentro do arquivo 'requirements.txt'

```python
pip install -r requirements.txt
```
