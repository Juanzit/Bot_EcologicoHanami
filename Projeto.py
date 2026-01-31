import discord
from discord.ext import commands
import os
import random
import requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def passo_a_passo(ctx):
    guia = [
        "1. Separe o lixo em dois. 1- Organico 2- Reciclavel",
        "2. Reduza o volume: esmague as embalagens",
        "3. Informe-se sobre pontos de coleta",
        "4. Engaje-se sobre a comunidade"
    ]
    for passo in guia:
        await ctx.send(passo)
        
@bot.command()
async def tempo(ctx):
    materiais = {
        "Plastico": "450 anos",
        "Vidro": "1.000.000 de anos (um milhão)",
        "Jornais": "3 a 5 anos"
    }
    item, tempo_vida = random.choice(list(materiais.items()))
    await ctx.send(f"Você sabia? O material {item} leva cerca de {tempo_vida} para se decompor!")

@bot.command()
async def tipos_de_reciclagem(ctx):
    caminhodapasata = r'C:\Projetos\Python_Pro\Turma_1517\M1L6\imagens'
    
    arquivos = os.listdir(caminhodapasata)
    img_name = random.choice(arquivos)
    
    explicações = {
        "papel": "🔵 Este item vai na lixeira AZUL (Papel e Papelão).",
        "plastico": "🔴 Este item vai na lixeira VERMELHA (Plásticos).",
        "vidro": "🟢 Este item vai na lixeira VERDE (Vidro).",
    }

    with open(f'{caminhodapasata}/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

    encontrou_info = False
    for chave in explicações:
        if chave in img_name.lower():
            await ctx.send(explicações[chave])
            encontrou_info = True
            break
            
    if not encontrou_info:
        await ctx.send("♻️ Lembre-se sempre de higienizar as embalagens antes de descartar!")
