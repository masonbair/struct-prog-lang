from tokenizer import tokenize

"""
    factor = <number> | <identifier> | "{" expression "}"
    term = factor { "*"|"/" factor }
    expression = term { "+"|"-" term }
    statement = <print> expression | expression
"""

def parse_factor(tokens):
    """
        factor = <number> | <identifier> | "{" expression "}"
    """
    token = tokens[0]
    if token["tag"] == "number":
        return {
            "tag": "number",
            "value": token["value"],
        }, tokens[1:]
    # if token["tag"] == "identifier": Not implementing identifier as they represent something and we are not at that stage yet

    if token["tag"] == "(": 
        ast, tokens = parse_expression(tokens[1:])
        assert token[0]["tag"] == ")"
        return ast, tokens[1:]
    raise Exception(f"Unexpected token '{token['tag']}")

def parse_terms(tokens):
    node, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_factor(tokens[1:])
        node = {"tag": tag, "left": node, "right":right_node}
    
    return node, tokens

def parse_expression(tokens):
    return parse_factor(tokens)

def parse_statement(tokens):

    return ast, tokens

# def parse(tokens):


#     return ast

# def test_parse():
#     t = tokenize("1")
#     ast = parse(t)
#     assert ast == {

#     }