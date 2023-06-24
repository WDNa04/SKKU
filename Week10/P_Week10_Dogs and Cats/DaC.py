def dog_sound():
    print("woof")
def cat_sound():
    print("meow")
num_dogs = int(input("Enter number of dogs: "))
num_cats = int(input("Enter number of cats: "))

for i in range(num_dogs):
	dog_sound()
	
for j in range(num_cats):
	cat_sound()
