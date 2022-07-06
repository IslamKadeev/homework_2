from itertools import permutations

def distance_count(current_point, next_point):
    return ((next_point[0] - current_point[0]) ** 2 + (next_point[1] - current_point[1]) ** 2) ** 0.5

def get_filtered_ways_combination(streets):
    all_ways = list(permutations(streets))
    sorted_ways = []

    for way in all_ways:
        if way[0] == 'start_point' and way[-1] == 'finish_point':
            sorted_ways.append(way)
    return sorted_ways

def find_best_way(streets):
    sorted_ways = get_filtered_ways_combination(streets)
    distance = 0
    total_distance = 0
    temp_answer = ''

    for way in sorted_ways:
        for i in range(len(way) - 1):
            distance += distance_count(streets.get(way[i]), streets.get(way[i + 1]))
        current_min = distance
        break

    for way in sorted_ways:
        for i in range(len(way) - 1):
            distance = distance_count(streets.get(way[i]), streets.get(way[i + 1]))
            total_distance += distance
            temp_answer += way[i] + ' -> ' + way[i + 1] + ' ' + str([total_distance]) + "\n"

        if total_distance < current_min:
            best_way = way
            answer = temp_answer
            current_min = total_distance
        total_distance = 0
        temp_answer = ''

    return answer

streets = {
        'start_point' : (0, 2), 'street_1' : (2, 5), 'street_2' : (5, 2),
        'street_3' : (6, 6), 'street_4' : (8, 3), 'finish_point' : (0, 2)
        }

print(find_best_way(streets))