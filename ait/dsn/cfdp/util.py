# Advanced Multi-Mission Operations System (AMMOS) Instrument Toolkit (AIT)
# Bespoke Link to Instruments and Small Satellites (BLISS)
#
# Copyright 2018, by the California Institute of Technology. ALL RIGHTS
# RESERVED. United States Government Sponsorship acknowledged. Any
# commercial use must be negotiated with the Office of Technology Transfer
# at the California Institute of Technology.
#
# This software may be subject to U.S. export control laws. By accepting
# this software, the user agrees to comply with all applicable U.S. export
# laws and regulations. User has the responsibility to obtain export licenses,
# or other export authority as may be required before exporting such
# information to foreign countries or providing access to foreign persons.

import binascii
import os
import struct


def string_length_in_bytes(s):
    """Returns length of a UTF-8 string in bytes

    Arguments:
        s:
            The value whose length is calculated as string
    """
    if not isinstance(s, str):
        s = str(s)
    return len(s.encode('utf-8'))


def string_to_bytes(value):
    """Converts string value to array of bytes

    Arguments:
        value:
            string value to be converted to list of bytes
    """
    if isinstance(value, str):
        return list(bytearray(value, 'utf-8'))
    return list(bytearray(value))

def bytes_to_string(data_bytes):
    """Converts list of bytes to a string

    Arguments:
        data_bytes:
            list of bytes to be converted to a string
    """
    hex_values = [format(b, '>02x') for b in data_bytes]
    str_values = [binascii.unhexlify(b).decode('utf-8') for b in hex_values]
    return ''.join(str_values)


def write_to_file(out_path, contents, offset=None):
    """Writes binary contents to file, at the optional offset

    Arguments:
        out_path:
            Full path of the file to write to
        contents:
            Contents to write to file as binary
        offset:
            Optional offset to denote where in the file the contents should be written
    """
    with open(out_path, 'wb') as f:
        if offset is not None and offset > 0:
            f.seek(offset)
        f.write(contents)


def calc_file_size(filepath):
    """Calculate size of a file

    Arguments:
        filepath:
            Full path of the file
    """
    statinfo = os.stat(filepath)
    return statinfo.st_size


def check_file_structure(target_file, segmentation_control):
    # TODO implement segmentation control check
    return True


def checksum_of_word(word_list: list[int]):
    """Returns of the value of a 4-byte word to be added to the running checksum.

    Arguments:
        word_list:
            list of integers with max length 4 (more will be ignored), each integer representing a byte
    """
    while len(word_list) < 4:
        word_list.append(0)
    word = word_list[0] << 24
    word += word_list[1] << 16
    word += word_list[2] << 8
    word += word_list[3]
    return word


def _calc_checksum_legacy(filename):
    """Calculates the checksum of a file according to the CFDP Blue Book.

    NOTE: This function (calc_checksum_legacy) is the way `calc_checksum` was implemented before version 3.1.0.
    
    `calc_checksum_buffered` is the new implementation that gives the same result as `calc_checksum` but is faster.

    This function is kept only because we have a test that verifies that `calc_checksum_legacy` and `calc_checksum_buffered`
    give the same result. This function is not used anywhere else in the code and should not be used for any other purpose.

    See issue #3
    https://github.com/msu-ssc/AIT-DSN/issues/3

    Arguments:
        filename:
            Full path of the file
    """
    try:
        checksum = 0
        open_file = open(filename, 'rb')
        file_size = calc_file_size(filename)

        # Checksum procedure
        # Mod 2^32 of 4 bytes words, aligned from start of file
        # Copy 1 byte of file data whose offset is mult of 4 (0, 4, 8, ...) into 1st higher order octet of word,
        # then copy  next 3 octets of file data into next 3 octets of word

        # Read file 4 bytes at a time while there is still data left to read
        # We want to pack each of the 4 bytes in order from high-order to low-order
        # E.g. if the four bytes read are 00 01 02 03, they will be packed into the first word as
        # 00010203 and summed which each subsequent similar word
        while open_file.tell() != file_size:
            # Convert file contents to list of bytes represented as integers
            # If there are less than 4 bytes, make it 4 by adding 0
            # Need to mash the bytes in the list into a single word
            byte_list = string_to_bytes(open_file.read(4))
            checksum += checksum_of_word(byte_list)
        open_file.close()

        # Must truncate it to 32 bits
        return checksum & 0xFFFFFFFF
    except IOError:
        return None


def _calc_checksum_struct(
    path: str,
    *,
    buffer_size=1024*1024,
):
    assert buffer_size % 4 == 0, f"Buffer size must be a multiple of 4. Got {buffer_size}."
    checksum = 0
    with open(path, 'rb') as f:
        while True:
            buffer = f.read(buffer_size)
            if not buffer:
                break
                
            # Process full 4-byte chunks
            full_chunks = len(buffer) // 4
            for index in range(0, full_chunks*4, 4):
                value, = struct.unpack('>I', buffer[index : index + 4])
                checksum = (checksum + value) & 0xFFFFFFFF
                
            # Handle remaining bytes (0-3)
            # Pad to the right with 0s to make it a full 4-byte word
            remaining = buffer[full_chunks*4:]
            if remaining:
                padded = remaining + b'\x00' * (4 - len(remaining))
                value, = struct.unpack('>I', padded)
                checksum = (checksum + value) & 0xFFFFFFFF
                
    return checksum

def calc_checksum(
    path: str,
    *,
    buffer_size: int = 1024*1024,
):
    """Calculates the checksum of a file according to the CFDP Blue Book.

    NOTE: The implementation of this function changed in version 3.1.0, but the returned value should not have. See issue #3
    https://github.com/msu-ssc/AIT-DSN/issues/3

    Arguments:
        filename:
            Full path of the file
    """
    return _calc_checksum_struct(path, buffer_size=buffer_size)
