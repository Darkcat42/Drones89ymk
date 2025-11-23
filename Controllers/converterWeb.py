# ИМПОРТЫ
from os import listdir, path
from pathlib import Path
from PIL import Image
import shutil
class ConverterWeb():
    """
    Для записи WebP-формата доступны:
    1. lossless: True - сжатие без потерь.
    2. quality: int 1-100, по умолчанию 80. количество усилий на сжатие: 0 - самое быстрое, зависимость - вес файла
    3. method: выбор - качеством или скоростью (0 = быстро, 6 = медленнее-лучше). По умолчанию 4.
    4. exact: True - сохраняет значения прозрачного RGB. В противном случае отбрасывает невидимые значения RGB для лучшего сжатия. по умолчанию False. Требуется libwebp 0.5.0
    """
    @classmethod
    # def convertImage(cls, img_src, quality=80, method=4, lossless=False, exact=False):
    #     output = 'str(self.output) + '/' + str(Path(file).stem) + '.webp' # строка куда сохранить'
    #     file_path = self.input_dir + '/' + file # строка что открыть
    #     image = Image.open(file_path) # метод бибы PIL (pillow) - открываем картину 
    #     image.save(output, 'webp')     # метод бибы PIL - закрываем в формате веба

    def convertImage(cls, img_src, dir_name, quality=80, method=4, lossless=False, exact=False):
        file = Path(img_src).stem+'.webp'
        output = f'static/webp/{dir_name}/{file}'
        image = Image.open(img_src) # метод бибы PIL (pillow) - открываем картину 
        image.save(output, 'webp')     # метод бибы PIL - закрываем в формате веба
        return output
# При вызове метода 
