class Operation:
    def __init__(self, name):
        self.__name = name
        self.__sets = []

    def set_dst(self, dst):
        if dst:
            for s in self.__sets:
                s.set_dst(dst)
                s.set_dst_address(dst)

    def set_src(self, src):
        if src:
            for s in self.__sets:
                s.set_src(src)
                s.set_src_address(src)

    def set_aux(self, aux):
        if aux:
            for s in self.__sets:
                s.set_aux(aux)

    def add_set(self, s):
        self.__sets += [s]

    def get_sets(self):
        return self.__sets

    def __str__(self):
        string = ''
        for s in self.__sets:
            string += str(s) + '\n'
        return string
