contract = self.contract

earth = set(contract.earth_ref)

return_list = [
    item
    for item in contract.samples
    if item not in earth
]

transmitter = get_component("transmitter")
transmitter.connect("earth")
transmitter.transmit(contract.id, return_list)