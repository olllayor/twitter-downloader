from aiogram import Bot, Dispatcher, types, executor
from aiogram.utils.exceptions import BadRequest
from api import get_video_url
# from db import insert_or_update_user, insert_video_url, get_user_id
from dotenv import load_dotenv
import os




load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# async def on_startup(_):
#     await db.create_tables()
#     print('Bot started')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    

    await message.reply("Hi! Send me a Twitter status URL and I'll try to retrieve the video from it.")

@dp.message_handler(regexp=r"(?i)(https?://(?:www\.)?twitter\.com/\S+/status/\d+|https?://x\.com/([a-zA-Z0-9_]+)/status/(\d+)(\?\S+)?)")
async def get_twitter_video(message: types.Message):
    tweet_url = message.text
    video_url = get_video_url(tweet_url)  # This function needs to return a direct video file URL

    if video_url is not None:
        try:
            # Attempt to send video by URL
            await bot.send_message(chat_id=message.chat.id, text="🎞Video is sending...")
            await bot.send_video(chat_id=message.chat.id, video=video_url)
        except BadRequest:
            # If sending the video fails, send the video URL as a message
            await message.reply(f"Sorry, I couldn't send the video directly. Here's the link to the video: {video_url}")
        except Exception as e:
            # Handle other possible exceptions
            await message.reply(f"An error occurred: {e}")
    else:
        await message.reply("Sorry, I couldn't retrieve the video URL from the provided tweet.")

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

