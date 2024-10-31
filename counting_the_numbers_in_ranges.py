#counting_the_numbers_in_each_range

#dictionary_for_the_range_of_numbers
range_category= {"range_1":0,
                 "range_2":0,
                 "range_3":0,
                 "range_4":0,
                 "range_5":0
                 }

#asking_the_user_to_input
def asking_user():
  try:
    asking_user=int(input("Please,input a number: "))
    return asking_user
  except:
    print("Error.")
    return None
  
#determining_the_range_category_of_the_numbers
def get_the_range(numbers):
    if numbers>=1 and numbers<= 10:
        range_category["range_1"] +=1  #updates_the_dictionary
    elif numbers>=11 and numbers<=20:
        range_category["range_2"] +=1
    elif numbers>=21 and numbers<=30:
        range_category["range_3"] +=1
    elif numbers>=31 and numbers<=40:
        range_category["range_4"] +=1
    elif numbers>=41 and numbers<=50:
        range_category["range_5"] +=1
    else:
       numbers<=1 and numbers>=50
       print("Invalid.")  #will_print_invalid
       print("range counts:",range_category) #will_display_the_range_counts_and_category