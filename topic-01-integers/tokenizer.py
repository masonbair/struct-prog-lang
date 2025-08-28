import re

# we put regular expressions in order of which we want to look for them
patterns = [
    [r"print", "print"], # Directly implemented token or KEY WORD
    [r"\d*\.\d+|\d+\.\d*|\d+","number"], # Number regex
    [r"[a-zA-Z_][a-zA-Z0-9_]*", "identifier"],
    [r"\+", "+"], # Plus regex
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\(", "("],
    [r"\)", ")"],
    [r"\s+", "whitespace"],
    [r".", "error"], #Generates an error for any left over characters
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        # Find first matching tokens
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break

        assert match

        if tag == "error":
            raise Exception(f"Syntax error: illegal charactor : {[match.group(0)]}")

        token = {"tag": tag, "position": position, "value":match.group(0)}
        value = match.group(0)
        if token["tag"] == "number":
            if "." in value:
                token["value"] = float(value)
            else:
                token["value"] = int(value)
        if token["tag"] == "identifier":
            token["value"] = value
        
        if token["tag"] != "whitespace":
            print(token)
            tokens.append(token)
        position = match.end()

    tokens.append({"tag":None, "position":position})  # Fixed typo here
    return tokens

def test_simple_tokens():
    print("Testing simple test")
    for c in "+-/*()":
        print(tokenize(c))
        assert tokenize(c) == [
            {"tag":c, "position":0, "value":c},
            {"tag":None, "position":1, "value":None}
        ]
    assert tokenize("3") == [
        {"tag":"number", "position":0, "value":3},
        {"tag":None, "position":1, "value":None}
    ]
    assert tokenize("cat") == [
        {"tag":"identifier", "position":0, "value":"cat"},
        {"tag":None, "position":3, "value":None}
    ]


def test_simple_expressions():
    print("Testing simple expressions")
    t = tokenize("3+4")
    assert t == [
        {'tag': 'number', 'position': 0, 'value': 3}, 
        {'tag': '+', 'position': 1, "value":"+"}, 
        {'tag': 'number', 'position': 2, 'value': 4}, 
        {'tag': None, 'position': 3, "value":None}
    ]

def test_whitespace():
    print("Testing whitespace")
    t = tokenize("3 + 4")
    assert t == [
        {'tag': 'number', 'position': 0, 'value': 3}, 
        {'tag': '+', 'position': 2, "value":'+'}, 
        {'tag': 'number', 'position': 4, 'value': 4}, 
        {'tag': None, 'position': 5, "value":None}
    ]

if __name__ == "__main__":
    print("Testing the tokinizer")
    test_simple_tokens()
    test_simple_expressions()
    test_whitespace()
    print("Finished")