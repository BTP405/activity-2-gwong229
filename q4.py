def decorator(func):
    """prints info about a string given by printStats"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs);
        for line in result:
            if (line[-1] == '\n'):
                line = line[:-1];
                line = line.split();
                floatLine = [float(number) for number in line];
                print("Line: ", *line);
                print ("Number of elements in the line (count): ", len(floatLine));
                print ("Average of the line: ", sum(floatLine)/len(floatLine));
                print ("Max of the line: ", max(floatLine));
    return wrapper;


@decorator
def printStats(t):
    """reads a file and returns the lines"""
    file = open(t, 'r');
    lines = file.readlines();
    return lines;

printStats("q4txt.txt");