person1 = ["David Doe",20,1,180.0,100.0]
person2 = ["John smit", 25,1,170.0,70.0]
person3 = ["Jane Carter",22,0,169.0,60.0]
person4 = ["Peter Kelly",40,1,150.0,50.0]
person_list = person1+person2+person3+person4
n_persons = int(len(person_list)/5)
age_sum = 0.0
for age in person_list[1::5]:
    age_sum += age
average_age = float(age_sum)/ n_persons
print("The average age is "+ str(average_age))