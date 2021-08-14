# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
a = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(input.splitlines())
print(len('\tsubdir'), len('subdir'))
# print(a.split('\n'))
# print(input.split('\n'))

def lengthLongestPath(input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        print(maxlen, name, depth, pathlen)
    return maxlen
print(lengthLongestPath(input))