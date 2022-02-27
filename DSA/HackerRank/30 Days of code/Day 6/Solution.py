# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_alternate_indices(num_arr):
    N = len(num_arr)
    if N > 0:
        for i in range(N):
            str = num_arr[i]
            left_str = "".join([str[i] for i in range(0, len(str), 2)])
            right_str = "".join([str[i] for i in range(1, len(str), 2)])
            print(f"{left_str} {right_str}")


if __name__ == '__main__':
    N = int(input())

    num_arr = []
    for i in range(N):
        num_arr.append(input())

    print_alternate_indices(num_arr)
