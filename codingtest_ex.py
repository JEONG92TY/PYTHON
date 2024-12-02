def solution(grid, d, k):
    a = 0
    b = 0
    c = 0
    answer = 0
    for a in range(len(grid)) :
        for b in range(len(grid[a])):
            print("===========b========================")
            list = []
            kk = 1
            for c in range(len(d)) :
                print("===========bsdfs========================")
                if c == len(d) : # 길이 3
                    c = 0
                    if kk < k :
                        kk += 1 # a=2, b=1, c=0, kk=1
                        print("여기")
                    else :
                        print("저기")
                        list.append(grid[a][b])
                        answer += 1
                        print(list)
                        break           
                elif b+1 < len(grid[a]) and grid[a][b+1] - grid[a][b] == d[c] :
                    list.append(grid[a][b])
                    print("1번")
                    b = b+1
                elif b-1 >= 0 and grid[a][b-1] - grid[a][b] == d[c] :
                    list.append(grid[a][b])
                    print("2번")
                    b = b-1
                elif a+1 < len(grid) and grid[a+1][b] - grid[a][b] == d[c] :
                    list.append(grid[a][b])
                    print("3번")
                    a = a+1
                elif a-1 >= 0 and grid[a-1][b] - grid[a][b] == d[c] :
                    list.append(grid[a][b])
                    print("4번")
                    a = a-1
                else :
                    pass

            return answer

g = [[3, 4, 6, 5, 3],
     [3, 5, 5, 3, 6],
     [5, 6, 4, 3, 6],
     [7, 4, 3, 5, 0]
]
d = [1, -2, -1, 0, 2]
k = 2
print(solution(g, d, k))

#[3 > 4 > 2 > 7 > 8 > 6 > 11 > 12 > 10 > 15]