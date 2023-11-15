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

test_cases = int(input())

for _ in range(test_cases):
    length = int(input())
    numbers = list(map(int, input().split()))
    result = ""
    last_num = 0
    first_num = 0
    is_true = 0
    
    for j in range(length):
        num = numbers[j]
        
        if j == 0:
            last_num = num
            first_num = num
            result += '1'
        elif not is_true and num >= first_num and last_num <= num:
            last_num = num
            result += '1'
        elif not is_true and num <= first_num and last_num > num:
            is_true = 1
            last_num = num
            result += '1'
        elif is_true and num >= last_num and num <= first_num:
            last_num = num
            result += '1'
        else:
            result += '0'
    
    print(result)




    # st = set()
    # lst = [1]
    # st.add(queries[0])
    # check = 0
    # for i in range(1, q):
    #     if check == 0:
    #         if queries[i]>= queries[i-1]:
    #             lst.append(1)
    #             st.add(queries[i])
    #     else:
    #         check += 1
    #     if check == 1:
    #         lst.append(1)
    #         st.add(queries[i])
    #     elif check >= 1:
    #         if queries[i] >= min(st) and queries[i] <= max(st) or queries[i] >= max(st):
    #             st.add(queries[i])
    #             lst.append(1)
    #         else:
    #             lst.append(0)
    
    # print(*lst)
