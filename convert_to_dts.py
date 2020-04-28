#!/usr/bin/python
"""Reads an fman binary file and converts it into a dts file"""

import sys
import glob

for binary_file in glob.glob("./*.bin"):
    dts_file = f"{binary_file.rsplit('.', 1)[0]}.dts"

    with open(dts_file, "w") as fo:
        fo.write('/dts-v1/;\n')

        fo.write('&fman0 {\n')
        fo.write('\tfirmware {\n')

        fo.write('\t\tcompatible = "fsl,fman-firmware";\n')
        fo.write('\t\tfsl,firmware = <\n')

        with open(binary_file, "rb") as fi:
            byte = fi.read(1)
            while byte != b"":
                fo.write(
                        f"\t\t\t0x{int.from_bytes(byte, byteorder='big'):00x}\n"
                )
                byte = fi.read(1)

        fo.write('\t\t>;\n')
        fo.write('\t}\n')
        fo.write('}\n')
