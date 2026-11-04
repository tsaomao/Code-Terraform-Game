arch = self.contract.archive

identified = {}
paired = []

for rw in range(arch.rows):
    for cl in range(arch.cols):
        word = arch.flip(rw, cl)

        if word in identified:
            r1, c1 = identified[word]
            paired.append([r1, c1, rw, cl])
        else:
            identified[word] = (rw, cl)

transmitter = get_component("transmitter")
transmitter.connect("earth")
transmitter.transmit(self.contract.id, paired)