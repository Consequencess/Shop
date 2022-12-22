from django.core.mail import send_mail


def send_confirmation_email(email, code, title, price):
    full_link = f'Привет подтверди заказ на продукт {title} на сумму {price}\n\nhttp://localhost:8000/order/confirm/{code}'

    send_mail(
        f'Привет от shop',
        full_link,
        'read87488@gmail.com',
        ['read87488@gmail.com']
    )