#Name: Amruth Kanakaraj
#Student ID: 201547293

""" Implement a simplified version of k-means algorithm using Python to
cluster a toy dataset comprising five data points into two clusters.
More specifically, consider the following dataset comprising five data points (2-dimensional)
{(0; 0); (1; 0); (1; 1); (0; 1); (-1; 0)} """


#Importing math library to use sqrt for ease of programming.
from math import sqrt

#defining mean separately to keep one common loop for both centroids.
def mean(clusterpoints):
    #defining size variable to find length of the list so average can be found.
    size = len(clusterpoints)
    xsum = 0
    ysum = 0
    for point in clusterpoints:
        xsum += point[0]
        ysum += point[1]
    #average or finding mean
    xmean = xsum/size
    ymean = ysum/size
    return [xmean,ymean]



#main fucntion program
def main():
    #Given data points as input. Note that I used lists despite fixed data as lists are mutable.
    dataPoints= [[0,0],[1,0],[1,1],[0,1],[-1,0]]
    print("Given datapoints are:", dataPoints,"\n")
    #Defined centroid one as c1 & centroid two as c2.
    c1 = [1,0]
    c2 = [1,1]
    print("Initial position of the centroid c1:", c1,"\n")
    print("Initial position of the centroid c2:", c2,"\n")
    #set up an iteration lable to show the number of iterations
    #a for loop for the 2 iterations
    for i in range(0,2):
    #empty lists to be filled or appended later by the program.
        c1DistanceList = []
        c2DistanceList = []
        #for loop to compute the distance "d" from c1 and c2,.
        for point in dataPoints:
            #setting values for x1,y1 & x2,y2
            x1,y1 = point
            x2,y2 = c1
            #computing the distance with the below formula
            c1topointdist = sqrt(((x2-x1)**2)+((y2-y1)**2))
            #appending the distance calculated
            c1DistanceList.append(c1topointdist)
            
            x2,y2 = c2
            
            c2topointdist = sqrt(((x2-x1)**2)+((y2-y1)**2))
            c2DistanceList.append(c2topointdist)
        #creating a list to store the cluster points close to the nearest centroids
        c1Cluster = []
        c2Cluster = []
        #for loop to append points to the list
        for j , d1 , d2 in zip(range(len(dataPoints)),c1DistanceList,c2DistanceList):
            if d1 <= d2:
                c1Cluster.append(dataPoints[j])
            else:
                c2Cluster.append(dataPoints[j])
        #taking the mean of both centroids and checking if the value is same after each iteration.
        c1 = mean(c1Cluster)
        c2 = mean(c2Cluster)
        #printing the iterations
        print("Iteration : ", i+1,"\n")
        print("The updated centroid c1 is : ", c1, "\n")
        print("The updated centroid c2 is : ", c2 ,"\n")
        print("\n")
    

#calling main function
main()