# Data Structures/3-Stack/2-ValidParenthesis.py
# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
#          determine if the input string is valid.
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.

# --- Simple Solution: Handles only one type of parenthesis ---
def is_valid_parentheses_simple(s: str) -> bool:
    """
    Checks if a string with only one type of parenthesis '(' and ')' is valid.
    Illustrates basic stack operation for parenthesis matching.
    Time Complexity: O(N)
    Space Complexity: O(N) in the worst case (all opening parentheses).
    """
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: # Closing parenthesis with no matching open
                return False
            stack.pop() # Matching open parenthesis found and popped
        # Ignores any other characters if present, or assumes only '(' and ')'
    return not stack # Valid if stack is empty (all parentheses matched)

# --- Robust Solution: Handles multiple types of parentheses ---
# (Based on the original function in the file)
def is_valid_parentheses_robust(s: str) -> bool:
    """
    Checks if a string with '(', ')', '{', '}', '[' and ']' is valid.
    Uses a stack to ensure correct order and type matching.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    stack = []
    # Iterate through each character in the string
    for char in s:
        if char == '(' or char == '[' or char == '{':
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
        elif char == ')':
            # If it's a closing ')'
            # Stack must not be empty and top must be '('
            if not stack or stack.pop() != '(':
                return False
        elif char == ']':
            # If it's a closing ']'
            # Stack must not be empty and top must be '['
            if not stack or stack.pop() != '[':
                return False
        elif char == '}':
            # If it's a closing '}'
            # Stack must not be empty and top must be '{'
            if not stack or stack.pop() != '{':
                return False
        # Any other characters in the string would be ignored by this logic
        # or could be handled as invalid if the problem strictly forbids them.

    # After iterating through the string, if the stack is empty, all brackets were matched.
    return not stack

# --- Jedi Solution: Using a Mapping & Discussing Edge Cases ---
def is_valid_parentheses_jedi(s: str) -> bool:
    """
    A slightly cleaner and more extensible version using a mapping for brackets.
    Also includes discussion of edge cases and efficiency.
    Time Complexity: O(N) - single pass over the string.
    Space Complexity: O(N) - for the stack in the worst-case (e.g., "(((((").
    """
    stack = []
    # Mapping closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in bracket_map.values(): # If it's an opening bracket
            stack.append(char)
        elif char in bracket_map: # If it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                # Stack is empty (no matching open) OR
                # top of stack doesn't match the expected opening bracket
                return False
            stack.pop() # Matching pair found
        # else:
            # Optional: Handle characters that are not parentheses
            # For this problem, we assume only bracket characters are present
            # or should be ignored. If other chars make it invalid, add check here.
            # pass

    return not stack # Valid if stack is empty

# **Jedi Solution - Discussion & Edge Cases:**
# 1.  **Mapping for Clarity**: The `bracket_map` makes the code for checking
#     closing brackets cleaner and easier to extend if more bracket types were added.
# 2.  **Edge Cases**:
#     -   **Empty String (`""`)**: Valid. The loop won't run, stack remains empty, `not stack` is `True`.
#     -   **Only Opening Brackets (`"((("`, `"[{("`)**: Invalid. Loop finishes, stack is not empty.
#     -   **Only Closing Brackets (`")))"`, `"]})`)**: Invalid. First closing bracket encountered
#         will find stack empty or a mismatch on `stack.pop()` in robust, or `stack[-1]` access in jedi, returning `False`.
#     -   **Mismatched Pairs (`"(]"` or `"{[)]}"`)**: Invalid. A closing bracket will not match
#         `bracket_map[char]` with `stack[-1]` (Jedi) or the popped element (Robust).
#     -   **Correct Order but Unmatched Internally (`"([)]"`)**: Invalid. Example: `(` pushed, `[` pushed.
#         When `)` is encountered, `stack[-1]` is `[`, `bracket_map[')']` is `(`, they don't match.
#     -   **Non-Bracket Characters**: If the string can contain other characters, the problem
#         statement needs to specify how to handle them (ignore, or consider string invalid).
#         The current Jedi and Robust implementations implicitly ignore them if they are not defined
#         as one of the six bracket characters.

# 3.  **Efficiency**:
#     -   Time Complexity: O(N) because we iterate through the input string once.
#         Stack operations (append, pop, accessing last element) are O(1) on average.
#     -   Space Complexity: O(N) in the worst-case scenario where the string consists
#         of all opening brackets, which are all stored on the stack. For a balanced
#         string like "((()))", it's O(N/2) = O(N).

# 4.  **Application**: This is a classic stack application used in parsing expressions,
#     validating code syntax (e.g., in IDEs), and processing structured text formats like JSON or XML.

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Valid Parentheses ---")

    print("\nSimple Solution (only '()'):")
    print(f"'()': {is_valid_parentheses_simple('()')}") # True
    print(f"'((': {is_valid_parentheses_simple('((')}") # False
    print(f"'))': {is_valid_parentheses_simple('))')}") # False
    print(f"'())': {is_valid_parentheses_simple('())')}") # False
    print(f"Empty '': {is_valid_parentheses_simple('')}") # True
    print(f"'(a)': {is_valid_parentheses_simple('(a)')}") # True, 'a' is ignored

    print("\nRobust Solution (multiple types):")
    print(f"'()': {is_valid_parentheses_robust('()')}") # True
    print(f"'()[]{{}}': {is_valid_parentheses_robust('()[]{}')}") # True
    print(f"'(]': {is_valid_parentheses_robust('(]')}") # False
    print(f"'([)]': {is_valid_parentheses_robust('([)]')}") # False
    print(f"'{{[]}}': {is_valid_parentheses_robust('{[]}')}") # True
    print(f"Empty '': {is_valid_parentheses_robust('')}") # True
    print(f"'[': {is_valid_parentheses_robust('[')}") # False
    print(f"']': {is_valid_parentheses_robust(']')}") # False, test stack empty on closing
    print(f"'(b)': {is_valid_parentheses_robust('(b)')}") # True, 'b' ignored


    print("\nJedi Solution (map-based, multiple types):")
    print(f"'()': {is_valid_parentheses_jedi('()')}") # True
    print(f"'()[]{{}}': {is_valid_parentheses_jedi('()[]{}')}") # True
    print(f"'(]': {is_valid_parentheses_jedi('(]')}") # False
    print(f"'([)]': {is_valid_parentheses_jedi('([)]')}") # False
    print(f"'{{[]}}': {is_valid_parentheses_jedi('{[]}')}") # True
    print(f"Empty '': {is_valid_parentheses_jedi('')}") # True
    print(f"']': {is_valid_parentheses_jedi(']')}") # False
    print(f"'{{': {is_valid_parentheses_jedi('{')}") # False
    print(f"'(c)': {is_valid_parentheses_jedi('(c)')}") # True, 'c' ignored

    # Test cases from Jedi discussion
    print("\nJedi - Edge Case Tests:")
    print(f"'(((': {is_valid_parentheses_jedi('(((')}") # False
    print(f"'))))': {is_valid_parentheses_jedi('))))')}") # False
    print(f"'[({{}})]': {is_valid_parentheses_jedi('[({{}})]')}") # True
    print(f"'[(])': {is_valid_parentheses_jedi('[(])')}") # False

