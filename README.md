# 💰 HTechFin - Assistente Virtual Financeira com IA Generativa

## 📖 Sobre o Projeto

A HTechFin é uma assistente virtual desenvolvida em Python com IA Generativa, criada para auxiliar usuários na análise de suas finanças pessoais.

O sistema utiliza dados financeiros simulados, incluindo transações bancárias, perfil do investidor, histórico de atendimentos e produtos financeiros, com o intuito de gerar respostas personalizadas e contextualizadas através do modelo Gemini.

Este projeto foi desenvolvido como um desafio prático do Bootcamp da Digital Innovation One (DIO).

---

## 🎯 Objetivo

O objetivo da HTech Financeira é ajudar usuários a:

* Compreender sua situação financeira atual;
* Acompanhar suas metas financeiras;
* Analisar receitas, despesas e saldo disponível;
* Identificar padrões de gastos;
* Conhecer produtos financeiros compatíveis com seu perfil;
* Receber orientações financeiras educativas baseadas em IA.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* Google Gemini API
* Python Dotenv
* JSON
* CSV

---

## 🤖 Inteligência Artificial

O projeto utiliza IA Generativa através do modelo Gemini.

Antes de enviar uma pergunta para a IA, o sistema realiza todo o processamento dos dados financeiros do cliente e gera um contexto estruturado contendo:

* Perfil do investidor;
* Receitas e despesas;
* Saldo atual;
* Gastos por categoria;
* Metas financeiras;
* Produtos financeiros disponíveis.

Esse contexto é enviado juntamente com a pergunta do usuário para que a IA analise e produza respostas personalizadas e alinhadas à realidade financeira do usuário.

---

## 📂 Estrutura do Projeto

```text
assistente-virtual-financeira/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   └── produtos_financeiros.json
│
└── README.md
```

---

## 📊 Base de Conhecimento

O sistema utiliza os seguintes arquivos:

### transacoes.csv

Contém o histórico financeiro do cliente:

* Data
* Descrição
* Categoria
* Valor
* Tipo (entrada ou saída)

### perfil_investidor.json

Contém informações do cliente:

* Nome
* Idade
* Profissão
* Perfil de investidor
* Objetivos financeiros
* Metas
* Patrimônio

### historico_atendimento.csv

Armazena interações anteriores realizadas pelo cliente.

### produtos_financeiros.json

Contém produtos financeiros disponíveis para análise e recomendação.

---

## 🔒 Segurança e Anti-Alucinação

A HTechFin segue as seguintes regras:

* Responde apenas com base nos dados fornecidos;
* Não inventa informações inexistentes;
* Informa quando não possui dados suficientes para responder;
* Considera o perfil do investidor antes de sugerir produtos;
* Não realiza recomendações financeiras definitivas;
* Atua apenas como ferramenta de apoio educacional.

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

### 4. Execute a aplicação

```bash
python -m streamlit run app.py
```

### 5. Acesse no navegador

```text
http://localhost:8501
```

---

## 💡 Exemplos de Perguntas

* Quanto falta para completar minha reserva de emergência?
* Qual é o meu perfil de investidor?
* Quanto gastei com moradia?
* Qual categoria possui o maior gasto?
* Quais produtos financeiros combinam com meu perfil?
* Qual é o meu saldo atual?

---

## 📈 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

* Manipulação de arquivos CSV e JSON;
* Análise de dados com Pandas;
* Engenharia de Prompt (Prompt Engineering);
* Consumo de APIs;
* IA Generativa;
* Estruturação de contexto para LLMs;
* Desenvolvimento de interfaces com Streamlit;
* Boas práticas de segurança com variáveis de ambiente.

---

## 👨‍💻 Autor

Desenvolvido por Hiarlley Freitas como projeto prático de aprendizado em Python, Análise de Dados e Inteligência Artificial Generativa.
