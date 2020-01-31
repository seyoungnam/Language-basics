class Address:
    def allPrn(self, name, addr, tel):
        self.name = name
        self.addr = addr
        self.tel = tel
        print(self.name, self.addr, self.tel)

if __name__ == '__main__':
    addr01 = Address()
    addr01.allPrn("Dominica", "Seoul", "010-111-1111")

    addr02 = Address()
    addr02.allPrn("Dominico", "Busan", "010-222-2222")
