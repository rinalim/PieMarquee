path = '"/home/user/RetroPie/roms/arcade/1941.zip"'

romname = path.replace('"','').split("/")[-1].split(".")[0]
print romname
