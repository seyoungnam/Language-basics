class MyDoit7_6:
    def __init__(self, temperature = 0):
        self._temperature = temperature
    def to_value(self):
        return (self.temperature*1.8) + 32
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        self._temperature = value

if __name__ == '__main__':
    v=MyDoit7_6()
    for i in range(10,15):
        v.temperature=i
        print(str(v.to_value()))