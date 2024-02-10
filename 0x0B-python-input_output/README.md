This directory contains tasks on file input and file output.
Before you can read from a file, you need to open it. Opening a file in Python couldn’t be easier:
a_file = open('examples/chinese.txt', encoding='utf-8')
Python has a built-in open() function, which takes a filename as an argument. Here the filename is
'examples/chinese.txt'. There are five interesting things about this filename:
1. It’s not just the name of a file; it’s a combination of a directory path and a filename. A hypothetical fileopening function could have taken two arguments — a directory path and a filename — but the open()
function only takes one. In Python, whenever you need a “filename,” you can include some or all of a
directory path as well.
