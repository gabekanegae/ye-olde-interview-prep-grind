def hasValidIPBlocks(ip):
    for block in ip.split("."):
        if len(block) > 1 and block[0] == "0": return False
        if not 0 <= int(block) <= 255: return False

    return True

def solve(ip):
    ans = []
    def rec(i, cur):
        if i == len(ip):
            if cur.count(".") == 3 and hasValidIPBlocks(cur):
                ans.append(cur)
            return

        if cur.count(".") > 3 or not hasValidIPBlocks(cur):
            return

        rec(i+1, cur + ip[i])
        rec(i+1, cur + "." + ip[i])

    if len(ip) == 0:
        return ans

    rec(1, ip[0])
    return ans

print(solve("25525511135"))
print(solve("0000"))
print(solve("101023"))
print(solve("010010"))