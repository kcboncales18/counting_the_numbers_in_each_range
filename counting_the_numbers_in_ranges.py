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