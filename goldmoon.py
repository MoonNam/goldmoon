import discord
import random
import time


client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!버닝로또"):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description=str(i)+'초'))
            time.sleep(1)
        else:
            Text = ""
            number = [1, 2, 3, 4, 5, 6, 7]
            count = 0
            for i in range(0, 7):
                num = random.randrange(1, 46)
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
            embed.set_thumbnail(url="https://o.remove.bg/uploads/cc1eb37d-e8d3-4550-aab3-ebedc0e06758/2.jpg")
            await message.channel.send(embed=embed)


    if message.content.startswith('!버닝홀짝'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description=str(i)+'초'))
            time.sleep(1)
        else:
            food = "홀 짝"
            foodchoice = food.split(" ")
            foodnumber = random.randint(1, len(foodchoice))
            foodresult = foodchoice[foodnumber - 1]
            print("땡")
            await message.channel.send(embed=discord.Embed(description="홀 짝 결과는 "+foodresult+" 입니다"))

client.run("NjgzNjE2MzU1NDI1MzIxMDEx.XlwROA.JPyd22xsz_6CmIk8zqSusVvb5Vc")