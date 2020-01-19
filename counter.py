import os


class Counter:
    def __init__(self, args):
        self.total_lines = 0
        self.args = args

        # Start traversing root directory
        self.traverse(args.root)

    def traverse(self, root_dir):
        for dir_name, _, file_list in os.walk(root_dir):
            # Determine proper indent to display tree structure
            level = dir_name.replace(root_dir, '').count(os.sep)
            folder_indent = ' ' * 2 * (level) + '+ '
            file_indent = ' ' * 2 * (level + 1) + '- '

            if self.args.tree:
                print(f'\n{folder_indent}{dir_name}:')

            for fname in file_list:
                self.count_lines(dir_name, fname, file_indent)

    # Count and print numbers of lines in a file
    def count_lines(self, dir_name, fname, file_indent):
        ext = os.path.splitext(fname)[1][1:]

        # Check if extension is in list of included extensions
        if ext not in self.args.extensions and len(self.args.extensions) != 0:
            return

        count = self.get_count(f'{dir_name}/{fname}')
        self.total_lines += count

        if self.args.tree:
            print(f'{file_indent}{fname}: ' + str(count))

    # Get number of lines in a single file
    def get_count(self, file_path):
        with open(file_path, errors='ignore', encoding='utf-8') as f:
            return len(f.readlines())

    # Get the total number of lines in root dir
    def get_total(self):
        return self.total_lines
