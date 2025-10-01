import re

# Define patterns for tokens
patterns = [
    [r"print","print"],
<<<<<<< HEAD
    [r"true","true"],
    [r"false","false"],
=======
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    [r"if","if"],
    [r"else","else"],
    [r"while","while"],
    [r"continue","continue"],
    [r"break","break"],
<<<<<<< HEAD
    [r"\d*\.\d+|\d+\.\d*|\d+", "number"],
    [r'"([^"]|"")*"', "string"],    #String Literals
=======
    [r"return","return"],
    [r"assert","assert"],
    [r"and","&&"],
    [r"or","||"],
    [r"not","!"],
    [r"\d*\.\d+|\d+\.\d*|\d+", "number"],
    [r'"([^"]|"")*"', "string"],  # string literals
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    [r"[a-zA-Z_][a-zA-Z0-9_]*", "identifier"],  # identifiers
    [r"\+", "+"],
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\(", "("],
    [r"\)", ")"],
<<<<<<< HEAD
    [r"\{", "{"],
    [r"\}", "}"],
    [r"\;", ";"],
    [r"\<\=", "<="],
    [r"\<", "<"],
    [r"\>\=", ">="],
    [r"\>", ">"],
    [r"\=\=", "=="],
    [r"\!\=", "!="],
    [r"\!", "!"],
    [r"\&\&", "&&"],
    [r"\|\|", "||"],
    [r"\=", "="],

=======
    [r"\)", ")"],
    [r"==", "=="],
    [r"!=", "!="],
    [r"<=", "<="],
    [r">=", ">="],
    [r"<", "<"],
    [r">", ">"],
    [r"\=", "="],
    [r"\;", ";"],
    [r"\&\&", "&&"],
    [r"\|\|", "||"],
    [r"\!", "!"],
    [r"\{", "{"],
    [r"\}", "}"],
    [r"\[", "["],
    [r"\]", "]"],
    [r"\.", "."],
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    [r"\s+","whitespace"],
    [r".","error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0]) 

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        assert match
        # (process errors)
        if tag == "error":
            raise Exception("Syntax error")
        token = {
            "tag":tag,
            "position":position,
            "value":match.group(0)
        }
        if token["tag"] == "number":
            if "." in token["value"]:
                token["value"] = float(token["value"])
            else:
                token["value"] = int(token["value"])
<<<<<<< HEAD
        
        if token["tag"] == "string":
            # token["value"] = token["value"][1:-1].replace('""','"')
            value = token["value"]
            assert len(value) >= 2
            value = value[1:-1]
            token["value"] = value
        if token["tag"] in ["true","false"]:
            token["value"] = (token["tag"] == "true")
            token["tag"] = "boolean"
=======
        if token["tag"] == "string":
            token["value"] = token["value"][1:-1].replace('""', '"')
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
        if token["tag"] != "whitespace":
            tokens.append(token)
        position = match.end()
    # append end-of-stream marker
    tokens.append({
        "tag":None,
        "value":None,
        "position":position
    })
    return tokens

def test_simple_token():
    print("test simple token")
<<<<<<< HEAD
    examples = [item[1] for item in [
        [r"\+", "+"],
        [r"\-", "-"],
        [r"\*", "*"],
        [r"\/", "/"],
        [r"\(", "("],
        [r"\)", ")"],
        [r"\{", "{"],
        [r"\}", "}"],
        [r"\;", ";"],
        [r"\<\=", "<="],
        [r"\<", "<"],
        [r"\>\=", ">="],
        [r"\>", ">"],
        [r"\=\=", "=="],
        [r"\!\=", "!="],
        [r"\!", "!"],
        [r"\&\&", "&&"],
        [r"\|\|", "||"],
        [r"\=", "="]
    ]]


=======
    examples = "+-*/()=;<>{}[]."
    for example in examples:
        t = tokenize(example)[0]
        assert t["tag"] == example
        assert t["position"] == 0
        assert t["value"] == example
    examples = "==\t!=\t<=\t>=\t&&\t||\t!".split("\t")
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    for example in examples:
        t = tokenize(example)[0]
        assert t["tag"] == example
        assert t["position"] == 0
        assert t["value"] == example

<<<<<<< HEAD
def test_number_token():
=======
def test_number_tokens():
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    print("test number tokens")
    for s in ["1","11"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == int(s)
    for s in ["1.1","11.11","11.",".11"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == float(s)

def test_string_tokens():
    print("test string tokens")
<<<<<<< HEAD
    for s in ['"1"','"hello"', '""', '"test me"', '"123abd s"']:
=======
    for s in ['"1"','"abc"','""']:
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "string"
        assert t[0]["value"] == s[1:-1]

<<<<<<< HEAD
def test_boolean_tokens():
    print("test boolean tokens")
    for s in ["true","false"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "boolean"
        assert t[0]["value"] == (s == "true")

=======
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
def test_multiple_tokens():
    print("test multiple tokens")
    tokens = tokenize("1+2")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, {'tag': '+', 'position': 1, 'value': '+'}, {'tag': 'number', 'position': 2, 'value': 2}, {'tag': None, 'value': None, 'position': 3}]

def test_whitespace():
<<<<<<< HEAD
    print("test whitespace...")
=======
    print("test whitespace")
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    tokens = tokenize("1 + 2")
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, {'tag': '+', 'position': 2, 'value': '+'}, {'tag': 'number', 'position': 4, 'value': 2}, {'tag': None, 'value': None, 'position': 5}]

def test_keywords():
    print("test keywords...")
    for keyword in [
<<<<<<< HEAD
        "print",
        "if",
        "else",
        "while",
        "break",
        "continue",
=======
        "print","if","else","while","continue","break","return","assert"
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    ]:
        t = tokenize(keyword)
        assert len(t) == 2
        assert t[0]["tag"] == keyword, f"expected {keyword}, got {t[0]}"
        assert "value" not in t

def test_identifier_tokens():
    print("test identifier tokens...")
    for s in ["x", "y", "z", "alpha", "beta", "gamma"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "identifier"
        assert t[0]["value"] == s



def test_error():
    print("test error")
    try:
        t = tokenize("$1+2")
        assert False, "Should have raised an error for an invalid character."
    except Exception as e:
        assert "Syntax error" in str(e),f"Unexpected exception: {e}"

if __name__ == "__main__":
    test_simple_token()
<<<<<<< HEAD
    test_number_token()
    test_string_tokens()
    test_boolean_tokens()
=======
    test_number_tokens()
    test_string_tokens()
>>>>>>> 25260d73c604edb33a98fbc4651fc53d3c75fce4
    test_multiple_tokens()
    test_whitespace()
    test_keywords()
    test_identifier_tokens()
    test_error()