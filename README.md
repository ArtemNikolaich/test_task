## Задача
Написать класс для поиска любых повторяющихся чисел в массиве из N+2 целых чисел, содержащих элементы в диапазоне [1, N].

## Решение
Класс FindDuplicates принимает на вход массив arr, содержащий N+2 целых чисел, и имеет метод find(), который возвращает любые повторяющиеся числа в массиве.

Метод find() использует два набора (set): seen для хранения чисел, которые уже были просмотрены, и duplicates для хранения чисел, которые повторяются.

Мы проходим по каждому числу в массиве и проверяем, есть ли оно уже в seen. Если да, то добавляем его в duplicates, иначе добавляем его в seen.

В конце метод возвращает набор duplicates, который содержит все повторяющиеся числа в массиве.

### Пример использования
Создаем экземпляр класса FindDuplicates с массивом arr, вызываем метод find(), чтобы найти повторяющиеся числа в массиве, и выводим результат.
