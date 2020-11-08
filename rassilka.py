from telegram import Bot, ParseMode
from random import shuffle
from dotenv import load_dotenv
import time
import psycopg2
import os

# Put message text in HTML here
message_text = '''
<b>***TEXT***</b>  
'''.strip()

# Change if required
DB_PORT = ***DBPORT***

# --- SCRIPT STARTS HERE ---
load_dotenv(verbose=True)

# Fetch chat ids
conn = psycopg2.connect(
		dbname=os.getenv('CROCODILE_GAME_DB_NAME'),
		user=os.getenv('CROCODILE_GAME_DB_USER'),
		password=os.getenv('CROCODILE_GAME_DB_PASS'),
		host='localhost',
		port=DB_PORT,
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM chats')
chats = [c[0] for c in cursor.fetchall()]
cursor.close()
conn.close()

# Randomize chats
shuffle(chats)

print(f'Total chats to send: {len(chats)}')
print('Press Ctrl+C to cancel')

time.sleep(5)
sent = 0

bot = Bot(os.getenv('CROCODILE_GAME_BOT_TOKEN'))

try:
	for chat in chats:
		try:
			bot.send_message(chat, message_text, parse_mode=ParseMode.HTML)
			sent += 1
		except Exception as e:
			if 'New chat id:' in f'{e}':
				new_chat_id = int(f'{e}'.split(' ')[-1])
				if new_chat_id not in chats:
					try:
						time.sleep(0.1)
						bot.send_message(new_chat_id, message_text, parse_mode=ParseMode.HTML)
						sent += 1
					except Exception as e:
						print(f'{sent}/{len(chats)} - {chat}: {e}')
			else:
				print(f'{sent}/{len(chats)} - {chat}: {e}')
		time.sleep(0.1)
finally:
	print(f'Sent to {sent} chats')
