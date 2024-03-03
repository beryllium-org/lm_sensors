for i in ["sensors.lja", "sensors.py"]:
    shutil.copy(i, path.join(root, "bin", i))

shutil.copy("sensors.man", path.join(root, "usr/share/man", "sensors.man"))
