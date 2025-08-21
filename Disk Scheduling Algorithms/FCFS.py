def FCFS(requests, head):
    seek_count = 0
    visited = set()
    visited.add(head)  

    for track in requests:
        if track not in visited:
            distance = abs(track - head)
            seek_count += distance
            head = track
            visited.add(track)
        else:
            print(f"Skipping track {track} (already visited)")

    print("\nTotal number of seek operations =", seek_count)



n = int(input("Enter the number of disk requests: "))

requests = []
print(f"Enter {n} request values:")
for i in range(n):
    value = int(input(f"Request {i + 1}: "))
    requests.append(value)

head = int(input("Enter the initial head position: "))

FCFS(requests, head)
