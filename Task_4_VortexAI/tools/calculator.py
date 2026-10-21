import ast
import math
import operator


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _evaluate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 1000:
            raise ValueError("Exponent is too large.")

        result = _ALLOWED_OPERATORS[type(node.op)](left, right)

        if isinstance(result, (int, float)) and (
            not math.isfinite(result) or abs(result) > 1e100
        ):
            raise ValueError("Result is too large or not finite.")

        return result

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_evaluate(node.operand))

    raise ValueError("Only basic mathematical expressions are allowed.")


def calculate(expression: str):
    """Safely evaluate a basic mathematical expression."""
    if not expression.strip():
        raise ValueError("Expression cannot be empty.")

    if len(expression) > 200:
        raise ValueError("Expression is too long.")

    try:
        tree = ast.parse(expression, mode="eval")
        result = _evaluate(tree.body)
        return result
    except (SyntaxError, ZeroDivisionError, OverflowError) as exc:
        raise ValueError(f"Invalid mathematical expression: {exc}") from exc
