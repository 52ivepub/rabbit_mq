import random
import string
from celeri_01.shop_app.tasks import send_email_newslatter


def fetch_users_ids_for_newslettr():
    return [
            # якобы юзер из базы
            random.randint(1, 100)
            # случаное число юзеров
            for _ in range(random.randint(20, 50))
            ]

def send_newslatters_task():
    user_ids = fetch_users_ids_for_newslettr()
    promo_code = "".join(random.choices(string.ascii_letters, k=5))
    result = send_email_newslatter.delay(
        user_ids=user_ids,
        promo_code=promo_code,
        sale_id=random.randint(50, 200),
    )
    print("sent task", result, repr(result))