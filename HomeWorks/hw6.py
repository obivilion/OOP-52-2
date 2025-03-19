def hw(lst, target):
    step = 0
    for i in nums:
        for j in nums:
            if i + j == target and nums[0] != nums[1]:
                print([nums[0], nums[1]])
                step = 1
                break
        if step == 1:
            break
    return nums[0], nums[1]


nums = [1,2,3,4,5,6,7,8,9,10]


print(nums[0] + nums[1] == 9)




# ---------------------------------------------------------------------

class Family:
    def action(self):
        return print("See you")

class Father(Family):
    def dad(self):
        return print("Dad")

class Mother(Family):
    def mom(self):
        return print("Mom")

class Daughter(Father, Mother):
    def baby(self):
        return print("My fanily")

Aya = Daughter()
Aya.action()
Aya.dad()
Aya.mom()
Aya.baby()