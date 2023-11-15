def minimalOperations(words):
    # Write your code her
    result = []
    for word in words:
        cnt1 = '_'
        counter1 = 0
        
        for i in range(len(word)-1):
            if (word[i] == word[i+1]) and (cnt1 != word[i]):
                counter1 +=1
                cnt1 == word[i]
                print(i," ",word[i]," if ",counter1)
            else:
                cnt1 == '_'
                print(i," ",word[i]," else ",counter1)

                
        result.append(counter1)
    return result

if __name__ == '__main__':
    
    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)
    print(result)

