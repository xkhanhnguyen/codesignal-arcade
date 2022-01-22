"""
A media access control address (MAC address) is a unique identifier assigned 
to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form 
is six groups of two hexadecimal digits (0 to 9 or A to F), 
separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.

"""

def solution(inputString):
    address = inputString.split("-")
    for i in range(0, len(address)):
        if len(address[i]) != 2:
            return False
        if (("0" <= address[i][0] <= "9" or "A" <= address[i][0] <= "F" ) and \
            ("0" <= address[i][1] <= "9" or "A" <= address[i][1] <= "F" )):
            continue
        return False
    return True

print(solution("00-1B-63-84-45-E6"))