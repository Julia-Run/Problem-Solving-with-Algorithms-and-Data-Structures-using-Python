class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.performance_gate()  # 出错点1
        # print(self.output)  # for test
        return self.output


class TwoPinGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def get_pinA(self):
        if self.pinA is None:
            return int(input('Pin1:'))
        else:
            return self.pinA.get_from().get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input('Pin2:'))
        else:
            return self.pinB.get_from().get_output()

    def set_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(TwoPinGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate(self):
        a, b = self.get_pinA(), self.get_pinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(TwoPinGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate(self):
        a, b = self.get_pinA(), self.get_pinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class OnePinGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin_in = None

    def get_pin_in(self):
        if self.pin_in is None:
            return int(input('pin_in:'))
        else:
            return self.pin_in.get_from().get_output()

    def set_pin(self, source):
        if self.pin_in is None:
            self.pin_in = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class NotGate(OnePinGate):
    def __init__(self, n):
        super().__init__(n)

    def performance_gate(self):
        a = self.get_pin_in()
        if a == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromegate = fgate
        self.togate = tgate

        tgate.set_pin(self)

    def get_from(self):
        return self.fromegate

    def get_to(self):
        return self.togate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())


main()
