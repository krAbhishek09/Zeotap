
from django.shortcuts import render, redirect
from .models import Rule
from .engine import create_rule, evaluate_rule
import json

def create_rule_view(request):
    
    if request.method == 'POST':
        rule_string = request.POST.get('rule_string')
        try:
         
            create_rule(rule_string)
            Rule.objects.create(rule_string=rule_string)
            return redirect('evaluate_rule')
        except ValueError as e:
            return render(request, 'create_rule.html', {'error': str(e)})
    return render(request, 'create_rule.html')



def evaluate_rule_view(request):
    
    result = None
    if request.method == 'POST':
        try:
            
            rule_id = request.POST.get('rule_id')

            
            if not rule_id.isdigit():
                return render(request, 'evaluate_rule.html', {'result': 'Invalid rule ID.', 'rules': Rule.objects.all()})

            rule_id = int(rule_id)
            attributes = json.loads(request.POST.get('attributes', '{}'))

         
            rule = Rule.objects.get(id=rule_id)

            ast_node = create_rule(rule.rule_string)
            result = evaluate_rule(ast_node, attributes)

        except Rule.DoesNotExist:
            result = "Rule not found."
        except json.JSONDecodeError:
            result = "Invalid JSON format in attributes."
        except Exception as e:
            result = f"Error: {e}"

    return render(request, 'evaluate_rule.html', {'result': result, 'rules': Rule.objects.all()})
