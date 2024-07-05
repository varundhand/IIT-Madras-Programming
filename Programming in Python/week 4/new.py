def placement_results(test_cases):
    results = []
    for case in test_cases:
        N, M, minSal, offSal, maxOff, qual = case
        
        jobOff = [0] * M
        candWithJobs = 0
        totalSal = 0
        compsWithoutJobs = 0
        
        for i in range(N):
            maxSal = 0
            compIdx = -1
            
            for j in range(M):
                if qual[i][j] == 1 and offSal[j] >= minSal[i] and jobOff[j] < maxOff[j]:
                    if offSal[j] > maxSal:
                        maxSal = offSal[j]
                        compIdx = j
            
            if compIdx != -1:
                jobOff[compIdx] += 1
                candWithJobs += 1
                totalSal += maxSal
        
        compsWithoutJobs = jobOff.count(0)
        
        results.append((candWithJobs, totalSal, compsWithoutJobs))
    
    return results

def read_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    test_cases = []
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        minSal = list(map(int, data[index:index + N]))
        index += N
        
        offSal = []
        maxOff = []
        
        for _ in range(M):
            offSal.append(int(data[index]))
            maxOff.append(int(data[index + 1]))
            index += 2
        
        qual = []
        for _ in range(N):
            qual.append(list(map(int, list(data[index]))))
            index += 1
        
        test_cases.append((N, M, minSal, offSal, maxOff, qual))
    
    return test_cases

if __name__ == "__main__":
    test_cases = read_input()
    results = placement_results(test_cases)
    for res in results:
        print(f"{res[0]} {res[1]} {res[2]}")
