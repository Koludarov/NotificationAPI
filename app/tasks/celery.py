from celery import Celery

celery_app = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")


@celery_app.task
def process_mailing(mailing_id):
    # Логика обработки активной рассылки и отправки сообщений клиентам
    mailing = Mailing.get(mailing_id)
    if mailing:
        clients = Client.filter(code=mailing.operator_code, tag=mailing.tag)
        for client in clients:
            # Отправка сообщения клиенту через внешний сервис
            result = external_service.send_message(client.phone, mailing.message)
            if result:
                # Создание записи о сообщении в базе данных
                message = Message(mailing_id=mailing.id, client_id=client.id, status="sent")
                message.save()
            else:
                # Обработка ошибки при отправке
                message = Message(mailing_id=mailing.id, client_id=client.id, status="failed")
                message.save()
