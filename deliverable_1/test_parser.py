import sys
from antlr4 import *
from generated_output.project_part_1Lexer import project_part_1Lexer
from generated_output.project_part_1Parser import project_part_1Parser

def main():
    # Load your test code file
    input_file = "project_deliverable_1.py"
    input_stream = FileStream(input_file, encoding='utf-8')
    
    # Set up the lexer and token stream
    lexer = project_part_1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Set up the parser
    parser = project_part_1Parser(stream)
    
    # Call the start rule defined in project_part_1.g4
    tree = parser.start()
    
    # Print the textual representation of the parse tree
    print("--- Parse Tree (Text) ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()