import os
import env
import logging
from twitchio.ext import commands


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
                token=os.environ['TOKEN'],
                prefix=os.environ['BOT_PREFIX'],
                initial_channels=[os.environ['CHANNEL']])
        self.log = logging

    def get_author_prefix(self, message):
        prefix = ''
        if message.author.is_subscriber:
            prefix = '[sub]'
        if message.author.is_mod:
            prefix = '[mod]'
        return prefix

    async def event_ready(self):
        ready_string = f'Ready: {self.nick}'
        print(ready_string)
        self.log.info(ready_string)

    # async def event_message(self, message):
    #     if message.author.name == 'segundofdez':
    #         await message.channel.send(f'Prueba para {message.author.name}')

    async def event_command_error(self, ctx, error):
        err = f'Error running: {error} - from <{ctx.message.author.name}>'
        self.log.error(err)
        await ctx.send('No te entiendo broh!')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def web(self, ctx):
        await ctx.send('https://oscarmlage.com')

    @commands.command()
    async def github(self, ctx):
        await ctx.send('https://github.com/oscarmlage')

    @commands.command()
    async def test(self, ctx):
        user_prefix = self.get_author_prefix(ctx.message)
        await ctx.send(f'Test passed, {user_prefix} {ctx.author.name}!')

    @commands.command()
    async def say(self, ctx, *, message: str = None):
        nomsg = f'Say something, {ctx.author.name}!'
        content = message or nomsg
        await ctx.channel.send(content)


if __name__ == '__main__':
    bot = Bot()
    bot.run()
