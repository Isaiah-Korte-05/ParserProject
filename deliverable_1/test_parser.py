from antlr4 import *
from generated_output.project_part_1Lexer import project_part_1Lexer
from generated_output.project_part_1Parser import project_part_1Parser

def print_tree(tree, parser, indent=0):
    if tree is None:
        return

    if isinstance(tree, TerminalNode):
        print("  " * indent + f"{tree.getText()}")
    else:
        rule_idx = tree.getRuleIndex()
        rule_name = parser.ruleNames[rule_idx]
        print("  " * indent + f"[{rule_name}]")
        for i in range(tree.getChildCount()):
            print_tree(tree.getChild(i), parser, indent+  + 1)

def main():
    # Load test code file
    input_file = "project_deliverable_1.py"
    input_stream = FileStream(input_file, encoding='utf-8')
    
    # Set up the lexer and token stream
    lexer = project_part_1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Set up parser
    parser = project_part_1Parser(stream)
    
    # Call the start rule
    tree = parser.start()
    
    print("--- Formatted Parse Tree ---")
    print_tree(tree, parser)

if __name__ == '__main__':
    main()