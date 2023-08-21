# Тестовое задание
Результат можно протестировать по ссылке: [https://testtask02.herokuapp.com/item/1/](https://testtask02.herokuapp.com/item/1/)
## Реализованный функционал:
 - Модель item с полями name, description, price.
 - Страница `item/{id}`, на которой указана информация о товаре, и кнопка "перейти к оплате".
 - API, доступный по ссылке `buy/{id}`, создающий сессию оплаты для выбранного товара, и переходящий на страницу оплату сервиса Stripe.
 - Панель администратора, доступная по ссылке `/admin`. Логин: admin, пароль: admin. Создать новые товары можно в таблице items. Id проставляется автоматически.
 - Использование переменных среды.
 - Подготовка приложения для использования в Docker.

# Установка

Клонирование репозитория:

$ git clone [https://github.com/petosbratok/testtask02](https://github.com/petosbratok/testtask02)

$ cd testtask02

В папке task нужно создать файл .env, куда необходимо добавить переменные STRIPE_SECRET_KEY, STRIPE_ENDPOINT_SECRET, STRIPE_PUBLIC_KEY, необходимые для работы сервиса Stripe.

Заранее нужно установить Python 3.9 и Pip.
Установка необходимых модулей:

$ pip install -r requirements.txt

Once  `pip`  has finished downloading the dependencies:

$ cd project
$ python manage.py runserver

# Main links
Home page:  `http://127.0.0.1:8000/`<br>
Product: `http://127.0.0.1:8000/product/<item_id>/`<br>
Cart `http://127.0.0.1:8000/cart/`<br>
Checkout: `http://127.0.0.1:8000/checkout/` <br>
Order: `http://127.0.0.1:8000/order/<order_id>/` <br>
Admin panel: `http://127.0.0.1:8000/admin/`
