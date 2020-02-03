from antlr4 import InputStream, CommonTokenStream
from gen.SlpLexer import SlpLexer
from gen.SlpParser import SlpParser
from string_visitor import SlpStringVisitor
from ast_visitor import AstVisitor


def output_ast():
    while True:
        print("CMD?")
        input_stream = InputStream(input())
        lexer = SlpLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SlpParser(stream)
        tree = parser.stm()

        visitor = SlpStringVisitor()
        visitor.visit(tree)
        print(visitor.string)

        ast_visitor = AstVisitor()
        result = ast_visitor.visit(tree)
        print(result)


if __name__ == '__main__':
    output_ast()
