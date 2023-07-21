# //=============================================================================
# //Radosław Tecmer)
# //(c)Copyright (2023) free of copyright
# //-----------------------------------------------------------------------------
# //The program allows you to connect to the Siemens S7 PLC unit and
# //write [float] values to the data block
# //-----------------------------------------------------------------------------
# //contact:
# //https://github.com/remceTkedaR
# //radek69tecmer@gmail.com
# //=============================================================================


import snap7
import struct


def main():
    # Address and size of the data block where we will write the value
    db_number = 10
    db_word = 200

    # Siemens S7 PLC IP address
    plc_ip = "192.168.3.211"  # Enter the actual IP address of your PLC here

    # Establishing a connection with the PLC
    plc = snap7.client.Client()
    plc.connect(plc_ip, 0, 1)

    try:
        # Input the floating-point value to be written from the keyboard
        data = float(input("Enter the value to write (float type): "))

        # Convert the value to FLOAT format (32-bit)
        data_bytes = struct.pack("!f", data)

        # Write the value to the PLC
        plc.db_write(db_number, db_word, data_bytes)

        print(f"Value {data} has been written to data block DB{db_number}.DBW{db_word}.")

    except ValueError:
        print("The entered value is not a valid floating-point number.")
    finally:
        # Close the connection with the PLC
        plc.disconnect()


if __name__ == "__main__":
    main()
