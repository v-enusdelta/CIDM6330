from celery import shared_task
from .models import Event

# This is a simple Celery task that adds two numbers together.
# It can be called asynchronously using Celery.
@shared_task
def create_event_task(session_id, item_id, event_type):
    try:
        Event.objects.create(
            session_id=session_id,
            item_id=item_id,
            event_type=event_type
        )
    except Exception as e:
        print(f"Error creating event: {e}")

# After defining this task, write more code in views.py. Sample code is below

# from django.http import JsonResponse
# from .tasks import your_async_task

# def your_view(request):
#     # Call the Celery task asynchronously using the delay() method
#     result = your_async_task.delay(4, 6)
#     return JsonResponse({'task_id': task_result.id})  