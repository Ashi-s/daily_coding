# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

# Return the modified image after performing the flood fill.

def floodFill(image, sr, sc, newColor):
  # lst = [(sr, sc+1), (sr, sc-1), (sr-1, sc), (sr+1, sc)]
  val = image[sr][sc]
  image[sr][sc] = newColor
  dfs(sr, sc, image, newColor, val)
  # for r, c in lst:
  #   if r >= 0 and r < len(image) and c >=0 and c < len(image[r]) and image[r][c] == val:
  #     image[r][c] = newColor
  #     dfs(r, c, image, newColor, val)
  return image
        
def dfs(r, c, image, newColor, val):
  lst = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]
  for r1, c1 in lst:
      if r1 >= 0 and r1 < len(image) and c1 >=0 and c1 < len(image[r]) and image[r1][c1] == val:
        image[r1][c1] = newColor
        dfs(r1, c1, image, newColor, val)
          
          
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
# print(floodFill([[0,0,0],[0,1,0]],0,0,2))