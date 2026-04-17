# Gerenciador de Tarefas

Um aplicativo simples de linha de comando para gerenciar suas tarefas diárias.

## Funcionalidades

- Adicionar novas tarefas
- Listar tarefas pendentes
- Marcar tarefas como concluídas
- Deletar tarefas
- Visualizar estatísticas
- Exportar/Importar tarefas em CSV
- Buscar tarefas por palavra-chave

## Instalação

`bash
git clone https://github.com/Novochadloc/python-intro-ptbr.git
cd python-intro-ptbr
pip install -r requirements.txt
`

## Uso

`bash
python main.py
`

O programa apresentará um menu interativo onde você pode:

1. **Adicionar tarefa** - Crie uma nova tarefa com título e descrição
2. **Listar tarefas** - Veja todas as tarefas pendentes
3. **Marcar como concluída** - Finalize uma tarefa
4. **Deletar tarefa** - Remova uma tarefa
5. **Ver estatísticas** - Acompanhe seu progresso
6. **Sair** - Encerre o programa

## Estrutura do Projeto

`
.
├── main.py              # Programa principal
├── utils.py             # Funções utilitárias
├── requirements.txt     # Dependências
├── tasks.json          # Arquivo de dados (criado automaticamente )
└── README.md           # Este arquivo
`

## Exemplos

### Adicionar uma tarefa

`
Escolha uma opção: 1
Título da tarefa: Estudar Python
Descrição (opcional): Aprender sobre decoradores
✓ Tarefa adicionada: Estudar Python
`

### Listar tarefas

`
Escolha uma opção: 2
○ [1] Estudar Python
   Aprender sobre decoradores
○ [2] Fazer exercícios
`

### Marcar como concluída

`
Escolha uma opção: 3
ID da tarefa: 1
✓ Tarefa 'Estudar Python' marcada como concluída
`

## Requisitos

- Python 3.8+
- Nenhuma dependência externa obrigatória

## Testes

`bash
pytest
pytest --cov=.
`

## Contribuindo

Sinta-se livre para fazer fork, criar branches e enviar pull requests.

## Licença

MIT License
