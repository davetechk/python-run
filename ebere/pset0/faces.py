def main():
    user_input=input()
    result = convert(user_input)
    print(result)

def convert(text):
    updated_text = text.replace(":)", "🙂").replace(":(", "🙁")
    return(updated_text)

main()