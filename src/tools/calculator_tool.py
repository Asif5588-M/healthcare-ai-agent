from langchain.tools import tool
import statistics

@tool
def medical_calculator(expression: str) -> str:
    """
    Calculate medical statistics and numbers.
    Use this tool for: percentages, averages, risk ratios,
    number needed to treat (NNT), confidence intervals.
    Input: mathematical expression or description
    Examples: '52.9 / 40 * 100', 'average of [3.56, 5.97, 6.79]'
    Output: calculated result with explanation
    """
    try:
        expression = expression.strip()

        # Average calculation
        if "average" in expression.lower() or "mean" in expression.lower():
            import re
            numbers = [float(x) for x in re.findall(r"[\d.]+", expression)]
            if numbers:
                avg = statistics.mean(numbers)
                return f"Average of {numbers} = {avg:.4f}"

        # Safe eval for math
        allowed = {
            "__builtins__": {},
            "round": round, "abs": abs, "max": max, "min": min,
            "sum": sum, "len": len,
        }
        result = eval(expression, allowed)
        return f"Result: {result}"

    except Exception as e:
        return f"Calculator error: {str(e)}. Try simpler expression."