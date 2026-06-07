import socket
import time

users = []
# Указали 1) тип айпи  2)тип соединения: двустороний
main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# SOL_SOCKET - тип доступа, SO_REUSEADDR - игроки с одинаковым айпи могут заходить на сервер
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.bind(('127.0.0.1', 51889)) # указали айпи и порт сервера
main_socket.setblocking(False) # не даёт серверу остановится даже после первого соединения
main_socket.listen(5) # максимум игроков на сервере

while True: # бесконечный цикл
    try:
        new_socket, addr = main_socket.accept() # принимаем соединение
        print(new_socket, addr)
        users.append(new_socket)  # добавляем в список игрока который щас на сервере
    except BlockingIOError:
        pass
    for player_socket in users: # перебирает игроков
        try:
            text = player_socket.recv(1024).decode() # декодировали сообщение из байтов
            print(text)
        except BlockingIOError:
            pass
    time.sleep(1)
