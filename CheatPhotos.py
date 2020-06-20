import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
import time
import random

def main():

    vk_session = vk_api.VkApi(login='+номер', password='пароль', app_id='2685278')
    
    vk_session.auth(token_only=True)
    longpoll = VkLongPoll(vk_session)
    vks = vk_session
    print("BOT STARTED!")
    def send(peer_id, message):
    	m = vks.method("messages.send", {"peer_id": peer_id, "random_id": 0, "message": message})
    	return m
    
    for event in longpoll.listen():
    	try:
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower() == "!help":
    			send(event.peer_id, "1. !photo {кол-во} {альбом}\n2. !music {кол-во} - загрузка музыки\n3. !video {кол-во} {альбом} {ссылка} - загрузка видео")
    			
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower()[:6] == "!music":
    			count = event.text.lower()[6:].split()[0]
    			m = random.randint(0, 100000000)
    			upload = VkUpload(vk_session)
    			for x in range(int(count)):
    				s = upload.audio(audio="face.mp3", artist=f"test {m}", title=f"test2 {m}")
    				m += 1
    			send(event.peer_id, f"Загрузку музыки закончил!\nколичество: {count}")
    		
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower()[:6] == "!video":
    			count = event.text.lower()[6:].split()[0]
    			al = event.text[6:].split()[1]
    			htps = event.text[6:].split()[2]
    			upload = VkUpload(vk_session)
    			for x in range(int(count)):
    				s = upload.video(link=htps, name="видео", description="видео", album_id=al)
    			send(event.peer_id, f"Загрузку видео закончил!\nколичество: {count}")
    			
    		if event.type == VkEventType.MESSAGE_NEW and event.text.lower()[:6] == "!photo":
    			count = event.text[6:].split()[0]
    			al = event.text[6:].split()[1]
    			upload = VkUpload(vk_session)
    			for x in range(int(count)):
    				s = upload.photo(photos="lol.png", album_id=int(al))
    				
    			vks.method("messages.send", {"peer_id": event.peer_id, "random_id": 0, "message": f"Загрузку окончил!\ncount: {count}"})
    			
    	except Exception as s:
    		print(f"Error: {s}")
   

while True:
	main()