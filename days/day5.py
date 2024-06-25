from .utils import read_file_lines, int_list_parse_from_string, int_try_parse, timing

# Puzzle 9 Helpers
def mapper(input, maps):
    current_value = input
    for map in maps:
        for source_start_index in map:
            dest_start_index = map[source_start_index][0]
            length = map[source_start_index][1]
            if current_value >= source_start_index and current_value < source_start_index + length:
                current_value = dest_start_index + (current_value - source_start_index)
                break
    return current_value

def map_maker(lines, reverse=False):
    # seed-to-soil map
    seed_to_soil_map = {}
    i = 3
    #print("seed-to-soil map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        seed_to_soil_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of seed-to-soil mappings:", len(seed_to_soil_map))

    # soil-to-fertilizer map
    soil_to_fertilizer_map = {}
    i += 2
    #print("soil-to-fertilizer map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        soil_to_fertilizer_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of soil-to-fertilizer mappings:", len(soil_to_fertilizer_map))

    # fertilizer-to-water map
    fertilizer_to_water_map = {}
    i += 2
    #print("fertilizer-to-water map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        fertilizer_to_water_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of fertilizer-to-water mappings:", len(fertilizer_to_water_map))

    # water-to-light map
    water_to_light_map = {}
    i += 2
    #print("water-to-light map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        water_to_light_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of water-to-light mappings:", len(water_to_light_map))

    # light-to-temperature map
    light_to_temperature_map = {}
    i += 2
    #print("light-to-temperature map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        light_to_temperature_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of light-to-temperature mappings:", len(light_to_temperature_map))

    # temperature-to-humidity map
    temperature_to_humidity_map = {}
    i += 2
    #print("temperature-to-humidity map")
    while lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        temperature_to_humidity_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of temperature-to-humidity mappings:", len(temperature_to_humidity_map))

    # humidity-to-location map
    humidity_to_location_map = {}
    i += 2
    #print("humidity-to-location map")
    while i < len(lines) and lines[i] != '':
        data = int_list_parse_from_string(lines[i])
        if reverse:
            data = [data[1], data[0], data[2]]
        #print(data)
        humidity_to_location_map[data[1]] = [data[0], data[2]]
        i += 1
    #print("Number of humidity-to-location mappings:", len(humidity_to_location_map))
    map_array = [seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]
    if reverse:
        map_array.reverse()
    return map_array

# Puzzle 9
@timing
def puzzle9():
    print('Puzzle 9')
    lines = read_file_lines('inputs/5.txt')
    seed_list_string = lines[0].split(':')[1]
    seed_list = int_list_parse_from_string(seed_list_string)
    #print(seed_list)
    
    min_location = 9999999999999
    min_seed = -1
    maps = map_maker(lines)
    for seed in seed_list:
        location = mapper(seed, maps)
        if location < min_location:
            min_location = location
            min_seed = seed
    print("Min Location:", min_location, "Corresponding Seed:", min_seed)

# Puzzle 10 Helper
def locationToSeed(seed_ranges, maps):
    # Start from a higher number because we know it's not THAT small
    location = 26000000
    while True:
        current_value = location
        for map in maps:
            for source_start_index in map:
                dest_start_index = map[source_start_index][0]
                length = map[source_start_index][1]
                if current_value >= source_start_index and current_value < source_start_index + length:
                    current_value = dest_start_index + (current_value - source_start_index)
                    break
        for seed_start in seed_ranges:
            seed_end = seed_start + seed_ranges[seed_start]
            if current_value >= seed_start and current_value < seed_end:
                print("Seed:", current_value)
                return location, current_value
        # literally just left here to make sure it's still running
        if location % 100000 == 0:
            print("Location:", location)
        location += 1

# Puzzle 10
# Could not figure out an elegant solution, so brute force it is. Work backwards from the location to the seed.
@timing
def puzzle10():
    print('Puzzle 10')
    lines = read_file_lines('inputs/5.txt')
    seed_pair_list_string = lines[0].split(':')[1]
    seed_pair_list = int_list_parse_from_string(seed_pair_list_string)
    maps = map_maker(lines)
    reverse_maps = map_maker(lines, reverse=True)
    seed_ranges = {}
    for i in range(0, len(seed_pair_list), 2):
        seed_ranges[seed_pair_list[i]] = seed_pair_list[i+1]
    min_loc, min_seed = locationToSeed(seed_ranges, reverse_maps)
    print("min loc:", min_loc)
    print("min seed:", min_seed)
    print("loc from min seed:", mapper(min_seed, maps))
    return

if __name__ == "__main__":
    puzzle9()
    # 10 takes forever, but it worked the once it needed to so... hooray?
    #puzzle10()