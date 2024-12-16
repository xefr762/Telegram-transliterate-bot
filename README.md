# Telegram transliterate bot with Docker
## Описание
A telegram bot, which accepts the cyrillic alphabet and translates it into the litinic alphabet
Телеграм бот, который принимает на вход сообщение на кириллице в сообщение на латинице. 
Основная задача перевод ФИО в соотетствии с [Приказом МИД России от 12.02.2020 № 2113](https://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/).

Для удобства использования на персональных компьютерах, создан **Docker** контейнер

## Инструкция по запуску **Бота** через **Docker**

1. Установите **Docker** -> [Установка](https://docs.docker.com/engine/install/)
2. Находясь в папке с данным репозиторием [Как установить репозиторий с github](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives), выполните следующу команду для создания образа:
```bash
docker build
```
3. Проверьте, что образ создан, с помощью команды:
```bash
docker images
```
4. Запустите полученный образ, указав **_IMAGE ID_** из предыдущего шага:
```bash
ducker run -d -p 80:80 <Ваш IMAGE ID>
```
5. Посмотреть статус работы контейнера можно с помощью команды:
```bash
docker ps
```
6. Если вы строке вывода вы видете **STATUS** с параметром **UP** - ваш контейнер успешно создан и запущен, и вы можете использовать бота по назначению!


## Порядок действий для удаления **Docker-образа**:
1. Остановите запущенный контейнер с помощью команды:
```bash
docker ps
docker stop <Ваш CONTAINER ID>
```
  - В дальнейшем нам понадобится значение из поля _IMAGE_, он же _IMAGE ID_
  
2. Удалите контейнер с помощью команды:
```bash
docker rm <Ваш CONTAINER ID>
```
3. Удаляем образ:
```bash
docker rmi <Ваш IMAGE ID>
```
## Вы сотворили магию и освободили пространство на диске!
