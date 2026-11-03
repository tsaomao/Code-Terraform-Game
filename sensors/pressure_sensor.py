press_sensor = get_component("pressure_sensor")

raw_value = press_sensor.get_value()

if (raw_value % 2 != 0):
    output = raw_value + 1
else:
    output = raw_value

press_sensor.stabilize(output)
