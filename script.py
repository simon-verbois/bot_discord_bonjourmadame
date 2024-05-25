import os
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import aiohttp

def fetch_image_and_title():
    url = "https://bonjourmadame.fr/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        post_content = soup.find('div', class_='post-content')
        post_title = soup.find('h1', class_='post-title')
        if post_content and post_title:
            img_tag = post_content.find('img')
            title_text = post_title.get_text(strip=True)
            if img_tag:
                return img_tag['src'], title_text
    return None, None

async def download_image(url, path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(path, 'wb') as f:
                    f.write(await response.read())

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await post_image_and_title()
    await bot.close()

async def post_image_and_title():
    image_url, title_text = fetch_image_and_title()
    if image_url and title_text:
        channel = bot.get_channel(CHANNEL_ID)
        await download_image(image_url, 'image.jpg')
        await channel.send(f"# **{title_text}**", file=discord.File('image.jpg'))
    else:
        print("No image or text found")

@bot.command()
async def bonjourmadame(ctx):
    image_url, title_text = fetch_image_and_title()
    if image_url and title_text:
        await download_image(image_url, 'image.jpg')
        await ctx.send(f"**{title_text}**", file=discord.File('image.jpg'))
    else:
        await ctx.send("No image or text found")

bot.run(TOKEN)
