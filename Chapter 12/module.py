def myFunc():
    print("hello world")

myFunc()

if __name__ == "__main__":
    #if this code is directly executed by running the file its present in
    print("we are directly running this code")
    myFunc()
    print(__name__)