def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family.keys()))

family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(find_the_redheads(family))
