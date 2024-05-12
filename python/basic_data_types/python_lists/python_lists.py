if __name__ == '__main__':
    N = int(input())
    holder = []
    answer = []
    
    for item in range(N):
        holder.append(input())
    
    for hold in holder:
        split = hold.split()
        
        if split[0] == 'insert':
            answer.insert(int(split[1]), int(split[2]))
        elif split[0] == 'print':
            print(answer)
        elif split[0] == 'remove':
            answer.remove(int(split[1]))
        elif split[0] == 'append':
            answer.append(int(split[1]))
        elif split[0] == 'sort':
            answer.sort()
        elif split[0] == 'pop':
            answer.pop()
        elif split[0] == 'reverse':
            answer.reverse()
        else:
            print('We shouldn\'t have reached here.')
    