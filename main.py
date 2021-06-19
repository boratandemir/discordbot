import discord
from discord.ext import commands
from utils import *
from functions import *
from API import *
from help import help as h

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

Bot = commands.Bot("!bot ", intents=intents,help_command=None)

game = Game()


@Bot.event
async def on_ready():
    print("hazirim!")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} aramiza katildi! (yardim icin !bot yardim yaz)")
    print(f"{member} aramiza katildi! (yardim icin !bot yardim yaz)")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="aramizdan-ayrildi")
    await channel.send(f"{member} aramizdan ayrildi!!")
    print(f"{member} aramizdan ayrildi!!")


@Bot.command()
async def roll(ctx):
    roll = game.roll_dice()
    if (roll == 1) or (roll == 6):
        await ctx.send(f"Boom {roll}")
    else:
        await ctx.send(roll)



@Bot.command()
async def clear(ctx, *args, amount=5):
    if "all" in args:
        amount = 9999
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.channel.purge(limit=amount)


@Bot.command(aliases=["create", "oluştur"])
async def create_channel(ctx, argument):
    await ctx.guild.create_text_channel(argument)


@Bot.command(aliases=["delete", "sil"])
async def delete_channel(ctx):
    await ctx.channel.delete()


@Bot.command()
async def pokemon(ctx,pok):
    await ctx.send(reqSumDate(pok))

@Bot.command(aliases=["yardim","yardım"])
async def help(ctx):
    await ctx.send(h())


Bot.run(Token)
