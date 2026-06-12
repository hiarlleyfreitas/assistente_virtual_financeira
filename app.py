import pandas as pd
import json
import os
import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

#Abrindo os arquivos CSV
transacoes = pd.read_csv("data/transacoes.csv")
historico = pd.read_csv("data/historico_atendimento.csv")

#Abrindo os arquivos JSON
with open("data/perfil_investidor.json", "r", encoding="utf-8") as arquivo:
    perfil = json.load(arquivo)

with open("data/produtos_financeiros.json", "r", encoding="utf-8") as arquivo:
    produtos = json.load(arquivo)

#Funções para acessar os dados

def calcular_total_receitas():
    total_receitas = transacoes[
        transacoes["tipo"] == "entrada"]["valor"].sum()
    return total_receitas

def calcular_total_despesas():
    total_despesas = transacoes[
        transacoes["tipo"] == "saida"]["valor"].sum()
    return total_despesas

def calcular_saldo_atual():
    saldo_atual = calcular_total_receitas() - calcular_total_despesas()
    return saldo_atual

def calcular_gastos_por_categoria():
    gastos_por_categoria = transacoes[
        transacoes["tipo"] == "saida"
    ].groupby("categoria")["valor"].sum()
    
    texto = ""

    for categoria, valor in gastos_por_categoria.items():
        texto += f"- {categoria}: R${valor:.2f}\n"

    return texto

def verificar_meta_reserva():
    metas = perfil.get("metas", [])
    reserva_atual = perfil.get("reserva_emergencia_atual", 0)
    texto = ""

    for meta in metas:
        texto += f"\nMeta: {meta['meta']}"
        texto += f"\nValor necessário: R${meta['valor_necessario']:.2f}"
        texto += f"\nPrazo: {meta['prazo']}"

        if meta["meta"] == "Completar reserva de emergência":
            progresso = (reserva_atual / meta["valor_necessario"]) * 100
            texto += f"\nReserva atual: R${reserva_atual:,.2f}"
            texto += f"\nProgresso: {progresso:.2f}%"
        
        texto += "\n"

    return texto

def gerar_contexto_financeiro():
    cliente = perfil.get("nome", "Cliente")
    perfil_investidor = perfil.get("perfil_investidor", "Perfil")
    contexto = ""

    contexto += f"\nDADOS DO CLIENTE\n\nNome: {cliente}\nPerfil: {perfil_investidor}\n"
    contexto += f"\nRESUMO FINANCEIRO\n"
    contexto += f"\nTotal de receitas: R${calcular_total_receitas():.2f}\n"
    contexto += f"Total de despesas: R${calcular_total_despesas():.2f}\n"
    contexto += f"Saldo atual: R${calcular_saldo_atual():.2f}\n"
    contexto += f"\nGASTOS POR CATEGORIA\n"
    contexto += f"\n{calcular_gastos_por_categoria()}\n"
    contexto += f"METAS FINANCEIRAS \n"
    contexto += verificar_meta_reserva()

    return contexto

def gerar_resposta_IA(prompt):
    resposta = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return resposta.text

system_prompt = """
    Você é uma assistente virtual financeira, especializada em ajudar os clientes que estão buscando organizar suas finanças pessoais, entender seu perfil de investidor e receber recomendações personalizadas de produtos financeiros.
    Seu objetivo é fornecer informações claras e úteis com base nos dados financeiros do cliente. Você tem acesso a um conjunto de dados que inclui:
    1. Transações financeiras do cliente, detalhadas por tipo (se é entrada ou saída), categoria, valor e data.
    2. Histórico de atendimento do cliente, incluindo os registros de interações anteriores, dúvidas frequentes e feedbacks fornecidos.
    3. Perfil de investidor do cliente, que inclui informações sobre a renda mensal, o objetivo principal do cliente, se ele aceita risco ou não, e as metas traçadas.
    4. Produtos financeiros, onde é detalhado o nome do produto, categoria do produto, risco, rentabilidade, aporte mínimo e o perfil de investidor que é indicado o produto.

    Você deve seguir estritamente as seguintes regras:
    1. Só responderá com base nos dados fornecidos.
    2. Quando não possuir informações suficientes para elaborar uma resposta clara, informe claramente essa limitação e solicite mais informações ao usuário.
    3. Evite a todo custo criar dados inexistentes.
    4. Apresente sugestões e alternativas, mas nunca afirme que um investimento é a escolha correta ou garantida para o cliente.
    5. Sempre considere o perfil de investidor antes de sugerir quaisquer produtos.
    6. Responda apenas perguntas relacionadas às finanças pessoais, investimentos, metas financeiras e informações sobre investimentos.
    7. Utilize linguagem clara, amigável e educativa, evitando termos excessivamente técnicos.

"""


st.title = "HTechFin - Assistente Financeira"
pergunta_usuario = st.text_input("Digite sua pergunta")

if st.button("Enviar"): 
    contexto = gerar_contexto_financeiro()

    prompt_final = f"""
    {system_prompt}

    Contexto financeiro do cliente:
    {contexto}

    Pergunta do usuário:
    {pergunta_usuario}

    Resposta:
    """
    resposta_IA = gerar_resposta_IA(prompt_final)

    st.write(resposta_IA)