import twitchio
import asyncio
from twitchio.ext import commands

# Defina suas variáveis
# Configurações do bot Twitch
bot_username = 'hawkinngx'
bot_token = 'oauth:rdjdrtbvsumf3127zffe8xniwqcxvc'
channel_name = 'xxmarciano'

# Criar a classe do bot
class MeuBot(commands.Bot):

    # Inicializar o bot
    def __init__(self):
        super().__init__(
            token=bot_token,
            prefix='!',
            initial_channels=[channel_name]
        )

    # Evento que ocorre quando o bot se conecta ao chat
    async def event_ready(self):
        print(f'{self.nick} está online!')
        await self.get_channel(channel_name).send(f'Olá, eu sou o {self.nick}, o bot do canal!')

    # Evento que ocorre quando o bot recebe uma mensagem no chat
    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

# Criar e executar o bot
bot = MeuBot()
bot.run()
