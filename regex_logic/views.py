from django.shortcuts import render
from django.http import JsonResponse
import re
import exrex 

def reverse_string_logic(request):
    if request.method == 'POST':
        input_string = request.POST.get('string', '')
        if not input_string:
            return JsonResponse({'error': 'String is required'}, status=400)
        reversed_string = input_string[::-1]  # Reverse the string
        return JsonResponse({'reversed_string': reversed_string})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def regex_generator(request):
    if request.method == 'POST':
        input_string = request.POST.get('string', '')
        if not input_string:
            return JsonResponse({'error': 'String is required'}, status=400)
        
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

def regex_testing(request):
    if request.method == 'POST':
        pattern = request.POST.get('pattern', '')
        
        if not pattern:
            return JsonResponse({
                'error': 'Pattern is required'
            }, status=400)
            
        try:
            # Validate the regex pattern
            re.compile(pattern)
            
            # Use a set to store unique examples
            unique_examples = set()
            
            # Keep generating until we have 5 unique examples or hit a limit
            max_attempts = 20  # Prevent infinite loop if pattern generates limited unique values
            attempts = 0
            
            while len(unique_examples) < 5 and attempts < max_attempts:
                example = exrex.getone(pattern)
                unique_examples.add(example)
                attempts += 1
            
            # Convert set back to list for JSON serialization
            examples = list(unique_examples)
            
            return JsonResponse({
                'pattern': pattern,
                'generated_strings': examples,
                'success': True,
                'unique_count': len(examples)
            })
            
        except re.error as e:
            return JsonResponse({
                'error': f'Invalid regex pattern: {str(e)}'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': f'Error generating string: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)

def regex_normal(request):
    if request.method == 'POST':
        pattern = request.POST.get('pattern', '')
        string = request.POST.get('string','')
        
        if not pattern or not string:
            return JsonResponse({
                'error': 'All fields are required'
            }, status=400)

        try:
            regex = re.compile(pattern)

            # Check for a match
            match = regex.search(string)

            if match:
                return JsonResponse({
                    'message': 'Pattern matches the string',
                    'match': match.group()  # Return the matched string
                })
            else:
                return JsonResponse({
                    'message': 'No match found'
                })

        except re.error as e:
            return JsonResponse({
                'error': f'Invalid regex pattern: {e}'
            }, status=400)

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)

 
