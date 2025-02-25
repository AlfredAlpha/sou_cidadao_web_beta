# README - Sou Cidadão (Web com SQLite)

## Descrição
"Sou Cidadão" é uma aplicação web desenvolvida com Flask e SQLite, projetada para permitir que moradores de Cabreúva/SP enviem solicitações aos vereadores da cidade diretamente pelo navegador. A interface utiliza as cores da bandeira de Cabreúva (verde, branco e azul) e armazena as solicitações em um banco de dados SQLite para persistência.

### Funcionalidades
- Tela inicial de apresentação.
- Seleção de um vereador da Câmara Municipal de Cabreúva.
- Preenchimento de dados obrigatórios: nome, telefone e descrição.
- Upload opcional de uma foto.
- Confirmação dos dados antes do envio.
- Envio da solicitação por e-mail ao vereador selecionado.
- Persistência das solicitações no banco de dados SQLite (status: Pendente, Enviado, Erro).
- Feedback de sucesso ou erro, com opção de voltar ao início.

## Pré-requisitos
- **Python 3.8+**: Necessário para executar o Flask e SQLAlchemy.
- **Git**: Para controle de versão (opcional).
- **Servidor SMTP**: Configuração de e-mail válida (ex.: Gmail com senha de aplicativo).
- **Navegador Web**: Para acessar a aplicação.

## Dependências
- `flask`: Framework web para backend e frontend.
- `flask-sqlalchemy`: ORM para integração com SQLite.

## Instalação
1. **Clone o Repositório** (se aplicável):
   ```bash
   git clone https://github.com/AlfredAlpha/sou_cidadao_web_beta.git
   cd sou_cidadao_web_beta

Ou baixe os arquivos manualmente.

2. **Crie um Ambiente Virtual** (opcional, recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. **Instale as Dependências**:

pip install -r requirements.txt

4. **Configure o Projeto**:
Crie a pasta uploads/:

mkdir uploads

Edite app.py e substitua EMAIL_USER e EMAIL_PASSWORD por credenciais válidas.


**Como Executar**
1. Inicie o Servidor:

python app.py

Acesse em http://127.0.0.1:5000 no navegador. O banco de dados solicitacoes.db será criado automaticamente.


**Estrutura do Projeto**

sou_ cidadao_web -BETA/
│
├── app.py              # Código principal do Flask com SQLite
├── static/             # Arquivos estáticos
│   └── style.css       # Estilização
├── templates/          # Templates HTML
│   ├── apresentacao.html
│   ├── selecao_vereador.html
│   ├── preencher_dados.html
│   ├── adicionar_foto.html
│   └── confirmacao.html
├── uploads/            # Pasta para fotos enviadas
├── solicitacoes.db     # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt    # Dependências
└── README.md           # Documentação

**Uso**

1. Apresentação: Clique em "Iniciar".
2. Seleção de Vereador: Escolha um vereador e clique em "Próximo".
3. Preenchimento de Dados: Insira nome, telefone e descrição, clique em "Próximo".
4. Adicionar Foto: Faça upload de uma foto (opcional) ou clique em "Pular".
5. Confirmação: Revise os dados e clique em "Enviar" ou "Voltar ao Início".
6. Feedback: Mensagem de sucesso ou erro será exibida; os dados são salvos no SQLite.


**Vereadores Pré-definidos**
* Antonio Carlos Pereira (Pereira da Saúde) - pereira.da.saude@camaracabreuva.sp.gov.br
* Armando Erik Domingues de Castro (Armando Castro) - armando.castro@camaracabreuva.sp.gov.br
* Devani Cristina de Araújo Debone (Devani Debone) - devani.debone@camaracabreuva.sp.gov.br
* Inivaldo dos Santos (Mirandinha) - mirandinha@camaracabreuva.sp.gov.br
* Luciano Carlos Barboza (Luciano Barboza) - luciano.barboza@camaracabreuva.sp.gov.br
* Luis Henrique Berti Barcelos (Barcelos) - barcelos@camaracabreuva.sp.gov.br
* Marlúcia de Fátima Valente (Marlúcia Valente) - marlucia.valente@camaracabreuva.sp.gov.br
* Rodrigo José Santi (Rodrigo Santi) - rodrigo.santi@camaracabreuva.sp.gov.br
* Vitor Davi Ricci Camargo (Vitor Camargo) - vitor.camargo@camaracabreuva.sp.gov.br

**Banco de Dados**

* Tabela: solicitacao
* Colunas:
    id: Chave primária (inteiro).
    nome: Nome do cidadão (texto, obrigatório).
    telefone: Telefone (texto, obrigatório).
    descricao: Descrição da solicitação (texto, obrigatório).
    vereador_email: E-mail do vereador (texto, obrigatório).
    foto_path: Caminho da foto (texto, opcional).
    status: Status do envio (texto: Pendente, Enviado, Erro).


**Controle de Versão**

git init
git add .
git commit -m "Versão inicial do Sou Cidadão Web com SQLite"


**Notas Adicionais**
    Segurança: Use HTTPS em produção e proteja as credenciais com variáveis de ambiente (os.environ).
    Escalabilidade: Para maior volume, substitua SQLite por PostgreSQL ou MySQL.
    Expansão: Adicione uma interface administrativa para consultar solicitações no banco de dados.


**Contribuição**
    Abra issues ou pull requests no repositório (se aplicável).


**Licença**
Código aberto para fins educacionais ou municipais.

Contato
Desenvolvido por [AlfredAlpha]. Contato: [alfredoamorim@gmail.com].