#!/usr/bin/python
"""Reads an fman binary file and converts it into a dts file"""

import glob

for binary_file in glob.glob("./*.bin"):
    dts_file = f"{binary_file.rsplit('.', 1)[0]}.dts"

    with open(dts_file, "w") as fo:
        fo.write('/dts-v1/;\n\n')

        fo.write('&fman0 {\n')
        fo.write('\tfman_firmware: fman-firmware {\n')

        fo.write('\t\tcompatible = "fsl,fman-firmware";\n')
        fo.write('\t\tfsl,firmware = [')

        with open(binary_file, "rb") as fi:
            byte = fi.read(1)
            fo.write(f"{int.from_bytes(byte, byteorder='big'):02x}")
            while byte != b"":
                byte = fi.read(1)
                fo.write(f" {int.from_bytes(byte, byteorder='big'):02x}")

        fo.write('];\n')
        fo.write('\t};\n')
        fo.write('};\n')
