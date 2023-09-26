import time
import random

import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Adicione o caminho da sua pasta "Downloads".
from_dir = "C:/Users/jo__a/Downloads"              
# Crie a pasta "Arquivos_Documentos" em sua área de trabalho e atualize o caminho de acordo.
to_dir = 'C:/Users/jo__a/Documents/byjus codes pro/c101 a c 120/c103'

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Classe Gerenciadora de Eventos
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
        
        time.sleep(1)
        for key, value in dir_tree.items():

            time.sleep(1)
            if extension in value:               

                file_name = os.path.basename(event.src_path)

                print("Baixado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                time.sleep(1)
                if os.path.exists(path2):

                    print("Diretório Existe...")
                    time.sleep(1)
                                        
                    if os.path.exists(path3):

                        print("Arquivo Já Existe em  " + key + "....")
                        print("Renomeando Arquivo " + file_name + "....")

                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]

                        path4 = to_dir + '/' + key + '/' + new_file_name

                        print("Movendo " + new_file_name + "....")
                        shutil.move(path1, path4)
                        time.sleep(1)

                    else:
                        print("Movendo " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Criando Diretório...")
                    os.makedirs(path2)
                    print("Movendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

            # print(event)
            
# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()