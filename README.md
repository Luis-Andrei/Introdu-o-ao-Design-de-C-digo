# Calculadora 4 - Média de Números

Este projeto implementa uma API REST para calcular a média de uma lista de números.

## Requisitos

- Python 3.7+
- pip

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a aplicação

```bash
python src/app.py
```

## Testes

Para executar os testes:

```bash
pytest
```

## Uso da API

### Calcular média

**Endpoint:** POST /calculator_4

**Corpo da requisição:**
```json
{
    "numbers": [1, 2, 3, 4, 5]
}
```

**Resposta de sucesso:**
```json
{
    "average": 3.0
}
```

**Respostas de erro:**
- 400: Lista de números inválida ou vazia
- 500: Erro interno do servidor 