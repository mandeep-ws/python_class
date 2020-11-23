guid = "65f67788-fb0e-4e89-ab00-083f39aeea35"

def guid_split(guid):
    guid = guid.split("-")
    x = guid[0][-2:]
    y = guid[1][-2:]
    z = guid[2][-2:]
    guid_new = [x+guid[0][:-2],y+guid[1][:-2],z+guid[2][:-2],guid[3],guid[4]]
    guid_new = "-".join([str(i) for i in guid_new])
    return guid_new
print(guid_split(guid))