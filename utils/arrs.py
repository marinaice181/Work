
def get_(array, index, default=None):
    def get(array, index, default=None):
       """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
@@ -9,7 +9,7 @@ def get_(array, index, default=None):
    :return: значение по индексу или значение по-умолчанию.
       """

    if 0 <= index < len(array):
        if -len(array) <= index < len(array):
            return array[index]
    return default

