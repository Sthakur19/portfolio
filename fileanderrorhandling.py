import sys

# Define the file where tasks are stored
TODO_FILE = "tasks.txt"

class Todo:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []

        # Load tasks from file
        with open(self.filename, 'r') as f:
            for line in f:
                self.tasks.append(line.strip())

    def write_file(self):
        '''To write the file creating this function'''
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f'{task}\n')

    def print_usage(self):
        '''If the application is ran without any arguments
        it will print the usage information'''
        print("""Command Line Todo application
                 =============================

                 Command line arguments:
                    -l   Lists all the tasks
                    -a   Adds a new task
                    -r   Removes an task
                    -c   Completes an task
                    """)

    def list_tasks(self, command_arg):
        ''' It will display all the task in the form of list
        and if no task was given it will print "No todos for today! :)"'''
        if not self.tasks:
            print('No todos for today! :)')
        else:
            if command_arg == "-la":
                for i, task in enumerate(self.tasks):
                    # Checking if the task is done
                    if task.startswith('x '):
                        status = '[x]'
                        task = task[2:]
                    else:
                        # For undone tasks
                        status = '[ ]'
                    print(f'{i+1} - {status} {task}')
            elif command_arg == "-l":
                for i, task in enumerate(self.tasks):
                    if task.startswith('x ') == False:
                        # All undone tasks
                        status = '[ ]'
                        print(f'{i+1} - {status} {task}')
    
    def list_tasks_number(self):
        '''Return the number of list from the tasks.txt'''
        for i, task in enumerate(self.tasks):
            number_index = i+1
        return number_index

    def add_task(self, description):
        '''When the application is ran with the `-a` argument than
        it should add the task in the file'''
        self.tasks.append(description)

        # Invoking write_file function to add the task in tasks.txt file
        self.write_file()
        new_argv = " ".join(sys.argv[2:])
        print(f"Added task: {new_argv}")

    def check_task(self, given_index):
        '''When the application is ran with the `-c 2` argument than
        it should check the second task from the file'''
        print(self.tasks[given_index])

    def remove_task(self, given_index):
        '''When the application is ran with the `-r 2` argument
        Then it should remove the second task from the file'''
        removed_item = self.tasks[given_index]
        del self.tasks[given_index] 

         # Invoking write_file function to remove the task in tasks.txt file
        self.write_file()
        print(f"Item has been removed {removed_item}")

if __name__ == '__main__':
    todo = Todo(TODO_FILE)

    if len(sys.argv) == 1:
        # Calling print_usage function to display all the related options
        todo.print_usage()   

    elif '-c' in sys.argv:
        # Get the index of the -c argument
        index = sys.argv.index('-c')
        # Check if the next argument is a valid integer
        if index+1 < len(sys.argv):
            try:
                count = int(sys.argv[index+1])
            except ValueError:
                # Show an error message if the index is not a number
                print('Unable to check: index is not a number')
            else:
                # Check if the count is greater than the number of tasks
                if count > todo.list_tasks_number():
                    # Show an error message if the index is out of bounds
                    print('Unable to check: index is out of bounds')
                else:
                    # Run the application with the specified count
                    todo.check_task(int(sys.argv[2])-1)
        else:
            # Show an error message if the -c argument is not followed any thing
            print('Unable to check: no index provided')

    elif len(sys.argv) > 2 and '-c' in sys.argv:
        # Calling check_task function to check the task from the file
        todo.check_task(int(sys.argv[2])-1)

    elif '-r' in sys.argv:
        # Get the index of the -c argument
        index = sys.argv.index('-r')
        # Check if the next argument is a valid integer
        if index+1 < len(sys.argv):
            try:
                count = int(sys.argv[index+1])
            except ValueError:
                # Show an error message if the index is not a number
                print('Unable to remove: index is not a number')
            else:
                # Check if the count is greater than the number of tasks
                if count > todo.list_tasks_number():
                    # Show an error message if the index is out of bounds
                    print('Unable to remove: index is out of bounds')
                else:
                    # Run the application with the specified count
                    todo.remove_task(int(sys.argv[2])-1)
        else:
            # Show an error message if the -c argument is not followed any thing
            print('Unable to remove: no index provided')

    elif len(sys.argv) > 2 and '-r' in sys.argv:
        # Calling remove_task function to remove the task from the file
        todo.remove_task(int(sys.argv[2])-1)

    elif '-l' in sys.argv:
        # Calling list_tasks function to display all the undone tasks from the file 
        todo.list_tasks("-l")

    elif '-la' in sys.argv:
        # Calling list_tasks function to display all the listed tasks from the file 
        todo.list_tasks("-la")

    elif '-a' in sys.argv:
        # Get the index of the -a argument
        index = sys.argv.index('-a')
        # Check if the next argument is a valid integer
        if index+1 < len(sys.argv):
            # Add the given task in the list
            new_argv = " ".join(sys.argv[2:])
            todo.add_task(new_argv)
        else:
            # Show an error message if the -a argument is not followed any thing
            print('Unable to Add: no index provided')

    elif len(sys.argv) > 2 and '-a' in sys.argv:
        # Calling add_tasks function to add the task in the file
        new_argv = " ".join(sys.argv[2:])
        todo.add_task(new_argv)

    else:
        '''When the application is ran with an unsupported argument *(eg. `get`)
        Then it should show an error message like: `Unsupported argument`'''
        print('Unsupported argument')
        print('Usage: todo [-l | -a <description> | -r <index>]')

