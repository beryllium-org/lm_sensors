for pv[get_pid()]["filee"] in ["sensors.lja", "sensors.py"]:
    be.based.run("cp " + vr("filee") + " /bin/" + vr("filee"))

be.based.run("cp sensors.man /usr/share/man/sensors.man")

be.api.setvar("return", "0")
