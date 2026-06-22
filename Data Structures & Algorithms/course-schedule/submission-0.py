class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses_dict = {}
        
        for i in range(0,len(prerequisites)):
            try:
                courses_dict[prerequisites[i][0]]
            except KeyError:
                courses_dict[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                courses_dict[prerequisites[i][0]].append(prerequisites[i][1])

        visited = {}
        visiting = {}

        def dfs(course):
            nonlocal is_poss

            try:
                courses_dict[course]
            except KeyError:
                visited[course] = 1
                return None
            else:
                if course in visited:
                    return None
                visiting[course] = 1
                for prereq in courses_dict[course]:
                    if prereq in visiting:
                        is_poss = False
                        return None
                    dfs(prereq)
                del visiting[course]
                visited[course] = 1

            return None


        for course in courses_dict:
            if course not in visited:
                is_poss = True
                dfs(course)
                if is_poss == False:
                    return False     

        return True   