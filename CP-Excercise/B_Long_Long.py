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
t = int(input())

for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))
    # arr = [x for x in arr if x != 0]

    # segments = []
    # for i in arr:
    #     if i > 0:
    #         segments.append('p')
    #     else:
    #         segments.append('n')
    
    # # ['n', 'p', 'n', 'n', 'p', 'n'] count each segment of n and p

    count_n = 0
    sm = 0
    tmp = False
    for i in arr:
        if i <= 0:
            if(i < 0): tmp = True
        else:
            if tmp:
                count_n += 1
                tmp = False
        if i < 0:
            i *= -1
        sm = sm+i
    if tmp: count_n += 1
    print(sm, count_n)
    