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
    arr = list(map(int, input().split()))
    bst = []
    for i in arr:
        bst.append(n+1-i)
    print(*bst)
