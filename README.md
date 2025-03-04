## Descrição
"Sou Cidadão" é uma aplicação web desenvolvida com Flask e MySQL, projetada para permitir que moradores de Cabreúva/SP enviem solicitações aos vereadores da cidade diretamente pelo navegador. A interface utiliza as cores da bandeira de Cabreúva (verde #006400, amarelo #FFD700 e branco #FFFFFF) e armazena as solicitações em um banco de dados MySQL para persistência.

### Funcionalidades
- Tela inicial de apresentação.
- Seleção de um vereador da Câmara Municipal de Cabreúva pré-definido.
- Preenchimento de dados obrigatórios: nome, telefone e descrição.
- Upload opcional de uma foto (via galeria ou direto do dispositivo).
- Confirmação dos dados antes do envio.
- Envio da solicitação por e-mail ao vereador selecionado.
- Persistência das solicitações no banco de dados MySQL.
- Feedback de sucesso ("Solicitação enviada com sucesso!") ou erro ("Não foi possível enviar sua solicitação"), com opção de voltar ao início.

## Pré-requisitos
- **Python 3.8+**: Necessário para executar o Flask.
- **MySQL**: Banco de dados para armazenamento das solicitações.
- **Git**: Para controle de versão (opcional).
- **Servidor SMTP**: Configuração de e-mail válida (ex.: Gmail com senha de aplicativo).
- **Navegador Web**: Para acessar a aplicação.

## Dependências
- `flask`: Framework web para backend e frontend.
- `mysql-connector-python`: Conector para integração com MySQL.
- `python-dotenv`: Para gerenciamento de variáveis de ambiente.

## Instalação
1. **Clone o Repositório** (se aplicável):
   ```bash
   git clone https://github.com/AlfredAlpha/sou_cidadao_web_beta.git
   cd sou_cidadao_web_beta
Ou baixe os arquivos manualmente.

2. **Crie um Ambiente Virtual** (opcional, recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. **Instale as Dependências:** 
    ```bash
    pip install -r requirements.txt

4. **Configure o MySQL:**
* Acesse o MySQL:
    ```bash
    mysql -u root -p

* Crie o banco de dados e a tabela:
    ```sql
    CREATE DATABASE sou_cidadao;
    USE sou_cidadao;
    CREATE TABLE solicitacoes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        vereador_id INT NOT NULL,
        nome VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        descricao TEXT NOT NULL,
        foto_path VARCHAR(255)
    );
    EXIT;

5. **Configure o Projeto:**
* Crie a pasta static/uploads/:
    ```bash
    mkdir static/uploads

* Crie um arquivo .env na raiz do projeto com suas credenciais:
    ```text
    MYSQL_HOST=localhost
    MYSQL_USER=root
    MYSQL_PASSWORD=sua-senha-aqui
    MYSQL_DB=sou_cidadao
    SECRET_KEY=sua-chave-secreta-aqui
    EMAIL_USER=seu-email@gmail.com
    EMAIL_PASSWORD=sua-senha-de-app-aqui

**Como Executar**

1. **Inicie o Servidor:**
    ```bash

    python app.py

2. **Acesse em http://127.0.0.1:5000 no navegador. O banco de dados será acessado automaticamente se configurado corretamente.**

**Estrutura do Projeto**
    ```text

sou_cidadao/
│
├── app.py              # Código principal do Flask com MySQL
├── config.py           # Configurações do projeto
├── static/             # Arquivos estáticos
│   ├── css/
│   │   └── style.css   # Estilização
│   └── uploads/        # Pasta para fotos enviadas
├── templates/          # Templates HTML
│   ├── index.html      # Tela inicial
│   ├── vereadores.html # Seleção de vereador
│   ├── formulario.html # Preenchimento de dados
│   ├── foto.html       # Upload de foto
│   └── confirmacao.html# Confirmação e envio
├── .env                # Variáveis de ambiente (não versionado)
├── requirements.txt    # Dependências
└── README.md           # Documentação

**Uso**
1. Apresentação: Clique em "Iniciar".
2. Seleção de Vereador: Escolha um vereador e clique em "Continuar".
3. Preenchimento de Dados: Insira nome, telefone e descrição, clique em "Próximo".
4. Adicionar Foto: Faça upload de uma foto (opcional) ou clique em "Pular". Botão "Voltar" disponível.
5. Confirmação: Clique em "Enviar" para mandar o e-mail ao vereador ou "Voltar" ao início.
6. Feedback: Mensagem de sucesso ou erro será exibida; os dados são salvos no MySQL.

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
* Tabela: solicitacoes
* Colunas:
    * id: Chave primária (inteiro, autoincrementado).
    * vereador_id: Índice do vereador na lista (inteiro, obrigatório).
    * nome: Nome do cidadão (texto, obrigatório).
    * telefone: Telefone (texto, obrigatório).
    * descricao: Descrição da solicitação (texto, obrigatório).
    * foto_path: Caminho da foto (texto, opcional).

**Controle de Versão**

1. Inicialize o Git:
    ```bash
    git init
    git add .
    git commit -m "Versão inicial do Sou Cidadão Web com MySQL"

2. Conecte ao repositório remoto:
    ```bash
    git remote add origin https://github.com/AlfredAlpha/sou_cidadao_web_beta.git
    git push -u origin main

**Contribuição**
Abra issues ou pull requests no repositório (se aplicável).

**Licença**
Código aberto para fins educacionais ou municipais.

Contato
Desenvolvido por [AlfredAlpha]. Contato: [alfredoamorim@gmail.com].