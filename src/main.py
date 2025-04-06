from random import randint


def generate(m=10, x1=(-1, 1), x2=(-1, 1)):
    data = []
    
    for x in range(m):
        data.append([randint(*x1), randint(*x2)])

    return data


def boundary(x1=(-1, 1), x2=(-1, 1)):
    point1 = [randint(*x1), randint(*x2)]
    point2 = [randint(*x1), randint(*x2)]

    try: 
        m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        b = point1[1] - (m * point1[0])
        return (b, -m, 1)
    except ZeroDivisionError:
        boundary()
    
    return boundary()
        

def predict(weight, data):

    for x in range(len(data)):
        if weight[0] <= data[x][0] * weight[1] + data[x][1] * weight[2]:
            data[x].append(1)
        else:
            data[x].append(-1)
        
    return data

        
if __name__ == '__main__':
    x_ext = generate()
    w = boundary()
    x = predict(w, x_ext)
    print(x)