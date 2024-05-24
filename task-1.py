import heapq

def min_cost(cable_lengths):
    
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        cable_1 = heapq.heappop(cable_lengths)
        cable_2 = heapq.heappop(cable_lengths)
    
        cost = cable_1 + cable_2
        total_cost += cost

        heapq.heappush(cable_lengths, cost)
    
    return total_cost

cable_lengths = [4, 3, 9, 2, 6]
total_cost = min_cost(cable_lengths)
print(f"Cost to connect all cables: {total_cost}")