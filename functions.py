FILEPATH= 'todos.txt'
def get_todos(filepath=FILEPATH):
    """This function tries to get the input files from txt"""
    with open(filepath,'r') as file:
        todos=file.readlines()
    return todos

def write_todos(todos_arg,filepath=FILEPATH):
    """This function will write our list to a txt file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

if __name__=='__main__':
    print('Hello mamali')