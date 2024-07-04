
__all__ = ["TEXT", "_a", "__a"]

TEXT = "TEST second"

def print_name():
    print(__name__)
print_name()

# print(f"file: {__name__}")

a = 1
_a = 2
__a = 3

# import first
def print_name2():
    print(f"file: {__name__}")

if __name__ == "__main__":
    print("second.py", __name__)