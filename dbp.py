import discord
from discord.ext import commands
from discord.ext.commands import Bot
from time import sleep
import os

#Создаём префикс для команд

prefix = '!'

Bot = commands.Bot(command_prefix= prefix)


@Bot.event
async def on_ready():
	'''Проверка на работу бота'''
	print('Бот Пюрыча работает!')

@Bot.event
async def on_member_join(member: discord.Member):
	'''Выдача роли и приветствие при присоединении нового участника'''
	role = discord.utils.get(member.guild.roles, name='Картошка')
	await member.add_roles(role, reason=None, atomic=True)

	emb = discord.Embed(title= 'Информация и советы о сервере **Армия Пюрыча**', colour= 0xffc400)
	emb.add_field(name= 'Команды', value= 'Если хочешь увидеть, что я могу, то в чате напиши \"!help\"')
	emb.add_field(name= 'Правила', value= 'Лично советую прочитать тебе правила')
	emb.add_field(name= 'Творчество', value= 'В категории \"Творчество\" ты можешь показать всему серверу своё творчество и выслушать критику')
	emb.add_field(name= 'Мастерская', value= 'В категории \"Мастерская\" ты можешь задать вопрос Пюрычу, предложить челендж и иногда помочь с контентом :D')

	await member.send(embed = emb)
	await member.send('**Короче, Картошка, я тебя спас и в благородство играть не буду: дальше разберёшься сам без моих подсказок :D**')

#Информация

@Bot.command(pass_context= True)
async def halp(ctx):
	'''Инфа о командах'''
	emb = discord.Embed(title= 'Всё, что я могу', colour= 0x008cff)
	emb.add_field(name= '{}halp'.format(prefix), value= 'Показывает это окно')
	emb.add_field(name= '{}историябраузера @Ник пользователя'.format(prefix), value= 'Показывает информацию о картофеле')
	emb.add_field(name= '{}гдевидео'.format(prefix), value= 'Ответит, когда оно будет')
	emb.add_field(name= '{}меме'.format(prefix), value= 'Выведет список мемесов')

	await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def историябраузера(ctx, user: discord.Member):
	'''Инфа о пользователе'''
	emb = discord.Embed(title= 'Информация о браузере {}'.format(user.name), colour= 0xff00ae)
	emb.add_field(name= 'Настоящее имя', value= user.name)
	emb.add_field(name= 'ID', value= user.id)
	emb.add_field(name= 'Подключился', value= str(user.joined_at)[:16])
	emb.add_field(name= 'Состояние', value= user.status)
	emb.add_field(name= 'Высшая роль', value= user.top_role)
	if user.nick is not None:
		emb.add_field(name= 'Фальшивка', value= user.nick)
	if user.activity is not None:
		emb.add_field(name= 'Играет в', value= user.activity.name)
	emb.set_thumbnail(url= user.avatar_url)
	emb.set_author(name= Bot.user.name, url= 'https://discordapp.com/oauth2/authorized')

	await ctx.send(embed = emb)


@Bot.command(pass_context= True)
async def меме(ctx):
	'''Инфа о командах'''
	emb = discord.Embed(title= 'Список мемесов', colour= 0xffdd00)
	emb.add_field(name= 'Выбирай'.format(prefix), value= '!F, !пюрешка, !картошка, !чилипиздрик')

	await ctx.send(embed = emb)

#Меме

@Bot.command(pass_context= True)
async def F(ctx):
	await ctx.send('https://media.discordapp.net/attachments/640218889896329216/681051475123634233/F_1.png')

@Bot.command(pass_context= True)
async def пюрешка(ctx):
	await ctx.send('https://media.discordapp.net/attachments/640218889896329216/689882065264574544/1526317516122019637.png')

@Bot.command(pass_context= True)
async def чилипиздрик(ctx):
	await ctx.send('https://media.discordapp.net/attachments/640218889896329216/689883673570312192/chilipizdrik-1.png')

