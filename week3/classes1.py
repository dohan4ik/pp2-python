class Methods:
    def __init__(self, a):
        self.get_inf(a)
        self.pri_inf()

    def get_inf(self, a):
        self.a = a
    def pri_inf(self):
        print(self.a.upper())
res = Methods(input())