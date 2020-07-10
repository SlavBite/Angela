# Тут работают самые глэчные глэки как мы
# boop for my friend
import discord
import random as r
from discord.ext import commands



bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print("Everything's all ready to go~\n--------------")

#---------------------------------------------------------------------
@bot.command()
async def ping(ctx):
    '''
    Проверка задержки бота
    '''
    latency = bot.latency  
    await ctx.send(latency)

# ЭХО-БОТ
@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент
# ПРОСТО ГИФКА С FBI 
@bot.command(pass_context=True)     
async def FBI(ctx):  
	await ctx.send("https://static.miraheze.org/atrociousyoutuberswiki/c/c2/FBIOPENUP.gif")

		
# РАНДОМАЙЗЕР	
@bot.command(pass_context=True) 	
async def random(ctx,number_1,number_2):  
	number_1 = int(number_1)
	number_2 = int(number_2)
	send = r.randint(number_1,number_2)
	await ctx.send(send) 


# ПРОТОТИП: РАБОТА С АНОМАЛИЙ !!!БЕЗ!!! УЧЁТА СПОСОБА РАБОТЫ И ЕГО УРОВНЯ
@bot.command(pass_context=True)
async def work_ALEPH(ctx):
	image = "\n"
	production = 0
	for i in range(1,34):
		d = r.randint(1,10)
		if d <= 4:
			production += 1
			image += "[+]"
	for i in range(1,33 - production):
		image += "[-]" 
	await ctx.send(str(production) + image)
	
# ПРОТОТИП: РАБОТЫ С АНОМАЛИЯМИ С УЧЁТОМ ВЫБОРА СПОСОБА РАБОТЫ И ЕГО УРОВНЯ
@bot.command(pass_context=True)
async def WORK_ALEPH_ГОЛУБАЯ_ЗВЕЗДА_МУДРОСТЬ_4(ctx):
	image = "\n"
	production = 0
	for i in range(1,34):
		d = r.randint(1,100)
		if d <= 50:
			production += 1
			image += "[+]"
	for i in range(1,33 - production):
		image += "[-]" 
	await ctx.send(str(production) + image)
	
	
	
	
# ВЫВОД АНОМАЛИЙ С ФОТОКАРТОЧКОЙ И ССЫЛКОЙ	
#-----------------------------------------------------

