def findDuplicates(nums):
        out= []
        nums=sorted(nums)

        if len(nums)<= 1:
            return []

        for i,num in enumerate(nums):
            if nums[i] == nums[i-1]:
                out.append(nums[i])

        return list(set(out))
