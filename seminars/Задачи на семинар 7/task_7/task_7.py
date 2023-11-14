"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os


def sort_files(directory):
    folders = {'Video': ['.mp4', '.avi', '.mkv'],
               'Pictures': ['.png', '.jpg', '.jpeg', '.gif', '.tiff'],
               'Texts': ['.txt', '.doc', '.docx', '.pdf']}
    if not os.path.exists(directory):
        print('Указанная директория не существует')
        exit()
    for directory, _, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            path = os.path.join(directory, file)
            for k, v in folders.items():
                if ext in v:
                    if not os.path.exists(os.path.join(directory, k)):
                        os.mkdir(os.path.join(directory, k))
                    new_path = os.path.join(directory, k, file)
                    os.replace(path, new_path)


if __name__ == '__main__':
    sort_files('\\task_7')
