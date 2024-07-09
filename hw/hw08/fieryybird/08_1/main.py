from utils import *
from models import *

print(list(filter(lambda str: not ('__' in str), dir())))


# Output: python3 main.py 
#        ['create_admin', 'create_user', 'format_string', 'log_in_file']