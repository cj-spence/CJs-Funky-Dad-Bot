import discord
import random
from datetime import datetime   

bad_words = [
        'fuck',
        'shit',
        'bitch',
        'cunt',
        'hell',
        'ass',
        'damn',
        'dick',
        'slut',
        'whore'
]

dad_intro = [
    'hey',
    'hi'
]

dad_funny_face =[
    '彡໒(⊙ᴗ⊙)७彡',
    '(✦ ‿ ✦)',
    '໒(⊙ᴗ⊙)७✎▤',
    '◑____________◑',
    '(^_ －）≡★',
    '-===≡≡≡( ͝° ͜ʖ͡°)',
    '¯\_(⊙_ʖ⊙)_/¯',
    '༼◥▶ل͜◀◤༽',
    'ᕦ⊙෴⊙ᕤ',
    '凸ಠ益ಠ)凸'
]

dad_silly = [
    'waddup',
    'whattup',
    'whats up'
]

dad_replies = [
    'im',
    "i'm"
]

dad_thanks = [
    'thanks',
    'thank'
]

class CJClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')

        words = message.content.lower().split()

        if message.content.split()[0].lower() in bad_words:
            await message.channel.send(f"Watch your languge! {message.author.mention}")

        if message.content == "do a funny face" or message.content == "make a funny face":
            await message.channel.send(f"{random.choice(dad_funny_face)}")

        if words[0] == "shut" and words[1] == "up":
            await message.channel.send(f"Now, {message.author.mention}, I will not tolerate that attitude. I pay the bills here.")

        if message.content.split()[0].lower() in dad_intro:
            await message.channel.send(f"Hey bud!")
        
        if words[0] == "whats" and words[1] == "up":
            await message.channel.send(f"The sky!")

        if message.content.split()[0].lower() in dad_silly:
            await message.channel.send(f"The sky!")
        
        if words[0] == "thank" and words[1] == "you":
             await message.channel.send(f" No problem.")
        elif message.content.split()[0].lower() in dad_thanks:
            await message.channel.send(f" Of course.")
        
        if message.content.split()[0].lower() in dad_replies:
            changed_message = message.content.replace("im", "hi")   
            await message.channel.send(f"Well {changed_message}, I'm Dad!")

intents = discord.Intents.default()
intents.message_content = True

client = CJClient(intents=intents)
client.run('token goes here')