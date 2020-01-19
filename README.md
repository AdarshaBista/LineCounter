# Line Counter

Count the total number of lines present in files in a directory.

## Usage

Run `python main.py` to scan the current working directory.

## Options 

- `-r` or `--root` Specify a root directory to start counting. Defaults to current working directory.
- `-e` or `--extensions` Specify list of extensions to be included. Defaults to all extensions.
- `-t` or `--tree` Print folder structure with line count.

### Example

`python main.py -r lib -t -e dart py js`

The above command recursively scans all files in the `lib` directory and counts lines for files with extensions `dart`, `py`, `js` and shows a tree structure.