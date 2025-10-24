from antlr4 import *
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .MiniLangVisitor import MiniLangVisitor

class EvalVisitor(MiniLangVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        return value

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            return self.memory.get(name, 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right
        elif ctx.expr(0):
            return self.visit(ctx.expr(0))
        return 0

    def visitProgram(self, ctx):
        results = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                results.append(result)
        return results

def ejecutar_codigo(codigo):
    input_stream = InputStream(codigo)
    lexer = MiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniLangParser(stream)
    tree = parser.program()
    visitor = EvalVisitor()
    resultados = visitor.visit(tree)
    return resultados, visitor.memory

#comando para generar los archivo .py 
#java -cp antlr-4.13.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 MiniLang.g4

#para que quite los errores cercanos 
#python manage.py migrate

#instalar ANTRL4 para python
#pip install antlr4-python3-runtime

#Instala migraciones necesarias 
#python manage.py migrate

#para correrlo en mi localhost 
#python runserver_auto.py 
#y abre el local host y la ip 

#Y luego para abrir en el  navegador
#http://10.161.169.123:8000/  (verificar porque cambia la ip con cada red)



