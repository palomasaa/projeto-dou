# 🚀 Guia Completo de Instalação no VS Code

Este guia detalha **passo a passo** como configurar e executar o Sistema de Monitoramento do DOU no VS Code.

## 📋 Pré-requisitos

### 1. Instalar o Python
- **Windows**: Baixe em https://python.org/downloads/
- **Mac**: Use Homebrew: `brew install python`
- **Linux**: `sudo apt install python3 python3-pip`

### 2. Instalar o VS Code
- Baixe em https://code.visualstudio.com/
- Instale normalmente

### 3. Instalar o Git (opcional)
- Baixe em https://git-scm.com/

## 🔧 Configuração Inicial

### Passo 1: Preparar o Projeto

1. **Criar pasta do projeto**:
   ```
   - Crie uma pasta chamada "projeto-dou" no seu computador
   - Exemplo: C:\Users\SeuNome\projeto-dou (Windows)
   - Exemplo: /home/seunome/projeto-dou (Linux)
   ```

2. **Copiar arquivos**:
   ```
   Copie todos os arquivos do projeto para esta pasta:
   - main.py
   - pipeline.py
   - send_notification.py
   - contacts.py
   - browser_tools.py
   - exemplo_uso.py
   - .env.example
   - README.md
   - GUIA_VSCODE.md
   - pasta dou_api/ (completa)
   ```

### Passo 2: Abrir no VS Code

1. **Abrir VS Code**
2. **Abrir pasta**: `File > Open Folder`
3. **Selecionar**: Escolha a pasta "projeto-dou"

### Passo 3: Instalar Extensões

1. **Abrir Extensions**: Clique no ícone de extensões (quadrado com peças) ou `Ctrl+Shift+X`
2. **Instalar estas extensões**:
   - `Python` (Microsoft) - OBRIGATÓRIA
   - `Python Debugger` (Microsoft) - OBRIGATÓRIA
   - `GitLens` (opcional)

### Passo 4: Configurar Python

1. **Abrir Terminal**: `Terminal > New Terminal` ou `Ctrl+Shift+``
2. **Verificar Python**:
   ```bash
   python --version
   # ou
   python3 --version
   ```
3. **Criar ambiente virtual**:
   ```bash
   # Windows
   python -m venv venv
   
   # Linux/Mac
   python3 -m venv venv
   ```

4. **Ativar ambiente virtual**:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

5. **Instalar dependências**:
   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

### Passo 5: Configurar Credenciais

1. **Copiar arquivo de exemplo**:
   ```bash
   # Windows
   copy .env.example .env
   
   # Linux/Mac
   cp .env.example .env
   ```

2. **Editar arquivo .env**:
   - Abra o arquivo `.env` no VS Code
   - Substitua as informações:
   ```env
   EMAIL_USER=seu_email@gmail.com
   EMAIL_PASSWORD=sua_senha_de_aplicativo
   ```

3. **Configurar Gmail** (se usar Gmail):
   - Acesse https://myaccount.google.com/
   - Vá em "Segurança"
   - Ative "Verificação em duas etapas"
   - Vá em "Senhas de app"
   - Gere uma senha para "Mail"
   - Use essa senha no arquivo `.env`

## 🎮 Como Executar

### Teste 1: Exemplo Básico

1. **No terminal do VS Code**:
   ```bash
   python exemplo_uso.py
   ```

2. **Resultado esperado**:
   ```
   🚀 SISTEMA DE MONITORAMENTO DO DOU - EXEMPLOS DE USO
   ============================================================
   ✅ Arquivo .env carregado
   === EXEMPLO BÁSICO ===
   Simulando busca de publicações do DOU...
   Encontradas 2 publicações:
   - Entidade: ANTT
     Edição: 121 de 01/07/2025
     Página: 45
     Link: /link1
   ...
   ```

### Teste 2: API REST

1. **Abrir novo terminal**: `Terminal > New Terminal`

2. **Navegar para API**:
   ```bash
   cd dou_api
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Iniciar servidor**:
   ```bash
   python src/main.py
   ```

