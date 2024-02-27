# Django Form com FileField

- Repositório criado para estudo antes de implementação efetiva no estágio. Aprendendo sobre o `FileField` no Django e sua manipulação dentro do banco de dados (que é feita referênciando o caminho para que não ocorra sobrecarga do banco e do servidor).
- Para envio dos dados, foi contruído um simples formulario no html, que, apesar de sua simplicidade, se não for definido o enctype="multipart/form-data em sua criação, não funcionará.
- A criação da MEDIA_ROOT e da MEDIA_URL no settings do projeto também é indispensável.
- A views terá o papel de devolver a página do formulário e de capturar e instanciar o documento enviado pelo usuário.
- No models.py, encontramos a criação dos campos da tabela do banco de dados. 

## Requisitos

- Django 
- Python
- Pip 
- Ambiente virtual 

## Instalação

1. Clone este repositório:
   
2. Navegue até o diretório do projeto:
 
3. Execute as migrações do Django (que não foram upadas para esse repositório para evitar conflitos)

4. Inicie o servidor de desenvolvimento com 'python manage.py runserver' 

7. Acesse [http://localhost:8000](http://localhost:8000) no seu navegador.

## Como funciona

1. Acesse a página inicial (`home.html`) para ver o formulário de envio de arquivos.
2. No formulário, é necessário selecionar um arquivo para upload.
3. Ao enviar o formulário, os dados são capturados pela view correspondente (`views.py`).
4. A view processa o arquivo e qualquer outro dado do formulário.
5. Os dados são então utilizados para instanciar um objeto do modelo correspondente (usando `FileField` no modelo) e salvo no banco de dados.

Certifique-se de que o formulário HTML contém `enctype="multipart/form-data"` para permitir o envio de arquivos. Isso é crucial para garantir que o Django possa processar corretamente os dados do arquivo.



