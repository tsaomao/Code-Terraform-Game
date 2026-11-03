thermometer = get_component("thermometer")
transmitter = get_component("transmitter")

curr_temp = thermometer.get_value()

transmitter.connect("earth")

transmitter.transmit("current_temperature", curr_temp)
