# :page_facing_up: Скрипт для обработки csv-файла
  Данный скрипт читает файлы с данными и формирует отчеты. Отчеты включают в себя список - позиция и среднюю эффективность. Отчеты структурируются по эффективности. 
  Скрипт может принимать несколько файлов и название в виде параметров --file и --report. Отчеты формируются по всем переданным файлам, а не по каждому отдельно. В 
  архитектуру заложенна возможность добавления новых отчетов.
  
## Содержание
- [Технологии](#технологии)
- [Установка](#установка)
- [Запуск](#запуск)
- [Автор](#автор)

## Технологии 
| Технология | Назначение |
| ----------- | ----------- |
| Python    | основной язык  |
| cvs  | работа с csv-файлами |
| argparse | парсинг аргументов командной строки |
| tabulate | вывод результата в консоль |
| pytest | тесты |

## Установка
### Клонирование проекта 
```
git clone https://github.com/DmitryLkT/reader_csv_file.git
cd reader_csv_file
```
### Активация вертуального окружения
```
.env\Scripts\activate
```
### Обновление pip
```
python -m pip install --upgrade pip
```
### Установка зависимостей
```
pip install -r requirements.txt
```
### Проверка тестов
```
pytest
```

## Запуск
```
python script.py --files file1.csv file2.csv --report performance
```
### Пример
![test](https://github.com/DmitryLkT/reader_csv_file/blob/master/static/images/test_image.jpg)

## Автор
Дмитрий Л.
- Почта: <Dmitry.plus1@yandex.ru>
- GitHub: [DmitryLkT](https://github.com/DmitryLkT)
