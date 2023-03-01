# by @Mr_AliMorradi, @Sigaris
# https://t.me/PiniGerTeam

from telethon.sync import TelegramClient, events
import os
import configparser

if not os.path.exists('config.ini'):
    session_name, api_id, api_hash = input('Enter a name for session: '), input('Enter your api_id: '), input('Enter your api_hash: ')
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['config'] = {}
    config['config']['session_name'] = session_name
    config['config']['api_id'] = api_id
    config['config']['api_hash'] = api_hash
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    config = configparser.ConfigParser()
    config.read('config.ini')
    session_name = config['config']['session_name']
    api_id = config['config']['api_id']
    api_hash = config['config']['api_hash']

bot = TelegramClient(session_name, api_id, api_hash).start()

@bot.on(events.NewMessage(pattern=r'(بصبر دان بشه|بصبر دان شه|بصب دان شه|بصب دان بشه)', func=lambda e: e.is_reply))
async def show_image(event):
    userid = await bot.get_me()
    if event.sender_id == userid.id:
        try:
            message = await event.get_reply_message()
            download = await bot.download_media(message)
            await bot.send_message('me', f'عکس نابود شونده از مرحوم 😂😂', file=download)
            os.remove(download)
        except Exception as e:
            await bot.send_message('me', f"خطایی دریافت شد:\n\n{e}")

bot.run_until_disconnected()