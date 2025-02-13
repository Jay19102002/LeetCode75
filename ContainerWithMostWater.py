# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height) - 1

# Initialize the maximum area to 0
max_area = 0

# Traverse the array from both ends towards the center
while left < right:
    # Calculate the width of the container
    width = right - left

    # Calculate the height of the container
    min_height = min(height[left], height[right])
    
    # Calculate the area of the container
    area = width * min_height                                   # current water

    # Update the maximum area if the current area is larger
    max_area = max(max_area, area)                              # max water
    
    # Move the pointer of the shorter bar towards the center
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(max_area)

