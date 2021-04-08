def main():

    queue = []
    stack = []
    min_queue = []

    is_queue = True
    is_stack = True
    is_min_queue = True
    is_sorted = False

    amount = int(input())

    for i in range(0, amount):

        command = input().split()

        command_var = command[0]
        int_var = int(command[1])

        if command_var == "I":
            if not len(min_queue) > amount and is_min_queue:
                min_queue.append(int_var)
                is_sorted = False
            if not len(queue) > amount and is_queue:
                queue.append(int_var)
            if not len(stack) > amount and is_stack:
                stack.append(int_var)
        try:
            if command_var == "E":
                if is_stack:
                    if int_var == stack[-1]:
                        stack.pop()
                    else:
                        is_stack = False

                if is_queue:
                    if int_var == queue[0]:
                        queue.pop(0)
                    else:
                        is_queue = False

                if is_min_queue:
                    if not is_sorted:
                        min_queue.sort()
                        is_sorted = True
                    if int_var == min_queue[0]:
                        min_queue.pop(0)
                    else:
                        is_min_queue = False
        except:
            print("F")

    if is_queue:
        print("YES")
    else:
        print("NO")

    if is_stack:
        print("YES")
    else:
        print("NO")

    if is_min_queue:
        print("YES")
    else:
        print("NO")


main()
