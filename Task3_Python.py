#   class human(Researcher):
#     "'my classs inherits from human an adds teaches as a paramter'"
#      def __init__(self,Name,Occupation,subject)
#      super __init__(self,Name,Occupation)
#      self.subject

# # Part 1
# def __str__(self):
#   return "the human surname:" + self.lastname

# # Part 2


# def isPalindrome(s): 
#     return s == s[::-1] 
  
  
# # Driver code 
# s = "suban"
# ans = isPalindrome(s) 
  
# if ans: 
#     print("Yes") 
# else: 
#     print("No")
# current date and time 

# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)


# import calendar
# for i in range(1,12):
#   print(calendar.month_name[i])

# import datetime

# today = datetime.date.today()
#  print(today)

# print('Month:', today.month)

# d week number of the year
# from datetime import date

# weekNumber = date.today().isocalendar()[1]
# print ('Week number:', weekNumber)

# import datetime 
# import calendar 
  
# def findDay(date): 
#     born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
#     return (calendar.day_name[born]) 
  
# # Driver program 
# date = '03 02 2019'
# print(findDay(date)) 

# import datetime
# today = datetime.datetime.now()
# day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
# print(day_of_year)

# import datetime
# dt = datetime.datetime.today()
# print (dt)



# from datetime import date, timedelta
# dt = date.today() - timedelta(30)
# print('Current Date :',date.today())
# print('30 days before Current Date :',dt)


# import re
# def text_match(text):
#         patterns = '^[a-zA-Z0-9_]*$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

# print(text_match("This is question 4"))
# print(text_match("Python_Assignment_4"))