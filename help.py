import discord
from discord.ext import commands

permissions = discord.Intents.default()
permissions.message_content = True

bot = commands.Bot(command_prefix="o!", intents=permissions, help_command=None)

# Avisa quando o bot está online
@bot.event
async def on_ready():
    print("Estou online!")

# Comando responsável por dizer todos os comandos do bot
@bot.command(name="help")
async def help(ctx: commands.Context):
    menu = discord.Embed(
        title="Lista de comandos: ",
        description=''
        )

    # Array de comandos 
    lista_de_comandos = [
        ("o!pergunta", "Disponibiliza informações do projeto e do servidor no geral"),
        ("o!comando 2", "Este comando faz exemplo 2"),
        ("o!comando 3", "Este comando faz exemplo 3"),
        ("o!comando 4", "Este comando faz exemplo 4")
    ]

    # Loop para mencionar todos os comandos do array ( deixando mais fácil de fazer qualquer mudança futura)
    for comando, informação in lista_de_comandos:
        menu.add_field(name=comando, value=informação, inline=False)


    # Manda a lista de comandos para o chat do servidor do discord
    await ctx.send(embed=menu)

# Responde perguntas sobre o projeto e sobre o servidor do discord
@bot.group()
async def pergunta(ctx: commands.Context):
    duvida = discord.Embed(
        title= "Sobre o que se trata a sua dúvida?",
        description= "Digite: <comando> <categoria>"
    )

    # Separar ainda mais as categorias das perguntas para caso haja uma futura implementação de ideia
    duvida.add_field(name="Informações:", value="", inline=False)
    # Sessão onde vai aparecer as "categorias" das perguntas
    duvida.add_field(name= "", value= "**Sobre o servidor:** o!pergunta servidor", inline=False)
    duvida.add_field(name= "", value= "**Sobre a comunidade:**  o!pergunta comunidade", inline=False)
    duvida.add_field(name= "", value= "**Como contribuir:**  o!pergunta contribuir", inline=False)
    duvida.add_field(name= "", value= "**Objetivos do projeto:** o!pergunta projeto", inline=False)

    # Manda a embed para o chat do discord se não for passado nenhum comando além do "o!pergunta"
    if ctx.invoked_subcommand is None:
        await ctx.send(embed=duvida)

# comando "o!pergunta servidor" com o objetivo de informar sobre o servidor do discord
@pergunta.command()
async def servidor(ctx: commands.Context):
    servidor_info = discord.Embed(
        title= "Sobre o servidor",
        description= "O servidor é onde nos reunimos para discutir sobre o projeto",
    )
    await ctx.send(embed=servidor_info)

# comando "o!pergunta comunidade" com o objetivo de informar sobre a comunidade do projeto
@pergunta.command()
async def comunidade(ctx: commands.Context):
    comunidade_info = discord.Embed(
        title= "Sobre a comunidade",
        description= "Nesta comunidade você encontra devs front-end, back-end, engenheiros de dados e etc..., se quiser se juntar a nós, seja bem-vindo"
    )
    await ctx.send(embed=comunidade_info)

# comando "o!pergunta contribuir" com o objetivo de informar sobre como o usuario pode contribuir para o projeto
@pergunta.command()
async def contribuir(ctx: commands.Context):
    contribuição_info = discord.Embed(
        title= "Sobre a contribuição",
        description= "Para contribuir com o nosso projeto, fale diretamente com um dos administradores do servidor do discord"
    )
    await ctx.send(embed=contribuição_info)

# comando "o!pergunta projeto" com o objetivo de informar sobre o objetivo do projeto
@pergunta.command()
async def projeto(ctx: commands.Context):
    projeto_info = discord.Embed(
        title = "Nosso objetivo",
        description= "Temos como objetivo criar um software de gerenciamento de recursos sobre aeroportos em escala global"
    )
    await ctx.send(embed=projeto_info)

# roda o bot
bot.run("")