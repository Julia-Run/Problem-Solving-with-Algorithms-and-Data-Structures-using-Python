class Connector(object):
    # 关联ingate和outgate。如何关联？ 取得ingate的输出并将其设置outgate的输入。
    def __init__(self, ingate, outgate):
        self.fromgate = ingate
        self.togate = outgate

        outgate.set_pin(self)

    def get_value(self):
        return self.fromgate


class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        return self.gate_performance()


class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def set_pin(self, connector):
        # set和get，set是为了给self.pinA赋值（self.pinA=...）。get是为了调用这个self.pinA的值（return一个值）
        if self.pinA is None:
            # self.pinA = connector
            self.pinA = connector.get_value().get_output()
        else:
            if self.pinB is None:
                self.pinB = connector.get_value().get_output()
            else:
                raise RuntimeError('Too Many Input!')

    def get_pinA(self):
        if self.pinA is None:
            return int(input(self.get_label() + '--PinA(1 or 0):'))
        else:
            # return self.pinA.get_value().get_output()
            return self.pinA

    def get_pinB(self):
        if self.pinB is None:
            return int(input(self.get_label() + '--PinB(1 or 0):'))
        else:
            # return self.pinB.get_value().get_output()
            return self.pinB


class SingleGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin_in = None

    def set_pin(self, connector):
        if self.pin_in is None:
            # self.pin_in = connector
            self.pin_in = connector.get_value().get_output()
        else:
            raise RuntimeError('Too Many Input!')

    def get_pin_in(self):
        if self.pin_in is None:
            return int(input(self.get_label() + '--Pin_in(1 or 0):'))
        else:
            # return self.pin_in.get_value().get_output()
            return self.pin_in


class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def gate_performance(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def gate_performance(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(SingleGate):
    def __init__(self, n):
        super().__init__(n)

    def gate_performance(self):
        a = self.get_pin_in()
        if a == 1:
            return 0
        else:
            return 1


def test():
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())


test()
