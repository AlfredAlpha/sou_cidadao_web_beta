Descrição
"Sou Cidadão" é uma aplicação web desenvolvida para permitir que moradores do município de Cabreúva/SP enviem solicitações diretamente aos vereadores pré-definidos. O sistema utiliza o framework Flask, um banco de dados SQLite para persistência de dados e envio de e-mails via SMTP. A interface gráfica segue as cores da bandeira de Cabreúva (verde, branco e azul).

Funcionalidades
Seleção de um vereador pré-definido (nome e e-mail).
Preenchimento de dados obrigatórios: nome, telefone e descrição.
Upload opcional de uma foto (via galeria ou câmera em dispositivos compatíveis).
Confirmação dos dados antes do envio.
Envio da solicitação por e-mail ao vereador selecionado.
Mensagem de sucesso ou erro após o envio, com opção de voltar ao início.
Pré-requisitos
Python 3.8+: Necessário para executar o Flask e dependências.
Git: Para controle de versão (opcional, mas recomendado).
Servidor SMTP: Configuração de e-mail válida (exemplo: Gmail com senha de aplicativo).
Navegador Web: Para acessar a aplicação.
Dependências
flask: Framework web em Python.
flask-sqlalchemy: ORM para integração com SQLite.
smtplib: Biblioteca padrão para envio de e-mails.
Instalação
Clone o Repositório (se estiver usando Git):
bash
Wrap
Copy
git clone https://github.com/AlfredAlpha/sou_cidadao_web_beta.git
cd sou_cidadao_web_beta
Caso contrário, baixe os arquivos manualmente.
Crie um Ambiente Virtual (opcional, mas recomendado):
bash
Wrap
Copy
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instale as Dependências:
bash
Wrap
Copy
pip install flask flask-sqlalchemy
Configure o Projeto:
Crie a pasta templates/ e adicione os arquivos HTML fornecidos:
apresentacao.html
selecao_vereador.html
preencher_dados.html
adicionar_foto.html
confirmacao.html
Crie a pasta uploads/ para armazenar as fotos enviadas:
bash
Wrap
Copy
mkdir uploads
Edite as Configurações:
Abra o arquivo Python (ex.: app.py) e substitua os valores de EMAIL_USER e EMAIL_PASSWORD por credenciais válidas de um serviço SMTP (ex.: Gmail com senha de aplicativo).
Atualize a lista VEREADORES com os nomes e e-mails reais dos vereadores de Cabreúva.
Como Executar
Inicie o Servidor:
bash
Wrap
Copy
python app.py
O servidor será iniciado em http://127.0.0.1:5000 por padrão.
Acesse no Navegador: Abra seu navegador e vá para http://127.0.0.1:5000.
Estrutura do Projeto
text
Wrap
Copy
sou-cidadao/
│
├── app.py              # Código principal do Flask
├── templates/          # Pasta com os templates HTML
│   ├── apresentacao.html
│   ├── selecao_vereador.html
│   ├── preencher_dados.html
│   ├── adicionar_foto.html
│   └── confirmacao.html
├── uploads/            # Pasta para fotos enviadas
└── solicitacoes.db     # Banco de dados SQLite (gerado automaticamente)
Uso
Tela de Apresentação: Clique em "Iniciar" para começar.
Seleção de Vereador: Escolha um vereador na lista e clique em "Próximo".
Preenchimento de Dados: Insira nome, telefone e descrição, então clique em "Próximo".
Adicionar Foto: Faça upload de uma foto (opcional) ou clique em "Pular".
Confirmação: Revise os dados e clique em "Enviar" para enviar a solicitação por e-mail, ou "Voltar ao Início" para recomeçar.
Feedback: Uma mensagem de sucesso ou erro será exibida após o envio.
Controle de Versão
Este projeto foi projetado para ser gerenciado com Git. Para iniciar um repositório:

bash
Wrap
Copy
git init
git add .
git commit -m "Primeiro commit do Sou Cidadão"
Exemplo de Commits
git commit -m "Adiciona templates HTML e estilização"
git commit -m "Implementa banco de dados SQLite com SQLAlchemy"
Notas Adicionais
Segurança: Use HTTPS em produção e proteja as credenciais de e-mail (ex.: variáveis de ambiente).
Escalabilidade: Para uso em larga escala, considere um banco de dados mais robusto (ex.: PostgreSQL) e um servidor de e-mail dedicado.
Melhorias: Adicionar validação de telefone, suporte a múltiplos arquivos ou uma interface administrativa para os vereadores.
Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests no repositório (se aplicável).

Licença
Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais ou municipais.

Contato
Desenvolvido por [AlfredAlpha]. Para dúvidas, entre em contato via [alfredoamorim@gmail.com.br].
