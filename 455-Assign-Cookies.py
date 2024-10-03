class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both the greed factors and the cookie sizes in ascending order
        g.sort()
        s.sort()

        # Initialize two pointers: one for greed factor and one for cookie sizes
        child = 0
        cookie = 0

        # Loop while both pointers are within their respective lists
        while child < len(g) and cookie < len(s):
            # If the current cookie size satisfies the current child's greed
            if s[cookie] >= g[child]:
                # Move to the next child
                child += 1
            # Move to the next cookie
            cookie += 1
        
        # Return the number of content children
        return child
