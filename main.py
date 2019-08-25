from mouse_vs_mouse import mouse_vs_mouse_from_file
from running_median import calculate_median_from_file

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Run tasks')
    parser.add_argument('--task', dest='task', required=True,
                        help='Which task you want to run: (running_median/mouse_vs_mouse)')
    parser.add_argument('--file_name', dest='file_name', required=True, help='Input file name')
    args = parser.parse_args()

    if args.task == 'running_median':
        calculate_median_from_file(args.file_name)
    if args.task == 'mouse_vs_mouse':
        mouse_vs_mouse_from_file(args.file_name)
