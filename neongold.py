import discord
import random
import time
import os


client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("골드썬")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!골드로또"):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description=str(i) + '초'))
            time.sleep(1)
        else:
            Text = ""
            number = [1, 2, 3, 4, 5, 6]
            count = 0
            for i in range(0, 6):
                num = random.randrange(1, 30)
                number[i] = num
                if count >= 1:
                    for i2 in range(0, i):
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))
                                if number[i] == number[i2]:
                                    numberText = number[i]
                                    print("작동 이전값 : " + str(numberText))
                                    number[i] = random.randrange(1, 46)
                                    numberText = number[i]
                                    print("작동 현재값 : " + str(numberText))

                count = count + 1
                Text = Text + "  " + str(number[i])

            print(Text.strip())
            embed = discord.Embed(
                title="로또 번호는 !",
                description=Text.strip(),
                colour=discord.Color.blurple()
            )
            embed.set_thumbnail(url="https://o.remove.bg/uploads/c9285490-71cc-491c-b1f1-fbf559da7009/2.png")
            await message.channel.send(embed=embed)

    if message.content.startswith('!골드홀짝'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description=str(i) + '초'))
            time.sleep(1)
        else:
            food = "홀 짝"
            foodchoice = food.split(" ")
            foodnumber = random.randint(1, len(foodchoice))
            foodresult = foodchoice[foodnumber - 1]
            print("땡")
            await message.channel.send(embed=discord.Embed(description="홀 짝 결과는 " + foodresult + " 입니다"))

    if message.content.startswith("!골드사다리"):
        team = message.content[7:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(embed=discord.Embed(description=person[i] + " ►►►►► " + teamname[i]))
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
