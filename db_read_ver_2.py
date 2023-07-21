# //=============================================================================
# //Radosław Tecmer)
# //(c)Copyright (2023) free of copyright
# //-----------------------------------------------------------------------------
# //The program allows you to read integer and float data from
# //the Simatic S7 controller data block
# //-----------------------------------------------------------------------------
# //contact:
# //https://github.com/remceTkedaR
# //radek69tecmer@gmail.com
# //=============================================================================

import snap7
import struct

client = snap7.client.Client()
client.connect('192.168.3.211', 0, 1)


# function reading real

def data_block_read(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!f", db_val[:4])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = float('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.4f' % result
    return my_str_value


# function reading int

def data_block_read_int(db_number, inst_number, data):
    db_val = client.db_read(db_number, inst_number, data)
    value_struct = struct.iter_unpack("!h", db_val[:2])
    for value_pack in value_struct:
        value_unpack = value_pack
    # Convert tuple to float
    # using join() + float() + str() + generator expression
    result = int('.'.join(str(ele) for ele in value_unpack))
    my_str_value = '%-.2i' % result
    return my_str_value


# reading db


read_db = data_block_read_int(10, 318, 2)  # siemens %DB14.DBD70 [type WORD]
read_db1 = data_block_read(10, 200, 4)  # siemens %DB14.DBD74 [type REAL]


print(read_db)
print(read_db1)
