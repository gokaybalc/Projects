"""
Summary of what the function is for
Parameters:

x(float):The input float given by the user
power(integer): The input integer given by the user

Returns:
type: None"""
def root(x,power):
    x1=min(-1,x)
    x2=max(1,x)
    mean=3
    epsilon=0.0000001
    while abs(mean**power-x)>epsilon:
        mean=((x1)+(x2))/2
        if (mean**power)<x:
            x1=mean
        else:
            x2=mean
    print(mean)
    return
            
root(x=int(input("Enter the number: ")),power=int(input("Enter the power: ")))

input("Press ENTER to exit")

        








