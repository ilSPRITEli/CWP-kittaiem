def array_of_names(names_dict):
    result = []
    for first, last in names_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        result.append(full_name)
    return result

persons = {
    "kittipat": "aiemluenam",
    "chanatip": "srichomchai",
    "natthanan": "seanghong",
    "chonlakorn": "jaitrakul",
    "narongrit": "sripanich",
    "sakun": "samart",
    "somnuk": "kongsomboon",
}
print(array_of_names(persons))
