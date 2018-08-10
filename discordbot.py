#http://discordpy.readthedocs.io/en/latest/api.html
#<discord.member.Member object at 0x0000029EA02B06A8> - member id of bot (i think?) -Suubwey

import discord
from discord.ext import commands
import random
import pyjokes
import aiohttp

bot = commands.Bot(command_prefix='?')

jokes = ["What did the green grape say to the purple grape?\nBREATHE STUPID!",
		"What happens to a frog's car when it breaks down?\nIt gets toad away.",
		"Why isn't the turkey hungry at Thanks giving?\nBecause it's stuffed.",
		"Why do witches wear name tags?\nSo they know which witch is which.",
		"My friend thinks he is so smart, told me today that onion is the only food that makes you cry\nSo I threw a coconut at his face.",
		"What stays in one corner but travels around the world?\nA stamp.",
		"What do you call a pig that does karate?\nPork chop.",
		"Why does Humpty Dumpty love autumn?\nBecause he had a great fall last year.",
		"Did you hear about the kidnapping at school today?\nIt's alright, he's awake now.",
		"Have you heard about the new restaurant Karma?\nThere's no menu, you get what you deserve.", 'Guess the number of programmers it takes to change a light bulb? Zero its a hardware problem','There are only 10 kinds of people in this world: those who know binary and those who don’t.','Real programmers count from 0.', 'Why did the programmer quit his job? Because he didnt get arrays.', 'A foo walks into a bar takes a look around and says Hello World','0 is false 1 is true right? 1','Things arent always #000000 and #FFFFFF.','What is the most used language in programming? Profanity','!False its funny because its True','You had me at Hello World','2b||!2b','Yesterday I changed the name on my wifi to Hack if you can. Today I found it named Challenge Accepted','A programmer is a person who fixed a problem that you didnt know you had in a way you dont understand','How can you tell if a computer geek is an extrovert? They stare at your shoes when you talk instead of their own.','I would love to change the world but they wont give me the source code.','If at first you dont succedd call it version 1.0','Computers make very fast very accurate mistakes','I farted in the Apple store and everyone got mad at me. Not my fault they dont have Windows.','Knock Knock... Whos there? Art... Art Who? R2D2','Hilarious and amazingly true thing: if a pizza has a radius (z) and a depth (a) that pizzas volume can be defined Pi*z*z*a.']
roasts = [" Go suck a fat dick.",
		" Even Darcy wouldn't tap your fat ass",
		" What are you fucking gay?",
        " You look like a sex doll for Ali-A",
        " You're so contaminated even Ligma Won't affect you\n\n\n\nLigma balls bitch. :joy::joy::joy:",
		" Prithy transport thyself to tarnation, bitch",
		" The only reason you're not dead yet is that disease is afraid to go near you, you sick fuck",
		" Why did the chicken cross the road? To get the fuck away from you, chicken-raping assfucker."]
