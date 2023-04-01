# czesc
# hello
# hola
# hallo
# ___error

def match_and_case_language(language):
    # if language == 'polish':
    #     return "cześć"
    # elif language == 'english':
    #     return "hello"
    if not language:
        raise Exception("Empty language")

    match language.lower():
        case 'polish':
            return "Cześć"
        case 'english':
            return "Hi"
        case 'spanish':
            return "!Hola!"
        case 'germany':
            return "Hallo!"
        case _:
            raise ValueError("Not supported language")


if __name__ == "__main__":
    language = input("Your langauge: ")
    try:
        slowo = match_and_case_language(language)
        print(slowo)
    except Exception as error:
        print(f"You have an error {error}")

