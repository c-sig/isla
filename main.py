#region token 
TOKEN = (os.environ.get('ISLA_TOKEN'))
CATGIRLS_TOKEN = os.environ.get('CATGIRLS_TOKEN')
#testaa
#endregion

from peewee import *    
import discord
from discord.ext import tasks, commands
import time
import requests
import mimetypes
import os

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

start_time = time.time()

db = SqliteDatabase('applications.sqlite')

class Applications(Model):
    unique_id = AutoField()
    applicant = CharField()
    role = CharField()
    thread_id = CharField()
    status = CharField()

    class Meta:
        database = db

db.connect()

if not Applications.table_exists():
    db.create_tables([Applications])

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(f"Time taken to start: {time.time() - start_time} seconds")

@bot.slash_command(name = "apply", description = "Apply for a role!")
async def apply(ctx,
                role: discord.Option(str, choices=['translation', 'beta reading', 'cleaning / redrawing', 'typesetting', 'copy editing'])):

    applicant_id = ctx.author.id
    