hansonRoast = " Valve's matchmaking must be broken when the equivalent of a monkey messing with a computer can get gold nova three. Hanson's height is just a Pinocchio representation of his giant and fragile ego. Go fuck yourself because nobody else will."
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if "Ana's bot#4932" not in str(message.author):
        #print(message.author)
        #makes sure that it only corrects the word oof and not the custom emoji -Suubwey
        changed = 0
        if 'adn' in message.content or 'oof' in message.content or 'ecksdee' in message.content:
            newMessage = message.content
            if 'adn' in message.content:
                changed = 1
                newMessage = newMessage.replace("adn", "and")
            if 'oof' in message.content and not ':oof:' in message.content:
                changed = 1
                for emoji in bot.get_all_emojis():
                    if("oof" in str(emoji.name)):
                        newMessage = newMessage.replace("oof",str(emoji))

            if 'ecksdee' in message.content and not ':ecksdee:' in message.content:
                changed = 1
                for emoji in bot.get_all_emojis():
                    if("ecksdee" in str(emoji.name)):
                        newMessage = newMessage.replace("ecksdee",str(emoji))
            if changed:
                if(message.author.nick != None):
                    await bot.send_message(message.channel, message.author.nick + ': ' + newMessage)
                else:
                    await bot.send_message(message.channel, message.author + ': ' + newMessage)
                await bot.delete_message(message)

    if message.content.startswith('?hello'):
        embed = discord.Embed(title="Tile", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await bot.send_message(message.channel, embed=embed)
    else:
        await bot.process_commands(message)

"""@bot.event
async def on_command_error(ctx, error):
    if(isinstance(error, commands.CommandNotFound)):
        await bot.send_message(error.message.channel, "Command \"{0}\" is not found.".format(error.invoked_with))
    else:
        if(error.command is None):
            await bot.send_message(error.message.channel, "Command \"{0}\" is not found.".format(error.invoked_with))
        else:
            await bot.send_message(error.message.channel, 'Ignoring exception in command {}'.format(error.command))"""

@bot.event
async def on_member_update(before, after):
    if(before.status != after.status):
        for channel in after.server.channels:
            if channel.name == 'status-notifications':
                #await bot.send_message(channel, 'user update')
                if(after.nick != "Snackbar"):
                    if(after.nick != None):
                        await bot.send_message(channel, "{0.nick} is now {0.status}".format(after))
                    else:
                        await bot.send_message(channel, "{0} is now {0.status}".format(after))

@bot.command()
async def roll(dice):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    while number > 100:
        mgs = []
        async for x in bot.logs_from(ctx.message.channel, limit = 100):
            mgs.append(x)
        await bot.delete_messages(mgs)
        number -= 100
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
async def rolecolour(ctx, hexcode : str):
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        hex_int = int(hexcode, 16)
        newColour = discord.Colour(hex_int)
        """print(ctx.message.server)
        print(ctx.message.author.roles[1])
        print(str(hex_int))
        print(str(newColour))"""
        await bot.edit_role(ctx.message.server, ctx.message.author.roles[1], colour = newColour)

@bot.command(pass_context=True)
async def bully(ctx, member : discord.Member):
    if ctx.message.author.server_permissions.manage_server:
        if "HDMasterReborn#5766" in str(member):
            await bot.say("{0}{1}".format(member.mention, hansonRoast))
        else:
            await bot.say("{0}{1}".format(member.mention, random.choice(roasts)))
        

@bot.command(pass_context=True)
async def channelinfo(ctx, channel : discord.Channel = None):
    """Gives you some channel information."""
    if channel == None:
        channel = ctx.message.channel
    passed = (ctx.message.timestamp - channel.created_at).days
    try:
        channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))
        em = discord.Embed(description="{}, here you go:".format(ctx.message.author.mention), title="Channel Info", color=0X008CFF)
        em.add_field(name="Channel Name", value=str(channel.name))
        em.add_field(name="Channel ID", value=str(channel.id))
        em.add_field(name="Channel Default", value=str(channel.is_default))
        em.add_field(name="Channel Position", value=str(channel.position + 1))
        em.add_field(name="Channel Topic", value=(channel.topic))
        em.set_footer(text=channel_created_at)
        await bot.say(embed=em)
    except discord.HTTPException:
        channel_created_at = ("Created on {} ({} days ago!)".format(channel.created_at.strftime("%d %b %Y %H:%M"), passed))            
        em = discord.Embed(description="{}, here you go:".format(ctx.message.author.mention), title="Channel Info", color=0X008CFF)
        em.add_field(name="Channel Name", value=str(channel.name))
        em.add_field(name="Channel ID", value=str(channel.id))
        em.add_field(name="Channel Default", value=str(channel.is_default))
        em.add_field(name="Channel Position", value=str(channel.position + 1))
        em.add_field(name="Channel Topic", value="None")
        em.set_footer(text=channel_created_at)
        await bot.say(embed=em) 

@bot.command(pass_context = True, description='For when you wanna settle the score some other way')
async def choose(ctx, *choices):
    """Chooses between multiple choices."""
    message = "?choose apple android"
    message2 = "?choose android apple"
    if choices[0] is None or choices[1] is None:
        await bot.say("Plesase provide 2 or more choices")
    else:
        if message not in ctx.message.content and message2 not in ctx.message.content:
            await bot.say(random.choice(choices))
        else:
            await bot.say("OF COURSE ANDROID, APPLE WANTS TO TAKE YOUR MONEY LIKE YOU\'RE SOME HOMELESS GUY")
    

@bot.command(pass_context=True)
async def pin(ctx):
    """Pins this message"""
    await bot.pin_message(ctx.message)

@bot.command(pass_context=True)
async def someone(ctx):
    memberlist = []
    for member in ctx.message.server.members:
        memberlist.append(member)
    chosenMember = random.choice(memberlist)
    while "Ana's bot#4932" in str(chosenMember):
        chosenMember = random.choice(memberlist)
        print("rechosen", chosenMember)
    await bot.say("{0}, YOU HAVE BEEN CHOSEN!" .format(chosenMember.mention))

