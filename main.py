# my:
def find_even_index(arr):
    
    for i in range(len(arr)):
        ballista = []
        jobblista = []
        
        for b in range(i-1, -1, -1):
            ballista.append(arr[b])

        for j in range(i+1, len(arr), 1):
            jobblista.append(arr[j])

        if sum(ballista) == sum(jobblista):
            return i
    return -1

# humanhelp:

#     for i in range(len(arr)):
#         ballista = []
        
#         for b in range(i-1, -1, -1):
#             ballista.append(arr[b])

#         if sum(ballista) == ((sum(arr)- arr[i]) / 2):
#             return i
#     return -1

# chatgpt:
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1
