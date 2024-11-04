import stripe
from forex_python.converter import CurrencyRates

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollar(amount):
    """Перевод рубли в доллары"""
    c = CurrencyRates()
    rate = c.get_rate('RUB', "USD")
    return int(rate * amount)


def create_stripe_product(product):
    """Создает продукт в страйпе"""
    stripe.Product.create(name="Payment")


def create_stripe_price(amount):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Payment"},
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        return_url="https://127.0.0.1:8000/materials/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
