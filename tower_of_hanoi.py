from_tower='A'
to_tower='C'
using_tower='B'
def hanoi(disk,from_tower,to_tower,using_tower):
    if disk>0:
        hanoi(disk-1,from_tower,using_tower,to_tower)
        print("Move from",from_tower,"to",to_tower)
        hanoi(disk-1,using_tower,to_tower,from_tower)
disk=int(input("Enter the number of disks: "))
hanoi(disk,from_tower,to_tower,using_tower)
