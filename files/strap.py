for i in ["sensors.lja", "sensors.py"]:
    shutil.copyfile(i, path.join(root, "bin", i))

shutil.copyfile("sensors.man", path.join(root, "usr/share/man", "sensors.man"))
