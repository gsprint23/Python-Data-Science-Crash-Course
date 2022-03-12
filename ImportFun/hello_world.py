print("hello from hello_world __name__:", __name__)
# 2 ways to run a python file (AKA module)
# 1. directly: e.g. python hello_world.py
# 2. indirectly: by importing it from another module
# e.g. a main.py it had a import hello_world

def main():
    print("hello from hello_world.py main()")

# __name__ is "__main__" when this module
# is executed directly
if __name__ == "__main__":
    main()