# Onlone store

## Описание проекта
Это интернет магазин в котором есть 2 страницы: 
+ Каталог (`home/`);
+ Контакты (`contacts/`). На этой странице можно оставить свои контакты для обратной связи.

## Использование
Для запуска приложения необходимо:
1. Клонируeте репозиторий:

```
https://github.com/IliaGirko/online_store.git
```
2. Устанавливаете виртуальное окружение:
```
poetry install
```
3. Для активации интернет магазина необходимо ввести в терминале команду:
```
python manage.py runserver #Произойдет активация сервера.
```
4. После того как Вы корректно выполите предыдущие шаги, запустить интернет магазин можно по сслыке в терминале:
```
Starting development server at http://127.0.0.1:8000/
```
при открытии браузера необходимо будет дописать(в адресной строке):
```
home/
```
таким образом чтобы получилось:
```
http://127.0.0.1:8000/home/
```
Открыть интернет магазин так же можно не переходя по ссылке, а прописав этот адрес в Вашем браузере:
```
http://127.0.0.1:8000/home/
```

## Пример работы
### В интернет магазине две страницы(`home` и `contacts`), вы може переключатся с домашней на контакты перейди по ссылкам или введя в адресной строке:
```
http://127.0.0.1:8000/contacts/
```
### На странице контакты есть форма обратной связи. При корректно заполненных полях Вы можете оставить заявку для обратного звонка. Для этого нажмите на кнопку `Отправить`



## Лицензии
Проект распространяеется под [лицензией MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
