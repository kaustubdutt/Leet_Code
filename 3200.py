class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red > blue:
            min_val = blue
            max_val = red
        else:
            min_val = red
            max_val = blue
        triangle = {}
        height = 0
        for i in range(1,min_val + 2):
            if i % 2 == 1 and min_val - i >= 0:
                height += 1
                triangle[i] = height
                min_val = min_val - height
            elif i % 2 == 0 and max_val - i >= 0:
                height += 1
                triangle[i] = height
                max_val = max_val - height
            else:
                break

        if red > blue:
            min_val1 = blue
            max_val1 = red
        else:
            min_val1 = red
            max_val1 = blue
        triangle2 ={}
        height1 = 0
        for i in range(1, min_val1 + 2):
            if i % 2 == 1 and max_val1 - i >= 0:
                height1 += 1
                triangle2[i] = height1
                max_val1 = max_val1 - height1
            elif i % 2 == 0 and min_val1 - i >= 0:
                height1 += 1
                triangle2[i] = height1
                min_val1 = min_val1 - height1
            else:
                break

        if len(triangle) > len(triangle2):
            print("triangle =",triangle , "min_val =",min_val , "max_val =",max_val )
            print("triangle2 =", triangle2 , "min_val =", min_val1 , "max_val =", max_val1)
            return len(triangle)
        else:
            print("triangle =",triangle , "min_val =",min_val , "max_val =",max_val )
            print("triangle2 =", triangle2 , "min_val1 =", min_val1 , "max_val1 =", max_val1)
            return len(triangle2)

solution = Solution()
result = solution.maxHeightOfTriangle(44,21)
print(result)