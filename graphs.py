from matplotlib import pyplot as plt #imports matplotlib for use with graphs
plt.style.use('seaborn-whitegrid')
import csv #imports CSV files for use with matplotlib

x = []
y = []
xa = []
ya = []

with open('bagweights.csv','r') as csvfile: #selects and reads thnvvnn nsi[sjntreifdi0asifik--e bagweight csv file
    plots = csv.reader(csvfile, delimiter=',')
    next(plots) #skips the first row in the file
    for row in plots:
        x.append(int(row[1]))
        y.append(int(row[2]))
        xa.append((row[3]))
        ya.append(int(row[4]))

# First Subplot
plt.subplot(1, 2, 1)
plt.scatter(x, y, marker='o',color='green')
plt.title('Barcode vs Day Scanned')
plt.xlabel('Barcode')
plt.ylabel('Day')

# Second Subplot
plt.subplot(1, 2, 2)
plt.scatter(xa, ya, marker='o', color='steelblue')
plt.title('Time vs Weight')
plt.xlabel('Time')
plt.ylabel('Weight')

plt.subplots_adjust(top=0.95, wspace=0.35) #adjusts subplots manually
plt.subplots_adjust(bottom=0.1)
plt.subplots_adjust(right=0.9)

plt.savefig('plot1.png') #saves plot as an image for use in the HTML format
