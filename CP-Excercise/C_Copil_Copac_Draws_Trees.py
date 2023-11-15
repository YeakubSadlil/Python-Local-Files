'''
/****************** * ********  Yeakub Sadlil Seyam  ************* * *******************
 *   __   ░░        * East West University, Dhaka, Bangladesh      *       ░░   __     **
 *                  *           Department of  ECE                 *                   *  *
/*****************************  ╚══I love LINUX══╝ *************************************    *     ░░░░░░░░░░░░░░░░░░░░░░░░
 *  //██║░░█╗ Machine-Learning║██╔══██╗██║╚══██╔══╝██╔════╝ ██╔══██╗████╗░██║╔══██╗||░ *     * >> Networking+Programming ░
 * //░╚██╗╗█╔╝██ ██╔╝██║░░██║░███╗ JAVA ██║░░██║██╔██╗██║BASH ██╔╝░╚██ ██╔╝░░║██║░░██║ *    *     ░░░░░░░░░░░░░░░░░░░░░░░░
 ME >--+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---    *   *
 * \\░╚█╔╝ C ╚█╔╝░██║░░██║██║░░░██║░░███╗  ╚█ ██╔╝██║░╚██ █--CV--██║░░██║░░╚██╔╝ C++ ░░* *
 *  \\░╚═╝░░░╚═╝ Python ░░╚═╝╚═╝░░░╚═╝ Practice ░╚════╝  ╚═╝░░╚══╝  ╚═╝░░░╚═╝░░╚═╝░╚═  **
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░*/
'''


def solve(aaaa, p, i, mp):
    ans = 0
    for j in range(len(aaaa[i])):
        if aaaa[i][j] == p:
            continue
        x = 0
        if mp[(p, i)] > mp[(i, aaaa[i][j])]:
            x += 1
        ans = max(ans, x + solve(aaaa, i, aaaa[i][j], mp))
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    aaaa = [[] for _ in range(n+1)]
    mp = {}
    for i in range(n-1):
        x, y = map(int, input().split())
        mp[(x, y)] = i
        mp[(y, x)] = i
        aaaa[x].append(y)
        aaaa[y].append(x)
    ans = float('-inf')
    for i in range(len(aaaa[1])):
        ans = max(ans, solve(aaaa, 1, aaaa[1][i], mp))
    print(ans + 1)
