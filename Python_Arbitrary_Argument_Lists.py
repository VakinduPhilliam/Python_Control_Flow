# Python Arbitrary Argument Lists

def write_multiple_items(file, separator, *args):
 file.write(separator.join(args))
