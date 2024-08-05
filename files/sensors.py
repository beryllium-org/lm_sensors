rename_process("sensors")
vr("no", True)
pass
vr("temp", cpu.temperature)
for _ in range(10):
    pass

if vr("temp") is not None:
    vr("no", False)
    term.write(
        "cpu_thermal\nAdapter: Cpu device\ntemp1: +" + str(vr("temp"))[:5] + "°C\n"
    )

if "temp" in be.devices.keys():
    vr("no", False)
    for pv[get_pid()]["i"] in be.devices["temp"].keys():
        term.write(vr("i").name + "\nAdapter: kernel\ntemp1:" + str(vr("i").temperature) + "°C\n")

if cpu.voltage is not None:
    vr("no", False)
    term.write("cpu_voltage\nAdapter: Cpu device\ninV: " + str(cpu.voltage) + "V\n")

if "bat" in be.devices.keys():
    vr("no", False)
    for pv[get_pid()]["i"] in be.devices["bat"].keys():
        vr("cdev", be.devices["bat"][vr("i")])
        term.write("bat" + str(vr("i")))
        term.write("Adapter: kernel")
        term.write("inV: " + str(vr("cdev").voltage) + "V")
        term.write("Charge: " + str(vr("cdev").percentage) + "%")
        if hasattr(vr("cdev"), "status"):
            term.write("Status: " + vr("cdev").status)
        if hasattr(vr("cdev"), "charging_enabled"):
            term.write("Charging enabled: " + str(vr("cdev").charging_enabled))
        term.write()

if vr("no"):
    term.write("No sensors detected!")
