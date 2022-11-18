import functools


def lfu_cache(max_limit=64):
    """Decorator for caching with deleting elements by LFU algorithm after going beyond the limit"""
    def internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_cache_key = (args, tuple(kwargs.values()))
            # Структура кэша = {cache_key: {cache_data: count_of_calls}, ...} до max_limit

            # Проверяем наличие полученного ключа в кэше
            for cache_key, cache_value in wrapper._cache.items():
                # Если находим ключ - изменяем колличество вызовов и возвращаем данные
                if new_cache_key == cache_key:
                    # Достаём данные из вложенного словаря - {cache_data: count_of_calls}
                    cache_data = tuple(cache_value.keys())[0]
                    count_of_calls = tuple(cache_value.values())[0]
                    # Изменяем колличество вызовов
                    cache_value = {cache_data: count_of_calls + 1}
                    # Новый кэш = {cache_key: {cache_data: count_of_calls + 1}, ...} до max_limit
                    wrapper._cache.update({cache_key: cache_value})
                    # Возвращаем данные
                    return cache_data

            # Если полученного ключа в кэше нет - вызываем функцию и записываем в кэш
            cache_data = func(*args, **kwargs)

            # Проверяем наличие места в кэше, если места нету - очищаем данные с наименьшим колличеством вызовов
            if len(wrapper._cache) >= max_limit:
                for cache_key, cache_value in wrapper._cache.items():
                    # Очищаем данные с наименьшим колличеством вызовов
                    if tuple(cache_value.values()) == wrapper.minimal_count_of_calls:
                        wrapper._cache.pop(cache_key)
                        break

            # Записываем в кэш полученные данные
            wrapper._cache.update({new_cache_key: {cache_data: 1}})

            # Обновляем наименьшое колличество вызовов на актуальное
            wrapper.minimal_count_of_calls = 1

            return cache_data

        wrapper.minimal_count_of_calls = 1
        wrapper._cache = dict()
        return wrapper

    return internal
