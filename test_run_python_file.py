from functions.run_python_file import run_python_file

def test_run_python_file():
    # 1. Should print usage instructions
    res = run_python_file("calculator", "main.py")
    print(res)

    # 2. Should run calculator with expression
    res = run_python_file("calculator", "main.py", ["3 + 5"])
    print(res)

    # 3. Should run tests successfully
    res = run_python_file("calculator", "tests.py")
    print(res)

    # 4. Path traversal should error
    
    res = run_python_file("calculator", "../main.py")
    print(res)

    # 5. Nonexistent file should error
    res = run_python_file("calculator", "nonexistent.py")
    print(res)

    # 6. not a python file to run.    
    res = run_python_file("calculator", "lorem.txt")
    print(res)    
    
if __name__ == '__main__':
    test_run_python_file()