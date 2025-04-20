# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

def dailyTemperatures(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # Stack to keep track of indices of temperatures

    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature at the index stored at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()  # Get the index of the temperature that is less than the current temperature
            result[index] = i - index  # Calculate the number of days until a warmer temperature
        stack.append(i)  # Add the current index to the stack

    return result

temperature = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperature))  