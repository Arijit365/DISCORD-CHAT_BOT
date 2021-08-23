import json
import random

import discord
import request

# add client

TOKEN = 'ODc3NjUwMTkyODIyODUzNzEy.YR1tbw.jO7x9NsQ7hYtjQAzMFlDTJlFMlI'
Client = discord.Client()
victim_name = ['Anirban']
new = [
    " Bokachoda",
    " psycopath",
    " bastardo",
    " khankir chele",
    " paglachoda",
    " bodhaichoda",
    " magibazz",
    " maimenat oke debe na",
    " kono meye oke debe na",
    " babachoda",
    " maa choda",
    " buddhochodda",
    " madarchod",
    " Dhon nai",
    " ami amar baper pod mari",
    " ami ekta chutmarike ",
    " amr bichii nei",
    " loker pod maar te giye amr mere jai",
    " ami shimpamji er che adhom ",
    " amr maal pore na",
]
swords = [
    ' sad '
]

encouragement = [
    " You are a great guy don't think too much",
    " i'm always here for you , you can talk to me anytime",
    " that's not a problem , i know you can do it ",
    " you are the best i know !",
    " you are the most admiral person  i know",
]

images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA7v9sfEti-R8M5rgyuD8SnyOEFm5R0d4i0g&usqp=CAU',
    'https://i.redd.it/0lx5b9lylhh41.jpg',
    'https://i.kym-cdn.com/photos/images/masonry/002/106/169/da8.jpg',
]


@Client.event
async def on_ready():
    print('we have logged in as {0.user} '.format(Client))

    # quote API
    def get_quote():
        response = request.get('https://zenquotes.io/api/random')
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return quote

    @Client.event
    async def on_message(message):
        if message.author == Client.user:
            return
            # msg = message.content
            if message.content.startswith('hello'):
                pass
            else:
                await message.channel.send('Hello folks')

        if any(word in message.content for word in victim_name):
            await message.channel.send(random.choice(new))

            if message.content.startswith('$inspire'):
                return
            # bringing quote
            quote = get_quote()
            await message.channel.send(quote)

            if any(word in message.content for word in swords):
                await message.channel.send(random.choice(encouragement))


Client.run(TOKEN)
