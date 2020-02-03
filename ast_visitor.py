from gen.SlpParser import SlpParser
from gen.SlpVisitor import SlpVisitor
from ast import bin_op_exp, int_exp, id_exp, eseq_exp, print_stm, assign_stm, compound_stm


class AstVisitor(SlpVisitor):
    def __init__(self):
        self._exp_list_stack = []

    def visitPrint_stm(self, ctx: SlpParser.Print_stmContext):
        self._exp_list_stack.append([])
        ctx.exp_list().accept(self)
        return print_stm.PrintStm(self._exp_list_stack.pop())

    def visitCompound_stm(self, ctx: SlpParser.Compound_stmContext):
        return compound_stm.CompoundStm(ctx.stm(0).accept(self), ctx.stm(1).accept(self))

    def visitAssign_stm(self, ctx: SlpParser.Assign_stmContext):
        return assign_stm.AssignStm(ctx.ID().getText(), ctx.exp().accept(self))

    def visitEseq(self, ctx: SlpParser.EseqContext):
        return eseq_exp.EseqExp(ctx.stm().accept(self), ctx.exp().accept(self))

    def visitNum(self, ctx: SlpParser.NumContext):
        return int_exp.IntExp(int(ctx.getText()))

    def visitId(self, ctx: SlpParser.IdContext):
        return id_exp.IdExp(ctx.ID().getText())

    def visitBin_op(self, ctx: SlpParser.Bin_opContext):
        return bin_op_exp.BinOpExp(ctx.exp(0).accept(self), ctx.op().getText(), right = ctx.exp(1).accept(self))

    def visitExp_list_not_final(self, ctx: SlpParser.Exp_list_not_finalContext):
        self._exp_list_stack[-1].append(ctx.exp().accept(self))

        return ctx.exp_list().accept(self)

    def visitExp_list_final(self, ctx: SlpParser.Exp_list_finalContext):
        self._exp_list_stack[-1].append(ctx.exp().accept(self))
        return self._exp_list_stack[-1]
