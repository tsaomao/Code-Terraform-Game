oxy_sensor = get_component("oxygen_sensor")

raw_read = oxy_sensor.get_value()

output = raw_read * 100

oxy_sensor.calibrate(output)