4. **Resultado esperado**:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

5. **Testar API** (em outro terminal):
   ```bash
   curl http://localhost:5000/api/dou/health
   ```

### Teste 3: Pipeline Completo

1. **No terminal principal**:
   ```bash
   python pipeline.py
   ```

**Nota**: Este teste requer configuração adicional de navegador automatizado.

## 🔍 Solução de Problemas no VS Code

### Problema 1: Python não encontrado

**Erro**: `'python' is not recognized as an internal or external command`

**Solução**:
1. Pressione `Ctrl+Shift+P`
2. Digite "Python: Select Interpreter"
3. Escolha o Python instalado
4. Ou use `python3` em vez de `python`

### Problema 2: Módulo não encontrado

**Erro**: `ModuleNotFoundError: No module named 'requests'`

**Solução**:
1. Verifique se o ambiente virtual está ativo (deve aparecer `(venv)` no terminal)
2. Se não estiver, ative:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```
3. Instale novamente:
   ```bash
   pip install requests beautifulsoup4 python-dotenv
   ```

### Problema 3: Erro de e-mail

**Erro**: `SMTPAuthenticationError`

**Solução**:
1. Verifique se o arquivo `.env` existe e tem as credenciais corretas
2. Para Gmail, use senha de aplicativo, não a senha normal
3. Teste com um e-mail simples primeiro

### Problema 4: API não responde

**Erro**: `Connection refused`

**Solução**:
1. Verifique se o servidor Flask está rodando
2. Olhe se apareceu a mensagem "Running on http://127.0.0.1:5000"
3. Teste no navegador: http://localhost:5000/api/dou/health

## 🎯 Dicas do VS Code

### Atalhos Úteis
- `Ctrl+Shift+P`: Paleta de comandos
- `Ctrl+Shift+``: Novo terminal
- `Ctrl+S`: Salvar arquivo
- `F5`: Executar com debug
- `Ctrl+F5`: Executar sem debug

### Configurações Recomendadas

1. **Abrir configurações**: `File > Preferences > Settings`
2. **Buscar por "python"**
3. **Configurar**:
   - `Python: Default Interpreter Path`: Caminho do seu Python
   - `Python: Terminal Execute In File Dir`: ✅ Ativado

### Debug no VS Code

1. **Criar arquivo de debug**:
   - Vá em `Run and Debug` (Ctrl+Shift+D)
   - Clique em "create a launch.json file"
   - Escolha "Python File"

2. **Executar com debug**:
   - Coloque breakpoints clicando na margem esquerda
   - Pressione F5 para executar

## 📁 Estrutura Final no VS Code

```
projeto-dou/
├── 📁 venv/                    # Ambiente virtual
├── 📁 dou_api/                 # API REST
│   ├── 📁 venv/
│   ├── 📁 src/
│   └── 📄 requirements.txt
├── 📄 main.py                  # Web scraper
├── 📄 pipeline.py              # Pipeline automático
├── 📄 send_notification.py     # Sistema de e-mail
├── 📄 contacts.py              # Contatos das entidades
├── 📄 browser_tools.py         # Ferramentas de navegação
├── 📄 exemplo_uso.py           # Exemplos de teste
├── 📄 .env                     # Suas credenciais (não compartilhar)
├── 📄 .env.example             # Exemplo de configuração
├── 📄 README.md                # Documentação principal
└── 📄 GUIA_VSCODE.md          # Este guia
```

## 🚀 Próximos Passos

Após configurar tudo:

1. **Teste todos os exemplos**
2. **Configure suas credenciais reais**
3. **Execute o pipeline completo**
4. **Explore a API**
5. **Personalize para suas necessidades**

## 📞 Suporte

Se tiver problemas:

1. **Verifique este guia novamente**
2. **Consulte o README.md**
3. **Teste os exemplos um por um**
4. **Verifique se todas as dependências estão instaladas**

---

**✅ Com este guia, qualquer pessoa consegue executar o projeto no VS Code!**

