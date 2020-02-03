from gen.SlpVisitor import SlpVisitor
from gen.SlpParser import SlpParser


class SlpStringVisitor(SlpVisitor):

    def __init__(self):
        self._string = ""

    def emit(self, string):
        self._string += string + " "

    @property
    def string(self):
        return self._string

    def visitNum(self, ctx: SlpParser.NumContext):
        self.emit(ctx.NUM().getText())

    def visitId(self, ctx: SlpParser.IdContext):
        self.emit(ctx.ID().getText())

    def visitOp(self, ctx: SlpParser.OpContext):
        self.emit(ctx.getText())

    def visitAssign_stm(self, ctx: SlpParser.Assign_stmContext):
        self.emit(ctx.ID().getText() + " =")
        ctx.exp().accept(self)

    def visitCompound_stm(self, ctx: SlpParser.Compound_stmContext):
        ctx.stm(0).accept(self)
        self.emit(";")
        ctx.stm(1).accept(self)

    def visitPrint_stm(self, ctx: SlpParser.Print_stmContext):
        self.emit("print (")
        ctx.exp_list().accept(self)
        self.emit(")")

    def visitExp_list_not_final(self, ctx: SlpParser.Exp_list_not_finalContext):
        ctx.exp().accept(self)
        self.emit(", ")
        ctx.exp_list().accept(self)

    def visitEseq(self, ctx: SlpParser.EseqContext):
        self.emit("(")
        ctx.stm().accept(self)
        self.emit(",")
        ctx.exp().accept(self)
        self.emit(")")
