import socket
"""
Сделай, чтобы сканер портов получал список IP из одного файла, а результаты сканирования записывал в другой.
"""
DIR = 'scan_port'
# Список портов для сканирования
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515,
         993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

# відкриваємо файл зі списком ip
with open(f'{DIR}/ip.txt', 'r', encoding='utf-8') as f:
    ip_data = f.read().split('\n')
    ip_data = [x for x in ip_data if x]


def write_to_file(ip, port_list):
    write_data = f"{ip} ||| {port_list}\n"
    with open(f'{DIR}/result.txt', 'a', encoding='utf-8') as file:
        file.write(write_data)


for ip in ip_data:
    lst = []
    print('Клієнт: ', ip)
    print("Ожидай, идет сканирование портов!")

    # В цикле перебираем порты из списка
    for port in ports:
        # Создаем сокет
        s = socket.socket()
        # Ставим тайм-аут в одну cекунду
        s.settimeout(1)
        # Ловим ошибки
        try:
            # Пробуем соединиться, хост и порт передаем как список
            s.connect((ip, port))
        # Если соединение вызвало ошибку
        except socket.error:
            # тогда ничего не делаем
            pass
        else:
            print(f"{ip}: {port} порт активен")
            lst.append(port)
            # Закрываем соединение
            s.close
    print("Сканирование завершено!")

    write_to_file(ip, lst)