@Bot.command(pass_context= True)
async def картошка(ctx):
	await ctx.send('https://media.discordapp.net/attachments/640218889896329216/689884095995445297/124845.png?width=936&height=702')

@Bot.command(pass_context= True)
async def гдевидео(ctx):
		await ctx.send('Как только - так сразу')

		sleep(2.0)

		await ctx.channel.purge(limit= 1)

#Команды для админов

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def админпомощь(ctx):
	'''Инфа о командах для админов'''

	await ctx.channel.purge(limit= 1)

	emb = discord.Embed(title= 'Информация о командах для высших пюрешек', colour= 0xffffff)
	emb.add_field(name= '{}чисти'.format(prefix), value= 'очищает определённое кол-во сообщений')
	emb.add_field(name= '{}УХАДИ @Ник пользователя причина'.format(prefix), value= 'кикает участника с сервера')
	emb.add_field(name= '{}бан @Ник пользователя причина'.format(prefix), value= 'банит участника')
	emb.add_field(name= '{}разбан @Ник пользователя'.format(prefix), value= 'забирает бан у участника')
	emb.add_field(name= '{}мут @Ник пользователя'.format(prefix), value= 'выдает участнику мут')
	emb.add_field(name= '{}размут @Ник пользователя'.format(prefix), value= 'забирает у участника мут')

	await ctx.author.send(embed = emb)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def чисти(ctx, value):
	'''Очистка определённого кол-ва сообщений'''
	if int(value) <= 0:
		await ctx.send('**Да как я вилкой-то буду чистить?**')
		sleep(1.0)
		await ctx.channel.purge(limit= 2)

	if int(value) > 0:
		await ctx.channel.purge(limit= int(value) + 1)
		await ctx.send('Пюрешка справилась с задачей и очистила при помощи ложки ' + value + ' сообщений, которые мешали людям :D')
		sleep(1.0)
		await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def УХАДИ(ctx, user: discord.Member, *, reason= None):
	'''Кик участника с сервера'''
	await user.kick(reason= reason)
	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def бан(ctx, user: discord.Member, *, reason= None):
	'''Выдача бана участнику'''
	await ctx.channel.purge(limit=1)

	await user.ban(reason= reason)
	await ctx.send(f'Пюрешка забанила {user.mention} по причине ' + reason + '\n https://media.tenor.co/videos/90ce55e5c90f5aa31a7007547f9bd954/mp4')

	sleep(1.0)
	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def разбан(ctx, *, member):
	'''Выдача разбана человеку'''
	await ctx.channel.purge(limit=1)

	banned_users = await ctx.guild.bans()

	for ban_entry in banned_users:
		user = ban_entry.user

		await ctx.guild.unban(user)
		await ctx.send(f'Пюрешка разбанила {user.mention} благодаря высшим пюрешкам')

		await ctx.channel.purge(limit=1)

		return

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def мут(ctx, member: discord.Member):
	'''Выдача человеку мута'''
	await ctx.channel.purge(limit= 1)
	
	mute_role = discord.utils.get(ctx.message.guild.roles, name= 'Мут')
	
	await member.add_roles(mute_role)
	
	await ctx.send(f'Пюрешка выдала мут {member.mention} за нарушение кодекса армии')

	sleep(1.0)

	await ctx.channel.purge(limit= 1)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator= True)
async def размут(ctx, member: discord.Member):
	'''Снятие мута участнику'''
	await ctx.channel.purge(limit= 1)

	mute_role = discord.utils.get(ctx.message.guild.roles, name= 'Мут')

	await member.add_roles(mute_role)

	await member.remove_roles(mute_role)
	await ctx.send(f'Пюрешка убрала {member.mention} мут благодаря высшим пюрешкам')

	sleep(1.0)

	await ctx.channel.purge(limit= 1)

#Запуск

token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
