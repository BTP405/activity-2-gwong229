import matplotlib.pyplot as plt;
def graphSnowfall(t):
    """This function takes information from a file, splits it, and counts
    the number that falls within each temperature range. Then the information
    is graphed on a bar graph"""
    #opens file
    file = open(t, 'r');
    content = file.readlines();
    
    #removes newlines and converts to integers
    count = 0;
    for line in content:
        if (line[-1] == '\n'):
            content[count] = line[:-1];
        content[count] = int(content[count]);
        count += 1;

    #initial dictionary
    graphDict = {"0 - 10 cms": 0, "11 - 20 cms": 0, "21 - 30 cms": 0, "31 - 40, cms": 0, "41 - 50 cms": 0}

    #adds for each record
    for fall in content:
        if ((fall >= 0) and (10 >= fall)):
            graphDict["0 - 10 cms"] = graphDict["0 - 10 cms"] + 1;
        elif ((fall >= 10) and (20 >= fall)):
            graphDict["11 - 20 cms"] = graphDict["11 - 20 cms"] + 1;
        elif ((fall >= 20) and (30 >= fall)):
            graphDict["21 - 30 cms"] = graphDict["21 - 30 cms"] + 1;
        elif ((fall >= 30) and (40 >= fall)):
            graphDict["31 - 40 cms"] = graphDict["31 - 40 cms"] + 1;
        elif ((fall >= 40) and (50 >= fall)):
            graphDict["41 - 50 cms"] = graphDict["41 - 50 cms"] + 1;
    

    #splits the dictionary
    ranges = list(graphDict.keys());
    values = list(graphDict.values());

    #creates bar graph and saves to snofall bar.png
    plt.bar(ranges, values);
    plt.xlabel("snowfall ranges");
    plt.ylabel("days");
    plt.title("snowfall accumulation");
    plt.savefig("snowfall bar");

    file.close();
graphSnowfall("falls.txt");