# ПРОСТО АЛЕФНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def ALEPH(ctx):
	anomaly = r.randint(1,7)
	if anomaly == 1:
		anomaly = ("Армия в чёрном" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f4/ArmyBlack.png/revision/latest/scale-to-width-down/310?cb=20180421133214&path-prefix=ru")
	elif anomaly == 2:
		anomaly = ("Безмолный аркестр" + " - 2"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/4f/%D0%91%D0%B5%D0%B7%D0%BC%D0%BE%D0%BB%D0%B2%D0%BD%D1%8B%D0%B9%D0%9E%D1%80%D0%BA%D0%B5%D1%81%D1%82%D1%80%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191201144457&path-prefix=ru")
	elif anomaly == 3:
		anomaly = ("Гора улыбающихся тел" + " - 3"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/d/d1/The_Mountain_of_Smiling_Bodies.png/revision/latest/scale-to-width-down/310?cb=20171028081049&path-prefix=ru")
	elif anomaly == 4:
		anomaly = ("Голубая звезда" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/e/e0/Blue_Star.png/revision/latest/scale-to-width-down/310?cb=20171227104718&path-prefix=ru")
	elif anomaly == 5:
		anomaly = ("Здесь ничего нет" + " - 5"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/41/%D0%97%D0%B4%D0%B5%D1%81%D1%8C%D0%9D%D0%B8%D1%87%D0%B5%D0%B3%D0%BE%D0%9D%D0%B5%D1%82%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180715214754&path-prefix=ru")
	elif anomaly == 6:
		anomaly = ("Зацензурено" + " - 6"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/56/CENSORED.png/revision/latest/scale-to-width-down/310?cb=20171119080133&path-prefix=ru")
	else: # anomaly == 7
		anomaly = ("Тающая любовь" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/1/1b/MeltLove.png/revision/latest/scale-to-width-down/310?cb=20180421133115&path-prefix=ru")
	await ctx.send(anomaly)




# ПРОСТО ВАВНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def WAW(ctx):
	anomaly = r.randint(1,21)
	if anomaly == 1:
		embed=discord.Embed(title="Королева Ненависти", url="https://bit.ly/2ZRJc3n", description='"_Во имя любви и справедливости, на сцену выходит Магическая девочка!_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/c/c1/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9D%D0%B5%D0%BD%D0%B0%D0%B2%D0%B8%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180120154738&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-04", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 3-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 2:
		embed=discord.Embed(title="Большая Птица", url="https://bit.ly/31Uwm71", description='"_Спустя месяц мы пришли к выводу, что не было никакого чудища_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/80/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F%D0%9F%D1%82%D0%B8%D1%86%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103412&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-02-40", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 2-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="5", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 3:
		embed=discord.Embed(title="Яблоко Белоснежки", url="https://bit.ly/3gJhAUD", description='"_В тот день, когда яблоко упало в саду принцессы и короля, сердце ведьмы сгорело от ненависти_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/d/d9/%D0%AF%D0%B1%D0%BB%D0%BE%D0%BA%D0%BE%D0%91%D0%B5%D0%BB%D0%BE%D1%81%D0%BD%D0%B5%D0%B6%D0%BA%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190723114436&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-04-42", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 3-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 4:
		embed=discord.Embed(title="Королева Пчёл", url="https://bit.ly/2CoYJPL", description='"_Если ты почувствовал резкую боль в животе или почёсывание в районе шеи, то всё, что тебе осталось — посмотреть вверх на голубое небо в свой последний раз_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/6a/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9F%D1%87%D1%91%D0%BB%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190716203020&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-04-50", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 5:
		embed=discord.Embed(title="Альриуна", url="https://bit.ly/2ZUCOIv", description='"_С её надеждой обернуться в прах, она вернётся в могилу со всем, что жаждет жизнь_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/a/a9/%D0%90%D0%BB%D1%8C%D1%80%D0%B8%D1%83%D0%BD%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190628232832&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-04-53", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 6:
		embed=discord.Embed(title="Наёмница в Красной Шапочке", url="https://bit.ly/3iH7tS6", description='"_Я повешу его голову над моей кроватью. Только так я смогу поспать без ночных кошмаров_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/89/%D0%9D%D0%B0%D1%91%D0%BC%D0%BD%D0%B8%D1%86%D0%B0%D0%B2%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B9%D0%A8%D0%B0%D0%BF%D0%BE%D1%87%D0%BA%D0%B5%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171213153154&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-57", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 7:
		embed=discord.Embed(title="Большой и, возможно, Злой Волк", url="https://bit.ly/38JcVj1", description='"_На самом деле мне наплевать. Меня должны звать Большим Злым Волком_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/e/ec/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%D0%B8%2C%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%2C%D0%97%D0%BB%D0%BE%D0%B9%D0%92%D0%BE%D0%BB%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103947&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-02-58", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 4-8", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 8:
		embed=discord.Embed(title="Птица Правосудия", url="https://bit.ly/3gKS4hT", description='"_Чаши её весов склоняются в зависимости от тяжести совершённых грехов_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/2/27/%D0%9F%D1%82%D0%B8%D1%86%D0%B0%D0%9F%D1%80%D0%B0%D0%B2%D0%BE%D1%81%D1%83%D0%B4%D0%B8%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20170502161504&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-02-62", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="PALE 5-7", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 9:
		embed=discord.Embed(title="Король Жадности", url="https://bit.ly/2W7QBui", description='"_Печаль скажет, "Исчезни! Умри!" Но желание жаждет вечности. Бессмертия, которого нельзя отринуть!_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/6d/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C%D0%96%D0%B0%D0%B4%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190726225437&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-64", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 5-7", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 10:
		embed=discord.Embed(title="Маленький Принц", url="https://bit.ly/3fhxRA3", description='"_Даже если это моё проклятие, я буду радоваться ему словно благословению_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/3/3c/%D0%9C%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180129231241&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-04-66", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 3-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 11:
		embed=discord.Embed(title="Мечта Чёрного Лебедя", url="https://bit.ly/2Zgj436", description='"_Что происходит, когда чёрный лебедь просыпается ото сна, где он был белым лебедем?_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/2/2d/%D0%9C%D0%B5%D1%87%D1%82%D0%B0%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B3%D0%BE%D0%9B%D0%B5%D0%B1%D0%B5%D0%B4%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191026205114&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-02-70", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 5-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="5", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 12:
		embed=discord.Embed(title="Поток Сновидений", url="https://bit.ly/2Dt6eWE", description='"_Скажи дитя, что сегодня будет конфета со вкусом винограда. Это его любимые_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/0/0a/%D0%9F%D0%BE%D1%82%D0%BE%D0%BA%D0%A1%D0%BD%D0%BE%D0%B2%D0%B8%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171029132834&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-02-71", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 3-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 13:
		embed=discord.Embed(title="Пронзающий Небеса", url="https://bit.ly/2W3Ntzv", description='"_Не отворачивайся, просто продолжай смотреть. Держи его в поле зрения_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/4/43/%D0%9F%D1%80%D0%BE%D0%BD%D0%B7%D0%B0%D1%8E%D1%89%D0%B8%D0%B9%D0%9D%D0%B5%D0%B1%D0%B5%D1%81%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171028082057&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-04-72", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 4-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 14:
		embed=discord.Embed(title="Рыцарь Отчаяния", url="https://bit.ly/2W4etPv", description='"_Всё, что осталось - это пустая гордость упрямого рыцаря_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/6c/%D0%A0%D1%8B%D1%86%D0%B0%D1%80%D1%8C%D0%9E%D1%82%D1%87%D0%B0%D1%8F%D0%BD%D0%B8%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg/revision/latest/scale-to-width-down/310?cb=20171028072448&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-01-73", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 15:
		embed=discord.Embed(title="Обнажённое Гнездо", url="https://bit.ly/3ef0oVz", description='"_Оно может попасть в любое отверстие вашего тела_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/82/%D0%9E%D0%B1%D0%BD%D0%B0%D0%B6%D1%91%D0%BD%D0%BD%D0%BE%D0%B5%D0%93%D0%BD%D0%B5%D0%B7%D0%B4%D0%BE%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171030091134&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-02-74", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 5-7", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 16:
		embed=discord.Embed(title="Различное Преломление Пространства", url="https://bit.ly/3gPLvuF", description='"_Единственное, что можно посоветовать - это обращать внимание на своё окружение_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/3/3d/Dimensional_Refraction_Variant.png/revision/latest/scale-to-width-down/310?cb=20171119075413&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-03-88", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-7", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 17:
		embed=discord.Embed(title="Жар-Птица", url="https://bit.ly/2ZfUOOv", description='"_Тот, кто сможет её поймать, будет награждён её пером, которого жаждали сотни охотников_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/f7/O-02-101.png/revision/latest/scale-to-width-down/310?cb=20180204123400&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-02-101", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 3-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 18:
		embed=discord.Embed(title="Инь", url="https://bit.ly/2DtgqhT", description='"_И вот ты станешь небом, а я - землёй_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/2/24/%D0%9E-05-102.png/revision/latest/scale-to-width-down/310?cb=20180204124541&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-05-102", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 19:
		embed=discord.Embed(title="Луна", url="https://bit.ly/323ONpK", description='"_Предание гласит, что луна очаровала мужчину. Но на самом деле, мужчина был в отчаянии под луной_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/0/0d/La_Luna.png/revision/latest/scale-to-width-down/310?cb=20180421133425&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="D-01-105", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 5-7", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="20", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 20:
		embed=discord.Embed(title="Дерево-Паразит", url="https://bit.ly/329f3PP", description='"_Расслабься, тебе разве не нужно благословение?_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/5/51/ParasTree.png/revision/latest/scale-to-width-down/310?cb=20180421133344&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="D-04-108", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 5-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="24", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 21:
		embed=discord.Embed(title="Героический Монах", url="https://bit.ly/3iNktFY", description='"_Однако, о твоём имени будут слагать легенды спустя поколения, если будет достаточно шариры, которая вобрала твоё мужество_"', color=0x9932cc)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/4/44/Monk.png/revision/latest/scale-to-width-down/310?cb=20180421133501&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="D-01-110", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="WAW", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="22", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	await ctx.send(embed=embed)	


# ПРОСТО ХЕШНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def HE(ctx):
	anomaly = r.randint(1,15)
	if anomaly == 1:
		embed=discord.Embed(title="Счастливый Мишка Тедди", url="https://bit.ly/3iNayAb", description='"_Его воспоминания начинаются с тёплого объятья_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/87/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9%D0%9C%D0%B8%D1%88%D0%BA%D0%B0%D0%A2%D0%B5%D0%B4%D0%B4%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg/revision/latest/scale-to-width-down/310?cb=20191201141140&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-04-06", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="15", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 2:
		embed=discord.Embed(title="Красные Туфли", url="https://bit.ly/3ffB0QV", description='"_Девочка молила в слезах: "Мистер, прошу, отрежьте мне ноги..._"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/9/98/%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B5%D0%A2%D1%83%D1%84%D0%BB%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20200224191838&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-04-08", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="16", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 3:
		embed=discord.Embed(title="Безымянный Зародыш", url="https://bit.ly/3gDUnDk", description='"_Однажды, наверное ты узнаешь. Что означает отчаянье на их лицах во время вращения рулетки_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/b/bd/%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9%D0%97%D0%B0%D1%80%D0%BE%D0%B4%D1%8B%D1%88%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191201142701&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-15", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 4:
		embed=discord.Embed(title="Поющая Машина", url="https://bit.ly/2AKsL02", description='"_Но ничто не сравнится с музыкой, создаваемой ею при пожирании людей_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/2/27/%D0%9F%D0%BE%D1%8E%D1%89%D0%B0%D1%8F%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227104603&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="О-05-30", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 5:
		embed=discord.Embed(title="Добрый Дровосек", url="https://bit.ly/323S8Fi", description='"_Этот лес полон сердец. Неважно, сколько раз он вырубал их, лес, как и раньше, оставался густым_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/a/a1/%D0%94%D0%BE%D0%B1%D1%80%D0%BE%D1%81%D0%B5%D1%80%D0%B4%D0%B5%D1%87%D0%BD%D1%8B%D0%B9%D0%94%D1%80%D0%BE%D0%B2%D0%BE%D1%81%D0%B5%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171119075700&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-05-32", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 3-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 6:
		embed=discord.Embed(title="Снежная Королева", url="https://bit.ly/2ZfgZnR", description='"_Льды тают... связано ли это с наступлением весны или это из-за того, что замок рушится, нам точно неизвестно_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/5/53/%D0%A1%D0%BD%D0%B5%D0%B6%D0%BD%D0%B0%D1%8F%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191201144707&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-37", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 7:
		embed=discord.Embed(title="Маленький Помощник", url="https://bit.ly/38MTwgT", description='"_Кровь покрывает пол, люди бегут в ужасе..._"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/0/06/%D0%9C%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9%D0%9F%D0%BE%D0%BC%D0%BE%D1%89%D0%BD%D0%B8%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190726225813&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-05-41", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 3-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="16", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 8:
		embed=discord.Embed(title="Рудоль-Та", url="https://bit.ly/32fpUYz", description='"_Я дарю свой подарок, наполненный моей бесконечной ненавистью_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/fe/%D0%A0%D1%83%D0%B4%D0%BE%D0%BB%D1%8C-%D0%A2%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190726230212&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-02-49", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 3-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 9:
		embed=discord.Embed(title="Дитя Галактики", url="https://bit.ly/3ekl7qN", description='"_Слёзы дитя падали будто звезды, падающие с небес. Мир погрузился в сон, будто в ловушке восхитительной колыбельной_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/1/1f/%D0%94%D0%B8%D1%82%D1%8F%D0%93%D0%B0%D0%BB%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227104927&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-55", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 2-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="16", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1-5", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 10:
		embed=discord.Embed(title="Летиция", url="https://bit.ly/3ehqTtw", description='"_Вот я и придумала эту замечательную идею!_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/f7/%D0%9B%D0%B5%D1%82%D0%B8%D1%86%D0%B8%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20170924083524&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-67", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="16", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 11:
		embed=discord.Embed(title="Похороны Мертвых Бабочек", url="https://bit.ly/3gDYYFA", description='"_Что происходит, когда человек умер?_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/e/e9/%D0%9F%D0%BE%D1%85%D0%BE%D1%80%D0%BE%D0%BD%D1%8B%D0%9C%D0%B5%D1%80%D1%82%D0%B2%D1%8B%D1%85%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171028072247&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-01-68", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 4-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="16", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 12:
		embed=discord.Embed(title="Вольный Стрелок", url="https://bit.ly/3iNr0R0", description='"_Эта магическая пуля может попасть в любую цель, на которую вы укажете!_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/b/bf/%D0%92%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%D0%A1%D1%82%D1%80%D0%B5%D0%BB%D0%BE%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171028072311&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-69", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 3-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="НЕТ", inline=True)
	elif anomaly == 13:
		embed=discord.Embed(title="Злорадство", url="https://bit.ly/2OfgYtC", description='"_Кажется, что из замочной скважины этой машины на вас постоянно направлен чей-то взгляд_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/7/76/Schadenfreude.png/revision/latest/scale-to-width-down/310?cb=20171030091212&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-05-76", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 3-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 14:
		embed=discord.Embed(title="Пугало, Ищущее Мудрость", url="https://bit.ly/3ehxmEy", description='"_В этом городе ещё остались прекрасные изумрудные дороги, сверкавшие ярче чем что-либо_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/2/2e/ScarecrowSearchingforWisdomPortrait.png/revision/latest/scale-to-width-down/310?cb=20180312180545&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-87", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-6", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	elif anomaly == 15:
		embed=discord.Embed(title="Суккубраз", url="https://bit.ly/2Zd71U3", description='"_Настало время моей голове взорваться. Приятного дня_"', color=0xffff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/85/Porccubus.png/revision/latest/scale-to-width-down/310?cb=20171227103731&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-02-98", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="HE", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 1-5", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="18", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
		embed.add_field(name="СБЕГАЕТ", value="ДА", inline=True)
	await ctx.send(embed=embed)		

	

# ПРОСТО ТЕЧНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def TETH(ctx):
	anomaly = r.randint(1,16)
	if anomaly == 1:
		embed=discord.Embed(title="Сожжённая Девочка", url="https://bit.ly/2Z1990Y", description='"_Я иду за тобой. Ты, кто скоро сгорит дотла как я_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/c/ca/%D0%A1%D0%BE%D0%B6%D0%B6%D1%91%D0%BD%D0%BD%D0%B0%D1%8F%D0%94%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20200224191823&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-02", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	elif anomaly == 2:
		embed=discord.Embed(title="Старая Леди", url="https://bit.ly/2O1FXk6", description='"_Она была очень разговорчива раньше. В конце концов, одиночество осталось её единственным слушателем_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/b/b4/%D0%A1%D1%82%D0%B0%D1%80%D0%B0%D1%8F%D0%9B%D0%B5%D0%B4%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg/revision/latest/scale-to-width-down/310?cb=20191201122057&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-12", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 1-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="4", inline=True)
	elif anomaly == 3:
		embed=discord.Embed(title="Смотрящая на Стену", url="https://bit.ly/3dZNtGZ", description='"_Её невыносимое горе со временем отрастило длинные, скорбные волосы_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/c/c7/%D0%A1%D0%BC%D0%BE%D1%82%D1%80%D1%8F%D1%89%D0%B0%D1%8F%D0%BD%D0%B0%D0%A1%D1%82%D0%B5%D0%BD%D1%83%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191201143751&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-01-18", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	elif anomaly == 4:
		embed=discord.Embed(title="1.76 МГц", url="https://bit.ly/2VQARM0", description='"_Запись того дня, что мы никогда не забудем_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/a/a0/1.76%D0%9C%D0%93%D1%86%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180322111738&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-06-27", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="4", inline=True)
	elif anomaly == 5:
		embed=discord.Embed(title="Паучья Матка", url="https://bit.ly/2NWcZlK", description='"_Ожидаемо, что ни один сотрудник не отважился вызволить обёрнутого в кокон коллегу_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/1/1c/%D0%9F%D0%B0%D1%83%D1%87%D1%8C%D1%8F%D0%9C%D0%B0%D1%82%D0%BA%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190926183756&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-02-43", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 6:
		embed=discord.Embed(title="Красавица и Чудовище", url="https://bit.ly/2Az7Lt3", description='"_Но проклятие продолжает существовать, оно лишь повторяется снова и снова_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/7/76/%D0%9A%D1%80%D0%B0%D1%81%D0%B0%D0%B2%D0%B8%D1%86%D0%B0%D0%B8%D0%A7%D1%83%D0%B4%D0%BE%D0%B2%D0%B8%D1%89%D0%B5%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190726224650&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-02-44", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 7:
		embed=discord.Embed(title="Кровавая Ванна", url="https://bit.ly/2C4HTFT", description='"_В ванной плавает множество рук. Это руки людей, которых я когда-то любил_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/68/%D0%9A%D1%80%D0%BE%D0%B2%D0%B0%D0%B2%D0%B0%D1%8F%D0%92%D0%B0%D0%BD%D0%BD%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190912172500&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-05-51", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 8:
		embed=discord.Embed(title="Брошенный Убийца", url="https://bit.ly/3ixwdMB", description='"_Но что действительно ужасно, так это такие как ты, умирающие в руках таких, как я_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/64/%D0%91%D1%80%D0%BE%D1%88%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%D0%A3%D0%B1%D0%B8%D0%B9%D1%86%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190628233129&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-01-54", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
	elif anomaly == 9:
		embed=discord.Embed(title="Карающая Птица", url="https://bit.ly/3iBu7vi", description='"_Люди совершают прегрешения с давних времён. "Зачем они совершают подобные вещи? Даже зная, что это плохо_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/6e/%D0%9A%D0%B0%D1%80%D0%B0%D1%8E%D1%89%D0%B0%D1%8F%D0%9F%D1%82%D0%B8%D1%87%D0%BA%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190726225559&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-02-56", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="4", inline=True)
	elif anomaly == 10:
		embed=discord.Embed(title="Фрагмент Вселенной", url="https://bit.ly/2ZFN739", description='"_Ты видишь пение перед своими глазами. Оно так великолепно и оно приближается к тебе..._"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/7/7e/%D0%A4%D1%80%D0%B0%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%92%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190730124136&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-03-60", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 1-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	elif anomaly == 11:
		embed=discord.Embed(title="Ветхие Доспехи", url="https://bit.ly/3izgTz8", description='"_Жизнь дана лишь тем, кто не боится смерти_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/3/3f/%D0%92%D0%B5%D1%82%D1%85%D0%B8%D0%B5%D0%94%D0%BE%D1%81%D0%BF%D0%B5%D1%85%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190730123952&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-05-61", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 12:
		embed=discord.Embed(title="Мясной Фонарь", url="https://bit.ly/2O1vKV4", description='"_Это не цветок, прикажи всем сотрудникам немедленно эвакуироваться_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/f9/Meat_Lantern.png/revision/latest/scale-to-width-down/310?cb=20171111170823&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-04-84", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 1-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
	elif anomaly == 13:
		embed=discord.Embed(title="Сегодня Стесняется", url="https://bit.ly/2Z5sbDE", description='"_Какой сегодня хороший день! Всё ещё стесняешься?_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/5/56/Shy_Look_Today.png/revision/latest/scale-to-width-down/310?cb=20171227104825&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-92", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 1-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 14:
		embed=discord.Embed(title="Пустой Сон", url="https://bit.ly/31SInd1", description='"_Прошу, ешь мои сны_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/d/d5/Void_Dream.png/revision/latest/scale-to-width-down/310?cb=20180120162901&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="T-02-99", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 1-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="14", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	elif anomaly == 15:
		embed=discord.Embed(title="Могила Цветущей Сакуры", url="https://bit.ly/3e5fmNC", description='"_Чем больше на ней крови, тем она прекрасней_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/fa/Grave_of_Cherry_Blossoms.png/revision/latest/scale-to-width-down/310?cb=20180120163329&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-04-100", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 2-4", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="3", inline=True)
	elif anomaly == 16:
		embed=discord.Embed(title="Пиподэ", url="https://bit.ly/3farNta", description='"_Сэр, этот ‘ангелочек’ жуёт часть тела вашего коллеги_"', color=0x002366)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/83/Ppodae.png/revision/latest/scale-to-width-down/310?cb=20180421133300&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="D-02-107", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="TETH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 2-3", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="12", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	await ctx.send(embed=embed)


# ПРОСТО ZAYIN АНОМАЛИИ
@bot.command(pass_context=True)
async def ZAYIN(ctx):
	anomaly = r.randint(1,7)
	if anomaly == 1:
		embed=discord.Embed(title="Один Грех и Сотни Благих Деяний", url="https://bit.ly/3irwTD8", description='"_Оно пожирает зло, что возникает во время общения между людьми_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/7/72/%D0%9E%D0%B4%D0%B8%D0%BD%D0%93%D1%80%D0%B5%D1%85%D0%B8%D0%A1%D0%BE%D1%82%D0%BD%D0%B8%D0%91%D0%BB%D0%B0%D0%B3%D0%B8%D1%85%D0%94%D0%B5%D1%8F%D0%BD%D0%B8%D0%B9%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190722195452&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-03-03", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 1-2", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="10", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 2:
		embed=discord.Embed(title="Чумной Доктор", url="https://bit.ly/3grZQgv", description='"_Я вылечу тебя и избавлю от любых болезней и травм, что есть у тебя_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/3/33/%D0%A7%D1%83%D0%BC%D0%BD%D0%BE%D0%B9%D0%94%D0%BE%D0%BA%D1%82%D0%BE%D1%80%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180204130109&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="O-01-45", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 1-2", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="10", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="1", inline=True)
	elif anomaly == 3:
		embed=discord.Embed(title="Не Трогай Меня", url="https://bit.ly/2Z2BKmC", description='"_Ты уже нажимал на неё множество раз и ты до сих пор хочешь знать что-то о ней?_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/e/e4/%D0%9D%D0%B5%D0%A2%D1%80%D0%BE%D0%B3%D0%B0%D0%B9%D0%9C%D0%B5%D0%BD%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180109033054&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="?", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="???", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="???", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 4:
		embed=discord.Embed(title='Открытая Банка "Wellcheers"', url="https://bit.ly/31KNUCs", description='"_Где-то вдалеке, вы слышите галдёж чаек_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/e/e7/%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B0%D1%8F%D0%91%D0%B0%D0%BD%D0%BA%D0%B0%22Wellcheers%22%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20180109051622&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-05-52", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 1-2", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="10", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 5:
		embed=discord.Embed(title="Ты Лысый...", url="https://bit.ly/2VL2yFW", description='"_Вы включили вашу машинку для стрижки волос..._"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/8/88/%D0%A2%D1%8B%D0%9B%D1%8B%D1%81%D1%8B%D0%B9...%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20180805212011&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="Лысина — Это Круто!", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="BLACK 1-2", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="6", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 6:
		embed=discord.Embed(title="Фестиваль фей", url="https://bit.ly/2BweFjr", description='"_Все будет в порядке, пока феи помогают тебе_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/6/6f/Fairy_Festival.png/revision/latest/scale-to-width-down/310?cb=20171111163439&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="F-04-83", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="RED 1-2", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="10", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="✕", inline=True)
	elif anomaly == 7:
		embed=discord.Embed(title="Армия в Чёрном", url="https://bit.ly/2Cafu10", description='"_Цвет человеческого сердца - розовый. Нося одежду такого же цвета мы можем вторгаться в человеческий разум_"', color=0x00ff00)
		embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/lobotomycorp/images/f/f4/ArmyBlack.png/revision/latest/scale-to-width-down/310?cb=20180421133214&path-prefix=ru")
		embed.add_field(name="КОДОВЫЙ НОМЕР", value="D-01-106", inline=True)
		embed.add_field(name="УРОВЕНЬ РИСКА", value="ZAYIN➝ALEPH", inline=True)
		embed.add_field(name="ТИП АТАКИ", value="WHITE 7-9", inline=True)
		embed.add_field(name="ДАЁТ Э-ЯЧЕЕК", value="30", inline=True)
		embed.add_field(name="СЧЁТЧИК КЛИПОТА", value="2", inline=True)
	await ctx.send(embed=embed)


# Test "ОТЧЕТЫ"

bot.run(TOKEN)
	
	
		
