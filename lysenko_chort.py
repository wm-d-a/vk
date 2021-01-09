import vk_api
import time

login = input('Введите логин: ')
password = input('Введите пароль: ')
vk_session = vk_api.VkApi(login, password, app_id=2685278)  # KateMobile id
vk_session.auth()

vk = vk_session.get_api()
id = int(input('Введите peer_id: '))

print('Выберите режим: 1 - только текст, 2 - только аудиосообщения, 3 - и то, и другое')
buf2 = input('Введите число: ')
aud_mes = True
txt_mes = True
peer_id = 2000000000 + id
if buf2 == '1':
    aud_mes = False
elif buf2 == '2':
    txt_mes = False

if len(str(id)) > 5:
    peer_id = id
print('Запуск...')
while True:
    if aud_mes:
        vk.messages.markAsRead(peer_id=peer_id)
        vk.messages.setActivity(peer_id=peer_id, type="audiomessage")
        time.sleep(6)
        print('Голосовое...')
    if txt_mes:
        vk.messages.markAsRead(peer_id=peer_id)
        vk.messages.setActivity(peer_id=peer_id, type="typing")  # можно audiomessage  будет голосовуха
        time.sleep(6)
        print('Текстовое...')
