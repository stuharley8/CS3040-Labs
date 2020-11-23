import antlr4
from antlr4.InputStream import InputStream
from antlr4.error.ErrorStrategy import BailErrorStrategy
from antlr4.error.Errors import ParseCancellationException
from complexLexer import complexLexer
from complexParser import complexParser
import sys

def main():
    filename = input('Enter a text file: ')
    file = open(filename, "r")
    text = file.read()
    text = text.replace(',', ' ,')
    input_stream = InputStream(text)
    
    lexer = complexLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = complexParser(stream)
    parser._errHandler = BailErrorStrategy()
    try:
        tree = parser.plans()
        print("Legal Input")
    except ParseCancellationException:
        print("Syntax error in input")

if __name__ == '__main__':
    main()