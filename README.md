# Link shortener

_Приложение для сокращения ссылок_

### Стек технологий:

* Python
* Django
* GraphQL
* SQLite

### Запуск проекта:

1. Склонировать репозиторий:
~~~~
git clone https://github.com/applepinepaprica/link_shortener.git
~~~~

2. Убедиться, что на компьютере установлен Python 2 версии:
~~~~
python --version
~~~~

3. Запустить сервер в папке проекта:
~~~~
cd link_shortener
python ./manage.py runserver
~~~~

4. По дефолту сайт будет доступен по порту 8000 (http://localhost:8000).

### How to use:

Используя `http://localhost:8000/graphql`, можно:

1. Создать ссылку:
~~~~
mutation createLink {
  createLink(input: {
    fullLink: "https://somenewasite.com"
  }) {
    ok
    link {
      fullLink
      shortLink
      id
    }
  }
}
~~~~
Ответ:
~~~~
{
  "data": {
    "createLink": {
      "ok": true,
      "link": {
        "fullLink": "https://somenewasite.com",
        "shortLink": "px7f99awst",
        "id": "9"
      }
    }
  }
}
~~~~
По ссылке `http://localhost:8000/px7f99awst` будет редирект на `https://somenewasite.com`

2. Так же сервер логирует время, в которое перешли по ссылке. Получить эти данные можно по запросу:
~~~~
{
  link(id: 7) {
    id
    shortLink
    fullLink
    linkInfoes {
      timeTrack
    }
  }
}
~~~~
