import discord
import asyncio
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = discord.Client()

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
    
client.run(Put Bot Token Here)
