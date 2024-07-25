import discord
from discord.ext import commands
from discord import app_commands
from urllib.parse import urlparse, parse_qs
import requests

TOKEN = 'MTIyMTc4NzIyNDQ5NzA2NjAyNg.GRTuYZ.R6H7ecOdy6ciHtPahnIaV1Rc9mdves0VY_XGS4'

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Bot is ready")
    await tree.sync()
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Minecraft 🔥"))
    
# Arceus Command
@tree.command(
    name="arceus",
    description="Bypass key Arceus-x"
)
@app_commands.describe(link="Link Get Key Arceus-x")
async def arceux(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    hwid = parse_qs(parsed_url.query).get('hwid', [''])[0]

    if not hwid:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://assets.podomatic.net/ts/a0/9b/70/arceusx-iowebsite/1400x1400_16515083.png")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-arceusx/?hwid={hwid}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://assets.podomatic.net/ts/a0/9b/70/arceusx-iowebsite/1400x1400_16515083.png")
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="```Not allowed bypass```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://assets.podomatic.net/ts/a0/9b/70/arceusx-iowebsite/1400x1400_16515083.png")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://assets.podomatic.net/ts/a0/9b/70/arceusx-iowebsite/1400x1400_16515083.png")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
# Codex Command
@tree.command(
    name="codex",
    description="Bypass key Codex"
)
@app_commands.describe(link="Link Get Key Codex")
async def codex(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    token = parse_qs(parsed_url.query).get('token', [''])[0]

    if not token:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYmd5xXBZdWjnrGc9RB2PwInFk7PNcAtS_Hg&s")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-codex/?token={token}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="**New link or try again**",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYmd5xXBZdWjnrGc9RB2PwInFk7PNcAtS_Hg&s")
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="```Not allowed bypass```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYmd5xXBZdWjnrGc9RB2PwInFk7PNcAtS_Hg&s")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYmd5xXBZdWjnrGc9RB2PwInFk7PNcAtS_Hg&s")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
# Delta Command
@tree.command(
    name="delta",
    description="Bypass key Delta"
)
@app_commands.describe(link="Link Get Key Delta")
async def delta(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    id = parse_qs(parsed_url.query).get('id', [''])[0]

    if not id:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://www.softlay.com/downloads/wp-content/uploads/Delta-Executor-for-Roblox-Logo-1.png")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-delta/?hwid={id}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://www.softlay.com/downloads/wp-content/uploads/Delta-Executor-for-Roblox-Logo-1.png")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://www.softlay.com/downloads/wp-content/uploads/Delta-Executor-for-Roblox-Logo-1.png")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
# Fluxus Command
@tree.command(
    name="fluxus",
    description="Bypass key Fluxus"
)
@app_commands.describe(link="Link Get Key Fluxus")
async def fluxus(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    HWID = parse_qs(parsed_url.query).get('HWID', [''])[0]

    if not HWID:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/2558-fluxus.png")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-fluxus/?hwid={HWID}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/2558-fluxus.png")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://cdn3.emoji.gg/emojis/2558-fluxus.png")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
# Vegax Command
@tree.command(
    name="vegax",
    description="Bypass key Vegax"
)
@app_commands.describe(link="Link Get Key Vegax")
async def vegax(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    hwid = parse_qs(parsed_url.query).get('hwid', [''])[0]

    if not hwid:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://www.vegax.gg/assets/img/V_logo_white.png")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-vegax/?hwid={hwid}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://www.vegax.gg/assets/img/V_logo_white.png")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://www.vegax.gg/assets/img/V_logo_white.png")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
# Btteam Command
@tree.command(
    name="btteam",
    description="Bypass key Btteam"
)
@app_commands.describe(link="Link Get Key Btteam")
async def btteam(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    hwid = parse_qs(parsed_url.query).get('hwid', [''])[0]

    if not hwid:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://tranhdecors.com/wp-content/uploads/edd/2023/09/Anh-nen-Anime-tieu-tho-anh-dao.jpg")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-btteam/?hwid={hwid}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://tranhdecors.com/wp-content/uploads/edd/2023/09/Anh-nen-Anime-tieu-tho-anh-dao.jpg")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://tranhdecors.com/wp-content/uploads/edd/2023/09/Anh-nen-Anime-tieu-tho-anh-dao.jpg")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)

# Hydrogen Command
@tree.command(
    name="hydrogen",
    description="Bypass key Hydrogen"
)
@app_commands.describe(link="Link Get Key Hydrogen")
async def delta(interaction: discord.Interaction, link: str):
    parsed_url = urlparse(link)
    id = parse_qs(parsed_url.query).get('id', [''])[0]

    if not id:
        embed = discord.Embed(
            title="❌ Invalid Link",
            description=f"```{link}```",
            color=discord.Color.blue()
        )
        embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
        )
        embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
        embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-7yFoKxV1uIkfFTfC-8FX6vQ-t500x500.jpg")
        await interaction.response.send_message(embed=embed)
        return

    api_url = f"https://stickx.top/api-hydrogen/?hwid={id}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description=f"```New link or try again```",
                    color=0xff0000
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-7yFoKxV1uIkfFTfC-8FX6vQ-t500x500.jpg")
            else:
                embed = discord.Embed(
                    title="**✅ Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="https://i1.sndcdn.com/artworks-7yFoKxV1uIkfFTfC-8FX6vQ-t500x500.jpg")
        else:
            embed = discord.Embed(
                title="**❌ Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**❌ Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)   

# Linkvertise Command
@tree.command(
    name="linkvertise",
    description="Bypass Linkvertise link"
)
@app_commands.describe(link="Linkvertise URL")
async def linkvertise(interaction: discord.Interaction, link: str):
    api_url = f"https://stickx.top/api-linkvertise/?link={link}&api_key=E99l9NOctud3vmu6bPne"
    
    # Create an Embed to display the bot's initial response
    initial_embed = discord.Embed(
        title="🫰🏻**Please wait...**🫰🏻",
        color=discord.Color.blue()
    )

    # Send the initial Embed response
    await interaction.response.send_message(embed=initial_embed)
    
    # Perform the API request
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'key' in data:
            if data['key'] == 'Error Pls New Link or Try again':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="```Error: New link or try again```",
                    color=0xff0000
                )
            elif data['key'] == 'Not allowed bypass':
                embed = discord.Embed(
                    title="**❌ Bypass Failed**",
                    description="```Not allowed bypass```",
                    color=0xff0000
                )
            else:
                embed = discord.Embed(
                    title="**Bypass Successful!**",
                    description=f"```{data['key']}```",
                    color=discord.Color.blue()
                )
                embed.add_field(
                    name="Follow updates:",
                    value="[Discord ScriptLuaVip](https://discord.gg/usHF6Gf9db)",
                    inline=False
                )
                embed.set_footer(text="Powered by StickX | Made by ScriptLuaVip")
                embed.set_thumbnail(url="")
        else:
            embed = discord.Embed(
                title="**Error**",
                description="**Unexpected response from API**",
                color=0xff0000
            )
    else:
        embed = discord.Embed(
            title="**Error**",
            description=f"**API request failed with status code {response.status_code}**",
            color=0xff0000
        )
    
    # Edit the original response with the new Embed
    await interaction.edit_original_response(embed=embed)
    
    # Send an ephemeral follow-up message
    await interaction.followup.send("https://discord.gg/usHF6Gf9db", ephemeral=True)
    
client.run(TOKEN)
