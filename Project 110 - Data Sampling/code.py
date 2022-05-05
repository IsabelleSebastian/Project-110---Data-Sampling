import pandas 
import plotly.figure_factory as pf
import statistics
import random

# getting the data and putting it in list
df = pandas.read_csv("data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean of Population: ", mean)
print("Standard Dev. of Population: ", stdev)


def randomSetofMean(counter):
    dataList = []
    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataList.append(value)
    mean = statistics.mean(dataList)
    return mean


# function to plot means on graph
def plotGraph(mean_list):
    df = mean_list
    graph = pf.create_distplot([df] , ["Science Data"] , show_hist=False)
    graph.show()


# function that calculates the mean of means
# function also calls 'plotGraph' function to display in graph
def setup():
    mean_list = []
    for c in range(0,100):
        meanSamples = randomSetofMean(30)
        mean_list.append(meanSamples)
    plotGraph(mean_list)

    sampleMean = statistics.mean(mean_list)
    print("Mean of Sample: ", sampleMean)

setup()


# calculating mean of population (not sampled)
population_mean = statistics.mean(data)
print("Population Mean: ", population_mean)


# function for standard deviation of sample
def sample_stdev():
    mean_stdev = []
    for a in range(0,1000):
        sample_stdev = randomSetofMean(100)
        mean_stdev.append(sample_stdev)

    stdev = statistics.stdev(mean_stdev)
    print("Standard Dev. of Sample: ", stdev)

sample_stdev()