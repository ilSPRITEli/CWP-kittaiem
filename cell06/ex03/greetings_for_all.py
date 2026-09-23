def greetings(name="noble stranger"):
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")

greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)
