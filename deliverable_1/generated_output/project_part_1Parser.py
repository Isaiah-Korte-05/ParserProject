# Generated from project_part_1.g4 by ANTLR 4.13.2
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
        4,1,20,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,
        0,12,0,14,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,29,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,
        1,3,1,3,1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,3,3,51,8,3,1,3,1,3,1,
        3,0,1,4,4,0,2,4,6,0,3,1,0,1,5,1,0,6,8,1,0,9,10,61,0,12,1,0,0,0,2,
        17,1,0,0,0,4,28,1,0,0,0,6,41,1,0,0,0,8,11,3,2,1,0,9,11,5,19,0,0,
        10,8,1,0,0,0,10,9,1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,
        0,0,13,15,1,0,0,0,14,12,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,
        5,15,0,0,18,19,7,0,0,0,19,20,3,4,2,0,20,3,1,0,0,0,21,22,6,2,-1,0,
        22,29,3,6,3,0,23,29,5,16,0,0,24,29,5,17,0,0,25,29,5,18,0,0,26,29,
        5,14,0,0,27,29,5,15,0,0,28,21,1,0,0,0,28,23,1,0,0,0,28,24,1,0,0,
        0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,38,1,0,0,0,30,31,
        10,7,0,0,31,32,7,1,0,0,32,37,3,4,2,8,33,34,10,6,0,0,34,35,7,2,0,
        0,35,37,3,4,2,7,36,30,1,0,0,0,36,33,1,0,0,0,37,40,1,0,0,0,38,36,
        1,0,0,0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,50,5,11,0,0,
        42,47,3,4,2,0,43,44,5,12,0,0,44,46,3,4,2,0,45,43,1,0,0,0,46,49,1,
        0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,50,
        42,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,5,13,0,0,53,7,1,0,0,
        0,7,10,12,28,36,38,47,50
    ]

class project_part_1Parser ( Parser ):

    grammarFileName = "project_part_1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+='", "'-='", "'*='", "'/='", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "ID", "STRING", 
                      "FLOAT", "INT", "NEWLINE", "WS" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_array = 3

    ruleNames =  [ "start", "statement", "expression", "array" ]

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
    BOOL=14
    ID=15
    STRING=16
    FLOAT=17
    INT=18
    NEWLINE=19
    WS=20

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
            return self.getToken(project_part_1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(project_part_1Parser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(project_part_1Parser.NEWLINE)
            else:
                return self.getToken(project_part_1Parser.NEWLINE, i)

        def getRuleIndex(self):
            return project_part_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = project_part_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==19:
                self.state = 10
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15]:
                    self.state = 8
                    self.statement()
                    pass
                elif token in [19]:
                    self.state = 9
                    self.match(project_part_1Parser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self.match(project_part_1Parser.EOF)
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

        def ID(self):
            return self.getToken(project_part_1Parser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(project_part_1Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return project_part_1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = project_part_1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(project_part_1Parser.ID)
            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            self.expression(0)
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

        def array(self):
            return self.getTypedRuleContext(project_part_1Parser.ArrayContext,0)


        def STRING(self):
            return self.getToken(project_part_1Parser.STRING, 0)

        def FLOAT(self):
            return self.getToken(project_part_1Parser.FLOAT, 0)

        def INT(self):
            return self.getToken(project_part_1Parser.INT, 0)

        def BOOL(self):
            return self.getToken(project_part_1Parser.BOOL, 0)

        def ID(self):
            return self.getToken(project_part_1Parser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(project_part_1Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return project_part_1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = project_part_1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 22
                self.array()
                pass
            elif token in [16]:
                self.state = 23
                self.match(project_part_1Parser.STRING)
                pass
            elif token in [17]:
                self.state = 24
                self.match(project_part_1Parser.FLOAT)
                pass
            elif token in [18]:
                self.state = 25
                self.match(project_part_1Parser.INT)
                pass
            elif token in [14]:
                self.state = 26
                self.match(project_part_1Parser.BOOL)
                pass
            elif token in [15]:
                self.state = 27
                self.match(project_part_1Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = project_part_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = project_part_1Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 34
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        self.expression(7)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(project_part_1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(project_part_1Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return project_part_1Parser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = project_part_1Parser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(project_part_1Parser.T__10)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 509952) != 0):
                self.state = 42
                self.expression(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 43
                    self.match(project_part_1Parser.T__11)
                    self.state = 44
                    self.expression(0)
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 52
            self.match(project_part_1Parser.T__12)
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
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




