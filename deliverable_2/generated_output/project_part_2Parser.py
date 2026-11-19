# Generated from deliverable_2/project_part_2.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,5,0,25,8,0,10,0,12,0,28,
        9,0,1,0,1,0,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,5,3,5,50,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,3,6,64,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,82,8,6,10,6,12,6,85,9,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,96,8,7,10,7,12,7,99,9,7,1,7,1,7,1,
        7,3,7,104,8,7,1,8,1,8,4,8,108,8,8,11,8,12,8,109,1,8,5,8,113,8,8,
        10,8,12,8,116,9,8,1,9,1,9,1,9,1,9,5,9,122,8,9,10,9,12,9,125,9,9,
        3,9,127,8,9,1,9,1,9,1,9,0,1,12,10,0,2,4,6,8,10,12,14,16,18,0,4,1,
        0,1,5,1,0,6,11,1,0,16,18,1,0,14,15,144,0,26,1,0,0,0,2,33,1,0,0,0,
        4,35,1,0,0,0,6,39,1,0,0,0,8,41,1,0,0,0,10,49,1,0,0,0,12,63,1,0,0,
        0,14,86,1,0,0,0,16,107,1,0,0,0,18,117,1,0,0,0,20,25,3,2,1,0,21,22,
        5,34,0,0,22,25,3,2,1,0,23,25,5,35,0,0,24,20,1,0,0,0,24,21,1,0,0,
        0,24,23,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,
        1,0,0,0,28,26,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,34,3,4,2,0,32,
        34,3,14,7,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,5,30,
        0,0,36,37,3,6,3,0,37,38,3,12,6,0,38,5,1,0,0,0,39,40,7,0,0,0,40,7,
        1,0,0,0,41,42,7,1,0,0,42,9,1,0,0,0,43,50,3,18,9,0,44,50,5,31,0,0,
        45,50,5,32,0,0,46,50,5,33,0,0,47,50,5,29,0,0,48,50,5,30,0,0,49,43,
        1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,
        49,48,1,0,0,0,50,11,1,0,0,0,51,52,6,6,-1,0,52,53,5,12,0,0,53,54,
        3,12,6,0,54,55,5,13,0,0,55,64,1,0,0,0,56,57,5,14,0,0,57,64,3,12,
        6,9,58,59,5,15,0,0,59,64,3,12,6,8,60,61,5,28,0,0,61,64,3,12,6,7,
        62,64,3,10,5,0,63,51,1,0,0,0,63,56,1,0,0,0,63,58,1,0,0,0,63,60,1,
        0,0,0,63,62,1,0,0,0,64,83,1,0,0,0,65,66,10,6,0,0,66,67,5,26,0,0,
        67,82,3,12,6,7,68,69,10,5,0,0,69,70,5,27,0,0,70,82,3,12,6,6,71,72,
        10,4,0,0,72,73,3,8,4,0,73,74,3,12,6,5,74,82,1,0,0,0,75,76,10,3,0,
        0,76,77,7,2,0,0,77,82,3,12,6,4,78,79,10,2,0,0,79,80,7,3,0,0,80,82,
        3,12,6,3,81,65,1,0,0,0,81,68,1,0,0,0,81,71,1,0,0,0,81,75,1,0,0,0,
        81,78,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,13,1,
        0,0,0,85,83,1,0,0,0,86,87,5,23,0,0,87,88,3,12,6,0,88,89,5,19,0,0,
        89,97,3,16,8,0,90,91,5,24,0,0,91,92,3,12,6,0,92,93,5,19,0,0,93,94,
        3,16,8,0,94,96,1,0,0,0,95,90,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,
        97,98,1,0,0,0,98,103,1,0,0,0,99,97,1,0,0,0,100,101,5,25,0,0,101,
        102,5,19,0,0,102,104,3,16,8,0,103,100,1,0,0,0,103,104,1,0,0,0,104,
        15,1,0,0,0,105,106,5,34,0,0,106,108,3,2,1,0,107,105,1,0,0,0,108,
        109,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,114,1,0,0,0,111,
        113,5,35,0,0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,
        115,1,0,0,0,115,17,1,0,0,0,116,114,1,0,0,0,117,126,5,20,0,0,118,
        123,3,12,6,0,119,120,5,21,0,0,120,122,3,12,6,0,121,119,1,0,0,0,122,
        125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,127,1,0,0,0,125,
        123,1,0,0,0,126,118,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,
        129,5,22,0,0,129,19,1,0,0,0,13,24,26,33,49,63,81,83,97,103,109,114,
        123,126
    ]

