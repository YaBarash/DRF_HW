import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(product):
    """Создает продукт в страйпе"""
    stripe_product = stripe.Product.create(name=product)
    return stripe_product.get("id")


def create_stripe_price(amount, product):
    """Создает цену в страйпе"""
    stripe_price = stripe.Price.create(
        currency="usd",
        unit_amount=int(amount * 100),
        product_data={"name": product},
    )
    return stripe_price


def create_stripe_session(stripe_price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": stripe_price, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
