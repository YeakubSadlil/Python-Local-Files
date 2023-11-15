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

tst = int(input())
for _ in range(tst):
    n = int(input())
    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))

    one = {}
    b = {}
    cnt = 1
    for i in range(1, n + 1):
        if i == n:
            one[array_a[i - 1]] = max(cnt, one.get(array_a[i - 1], 0))
            break
        if array_a[i] == array_a[i - 1]:
            cnt += 1
        else:
            one[array_a[i - 1]] = max(cnt, one.get(array_a[i - 1], 0))
            cnt = 1

    cnt = 1
    for i in range(1, n + 1):
        if i == n:
            b[array_b[i - 1]] = max(cnt, b.get(array_b[i - 1], 0))
            break
        if array_b[i] == array_b[i - 1]:
            cnt += 1
        else:
            b[array_b[i - 1]] = max(cnt, b.get(array_b[i - 1], 0))
            cnt = 1

    result = 0
    for i in array_a:
        result = max(result, one.get(i, 0) + b.get(i, 0))
    for j in array_b:
        result = max(result, b.get(j, 0) + one.get(j, 0))
    print(result)