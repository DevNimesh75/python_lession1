def run_assignment_1_task_1():
    from assignment_1.task_1 import main as task_1_main
    task_1_main()

def run_assignment_1_task_2():
    from assignment_1.task_2 import main as task_2_main
    task_2_main()

def main():
    print("Python Assignments")
    print("1. Task 1 - Basic Calculator")
    print("2. Task 2 - Greeting Program")

    choice = input("Enter the task number to run (1/2): ")

    if choice == '1':
        run_assignment_1_task_1()
    elif choice == '2':
        run_assignment_1_task_2()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == '__main__':
    main()