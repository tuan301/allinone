import requests
import datetime
from nextcord.ext import commands
import nextcord

intents = nextcord.Intents.all()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

apikey = "E99l9NOctud3vmu6bPne" # u can change it to ur private api
token = "ur token here" # no need for credit :D

def get_api_link(link):
    replacements = {
        "PlutoniumHub": "https://keyrblx.com/getkey/PlutoniumHub?hwid=",
        "MTrietHub": "https://keyrblx.com/getkey/MTrietHub?hwid=",
        "GatoHub": "https://keyrblx.com/getkey/GatoHub?hwid=",
        "DemonicHub": "https://keyrblx.com/getkey/DemonicHub?hwid=",
        "BuangHub": "https://keyrblx.com/getkey/BuangHub?hwid=",
        "DevHub": "https://keyrblx.com/getkey/DevHub?hwid=",
        "NilHub": "https://keyrblx.com/getkey/NilHub?hwid=",
        "NSHUB": "https://keyrblx.com/getkey/NSHUB?hwid=",
        "ToraScripts": "https://keyrblx.com/getkey/ToraScripts?hwid=",
        "NinjaHub": "https://keyrblx.com/getkey/NinjaHub?hwid=",
        "ZapHub": "https://keyrblx.com/getkey/ZapHub?hwid=",
        "Kidachi": "https://keyrblx.com/getkey/Kidachi?hwid=",
        "SpacexSouly": "https://keyrblx.com/getkey/SpacexSouly?hwid=",
        "K1ng": "https://keyrblx.com/getkey/K1ng?hwid=",
        "project_nexus": "https://keyrblx.com/getkey/project_nexus?hwid=",
        "ZenHub": "https://keyrblx.com/getkey/ZenHub?hwid=",
        "MaxHub": "https://keyrblx.com/getkey/MaxHub?hwid="
    }

    for key, replacement in replacements.items():
        if key in link:
            hwid = link.replace(replacement, "")
            link = hwid
            hubname = key
            return f"https://stickx.top/api-rblx/?hub={hubname}&hwid={link}&api_key={apikey}"
    
    if "evon" in link:
            linkk = link.replace("https://pandadevelopment.net/getkey?service=evon&hwid=", "")
        return f"https://stickx.top/api-evon/?hwid={linkk}&api_key={apikey}"
    elif "vegax" in link:
            linkk = link.replace("https://pandadevelopment.net/getkey?service=vegax&hwid=", "")
        return f"https://stickx.top/api-vegax/?hwid={linkk}&api_key={apikey}"
    else:
        return f"http://optimus.forcehost.net:25637/bypass?link={link}&key={apikey}"

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="TEST"))
    print(f"Login As {bot.user}")

@bot.slash_command(name="bypass")
async def bypass(ctx, link: str):
    if not link.startswith("https://"):
        await ctx.send("Invalid link. Please provide a valid URL.")
        return

    start_time = datetime.datetime.now()
    wait_message = await ctx.send(embed=nextcord.Embed(title="In Process ⏳", description="Try 2 times when it not sending key", color=0xffff00))

    api_link = get_api_link(link)
    try:
        response = requests.get(api_link)
        response.raise_for_status()

        if response.text:
            json_data = response.json()
            result = json_data.get("result")
            key = json_data.get("key")
            status = json_data.get("success")

            embed = None
            if "vegax" in api_link:
                if status == False:
                    embed = nextcord.Embed(title="Error ❌", description="```Invalid Link or Not Support```", color=0xFF0000)
                    embed.add_field(name="Your Link:", value=f"```\n{link}\n```", inline=False)
                else:
                    embed = nextcord.Embed(title="Status:", description=f"**Key:**```{key}```", color=0xA020F0)
            elif "evon" in api_link:
                if status == False:
                    embed = nextcord.Embed(title="Error ❌", description="```Invalid Link or Not Support```", color=0xFF0000)
                    embed.add_field(name="Your Link:", value=f"```\n{link}\n```", inline=False)
                else:
                    embed = nextcord.Embed(title="Status:", description=f"**Key:**```{key}```", color=0xA020F0)
            elif "rblx" in api_link:
                if status == False:
                    embed = nextcord.Embed(title="Error ❌", description="```Invalid Link or Not Support```", color=0xFF0000)
                    embed.add_field(name="Your Link:", value=f"```\n{link}\n```", inline=False)
                else:
                    embed = nextcord.Embed(title="Status:", description=f"**Key:**```{key}```", color=0xA020F0)
            else:
                if status == False:
                    embed = nextcord.Embed(title="Error ❌", description="```Invalid Link or Not Support```", color=0xFF0000)
                    embed.add_field(name="Your Link:", value=f"```\n{link}\n```", inline=False)
                else:
                    embed = nextcord.Embed(title="Status:", description=f"```{result}```", color=0xA020F0)
            if embed is not None:
                embed.add_field(name="Your Link:", value=f"```{link}```", inline=False)
                embed.set_image(url="https://cdn.discordapp.com/attachments/1222148598263971920/1222148967517650985/rainbow-1-1.gif?ex=661529ec&is=6602b4ec&hm=15e7436f0849d4bd9a9027d207681eb886dd8c0990955e335743c7005c227df5&")
                embed.set_footer(text=f"| TEST |")
                embed.timestamp = datetime.datetime.now(datetime.timezone.utc)

    except requests.RequestException as e:
        embed = nextcord.Embed(title="Error ❌", description=f"```api offline```", color=0xFF0000)

    await wait_message.edit(embed=embed)

bot.run(token)
