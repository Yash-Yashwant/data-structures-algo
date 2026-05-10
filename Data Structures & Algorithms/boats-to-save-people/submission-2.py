class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boat = 0
        while l <= r: 
# here <= is imp because it is possible that will be left with 1 person, so if we do <  then that person is never onboarded a boat

            if people[l] + people[r] <=limit:
                boat+=1
                r -=1
                l+=1 
            else:
                boat+=1
                r-=1
        return boat
                