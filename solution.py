def solution(entrances, exits, path):
    le = len(entrances)
    lp = len(path)
    lx = len(exits)
    bunn_count = 0
    inter_paths = path[le:(lp-lx)]                # To find all intermediate rooms
    for i in range(lp - le - lx):                 # Loop through range of length of intermediate rooms
        sum_range = sum(inter_paths[i])           # Sum of an intermediate room's possible number of bunnies allowed
        sum_enter = 0                             # Sum of bunnies that enter that room
        for j in entrances:
            sum_enter += path[j][le + i]          # Get all bunnies that enter a room
        bunn_count += min(sum_enter, sum_range)
    return bunn_count
