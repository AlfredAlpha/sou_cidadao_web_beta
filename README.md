# README - Sou Cidadão (Kivy + Flask)

## Descrição
"Sou Cidadão" é um aplicativo multiplataforma desenvolvido com Kivy (cliente) e Flask (servidor), permitindo que moradores de Cabreúva/SP enviem solicitações aos vereadores da cidade. O cliente Kivy apresenta uma interface gráfica com as cores da bandeira de Cabreúva (verde, branco e azul), enquanto o servidor Flask gerencia o envio de e-mails, eliminando a necessidade de configurações SMTP no aplicativo cliente.

### Funcionalidades
- Interface inicial com apresentação do aplicativo.
- Seleção de um vereador pré-definido da Câmara Municipal de Cabreúva.
- Preenchimento de campos obrigatórios: nome, telefone e descrição.
- Opção de tirar uma foto com a câmera ou escolher da galeria (opcional).
- Tela de confirmação com os dados preenchidos.
- Envio da solicitação ao servidor, que a encaminha por e-mail ao vereador.
- Mensagem de sucesso ou erro após o envio, com opção de voltar ao início.

## Pré-requisitos
- **Python 3.8+**: Necessário para executar Kivy e Flask.
- **Git**: Para controle de versão (opcional, mas recomendado).
- **Servidor SMTP**: Configuração de e-mail válida no servidor (ex.: Gmail com senha de aplicativo).
- **Sistema Operacional**: Testado em Windows, Linux e macOS; para mobile, requer compilação adicional.

## Dependências
### Cliente (Kivy)
- `kivy`: Framework para interfaces gráficas.
- `plyer`: Acesso a câmera e galeria.
- `requests`: Para comunicação com o servidor.

### Servidor (Flask)
- `flask`: Framework web para processar solicitações e enviar e-mails.

## Instalação
1. **Clone o Repositório** (se estiver usando Git):
   ```bash
   git clone https://github.com/AlfredAlpha/sou_cidadao_web_beta.git
   cd sou_cidadao_web_beta

Caso contrário, baixe os arquivos manualmente.

Configure o Servidor:
bash
Wrap
Copy
cd server
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Edite app.py e substitua EMAIL_USER e EMAIL_PASSWORD por credenciais válidas.
Configure o Cliente:
bash
Wrap
Copy
cd client
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
mkdir uploads
Como Executar
Inicie o Servidor:
bash
Wrap
Copy
cd server
python app.py
O servidor estará disponível em http://127.0.0.1:5000.
Inicie o Cliente:
bash
Wrap
Copy
cd client
python main.py
Uma janela gráfica será aberta com a tela inicial do "Sou Cidadão".
Estrutura do Projeto
text
Wrap
Copy
sou-cidadao-kivy/
│
├── client/             # Código do cliente Kivy
│   ├── main.py         # Aplicativo Kivy
│   ├── uploads/        # Pasta para fotos temporárias
│   └── requirements.txt
│
├── server/             # Código do servidor Flask
│   ├── app.py          # Servidor Flask
│   └── requirements.txt
│
└── README.md           # Este arquivo de documentação
Arquivo client/requirements.txt
text
Wrap
Copy
kivy==2.1.0
plyer==2.1.0
requests==2.28.1
Arquivo server/requirements.txt
text
Wrap
Copy
flask==2.2.2
Uso
Tela de Apresentação: Clique em "Iniciar".
Seleção de Vereador: Escolha um vereador da lista e clique no nome.
Preenchimento de Dados: Insira nome, telefone e descrição, clique em "Próximo".
Adicionar Foto: Tire uma foto ou escolha da galeria (opcional), clique em "Próximo".
Confirmação: Revise os dados e clique em "Enviar" para enviar ao servidor, ou "Voltar ao Início".
Feedback: Um popup exibirá "Solicitação enviada com sucesso!" ou um erro.
Vereadores Pré-definidos
Antonio Carlos Pereira (Pereira da Saúde) - pereira.da.saude@camaracabreuva.sp.gov.br
Armando Erik Domingues de Castro (Armando Castro) - armando.castro@camaracabreuva.sp.gov.br
Devani Cristina de Araújo Debone (Devani Debone) - devani.debone@camaracabreuva.sp.gov.br
Inivaldo dos Santos (Mirandinha) - mirandinha@camaracabreuva.sp.gov.br
Luciano Carlos Barboza (Luciano Barboza) - luciano.barboza@camaracabreuva.sp.gov.br
Luis Henrique Berti Barcelos (Barcelos) - barcelos@camaracabreuva.sp.gov.br
Marlúcia de Fátima Valente (Marlúcia Valente) - marlucia.valente@camaracabreuva.sp.gov.br
Rodrigo José Santi (Rodrigo Santi) - rodrigo.santi@camaracabreuva.sp.gov.br
Vitor Davi Ricci Camargo (Vitor Camargo) - vitor.camargo@camaracabreuva.sp.gov.br
Controle de Versão
Para gerenciar com Git:

bash
Wrap
Copy
git init
git add .
git commit -m "Versão inicial do Sou Cidadão com Kivy e Flask"
Notas Adicionais
Mobile: Para Android/iOS, use Buildozer no cliente Kivy (ajuste buildozer.spec com permissões de câmera e internet).
Segurança: Em produção, use HTTPS no servidor e proteja as credenciais com variáveis de ambiente (os.environ).
Escalabilidade: Considere um serviço de e-mail terceirizado (ex.: SendGrid) para maior robustez.
Contribuição
Abra issues ou pull requests no repositório (se aplicável).

Licença
Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais ou municipais.

Contato
Desenvolvido por [AlfredAlpha]. Para dúvidas, entre em contato via [alfredoamorim@gmail.com.br].