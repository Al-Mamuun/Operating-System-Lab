def SSTF(requests, head):
    seek_count = 0
    seek_sequence = []
    visited_tracks = set()

    for _ in range(len(requests)):
        min_distance = float('inf')
        closest_track = None

        for track in requests:
            if track in visited_tracks:
                continue
            distance = abs(track - head)
            if distance < min_distance:
                min_distance = distance
                closest_track = track

        if closest_track is not None:
            seek_count += abs(closest_track - head)
            head = closest_track
            seek_sequence.append(closest_track)
            visited_tracks.add(closest_track)
        else:
            break 

    for track in requests:
        if track in visited_tracks:
            continue
        else:
            print(f"Skipping track {track} (already visited)")

    print("\nSeek sequence:")
    for track in seek_sequence:
        print(track)

    print("\nTotal number of seek operations:", seek_count)



n = int(input("Enter number of disk requests: "))
requests = []

print("Enter the request values:")
for i in range(n):
    req = int(input(f"Request {i+1}: "))
    requests.append(req)

head = int(input("Enter initial head position: "))


SSTF(requests, head)