class project_part_2Parser ( Parser ):

    grammarFileName = "project_part_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'('", 
                     "')'", "'-'", "'+'", "'*'", "'/'", "'%'", "':'", "'['", 
                     "','", "']'", "'if'", "'elif'", "'else'", "'and'", 
                     "'or'", "'not'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELIF", 
                      "ELSE", "AND", "OR", "NOT", "BOOL", "ID", "STRING", 
                      "FLOAT", "INT", "INDENT", "NEWLINE", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assignment_operator = 3
    RULE_comparison_operator = 4
    RULE_data_type = 5
    RULE_expression = 6
    RULE_if_statement = 7
    RULE_block = 8
    RULE_array = 9

    ruleNames =  [ "start", "statement", "assignment", "assignment_operator", 
                   "comparison_operator", "data_type", "expression", "if_statement", 
                   "block", "array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    IF=23
    ELIF=24
    ELSE=25
    AND=26
    OR=27
    NOT=28
    BOOL=29
    ID=30
    STRING=31
    FLOAT=32
    INT=33
    INDENT=34
    NEWLINE=35
    WS=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(project_part_2Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.StatementContext,i)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_2Parser.INDENT)
            else:
                return self.getToken(project_part_2Parser.INDENT, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_2Parser.NEWLINE)
            else:
                return self.getToken(project_part_2Parser.NEWLINE, i)

        def getRuleIndex(self):
            return project_part_2Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = project_part_2Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 52621737984) != 0):
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23, 30]:
                    self.state = 20
                    self.statement()
                    pass
                elif token in [34]:
                    self.state = 21
                    self.match(project_part_2Parser.INDENT)
                    self.state = 22
                    self.statement()
                    pass
                elif token in [35]:
                    self.state = 23
                    self.match(project_part_2Parser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(project_part_2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(project_part_2Parser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(project_part_2Parser.If_statementContext,0)


        def getRuleIndex(self):
            return project_part_2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = project_part_2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.assignment()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.if_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(project_part_2Parser.ID, 0)

        def assignment_operator(self):
            return self.getTypedRuleContext(project_part_2Parser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(project_part_2Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return project_part_2Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = project_part_2Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(project_part_2Parser.ID)
            self.state = 36
            self.assignment_operator()
            self.state = 37
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return project_part_2Parser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = project_part_2Parser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return project_part_2Parser.RULE_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)




    def comparison_operator(self):

        localctx = project_part_2Parser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(project_part_2Parser.ArrayContext,0)


        def STRING(self):
            return self.getToken(project_part_2Parser.STRING, 0)

        def FLOAT(self):
            return self.getToken(project_part_2Parser.FLOAT, 0)

        def INT(self):
            return self.getToken(project_part_2Parser.INT, 0)

        def BOOL(self):
            return self.getToken(project_part_2Parser.BOOL, 0)

        def ID(self):
            return self.getToken(project_part_2Parser.ID, 0)

        def getRuleIndex(self):
            return project_part_2Parser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)




    def data_type(self):

        localctx = project_part_2Parser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_data_type)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.array()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(project_part_2Parser.STRING)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(project_part_2Parser.FLOAT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(project_part_2Parser.INT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.match(project_part_2Parser.BOOL)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(project_part_2Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExpressionContext
            self.right = None # ExpressionContext
            self.compOp = None # Comparison_operatorContext
            self.mulOp = None # Token
            self.addOp = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.ExpressionContext,i)


        def NOT(self):
            return self.getToken(project_part_2Parser.NOT, 0)

        def data_type(self):
            return self.getTypedRuleContext(project_part_2Parser.Data_typeContext,0)


        def AND(self):
            return self.getToken(project_part_2Parser.AND, 0)

        def OR(self):
            return self.getToken(project_part_2Parser.OR, 0)

        def comparison_operator(self):
            return self.getTypedRuleContext(project_part_2Parser.Comparison_operatorContext,0)


        def getRuleIndex(self):
            return project_part_2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = project_part_2Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 52
                self.match(project_part_2Parser.T__11)
                self.state = 53
                self.expression(0)
                self.state = 54
                self.match(project_part_2Parser.T__12)
                pass
            elif token in [14]:
                self.state = 56
                self.match(project_part_2Parser.T__13)
                self.state = 57
                self.expression(9)
                pass
            elif token in [15]:
                self.state = 58
                self.match(project_part_2Parser.T__14)
                self.state = 59
                self.expression(8)
                pass
            elif token in [28]:
                self.state = 60
                self.match(project_part_2Parser.NOT)
                self.state = 61
                self.expression(7)
                pass
            elif token in [20, 29, 30, 31, 32, 33]:
                self.state = 62
                self.data_type()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = project_part_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 66
                        self.match(project_part_2Parser.AND)
                        self.state = 67
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = project_part_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 69
                        self.match(project_part_2Parser.OR)
                        self.state = 70
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = project_part_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 71
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 72
                        localctx.compOp = self.comparison_operator()
                        self.state = 73
                        localctx.right = self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = project_part_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        localctx.mulOp = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                            localctx.mulOp = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = project_part_2Parser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 78
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 79
                        localctx.addOp = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.addOp = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        localctx.right = self.expression(3)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(project_part_2Parser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.BlockContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.BlockContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_2Parser.ELIF)
            else:
                return self.getToken(project_part_2Parser.ELIF, i)

        def ELSE(self):
            return self.getToken(project_part_2Parser.ELSE, 0)

        def getRuleIndex(self):
            return project_part_2Parser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = project_part_2Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(project_part_2Parser.IF)
            self.state = 87
            self.expression(0)
            self.state = 88
            self.match(project_part_2Parser.T__18)
            self.state = 89
            self.block()
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 90
                    self.match(project_part_2Parser.ELIF)
                    self.state = 91
                    self.expression(0)
                    self.state = 92
                    self.match(project_part_2Parser.T__18)
                    self.state = 93
                    self.block() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(project_part_2Parser.ELSE)
                self.state = 101
                self.match(project_part_2Parser.T__18)
                self.state = 102
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_2Parser.INDENT)
            else:
                return self.getToken(project_part_2Parser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_2Parser.NEWLINE)
            else:
                return self.getToken(project_part_2Parser.NEWLINE, i)

        def getRuleIndex(self):
            return project_part_2Parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = project_part_2Parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 105
                    self.match(project_part_2Parser.INDENT)
                    self.state = 106
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 109 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 111
                    self.match(project_part_2Parser.NEWLINE) 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(project_part_2Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return project_part_2Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = project_part_2Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(project_part_2Parser.T__19)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16912535552) != 0):
                self.state = 118
                self.expression(0)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 119
                    self.match(project_part_2Parser.T__20)
                    self.state = 120
                    self.expression(0)
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 128
            self.match(project_part_2Parser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




