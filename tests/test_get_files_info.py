from functions.get_files_info import get_files_info

def main():
    res = get_files_info("calculator",".")
    print(res)

    res = get_files_info("calculator","pkg")
    print(res)

    res = get_files_info("calculator","/bin")
    print(res)

    res = get_files_info("calculator","../")
    print(res)


if __name__ == "__main__":
    print("hi")
    main()