@bot.command(pass_context=True)
async def shame(ctx, member : discord.User, *, reason = None):
    """Changes a user's nickname and removes some permissions"""
    if ctx.message.author.server_permissions.manage_server:
        await bot.change_nickname(member, reason)
        role = discord.utils.get(member.server.roles, name="SHAMED")
        await bot.replace_roles(member, role)
        usrmessage = await bot.say("{0} IS BEING SHAMED".format(member.mention))
        await bot.pin_message(usrmessage)
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command(pass_context=True)
async def praise(ctx, member : discord.User):
    """Gives a user extra permissions"""
    if ctx.message.author.server_permissions.manage_server:
        role = discord.utils.get(member.server.roles, name="PRAISED")
        await bot.replace_roles(member, role)
        usrmessage = await bot.say("{0} IS BEING PRAISED.\nYOU CAN NOW USE ALL BOT COMMANDS EXCEPT ?stop AND HAVE NEW SERVER PERMISSIONS.".format(member.mention))
        await bot.pin_message(usrmessage)
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command(pass_context=True)
async def unshame(ctx, member : discord.User, *, reason = None):
    """Reverses ?shame"""
    if ctx.message.author.server_permissions.manage_server:
        await bot.change_nickname(member, reason)
        role = discord.utils.get(member.server.roles, name="regulars")
        await bot.replace_roles(member, role)
        usrmessage = await bot.say("{0} IS NO LONGER BEING SHAMED".format(member.mention))
        await bot.pin_message(usrmessage)
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command(pass_context=True)
async def unpraise(ctx, member : discord.User):
    """Reverses ?praise"""
    if ctx.message.author.server_permissions.manage_server:
        role = discord.utils.get(member.server.roles, name="regulars")
        await bot.replace_roles(member, role)
        usrmessage = await bot.say("{0} IS NO LONGER BEING PRAISED".format(member.mention))
        await bot.pin_message(usrmessage)
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command(pass_context=True)
async def repeat(ctx, times, *, content):
    """Repeats a message multiple times."""
    if ctx.message.author.server_permissions.manage_server:
        for y in range(int(times)):
            await bot.say(content)
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command(pass_context=True)
async def nick(ctx, member : discord.Member, *, nickname = None):
    """Changes someone's nickname"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        if(nickname is None):
            await bot.change_nickname(member, None)
        else:
            await bot.change_nickname(member, nickname)
    

@bot.command(pass_context=True)
async def stop(ctx):
    """Stops the bot"""
    if ctx.message.author.server_permissions.manage_server:
        await bot.logout()
    else:
        await bot.say("You don't have permission to use this command.")

@bot.command()
async def joke():
    """Random joke"""
    num = random.randint(0, 2)
    if num:
        await bot.say(pyjokes.get_joke())
    else:
        await bot.say(jokes[random.randint(0, len(jokes))])

@bot.command(pass_context=True)
async def members(ctx):
    """Randomly lists all members"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        memberlist = []
        for member in ctx.message.server.members:
            memberlist.append(member)
        random.shuffle(memberlist)
        #print(memberlist)
        for item in memberlist:
            await bot.say(item)

@bot.command(pass_context=True)
async def setgame(ctx, *, game = None):
    """Changes the bot's 'playing' status"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        if game != None:
            game = game.strip()
        if game != "":
            try:
                await bot.change_presence(game=discord.Game(name=game))
            except:
                await bot.say("Failed to change game")
            else:
                await bot.say("Successfully changed game to {}".format(game))
        else:
            await bot.send_cmd_help(ctx)

@bot.command(pass_context=True)
async def setavatar(ctx, url):
    """Changes the bot's avatar"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()
        await bot.edit_profile(avatar=data)
        await bot.say("I changed my icon")

#Reaction Poll with 2 options
@bot.command(pass_context=True)
async def poll(ctx):
    """Creates a 2 reaction poll from the message"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        if ctx.message.author.bot:
            print('bot tried to send message and was denied')
        else:
            await bot.add_reaction(ctx.message, '👍')
            await bot.add_reaction(ctx.message, '👎')

@bot.command(pass_context=True)
async def yt(ctx, url):
    """Plays music in whatever voice channel you're connected to"""
    role = discord.utils.get(ctx.message.author.server.roles, name="SHAMED")
    if role in ctx.message.author.roles:
        await bot.say("YOU ARE BEING SHAMED AND CANNOT USE BOT COMMANDS")
    else:
        if(ctx.message.channel.name != 'music-requests'):
            await bot.say("Music requests go in the #music-requests channel only")
        else:
            for x in bot.voice_clients:
                if(x.server == ctx.message.server):
                    await x.disconnect()
                    break

            author = ctx.message.author
            voice_channel = None
            voice_channel = author.voice_channel
            if(voice_channel == None):
                await bot.say("You must be in a voice channel to invoke this command")
            else:
                vc = await bot.join_voice_channel(voice_channel)

                player = await vc.create_ytdl_player(url)
                player.start()

bot.run('NDc1NzM1OTQ1MTExNDA0NTQ0.DkjXmQ.ABS3ku3KIvi3KxNfrnAKE9HR2_E')