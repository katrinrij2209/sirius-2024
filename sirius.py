
import yadisk
token = input("Введите токен для API Яндекс.Диска:")
client = yadisk.Client(token=token)
file = input("Введите название файла")
with client:
    # Проверяет, валиден ли токен
    print(client.check_token())

    # Получает общую информацию о диске
    print(client.get_disk_info())

    # Скачивает файл запрошенный пользователем
    client.download("/"+file, file)
    print("Скачано")