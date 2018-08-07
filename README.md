# python-serverless-flask-api

Para rodar o projeto:

##### Utilizando python do sistema operacional
- Instalar o python3
- Instalar o python3-pip
- Instalar o virtualenv `$ sudo pip3 install virtualenv`
- Criar o ambiente virtual `$ virtualenv -p python3 venv`
- Ativar o ambiente virtual no terminal `$ source venv/bin/activate`
- Após entrar no python do ambiente virtual instalar as dependências `$pip install -r requirements.txt`

##### Utilizando pyenv (recomendado)
- Instalar o pyenv `$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv`
- Instalando ambiente virtual via pyenv `$ virtualenv -p ~/.pyenv/versions/3.6.5/bin/python venv`
- Definir variáveis de ambiente:
```
    $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    $ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
    $ source ~/.bash_profile
```
- Instalando o python `pyenv install 3.6.5`
- Instalando o virtualenv `$ sudo ~/.pyenv/versions/3.6.5/bin/pip3 install virtualenv`
- Criando ambiente virtual `$ ~/.pyenv/versions/3.6.5/bin/virtualenv -p ~/.pyenv/versions/3.6.5/bin/python venv`
- Ativar o ambiente virtual no terminal `$ source venv/bin/activate`

Dicas:

1) P: Como sair do venv?
   R: deactivate

Utilitários:
- Gerenciador de versões: https://github.com/pyenv/pyenv
- Problemas comuns após instalação do pyenv: https://github.com/pyenv/pyenv/wiki/Common-build-problems

## Para executar local
 `$ sls wsgi serve
