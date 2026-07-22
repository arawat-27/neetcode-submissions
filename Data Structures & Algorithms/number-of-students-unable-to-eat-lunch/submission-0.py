class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n

        for s in sandwiches:
            count = 0
            while count < n and q[0] != s:
                cur = q.popleft()
                q.append(cur)
                count += 1

            if q[0] == s:
                q.popleft()
                res -= 1
                #remove i and j from both list
            else:
                break
                #remove i + add to the end
        return res
