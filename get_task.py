

from celeri_01.shop_app.celery_app import app
from celery.result import AsyncResult


def main():
    result = AsyncResult(
        id="75a81b4b-394a-4b79-a908-e03ae81ec896",
        app=app,
    )

    print("result: ", result)
    print("result.status: ", result.status)
    print("result.name: ", result.name)

main()