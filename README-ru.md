# RailsClassToPath

Плагин для Sublime Text, который преобразует имя Ruby/Rails-класса в путь к
файлу и обратно.

Удобен для навигации между кодом и файловой структурой Rails-приложения.
Полезен, когда нужно создать файл, имея имя класса, или определить имя класса
по пути.


## Возможности

- Class → path
  - `Api::V1::UsersController` → `api/v1/users_controller`
- Path → Class
  - `api/v1/users_controller` → `Api::V1::UsersController`
- Поддержка абсолютных namespace
  - `::Api::V1` → `/api/v1`
  - `/api/v1` → `::Api::V1`
- Преобразование snake_case → CamelCase
- Поддержка множественного выделения


## Использование

1. Выделите текст (имя Ruby-класса или путь).
2. Нажмите горячую клавишу (по умолчанию `Ctrl+k, Ctrl+h`).

Выделенный текст будет заменён результатом преобразования.


## Примеры

| Вход | Результат |
|-----|----------|
| Api::V1::Catalogs::OfferSerializer | api/v1/catalogs/offer_serializer |
| api/v1/catalogs/offer_serializer | Api::V1::Catalogs::OfferSerializer |
| ::Api::V1 | /api/v1 |
| /api/v1 | ::Api::V1 |


## Установка

### Через Package Control

1. Откройте Command Palette (`Ctrl+Shift+P`)
2. Выполните `Package Control: Install Package`
3. Найдите `RailsClassToPath`


### Ручная установка

Склонируйте репозиторий в папку Packages:

`git clone git@github.com:Zlatov/RailsClassToPath.git ~/.config/sublime-text/Packages/RailsClassToPath`


## Требования

- Sublime Text 4
- Linux


## Лицензия

MIT

## Автор

Zlatov
