from django.shortcuts import render
from django.http import JsonResponse

def reverse_string_logic(request):
    if request.method == 'POST':
        input_string = request.POST.get('string', '')  # Use .get() to access POST data
        reversed_string = input_string[::-1]  # Reverse the string
        return JsonResponse({'reversed_string': reversed_string})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
