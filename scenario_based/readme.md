# Leetcode Problems

## Problem 1 - Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

**Example 1:**

![alt text](image.png)

**Input**: height = [1,8,6,2,5,4,8,3,7] <br/>
**Output**: 49 <br/>
**Explanation**: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. <br/> 


**Example 2:**

**Input**: height = [1,1] <br/>
**Output**: 1

The Python code you've provided, `maxArea`, solves the "Container With Most Water" problem. The goal is to find the two lines (from a given list of heights) that, along with the x-axis, form a container that can hold the most water.

### Problem Breakdown

Imagine you have a series of vertical lines of varying heights. You want to pick two of these lines to form a container. The amount of water this container can hold is limited by the shorter of the two lines and the distance between them. The area is calculated as **height \* width**, where the height is the `min` of the two line heights and the width is the distance between them. The challenge is to maximize this area.

\<br\>

### Solution

```python
def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) -1
    max_area = 0
    while left != right:
        curr = min([height[left], height[right]]) * (right-left)
        max_area = max([max_area, curr])

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

\<br\>

### The Two-Pointer Approach

The code uses a clever and efficient technique called the **two-pointer approach**. This method starts with two pointers, one at the very beginning (`left`) and one at the very end (`right`) of the `height` list.

  * `left`: Starts at the index `0`.
  * `right`: Starts at the last index, `len(height) - 1`.
  * `maxArea`: A variable to keep track of the maximum area found so far, initialized to `0`.

The code then enters a `while` loop that continues as long as the `left` pointer is to the left of the `right` pointer (`left < right`).

\<br\>

### Step-by-Step Logic

Inside the loop, the algorithm performs these steps:

1.  **Calculate `currentArea`**: It calculates the area of the container formed by the lines at the `left` and `right` pointers. The height of this container is determined by the shorter of the two lines, `min(height[left], height[right])`. The width is the distance between them, `right - left`.
2.  **Update `maxArea`**: It compares the `currentArea` with the `maxArea` found so far and updates `maxArea` if the `currentArea` is larger.
3.  **Move the Pointers**: This is the most crucial part. The goal is to potentially find a larger area. To do this, the algorithm moves the pointer of the **shorter line** inward.
      * If `height[left] < height[right]`, it means the height of the container is limited by the left line. To possibly increase the area, we need a taller left line, so we move the left pointer to the right (`left += 1`). Moving the right pointer in this case would only decrease the width and the height (as the new container would still be limited by the same short left line), guaranteeing a smaller or equal area.
      * If `height[left] >= height[right]`, the height is limited by the right line. We move the right pointer to the left (`right -= 1`) to potentially find a taller line.

The loop continues, calculating and comparing areas, until the pointers meet. By moving the shorter pointer, we strategically explore combinations that have the best chance of increasing the area, avoiding unnecessary calculations.

