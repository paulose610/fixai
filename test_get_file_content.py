from functions.get_file_content import get_file_content

def main():
    #res = get_file_content("calculator", "lorem.txt")
    res = get_file_content("calculator","main.py")
    print(res)

    res = get_file_content("calculator","pkg/calculator.py")
    print(res)

    res = get_file_content("calculator","/bin/cat")
    print(res)

    res = get_file_content("calculator","pkg/blah.py")
    print(res)


if __name__ == "__main__":
    print("hi")
    main()