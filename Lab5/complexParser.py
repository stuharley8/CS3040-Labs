# Generated from complex.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\23")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3\3")
        buf.write("\3\6\3\34\n\3\r\3\16\3\35\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4*\n\4\3\5\3\5\3\5\3\5\7\5\60\n\5\f\5\16")
        buf.write("\5\63\13\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7C\n\7\3\b\3\b\3\b\3\b\7\bI\n\b\f\b\16")
        buf.write("\bL\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f")
        buf.write("\16\20\2\2Q\2\23\3\2\2\2\4\31\3\2\2\2\6)\3\2\2\2\b+\3")
        buf.write("\2\2\2\n\66\3\2\2\2\fB\3\2\2\2\16D\3\2\2\2\20O\3\2\2\2")
        buf.write("\22\24\5\f\7\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\27\3\2\2\2\27\30\5\4\3\2\30\3\3\2")
        buf.write("\2\2\31\33\7\5\2\2\32\34\5\6\4\2\33\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37 \7")
        buf.write("\6\2\2 !\7\3\2\2!\"\7\7\2\2\"#\7\b\2\2#*\5\b\5\2$%\7\6")
        buf.write("\2\2%&\7\3\2\2&\'\7\7\2\2\'(\7\t\2\2(*\5\b\5\2)\37\3\2")
        buf.write("\2\2)$\3\2\2\2*\7\3\2\2\2+,\7\n\2\2,\61\5\n\6\2-.\7\f")
        buf.write("\2\2.\60\5\n\6\2/-\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\13\2\2")
        buf.write("\65\t\3\2\2\2\66\67\7\3\2\2\67\13\3\2\2\289\7\b\2\29:")
        buf.write("\7\3\2\2:;\7\r\2\2;<\7\16\2\2<C\5\16\b\2=>\7\b\2\2>?\7")
        buf.write("\3\2\2?@\7\r\2\2@A\7\17\2\2AC\5\16\b\2B8\3\2\2\2B=\3\2")
        buf.write("\2\2C\r\3\2\2\2DE\7\20\2\2EJ\5\20\t\2FG\7\f\2\2GI\5\20")
        buf.write("\t\2HF\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2")
        buf.write("LJ\3\2\2\2MN\7\21\2\2N\17\3\2\2\2OP\7\4\2\2PQ\7\22\2\2")
        buf.write("QR\7\4\2\2R\21\3\2\2\2\b\25\35)\61BJ")
        return buf.getvalue()


