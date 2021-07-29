def flatten(my_list):
    result = []
    for element in my_list:
        if isinstance(element, list):
            flat_list = flatten(element)
            result += flat_list
        else:
            result.append(element)

    return result


planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
flattened_planets = flatten(planets)
print(flattened_planets)