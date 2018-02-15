import discord
import asyncio
import json
import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

with open('swagger.json') as w:
    warframe = json.load(w)

client = discord.Client()

version = str(0.1)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    

@client.event
async def on_message(message):
    
    if message.content.startswith('!ping'):
        await client.send_message(message.channel, 'Pong')
        
    if message.content.startswith('!help'):
        await client.send_message(message.channel, '''
        !searchds - searches though darksouls 3 wepons
        !ping - pings bot''')
    
    if message.content.startswith('!searchds3'):
        que = await client.send_message(message.channel, 'searching...')
        global wepsearch
        print('searching ds3 wep...')
        wepsearch = message.content
        wepsearch = wepsearch[11:]
        gc = gspread.authorize(credentials)
        sheet = gc.open("ds3 bot sheet").sheet1 # open sheet

        def search(str):
            cell = sheet.find(str)
            
            return sheet.row_values(cell.row)
        
        await client.edit_message(que, search(wepsearch))
        
    if message.content.startswith('!praise'):
        await client.send_file(message.channel, 'praisethesun.gif')
    
    if message.content.startswith('!purge'):
        await client.purge_from(message.channel)
        
    if message.content.startswith('!invite'):
        invite = await client.create_invite(message.channel)
        await client.send_message(message.channel, invite)
    
    if message.content.startswith('!coinflip'):
        coinstate = random.randint(0,1)
        if coinstate == 1:
            coin = 'Heads'
        else:
            coin = 'Tails'
        await client.send_message(message.channel, coin)

    if message.content.startswith('!v'):
        await client.send_message(message.channel, version)
        
    if message.content.startswith('!sortie'):
        print(warframe.'/pc/sortie.get.summary'])
    
    if message.content.startswith('!'):
        await client.send_message(message.channel, 'yeah?')
            
client.run(Token Here)
