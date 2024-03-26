# Define function full_name
def ask (prompt = "Please enter a value: "):
    return input(prompt + " ")

a = ask()
b = ask("What do you want for b?")
print(a)


def ask(prompt = "Please enter a value: "):
    if prompt.endswith(" "):
        return input(prompt)
    else:
        return input(prompt + " ")