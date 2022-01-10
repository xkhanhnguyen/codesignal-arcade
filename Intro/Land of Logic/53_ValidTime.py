"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
"""

def solution(time):
    time = time.split(":")
    
    if 0 <= int(time[0]) < 24 and 0 <= int(time[1]) < 60:
        return True

    return False

print(solution("2:98"))