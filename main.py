import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

# --- Mini server per tenerlo online ---
app = Flask('')


@app.route('/')
def home():
    return "Il bot è attivo!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


# --- Discord bot ---
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot attivo come {bot.user}")


@bot.event
async def on_member_join(member):
    try:
        await member.send(
            "👋 Benvenuto nel server! Per poter accedere aicanali invia un'email a comunicazioni@associazionedracones.it con il tuo nome utente (es. caio#0000) e il numero della tua tessera, oggetto DISCORD"
        )
        print(f"📩 Messaggio inviato a {member.name}")
    except discord.Forbidden:
        print(f"⚠️ Non posso inviare un DM a {member.name}")


# --- Avvio ---
keep_alive()
bot.run(os.environ["DISCORD_TOKEN"])
