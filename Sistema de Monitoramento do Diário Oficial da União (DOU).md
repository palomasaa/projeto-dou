# Sistema de Monitoramento do Diário Oficial da União (DOU)

## 📋 Descrição do Projeto

Este projeto implementa um sistema automatizado de web scraping para monitorar o Diário Oficial da União, coletar edições diárias e notificar via e-mail (e opcionalmente WhatsApp) quando entidades específicas forem mencionadas. O sistema também expõe uma API REST para consulta dos dados coletados.

## 🎯 Funcionalidades

### ✅ Funcionalidades Implementadas
- ✅ Web scraping automatizado do site oficial do DOU (https://www.in.gov.br/leiturajornal)
- ✅ Filtragem por entidades específicas (27 entidades governamentais cadastradas)
- ✅ Sistema de notificação por e-mail
- ✅ API REST para consulta de dados
- ✅ Pipeline automatizado de execução
- ✅ Base de dados de contatos das entidades

### 🔄 Funcionalidades Planejadas
- 🔄 Integração com WhatsApp Business API (requer configuração externa)
- 🔄 Agendamento automático (cron jobs)
- 🔄 Interface web para visualização

## 🏗️ Arquitetura do Sistema

### Componentes Principais

1. **Web Scraper** (`main.py`)
   - Extrai dados do site oficial do DOU
   - Filtra publicações por entidades específicas
   - Estrutura os dados extraídos

2. **Sistema de Notificação** (`send_notification.py`)
   - Envia e-mails para as entidades mencionadas
   - Suporte para WhatsApp (configuração externa necessária)

3. **Base de Contatos** (`contacts.py`)
   - 27 entidades governamentais cadastradas
   - Informações de telefone, e-mail e WhatsApp

4. **Pipeline** (`pipeline.py`)
   - Orquestra todo o processo automatizado
   - Integra scraping, filtragem e notificação

5. **API REST** (`dou_api/`)
   - Endpoints para consulta de dados
   - Interface programática para o sistema

## 📦 Estrutura do Projeto

```
projeto-dou/
├── main.py                 # Web scraper principal
├── pipeline.py             # Pipeline de automação
├── send_notification.py    # Sistema de notificação
├── contacts.py             # Base de dados de contatos
├── browser_tools.py        # Ferramentas de navegação
├── .env.example           # Exemplo de configuração
├── dou_api/               # API REST
│   ├── src/
│   │   ├── main.py        # Servidor Flask
│   │   └── routes/
│   │       └── dou.py     # Endpoints da API
│   ├── requirements.txt   # Dependências da API
│   └── venv/             # Ambiente virtual
└── README.md             # Esta documentação
```

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.11+
- VS Code (recomendado)
- Git

### Passo a Passo Detalhado

#### 1. Preparação do Ambiente

```bash
# Clone ou baixe o projeto
git clone <url-do-repositorio>
cd projeto-dou

# Ou crie um diretório e copie os arquivos
mkdir projeto-dou
cd projeto-dou
# Copie todos os arquivos do projeto para este diretório
```

#### 2. Configuração do VS Code

1. **Abra o VS Code**
2. **Abra a pasta do projeto**: `File > Open Folder` → Selecione a pasta `projeto-dou`
3. **Instale as extensões recomendadas**:
   - Python (Microsoft)
   - Python Debugger (Microsoft)
   - GitLens (opcional)

#### 3. Configuração do Ambiente Python

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install requests beautifulsoup4 python-dotenv
```

#### 4. Configuração das Credenciais de E-mail

1. **Crie o arquivo `.env`** na raiz do projeto:
```bash
cp .env.example .env
```

2. **Edite o arquivo `.env`** com suas credenciais:
```env
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
```

3. **Configure uma senha de aplicativo no Gmail**:
   - Acesse sua Conta do Google
   - Vá em "Segurança" → "Senhas de app"
   - Gere uma nova senha de aplicativo
   - Use essa senha no arquivo `.env`

#### 5. Configuração da API

```bash
# Entre no diretório da API
cd dou_api

# Ative o ambiente virtual da API
source venv/bin/activate

# As dependências já estão instaladas, mas se necessário:
pip install -r requirements.txt
```

## 🎮 Como Usar

### Execução Manual

#### 1. Web Scraping Simples
```bash
# Ative o ambiente virtual
source venv/bin/activate

# Execute o scraper
python main.py
```

#### 2. Pipeline Completo
```bash
# Execute o pipeline completo
python pipeline.py
```

#### 3. API REST
```bash
# Entre no diretório da API
cd dou_api
source venv/bin/activate

# Inicie o servidor
python src/main.py
```

A API estará disponível em: `http://localhost:5000`

### Endpoints da API

#### 1. Health Check
```bash
curl -X GET http://localhost:5000/api/dou/health
```

#### 2. Listar Entidades
```bash
curl -X GET http://localhost:5000/api/dou/entities
```

#### 3. Obter Contato de Entidade
```bash
curl -X GET http://localhost:5000/api/dou/entity/ANTT/contact
```

#### 4. Buscar Publicações
```bash
# Todas as publicações
curl -X GET http://localhost:5000/api/dou/publications

# Filtrar por entidade
curl -X GET "http://localhost:5000/api/dou/publications?entity=ANTT"

# Filtrar por data
curl -X GET "http://localhost:5000/api/dou/publications?date=01/07/2025"
```

## 🔧 Configuração Avançada

### Agendamento Automático

Para executar o sistema automaticamente todos os dias:

#### Linux/Mac (crontab)
```bash
# Edite o crontab
crontab -e

# Adicione a linha para executar às 9h todos os dias
0 9 * * * cd /caminho/para/projeto-dou && source venv/bin/activate && python pipeline.py
```

#### Windows (Task Scheduler)
1. Abra o "Agendador de Tarefas"
2. Crie uma nova tarefa básica
3. Configure para executar diariamente às 9h
4. Ação: Iniciar programa
5. Programa: `python`
6. Argumentos: `pipeline.py`
7. Iniciar em: `C:\caminho\para\projeto-dou`

### Configuração do WhatsApp

Para habilitar notificações via WhatsApp, você precisará:

1. **WhatsApp Business API**:
   - Registre-se no Facebook for Developers
   - Configure uma aplicação WhatsApp Business
   - Obtenha as credenciais da API

2. **Serviços Terceirizados** (mais fácil):
   - Twilio WhatsApp API
   - MessageBird
   - Vonage (Nexmo)

3. **Atualize o código**:
```python
# Em send_notification.py, adicione:
import requests

def send_whatsapp(phone, message):
    # Exemplo com Twilio
    url = "https://api.twilio.com/2010-04-01/Accounts/YOUR_SID/Messages.json"
    data = {
        'From': 'whatsapp:+14155238886',  # Número do Twilio
        'To': f'whatsapp:+55{phone}',
        'Body': message
    }
    auth = ('YOUR_SID', 'YOUR_TOKEN')
    response = requests.post(url, data=data, auth=auth)
    return response.status_code == 201
```

## 📊 Entidades Monitoradas

O sistema monitora 27 entidades governamentais:

### Poder Executivo
- Ministério da Agricultura e Pecuária (MAPA)
- Ministério da Ciência, Tecnologia e Inovações (MCTI)
- Ministério da Defesa (MD)
- Ministério do Planejamento e Orçamento (MPO)
- Ministério da Gestão e da Inovação em Serviços Públicos (MGI)
- Ministério da Justiça e Segurança Pública (MJSP)
- Ministério da Saúde (MS)
- Ministério das Relações Exteriores (Itamaraty)
- Ministério do Trabalho
- Ministério do Turismo

### Órgãos Extra-Ministeriais
- Advocacia-Geral da União (AGU)
- Controladoria-Geral da União (CGU)
- Gabinete de Segurança Institucional (GSI)
- Agência Brasileira de Inteligência (ABIN)

### Agências Reguladoras
- ANVISA, ANEEL, ANP, ANATEL, ANAC, ANS, ANTT, ANTAQ

### Autarquias e Institutos
- Instituto Nacional do Seguro Social (INSS)
- Instituto Nacional de Metrologia (Inmetro)
- Banco Central
- DNIT, DNOCS

## 🔍 Solução de Problemas

### Problemas Comuns

#### 1. Erro de Importação
```
ModuleNotFoundError: No module named 'requests'
```
**Solução**: Ative o ambiente virtual e instale as dependências
```bash
source venv/bin/activate
pip install requests beautifulsoup4 python-dotenv
```

#### 2. Erro de E-mail
```
SMTPAuthenticationError: Username and Password not accepted
```
**Solução**: 
- Verifique se a senha de aplicativo está correta
- Confirme que a verificação em duas etapas está ativada no Gmail
- Use a senha de aplicativo, não a senha da conta

#### 3. API não responde
```
Connection refused
```
**Solução**:
- Verifique se o servidor Flask está rodando
- Confirme que está usando a porta correta (5000)
- Teste com `curl http://localhost:5000/api/dou/health`

#### 4. Web Scraping falha
```
Nenhuma publicação encontrada
```
**Solução**:
- Verifique se o site do DOU está acessível
- Confirme que a estrutura HTML não mudou
- Teste manualmente no navegador

### Logs e Debug

Para ativar logs detalhados:

```python
# Adicione no início dos arquivos Python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Melhorias Futuras

### Curto Prazo
- [ ] Interface web para visualização
- [ ] Relatórios em PDF
- [ ] Filtros avançados por tipo de ato
- [ ] Histórico de notificações

### Médio Prazo
- [ ] Machine Learning para classificação automática
- [ ] Análise de sentimento das publicações
- [ ] Dashboard com métricas
- [ ] Integração com Telegram

### Longo Prazo
- [ ] App mobile
- [ ] Análise preditiva
- [ ] Integração com outros diários oficiais
- [ ] Sistema de alertas inteligentes

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:

1. **Issues**: Abra uma issue no GitHub
2. **E-mail**: Entre em contato através do e-mail do projeto
3. **Documentação**: Consulte esta documentação completa

---

**Desenvolvido com ❤️ para automatizar o monitoramento do Diário Oficial da União**

