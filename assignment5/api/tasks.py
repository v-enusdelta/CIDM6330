from celery import shared_task

# This is a simple Celery task that adds two numbers together.
# It can be called asynchronously using Celery.
@shared_task
def your_async_task(arg1, arg2):
    result = arg1 + arg2
    return result

# After defining this task, write more code in views.py. Sample code is below

# from django.http import JsonResponse
# from .tasks import your_async_task

# def your_view(request):
#     # Call the Celery task asynchronously using the delay() method
#     result = your_async_task.delay(4, 6)
#     return JsonResponse({'task_id': task_result.id})  