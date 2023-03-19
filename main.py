# python3
# Egija Kokoreviča 	221RDB288

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads=[0]*n
    time=0
    while data:
        for i in range(n):
            if threads[i] <= time and data:
                output.append([i,time])
                threads[i]= time+data.pop(0)
        time+=1

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # n = 0
    # m = 0
    n,m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for pair in result:
        print(pair[0],pair[1])
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
