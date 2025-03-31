import numpy as np
import matplotlib.pyplot as plt

plt.ion()
x_arr = []
y_arr = []

fig, ax = plt.subplots()
sc = ax.scatter(x_arr, y_arr) 

plt.show()



userInput = ""
print("To exit write -")
print("Enter first point(x,y):")
userInput = input()
x_temp = float(userInput.split(',')[0])
y_temp = float(userInput.split(',')[1])
x_arr.append(x_temp)
y_arr.append(y_temp)

print("Enter second point(x,y):")
userInput = input()
x_temp = float(userInput.split(',')[0])
y_temp = float(userInput.split(',')[1])
x_arr.append(x_temp)
y_arr.append(y_temp)


#updating chart
sc.set_offsets(np.c_[x_arr, y_arr]) 

ax.set_xlim([min(x_arr), max(x_arr)])  
ax.set_ylim([min(y_arr), max(y_arr)])

plt.draw()
plt.pause(0.1)


m, b = np.polyfit(np.array(x_arr), np.array(y_arr), 1)
line, = ax.plot(np.array(x_arr), m * np.array(x_arr) + b, color="red", label="correlation line")

def update_chart(x:float,y:float):
    #dots part
    x_arr.append(x)
    y_arr.append(y)
    sc.set_offsets(np.c_[x_arr, y_arr]) 
    ax.set_xlim([min(x_arr), max(x_arr)])  
    ax.set_ylim([min(y_arr), max(y_arr)])


    plt.legend()
    plt.draw() 
    print(f"correlation:{np.corrcoef(np.array(x_arr),np.array(y_arr))[0,1]}")
    m, b = np.polyfit(np.array(x_arr), np.array(y_arr), 1)
    correlation_x_arr = [min(x_arr),max(x_arr)]
    correlation_y_arr = [correlation_x_arr[0]*m + b,correlation_x_arr[1]*m + b]
    line.set_xdata(correlation_x_arr)
    line.set_ydata(correlation_y_arr)
    plt.draw()
    plt.pause(0.1)


while userInput != "-":
    print("Enter new point(x,y):")
    userInput = input()
    temp = userInput.split(',')
    try:
        update_chart(float(temp[0]), float(temp[1]))
    except IndexError:
        print("An exception occurred,less than two values")
    except ValueError:
        print("You passed invalid argument")
