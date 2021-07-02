import pyads

# create some constants for connection

CLIENT_NETID = "192.168.1.10.1.1"
CLIENT_IP = "192.168.1.10"
TARGET_IP = "192.168.1.11"
TARGET_USERNAME = "Administrator"
TARGET_PASSWORD = "1"
ROUTE_NAME = "plc1"

# add a new route to the target plc
pyads.add_route_to_plc(
    amsNET_ID, CLIENT_IP, TARGET_IP, TARGET_USERNAME, TARGET_PASSWORD,
    route_name=ROUTE_NAME
)

# connect to plc and open connection
# route is added automatically to client on Linux, on Windows use the TwinCAT router
#plc = pyads.Connection(CLIENT_NETID, pyads.PORT_SPS1)
plc = pyads.Connection(CLIENT_NETID, 851)

plc.open()

# check the connection state
#plc.read_state()

# read int value by name
a = plc.read_by_name("GVL.int_val", pyads.PLCTYPE_INT)
print(a)

# write int value by name
#plc.write_by_name("GVL.real_val", 42.0)

# create a symbol that automatically updates to the plc value
#real_val = plc.get_symbol("GVL.real_val", auto_update=True)
#print(real_val.value)

#real_val.value = 5.0
#print(plc.read_by_name("GVL.real_val"))

# close connection
plc.close()
