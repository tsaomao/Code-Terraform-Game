lock = self.contract.lock

input_code = [0] * lock.tumblers
identified = [False] * lock.tumblers

for val in range(lock.range):
    guess = lock.intercept([val] * lock.tumblers)

    for i in range(lock.tumblers):
        if guess[i]:
            input_code[i] = val
            identified[i] = True

    if all(identified):
        break

transmitter = get_component("transmitter")
transmitter.connect("earth")
transmitter.transmit(self.contract.id, input_code)