from settings import settings
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= '!', intents=intents)
@bot.command()

async def cuphead(ctx):
    await ctx.send(f"""Hola, soy un bot {bot.user}!""")
    await ctx.send(f'Te voy hablar un poco sobre el juego Cuphead')
    await ctx.send(f"""
                   Cuphead es un juego clásico de acción de disparos muy enfocado en batallas de jefes. 
                   Inspirado en las caricaturas de 1930, las imágenes y el audio se crearon de forma 
                   minuciosa con las mismas técnicas de la era, esto es, animación tradicional a mano, 
                   fondos de marca de agua y grabaciones originales de jazz.""")
    # Enviar una pregunta al usuario
    await ctx.send("Quieres consejos para ganar facilmente? Responde con 'sí' o 'no'.")
# Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['sí', 'si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content in ['sí', 'si']:
            await ctx.send("1. No olvides equipar el dash (sera de vital importancia)")
            await ctx.send("2. Utiliza la tienda de Porkrind's Emporium para equiparte buenas armas") 
            await ctx.send("3. Puedes usar vidas adicionales si apenas estas empezando")  
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("¿Quieres saber la definicion de la palabra Cuphead?, responde si o no")
    response1 = await bot.wait_for('message', check=check)
    if response1:
        if response1.content in ['sí', 'si']:
            await ctx.send("""Su nombre al español significa "Cabeza de Taza". Cuando se 
                           inicia una batalla contra el jefe, Cuphead siempre levanta sus 
                           pantalones, sonriendo y con determinación.""") 
        else:
            await ctx.send("Está bien, si alguna vez necesitas consejos, no dudes en preguntar.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
bot.run(settings["TOKEN"])