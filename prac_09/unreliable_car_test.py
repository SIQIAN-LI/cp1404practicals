
from prac_09.unreliable_car import UnreliableCar

test_car = UnreliableCar('Ferri', 100, 30)
print("Initial car：", test_car)

successful_drives = 0
for i in range(10):
    distance_driven = test_car.drive(10)
    print(f"Attempt {i + 1}: drove {distance_driven} km")
    if distance_driven > 0:
        successful_drives += 1

print()
print(f"Successful drives: {successful_drives} / 10")
print("Final car:", test_car)