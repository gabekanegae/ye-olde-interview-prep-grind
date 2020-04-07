def countChars(s):
    count = [0 for _ in range(26)]
    for c in s:
        count[ord(c)-ord("a")] += 1

    return count

def canConstruct(ransomNote, magazine):
    countNote = countChars(ransomNote)
    countMag = countChars(magazine)

    for n, m in zip(countNote, countMag):
        if n > m: return False

    return True