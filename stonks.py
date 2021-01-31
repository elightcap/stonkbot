#stonks.py

import os
import requests
import json
import discord
import threading
import yfinance as yf

from dotenv import load_dotenv
from operator import itemgetter

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg=message.content
    case = msg.lower()
    try:
        if  "!stonk" in case:
            str1 = case.replace("!stonk ","")
            if "$" in str1:
                str2 = str1.replace("$","")
                print(str2)
            else:
                str2 = str1
            ticker = yf.Ticker(str2)
            info = ticker.info
            result = json.dumps(info)
            json_data = json.loads(result)
            title = json_data['shortName']
            symbol = json_data['symbol']
            mOpen = json_data['open']
            price = json_data['bid']
            img = json_data['logo_url']
            embed = discord.Embed(title="{}".format(title), description="{}".format(symbol), color=0x00ff00)
            embed.add_field(name="Price", value="{:,}".format(price), inline=False)
            embed.add_field(name="Market Open", value="{:,}".format(mOpen), inline=False)
            embed.set_image(url="{}".format(img))
            print(title)
            send = await message.channel.send(embed=embed)
    except:
        mes = "You fucked up retard"
        send = await message.channel.send(mes)
client.run(TOKEN)
