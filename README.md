# Teste para desenvolvedor backend Python
Neste teste vamos avaliar sua capacidade de desenvolver uma aplicação back-end utilizando a linguagem de programação Python.

Queremos que você crie uma API REST responsável por retornar sinais processados utilizando possíveis algoritmos desenvolvidos pela equipe de ciência de dados. Neste exemplo, queremos disponibilizar a função *get_spectrum()* através de um endpoint *spectrum* do tipo GET. Não vamos considerar interações com bancos de dados - o sinal a ser processado é definido pela função *generate_signal()*.


## Requisitos funcionais

Considere os seguintes requisitos:
- estruture a aplicação de maneira que seja organizada e escalável para abrigar novos endpoints no futuro
- o endpoint requer dois parâmetros obrigatórios: *nperseg* do tipo int, e *window* do tipo string. Estes parâmetros devem ser passados a função *get_spectrum()* para o processamento do sinal.
- o endpoint deve retornar duas listas: um vetor de frequências *f*, e um vetor de amplitudes espectrais *Pxx*. O endpoint deve retornar um objeto, contendo as chaves 'frequencies' e 'amplitudes' relacionadas às variáveis *f* e *Pxx*, respectivamente, juntamente com o status da resposta.
- escreva pelo menos **um** teste unitário para sua aplicação.

## Critérios de avaliação

A aplicação deve estar funcional quando executada localmente e responder corretamente a diferentes parâmetros. Em especial, o endpoint deve retornar valores válidos para os seguintes parâmetros: nperseg = 1024 e window = 'hann'.

Sua aplicação deverá conter:
- um arquivo main.py contendo a inicialização da aplicação
- uma lista de pacotes necessários para instalação em ambiente virtual (ex: requirements.txt)
- uma lista de variáveis de ambiente, se aplicável
- uma pasta de testes
- estruturação do repositório fica a seu critério

Os seguintes itens também serão avaliados:

- Organização e estrutura do repositório
- Documentação de funções e classes via docstring, typehint, etc
- Legibilidade do código
- Qualidade dos testes

## Tecnologias, frameworks e bibliotecas

- O framework utilizado para a criação da aplicação fica a seu critério (FastAPI, Flask, Django, etc)
- O framework utilizado para os testes unitários fica a seu critério (pytest, unittest, etc)

## Como submeter a avaliação

- Crie um branch remota com o seu nome
- Clone o repositório localmente
- Implemente o código na sua branch local
- Suba as alterações para sua branch remota
- Quando concluir o teste, envie um e-mail para andre.spillere@dynamox.net para receber a avaliação
