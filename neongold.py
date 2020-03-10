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
            food = "짝 "
            foodchoice = food.split(" ")
            foodnumber = random.randint(1, len(foodchoice))
            foodresult = foodchoice[foodnumber - 1]
            print("땡")
            await message.channel.send(embed=discord.Embed(description="홀 짝 결과는 " + "[" + foodresult + "]" + " 입니다"))

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

    if message.content.startswith('!골드제비'):
        channel = message.channel
        embed = discord.Embed(
            title='골드썬 제비뽑기',
            description='순서대로 번호를 지정합니다.',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='종료')


        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip()) #입력한 명령어

        number = int(Text)

        List = []
        num = random.randrange(0, number)
        for i in range(number):
            while num in List:  # 중복일때만
                num = random.randrange(0, number)  # 다시 랜덤수 생성

            List.append(num)  # 중복 아닐때만 리스트에 추가
            embed.add_field(name=str(i) + '번째', value=str(num), inline=True)

        print(List)
        await message.channel.send(embed=embed)
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
