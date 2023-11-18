import numpy as np
from matplotlib import pylab

def read_csv(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = [ line.strip().split(',') for line in lines[1:] ]
    data = np.array(data).astype('float')
    return header,data

filename_one = "data/dataset-one.csv"
header,data = read_csv(filename_one)
examples,labels = data[:,:-1],data[:,-1]

print("=== header")
print(header)
print("=== first 10 examples")
print(examples[:10])
print("=== first 10 labels")
print(labels[:10])

def plot(examples,labels,a,b,color="red"):
    x0,x1 = min(examples),max(examples)
    y0 = a[0]*x0 + b
    y1 = a[0]*x1 + b

    pylab.scatter(examples,labels,color=color)
    pylab.plot([x0,x1],[y0,y1],'k-')
    pylab.xlabel('exercise')
    pylab.ylabel('cholesterol')

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(examples,labels)
print("model: y = %.4f x + %.4f (ax + b)" % (model.coef_,model.intercept_))
plot(examples,labels,model.coef_,model.intercept_)
pylab.savefig('one.png')
pylab.savefig('one.pdf')
pylab.close()

filename_two = "data/dataset-two.csv"
header,data = read_csv(filename_two)
all_examples,all_labels = data[:,:-1],data[:,-1]
ages = all_examples[:,0]



base_ages = [20,30,40,50,60,70]
colors = ["red","orange","yellow","green","blue","violet"]
for base_age,color in zip(base_ages,colors):
    indices = (base_age <= ages) & (ages < base_age+10)
    examples = all_examples[indices][:,1].reshape(-1,1)
    labels = all_labels[indices]

    model = LinearRegression()
    model.fit(examples,labels)
    print("ages: [%d,%d)" % (base_age,base_age+10))
    print("model: y = %.4f x + %.4f (ax + b)" % (model.coef_,model.intercept_))
    plot(examples,labels,model.coef_,model.intercept_,color=color)
pylab.savefig('two.png')
pylab.savefig('two.pdf')
pylab.close()
