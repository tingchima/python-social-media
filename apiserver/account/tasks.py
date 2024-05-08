from celery import Task, shared_task


class EmailSend(Task):

    name = "email send"

    def on_success(self, retval, task_id, args, kwargs):
        print(f"task_id={task_id}")

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))


@shared_task(
    name="email send",
    bind=True,
    base=EmailSend,
)
def email_send(self, email_id):

    from account.containers import email_service

    try:
        email = email_service.email_get_by_id(id=email_id)
        email_service.email_send(email)
    except Exception as e:
        self.retry(exc=e, countdown=1)
