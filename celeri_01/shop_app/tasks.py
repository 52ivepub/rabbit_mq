import logging
from time import sleep
from celeri_01.shop_app.smtp_email_backends import SmtpEmailBackend
from celeri_01.shop_app.celery_app import app

log = logging.getLogger(__name__)


def fetch_users_info(user_ids: list[int]):
    return [
        (
        f"User #{user_id:02d}",
        f"email.user{user_id:02d}@example.com"
        ) for user_id in user_ids]


newslatter_body_template = """ \
Dear {name},

Our sale jast started!
Sale # {sale_id}
Use our promocod: "{promo}"!
"""
@app.task
def send_email_newslatter(
        user_ids: list[int],
        promo_code: str,
        sale_id: int,


):
    log.info("Start sending email newslattes #%s email to %s users",
            sale_id,
            len(user_ids),
            )
    
    email_backend = SmtpEmailBackend(
        smtp_server="localhost",
        smtp_port=1025,
        from_email="noreply@shop.com",
    )
    users_info = fetch_users_info(user_ids)
    for name, email in users_info:
        subject = f"{name}, join our sale #{sale_id}!"
        body = newslatter_body_template.format(
            name = name,
            sale_id = sale_id,
            promo = promo_code,
        )
        email_backend.send_email(
            recipient=email,
            subject=subject,
            body=body,
        )
        log.info("Sent email to user %s", email)
        # это только для демонстрации
        sleep(1)

    log.info("Finished sending email newslattes #%s email to %s users",
        sale_id,
        len(user_ids),
        )
    
print("helloo!!!!!")
