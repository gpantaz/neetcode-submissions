class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        prereq_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq_map[course].append(pre)

        visited = set()
        def dfs(course):
            # Found a cycle
            if course in visited:
                return False

            # Found empty path
            if not prereq_map[course]:
                return True

            visited.add(course)
            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            prereq_map[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True