class complexParser ( Parser ):

    grammarFileName = "complex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'complex'", 
                     "'building'", "'with'", "'floor'", "'floors'", "'{'", 
                     "'}'", "','", "'has'", "'room'", "'rooms'", "'['", 
                     "']'", "'by'" ]

    symbolicNames = [ "<INVALID>", "NAME", "NUMBER", "COMP", "BUILDING", 
                      "WITH", "FLOOR", "FLOORS", "LBRACKET", "RBRACKET", 
                      "COMMA", "HAS", "ROOM", "ROOMS", "LSBRACKET", "RSBRACKET", 
                      "BY", "WS" ]

    RULE_plans = 0
    RULE_comp = 1
    RULE_building = 2
    RULE_floor_list = 3
    RULE_floor_reference = 4
    RULE_floor = 5
    RULE_room_list = 6
    RULE_room = 7

    ruleNames =  [ "plans", "comp", "building", "floor_list", "floor_reference", 
                   "floor", "room_list", "room" ]

    EOF = Token.EOF
    NAME=1
    NUMBER=2
    COMP=3
    BUILDING=4
    WITH=5
    FLOOR=6
    FLOORS=7
    LBRACKET=8
    RBRACKET=9
    COMMA=10
    HAS=11
    ROOM=12
    ROOMS=13
    LSBRACKET=14
    RSBRACKET=15
    BY=16
    WS=17

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class PlansContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(complexParser.CompContext,0)


        def floor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(complexParser.FloorContext)
            else:
                return self.getTypedRuleContext(complexParser.FloorContext,i)


        def getRuleIndex(self):
            return complexParser.RULE_plans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlans" ):
                listener.enterPlans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlans" ):
                listener.exitPlans(self)




    def plans(self):

        localctx = complexParser.PlansContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_plans)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.floor()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==complexParser.FLOOR):
                    break

            self.state = 21
            self.comp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMP(self):
            return self.getToken(complexParser.COMP, 0)

        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(complexParser.BuildingContext)
            else:
                return self.getTypedRuleContext(complexParser.BuildingContext,i)


        def getRuleIndex(self):
            return complexParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)




    def comp(self):

        localctx = complexParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(complexParser.COMP)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.building()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==complexParser.BUILDING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BUILDING(self):
            return self.getToken(complexParser.BUILDING, 0)

        def NAME(self):
            return self.getToken(complexParser.NAME, 0)

        def WITH(self):
            return self.getToken(complexParser.WITH, 0)

        def FLOOR(self):
            return self.getToken(complexParser.FLOOR, 0)

        def floor_list(self):
            return self.getTypedRuleContext(complexParser.Floor_listContext,0)


        def FLOORS(self):
            return self.getToken(complexParser.FLOORS, 0)

        def getRuleIndex(self):
            return complexParser.RULE_building

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilding" ):
                listener.enterBuilding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilding" ):
                listener.exitBuilding(self)




    def building(self):

        localctx = complexParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_building)
        try:
            self.state = 39
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(complexParser.BUILDING)
                self.state = 30
                self.match(complexParser.NAME)
                self.state = 31
                self.match(complexParser.WITH)
                self.state = 32
                self.match(complexParser.FLOOR)
                self.state = 33
                self.floor_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(complexParser.BUILDING)
                self.state = 35
                self.match(complexParser.NAME)
                self.state = 36
                self.match(complexParser.WITH)
                self.state = 37
                self.match(complexParser.FLOORS)
                self.state = 38
                self.floor_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Floor_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(complexParser.LBRACKET, 0)

        def floor_reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(complexParser.Floor_referenceContext)
            else:
                return self.getTypedRuleContext(complexParser.Floor_referenceContext,i)


        def RBRACKET(self):
            return self.getToken(complexParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(complexParser.COMMA)
            else:
                return self.getToken(complexParser.COMMA, i)

        def getRuleIndex(self):
            return complexParser.RULE_floor_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_list" ):
                listener.enterFloor_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_list" ):
                listener.exitFloor_list(self)




    def floor_list(self):

        localctx = complexParser.Floor_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_floor_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(complexParser.LBRACKET)
            self.state = 42
            self.floor_reference()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==complexParser.COMMA:
                self.state = 43
                self.match(complexParser.COMMA)
                self.state = 44
                self.floor_reference()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(complexParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Floor_referenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(complexParser.NAME, 0)

        def getRuleIndex(self):
            return complexParser.RULE_floor_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_reference" ):
                listener.enterFloor_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_reference" ):
                listener.exitFloor_reference(self)




    def floor_reference(self):

        localctx = complexParser.Floor_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_floor_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(complexParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOOR(self):
            return self.getToken(complexParser.FLOOR, 0)

        def NAME(self):
            return self.getToken(complexParser.NAME, 0)

        def HAS(self):
            return self.getToken(complexParser.HAS, 0)

        def ROOM(self):
            return self.getToken(complexParser.ROOM, 0)

        def room_list(self):
            return self.getTypedRuleContext(complexParser.Room_listContext,0)


        def ROOMS(self):
            return self.getToken(complexParser.ROOMS, 0)

        def getRuleIndex(self):
            return complexParser.RULE_floor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor" ):
                listener.enterFloor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor" ):
                listener.exitFloor(self)




    def floor(self):

        localctx = complexParser.FloorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_floor)
        try:
            self.state = 64
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(complexParser.FLOOR)
                self.state = 55
                self.match(complexParser.NAME)
                self.state = 56
                self.match(complexParser.HAS)
                self.state = 57
                self.match(complexParser.ROOM)
                self.state = 58
                self.room_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(complexParser.FLOOR)
                self.state = 60
                self.match(complexParser.NAME)
                self.state = 61
                self.match(complexParser.HAS)
                self.state = 62
                self.match(complexParser.ROOMS)
                self.state = 63
                self.room_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Room_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSBRACKET(self):
            return self.getToken(complexParser.LSBRACKET, 0)

        def room(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(complexParser.RoomContext)
            else:
                return self.getTypedRuleContext(complexParser.RoomContext,i)


        def RSBRACKET(self):
            return self.getToken(complexParser.RSBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(complexParser.COMMA)
            else:
                return self.getToken(complexParser.COMMA, i)

        def getRuleIndex(self):
            return complexParser.RULE_room_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom_list" ):
                listener.enterRoom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom_list" ):
                listener.exitRoom_list(self)




    def room_list(self):

        localctx = complexParser.Room_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_room_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(complexParser.LSBRACKET)
            self.state = 67
            self.room()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==complexParser.COMMA:
                self.state = 68
                self.match(complexParser.COMMA)
                self.state = 69
                self.room()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(complexParser.RSBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RoomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(complexParser.NUMBER)
            else:
                return self.getToken(complexParser.NUMBER, i)

        def BY(self):
            return self.getToken(complexParser.BY, 0)

        def getRuleIndex(self):
            return complexParser.RULE_room

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom" ):
                listener.enterRoom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom" ):
                listener.exitRoom(self)




    def room(self):

        localctx = complexParser.RoomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_room)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(complexParser.NUMBER)
            self.state = 78
            self.match(complexParser.BY)
            self.state = 79
            self.match(complexParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





