# rule_engine/engine.py

import ast
import operator

OPERATORS = {
    ast.And: operator.and_,
    ast.Or: operator.or_,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
}

def create_rule(rule_string):
    
    try:
        tree = ast.parse(rule_string, mode='eval')
        return tree.body 
    except SyntaxError as e:
        raise ValueError(f"Invalid rule syntax: {e}")

def evaluate_node(node, data):
    
    if isinstance(node, ast.BoolOp):  
        op = OPERATORS[type(node.op)]
        return op(*(evaluate_node(value, data) for value in node.values))
    
    elif isinstance(node, ast.Compare): 
        left = evaluate_node(node.left, data)
        comparisons = [OPERATORS[type(op)](left, evaluate_node(comp, data))
                       for op, comp in zip(node.ops, node.comparators)]
        return all(comparisons)
    
    elif isinstance(node, ast.Name): 
        return data.get(node.id)
    
    elif isinstance(node, ast.Constant):  
        return node.value
    
    else:
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")

def evaluate_rule(ast_node, data):
   
    try:
        return evaluate_node(ast_node, data)
    except Exception as e:
        raise ValueError(f"Error evaluating rule: {e}")
