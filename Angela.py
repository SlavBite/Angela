# Тут работают самые глэчные глэки как мы
# boop for my friend
import discord
import random as r
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    print("Everything's all ready to go~\n--------------")

#---------------------------------------------------------------------


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
		anomaly = ("Альруина" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/a/a9/%D0%90%D0%BB%D1%8C%D1%80%D0%B8%D1%83%D0%BD%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20190628232832&path-prefix=ru")
	elif anomaly == 2:
		anomaly = ("Большая птица" + " - 2"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/8/80/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F%D0%9F%D1%82%D0%B8%D1%86%D0%B0%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103412&path-prefix=ru")
	elif anomaly == 3:
		anomaly = ("Большой и, возможно, Злой Волк" + " - 3"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/e/ec/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%D0%B8%2C%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%2C%D0%97%D0%BB%D0%BE%D0%B9%D0%92%D0%BE%D0%BB%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20171227103947&path-prefix=ru")
	elif anomaly == 4:
		anomaly = ("Героический Монах" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/4/44/Monk.png/revision/latest/scale-to-width-down/310?cb=20180421133501&path-prefix=ru")
	elif anomaly == 5:
		anomaly = ("Дерево-Паразит" + " - 5"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/51/ParasTree.png/revision/latest/scale-to-width-down/310?cb=20180421133344&path-prefix=ru")
	elif anomaly == 6:
		anomaly = ("Жар-Птица" + " - 6"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f7/O-02-101.png/revision/latest/scale-to-width-down/310?cb=20180204123400&path-prefix=ru")
	elif anomaly == 7:
		anomaly = ("Инь" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/2/24/%D0%9E-05-102.png/revision/latest/scale-to-width-down/310?cb=20180204124541&path-prefix=ru")
	elif anomaly == 8:
		anomaly = ("Королева ненависти" + " - 8"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/c/c1/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9D%D0%B5%D0%BD%D0%B0%D0%B2%D0%B8%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180120154738&path-prefix=ru")
	elif anomaly == 9:
		anomaly = ("Королева пчел" + " - 9"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/6a/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D0%B0%D0%9F%D1%87%D1%91%D0%BB%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190716203020&path-prefix=ru")
	elif anomaly == 10:
		anomaly = ("Король жадности" + " - 10"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/6d/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C%D0%96%D0%B0%D0%B4%D0%BD%D0%BE%D1%81%D1%82%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20190726225437&path-prefix=ru")
	elif anomaly == 11:
		anomaly = ("Луна" + " - 11"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/0/0d/La_Luna.png/revision/latest/scale-to-width-down/310?cb=20180421133425&path-prefix=ru")
	elif anomaly == 12:
		anomaly = ("Маленький принц" + " - 12"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/3/3c/%D0%9C%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B8%D0%B9%D0%9F%D1%80%D0%B8%D0%BD%D1%86%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20180129231241&path-prefix=ru")
	elif anomaly == 13:
		anomaly = ("Мечта черного лебедя" + " - 13"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/2/2d/%D0%9C%D0%B5%D1%87%D1%82%D0%B0%D0%A7%D1%91%D1%80%D0%BD%D0%BE%D0%B3%D0%BE%D0%9B%D0%B5%D0%B1%D0%B5%D0%B4%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/310?cb=20191026205114&path-prefix=ru")
	elif anomaly == 14:
		anomaly = ("Наёмница в красной шапочке" + " - 14"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/8/89/НаёмницавКраснойШапочкеПортрет.png/revision/latest/scale-to-width-down/310?cb=20171213153154&path-prefix=ru")
	elif anomaly == 15:
		anomaly = ("Обнажённое гнездо" + " - 15"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/50/The_Naked_Nest.png/revision/latest/scale-to-width-down/310?cb=20171030091134&path-prefix=ru")
	elif anomaly == 16:
		anomaly = ("Поток сновидений" + " - 16"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/1/12/The_Dreaming_Current.png/revision/latest/scale-to-width-down/310?cb=20171029132834&path-prefix=ru")
	elif anomaly == 17:
		anomaly = ("Пронзающий небеса" + " - 17"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/1/1f/The_Burrowing_Heaven.png/revision/latest/scale-to-width-down/310?cb=20171028082057&path-prefix=ru")
	elif anomaly == 18:
		anomaly = ("Птица правосудия" + " - 18"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/2/27/ПтицаПравосудияПортрет.png/revision/latest?cb=20170502161504&path-prefix=ru")
	elif anomaly == 19:
		anomaly = ("Различное преломление пространства" + " - 19"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/3/3d/Dimensional_Refraction_Variant.png/revision/latest/scale-to-width-down/310?cb=20171119075413&path-prefix=ru")
	elif anomaly == 20:
		anomaly = ("Рыцарь отчаяния" + " - 20"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f0/The_Knight_of_Despair.jpg/revision/latest/scale-to-width-down/310?cb=20171028072448&path-prefix=ru")
	else: # anomaly == 21
		anomaly = ("Яблоко белоснежки" + " - 21"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/d/d9/ЯблокоБелоснежкиПортрет.png/revision/latest/scale-to-width-down/310?cb=20190723114436&path-prefix=ru")
	await ctx.send(anomaly)	


# ПРОСТО ХЕШНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def HE(ctx):
	anomaly = r.randint(1,15)
	if anomaly == 1:
		anomaly = ("Безымянный Зародыш" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/b/bd/%D0%91%D0%B5%D0%B7%D1%8B%D0%BC%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9%D0%97%D0%B0%D1%80%D0%BE%D0%B4%D1%8B%D1%88%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20191201142701&path-prefix=ru")
	elif anomaly == 2:
		anomaly = ("Вольный Стрелок" + " - 2"
			"\nhttps://avatars.mds.yandex.net/get-pdb/2846057/04441d0a-515b-40b3-b1e5-899e682f381e/s1200")
	elif anomaly == 3:
		anomaly = ("Дитя Галактики" + " - 3"
			"\nhttps://pbs.twimg.com/ext_tw_video_thumb/1125324428588437504/pu/img/Q_L_CaQS8lFJKSAI.jpg")
	elif anomaly == 4:
		anomaly = ("Добрый Дровосек" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/a/a1/%D0%94%D0%BE%D0%B1%D1%80%D0%BE%D1%81%D0%B5%D1%80%D0%B4%D0%B5%D1%87%D0%BD%D1%8B%D0%B9%D0%94%D1%80%D0%BE%D0%B2%D0%BE%D1%81%D0%B5%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20171119075700&path-prefix=ru")
	elif anomaly == 5:
		anomaly = ("Злорадство" + " - 5"
			"\nhttps://4.bp.blogspot.com/-HKC6qZg4tr4/WgCLiqvonBI/AAAAAAAAS1A/g0BXJgGpHL8VetWoA2BDPbeqKDcxffCigCLcBGAs/s1600/schaden.png")
	elif anomaly == 6:
		anomaly = ("Красные Туфли" + " - 6"
			"\hhttps://i.pinimg.com/736x/db/1e/e2/db1ee20ac059b10e59bcb19ce7c57cef.jpg")
	elif anomaly == 7:
		anomaly = ("Летиция" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f7/%D0%9B%D0%B5%D1%82%D0%B8%D1%86%D0%B8%D1%8F%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest?cb=20170924083524&path-prefix=ru")
	elif anomaly == 8:
		anomaly = ("Маленький Помощник" + " - 8"
			"\nhttps://i.ytimg.com/vi/8DouN5PBWHg/hqdefault.jpg")
	elif anomaly == 9:
		anomaly = ("Похороны Мертвых Бабочек" + " - 9"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/e/e9/%D0%9F%D0%BE%D1%85%D0%BE%D1%80%D0%BE%D0%BD%D1%8B%D0%9C%D0%B5%D1%80%D1%82%D0%B2%D1%8B%D1%85%D0%91%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%BA%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.png/revision/latest/scale-to-width-down/55?cb=20171028072247&path-prefix=ru")
	elif anomaly == 10:
		anomaly = ("Поющая Машина" + " - 10"
			"\nhttps://www.infjs.com/proxy.php?image=https%3A%2F%2Fsteamuserimages-a.akamaihd.net%2Fugc%2F904528334371742102%2F05F17F5F91520219B908912DE4CFED3409CCD70B%2F&hash=670aa8713d3bd99e464648d0d1a5f37f")
	elif anomaly == 11:
		anomaly = ("Пугало, Ищущее Мудрость" + " - 11"
			"\nhttps://im0-tub-ru.yandex.net/i?id=3d23184f1c7e3d2c1ee4880706e27913&n=13")
	elif anomaly == 12:
		anomaly = ("Рудоль-Та" + " - 12"
			"\nhttps://im0-tub-ru.yandex.net/i?id=d4046f35848bc138bfeea730091490c0&n=13")
	elif anomaly == 13:
		anomaly = ("Снежная Королева" + " - 13"
			"\nhttps://pbs.twimg.com/media/D593No3WsAAJwcV.jpg")
	elif anomaly == 14:
		anomaly = ("Суккубраз" + " - 14"
			"\nhttps://memestatic.fjcdn.com/pictures/Humanized_cec400_6711788.jpg")
	else: # anomaly == 15
		anomaly = ("Счастливый Мишка Тедди" + " - 15"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/8/87/%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B%D0%B9%D0%9C%D0%B8%D1%88%D0%BA%D0%B0%D0%A2%D0%B5%D0%B4%D0%B4%D0%B8%D0%9F%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg/revision/latest?cb=20191201141140&path-prefix=ru")
	await ctx.send(anomaly)		

	

# ПРОСТО ТЕЧНЫЕ АНОМАЛИИ
@bot.command(pass_context=True)
async def TETH(ctx):
	anomaly = r.randint(1,15)
	if anomaly == 1:
		anomaly = ("1.76 МГц" + " - 1"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/a/a0/1.76МГцПортрет.png/revision/latest/scale-to-width-down/310?cb=20180322111738&path-prefix=ru")
	elif anomaly == 2:
		anomaly = ("Брошенный убийца" + " - 2"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/64/БрошенныйУбийцаПортрет.png/revision/latest?cb=20190628233129&path-prefix=ru")
	elif anomaly == 3:
		anomaly = ("Ветхие доспехи" + " - 3"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/3/3f/ВетхиеДоспехиПортрет.png/revision/latest?cb=20190730123952&path-prefix=ru")
	elif anomaly == 4:
		anomaly = ("Карающая птица" + " - 4"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/6e/КарающаяПтичкаПортрет.png/revision/latest?cb=20190726225559&path-prefix=ru")
	elif anomaly == 5:
		anomaly = ("Красавица и чудовище" + " - 5"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/7/76/КрасавицаиЧудовищеПортрет.png/revision/latest/scale-to-width-down/310?cb=20190726224650&path-prefix=ru")
	elif anomaly == 6:
		anomaly = ("Кровавая ванна" + " - 6"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/6/68/КроваваяВаннаПортрет.png/revision/latest?cb=20190912172500&path-prefix=ru")
	elif anomaly == 7:
		anomaly = ("Могила цветущей сакуры" + " - 7"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/fa/Grave_of_Cherry_Blossoms.png/revision/latest/scale-to-width-down/310?cb=20180120163329&path-prefix=ru")
	elif anomaly == 8:
		anomaly = ("Мясной фонарь" + " - 8"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/f/f9/Meat_Lantern.png/revision/latest/scale-to-width-down/310?cb=20171111170823&path-prefix=ru")
	elif anomaly == 9:
		anomaly = ("Паучья матка" + " - 9"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/1/1c/ПаучьяМаткаПортрет.png/revision/latest/scale-to-width-down/310?cb=20190926183756&path-prefix=ru")
	elif anomaly == 10:
		anomaly = ("Пустой сон" + " - 10"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/d/d5/Void_Dream.png/revision/latest/scale-to-width-down/310?cb=20180120162901&path-prefix=ru")
	elif anomaly == 11:
		anomaly = ("Сегодня стесняется" + " - 11"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/5/56/Shy_Look_Today.png/revision/latest/scale-to-width-down/310?cb=20171227104825&path-prefix=ru")
	elif anomaly == 12:
		anomaly = ("Смотрящая на стену" + " - 12"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/c/c7/СмотрящаянаСтенуПортрет.png/revision/latest/scale-to-width-down/310?cb=20191201143751&path-prefix=ru")
	elif anomaly == 13:
		anomaly = ("Сожжённая девочка" + " - 13"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/c/ca/СожжённаяДевочкаПортрет.png/revision/latest?cb=20200224191823&path-prefix=ru")
	elif anomaly == 14:
		anomaly = ("Старая леди" + " - 14"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/b/b4/СтараяЛедиПортрет.jpg/revision/latest/scale-to-width-down/310?cb=20191201122057&path-prefix=ru")
	else: # anomaly == 15
		anomaly = ("Фрагмент вселенной" + " - 15"
			"\nhttps://vignette.wikia.nocookie.net/lobotomycorp/images/7/7e/ФрагментВселеннойПортрет.png/revision/latest?cb=20190730124136&path-prefix=ru")
	await ctx.send(anomaly)





bot.run(TOKEN)
