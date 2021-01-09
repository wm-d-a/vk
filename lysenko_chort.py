import vk_api
import time

login = input('Введите логин: ')
password = input('Введите пароль: ')
vk_session = vk_api.VkApi(login, password, app_id=2685278)  # KateMobile id
vk_session.auth()

vk = vk_session.get_api()
id = int(input('Введите peer_id: '))
print('Для беседы: 1; для лички: 2')
buf = input('Введите число: ')
peer_id = 2000000000 + id
if buf == '2':
    peer_id = id
print('Запуск...')
while True:
    vk.messages.markAsRead(peer_id=peer_id)
    vk.messages.setActivity(peer_id=peer_id, type="audiomessage")
    time.sleep(6)
    print('Голосовое...')
    vk.messages.markAsRead(peer_id=peer_id)
    vk.messages.setActivity(peer_id=peer_id, type="typing")  # можно audiomessage  будет голосовуха
    time.sleep(6)
    print('Текстовое...')