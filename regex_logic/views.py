from django.shortcuts import render
from django.http import JsonResponse
import re
def reverse_string_logic(request):
    if request.method == 'POST':
        input_string = request.POST.get('string', '')  # Use .get() to access POST data
        reversed_string = input_string[::-1]  # Reverse the string
        return JsonResponse({'reversed_string': reversed_string})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def regex_generator(request):
    if request.method == 'POST':
        input_string = request.POST.get('string', '')
        
        # Generate regex patterns
        pattern = [
            re.escape(input_string),  # Exact match
            rf".*{re.escape(input_string)}.*",  # Contains the string
            rf"^{re.escape(input_string)}$",  # Matches the entire string exactly
            rf"^{re.escape(input_string[:len(input_string)//2])}.*",  # Starts with the first half
            rf".*{re.escape(input_string[len(input_string)//2:])}$",  # Ends with the second half
            rf"({re.escape(input_string)}){{2,}}",
            rf"^.{{{len(input_string)}}}$",
            rf"{''.join([f'{re.escape(c)}.' for c in input_string[:-1]])}{re.escape(input_string[-1])}",
            rf"^{re.escape(input_string[:2])}.*{re.escape(input_string[-2:])}$",
            re.sub(r'[aeiou]', '[aeiou]', re.escape(input_string), flags=re.IGNORECASE)
        ]
        
        # Return JSON response with the patterns
        return JsonResponse({
            'pattern': pattern
        })
        
    # Handle GET request or return error for other methods
    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)
