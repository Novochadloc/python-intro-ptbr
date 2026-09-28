# Gerenciador de Tarefas

Projeto simples feito em Python para praticar testes, GitHub Actions e Docker.

## Instalação

```bash
pip install -r requirements.txt
```

## Executar

```bash
python main.py
```

## Testes

```bash
pytest -v
```

O workflow do GitHub Actions executa os testes quando uma pull request é aberta ou recebe um novo commit. Se algum teste falhar, ele deixa um aviso na PR.

## Docker

```bash
docker build -t task-manager .
docker run --name task-manager-container task-manager
```

A saída esperada é:

```text
Task Manager Ready
```

Como o programa é de linha de comando, o container termina depois de executar. Para conferir o resultado:

```bash
docker ps -a
```

## Arquivos principais

- `main.py`: classe para gerenciar tarefas.
- `utils.py`: funções auxiliares.
- `test_main.py`: testes do gerenciador.
- `test_utils.py`: testes das funções auxiliares.
- `Dockerfile`: configuração do container.
- `.github/workflows/python-package.yml`: execução dos testes no GitHub.
