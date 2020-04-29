import discord
import random as r
from discord.ext import commands


bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg): #создаем асинхронную фунцию бота
    await ctx.send(arg) #отправляем обратно аргумент

@bot.command(pass_context=True)     
async def FBI(ctx):  # создаем асинхронную фунцию бота
	await ctx.send("https://static.miraheze.org/atrociousyoutuberswiki/c/c2/FBIOPENUP.gif")

		
# РАНДОМАЙЗЕР	
@bot.command(pass_context=True) 	
async def random(ctx,number_1,number_2):  # создаем асинхронную фунцию бота
	number_1 = int(number_1)
	number_2 = int(number_2)
	send = r.randint(number_1,number_2)
	await ctx.send(send)  # отправляем обратно аргумент


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


# ПРОСТО АЛЕФНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def ALEPH(ctx):
	anomaly = r.randint(1,7)
	if anomaly == 1:
		anomaly = ("Армия в чёрном" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f4/ArmyBlack.png/revision/latest/scale-to-width-down/310?cb=20180421133214&path-prefix=ru")
	if anomaly == 2:
		anomaly = ("Безмолный аркестр" + " - 2"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/4f/%D0%91%D0%B5%D0%B7%D0%BC%D0%BE%D0%BB%D0%B2%D0%BD%D1%8B%D0%B9%D0%9E%D1%80%D0%BA%D0%B5%D1%81%D1%82%D1%80%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191201144457&path-prefix=ru")
	if anomaly == 3:
		anomaly = ("Гора улыбающихся тел" + " - 3"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/d/d1/The_Mountain_of_Smiling_Bodies.png/revision/latest/scale-to-width-down/310?cb=20171028081049&path-prefix=ru")
	if anomaly == 4:
		anomaly = ("Голубая звезда" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/e/e0/Blue_Star.png/revision/latest/scale-to-width-down/310?cb=20171227104718&path-prefix=ru")
	if anomaly == 5:
		anomaly = ("Здесь ничего нет" + " - 5"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/41/%D0%97%D0%B4%D0%B5%D1%81%D1%8C%D0%9D%D0%B8%D1%87%D0%B5%D0%B3%D0%BE%D0%9D%D0%B5%D1%82%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180715214754&path-prefix=ru")
	if anomaly == 6:
		anomaly = ("Зацензурено" + " - 6"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/56/CENSORED.png/revision/latest/scale-to-width-down/310?cb=20171119080133&path-prefix=ru")
	if anomaly == 7:
		anomaly = ("Тающая любовь" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/1/1b/MeltLove.png/revision/latest/scale-to-width-down/310?cb=20180421133115&path-prefix=ru")
	await ctx.send(anomaly)




# ПРОСТО ВАВНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def WAW(ctx):
	anomaly = r.randint(1,13)
	if anomaly == 1:
		anomaly = ("Альруина" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/a/a9/%D0%90%D0%BB%D1%8C%D1%80%D0%B8%D1%83%D0%BD%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190628232832&path-prefix=ru")
	if anomaly == 2:
		anomaly = ("Большая птица" + " - 2"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/8/80/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F%D0%9F%D1%82%D0%B8%D1%86%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103412&path-prefix=ru")
	if anomaly == 3:
		anomaly = ("Большой и, возможно, Злой Волк" + " - 3"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/e/ec/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%D0%B8%2C%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%2C%D0%97%D0%BB%D0%BE%D0%B9%D0%92%D0%BE%D0%BB%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103947&path-prefix=ru")
	if anomaly == 4:
		anomaly = ("Героический Монах" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/44/Monk.png/revision/latest/scale-to-width-down/310?cb=20180421133501&path-prefix=ru")
	if anomaly == 5:
		anomaly = ("Дерево-Паразит" + " - 5"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/51/ParasTree.png/revision/latest/scale-to-width-down/310?cb=20180421133344&path-prefix=ru")
	if anomaly == 6:
		anomaly = ("Жар-Птица" + " - 6"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f7/O-02-101.png/revision/latest/scale-to-width-down/310?cb=20180204123400&path-prefix=ru")
	if anomaly == 7:
		anomaly = ("Инь" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/2/24/%D0%9E-05-102.png/revision/latest/scale-to-width-down/310?cb=20180204124541&path-prefix=ru")
	if anomaly == 8:
		anomaly = ("Королева ненависти" + " - 8"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/c/c1/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9D%D0%B5%D0%BD%D0%B0%D0%B2%D0%B8%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180120154738&path-prefix=ru")
	if anomaly == 9:
		anomaly = ("Королева пчел" + " - 9"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/6a/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9F%D1%87%D1%91%D0%BB%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190716203020&path-prefix=ru")
	if anomaly == 10:
		anomaly = ("Король жадности" + " - 10"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/6d/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C%D0%96%D0%B0%D0%B4%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190726225437&path-prefix=ru")
	if anomaly == 11:
		anomaly = ("Луна" + " - 11"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/0/0d/La_Luna.png/revision/latest/scale-to-width-down/310?cb=20180421133425&path-prefix=ru")
	if anomaly == 12:
		anomaly = ("Маленький принц" + " - 12"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/3/3c/%D0%9C%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180129231241&path-prefix=ru")
	if anomaly == 13:
		anomaly = ("Мечта черного лебедя" + " - 13"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/2/2d/%D0%9C%D0%B5%D1%87%D1%82%D0%B0%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B3%D0%BE%D0%9B%D0%B5%D0%B1%D0%B5%D0%B4%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191026205114&path-prefix=ru")
	await ctx.send(anomaly)		

	


bot.run(TOKEN)
