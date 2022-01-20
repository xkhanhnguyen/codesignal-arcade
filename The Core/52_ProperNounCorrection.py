"""
Proper nouns always begin with a capital letter, followed by small letters.

Correct a given proper noun so that it fits this statement.

Example

For noun = "pARiS", the output should be
solution(noun) = "Paris";
For noun = "John", the output should be
solution(noun) = "John".

"""
def solution(noun):
    # return noun[0].upper()+noun[1:].lower()
    return noun.title()

print(solution("pARiS"))