# for i in range (10) : 
#     print("Hello My Love, we die on this")

# x = 100
# y = 6

# print (x%y)

# print(x+y)

# x=90
# y=67

# if x>=y:
#     print ("Impossible arithmetic")
# if x != 17:
#     print ("Check the inputs")
# else:
#     print (x+y)

# wale_best_food = "pounded yam"
# if wale_best_food =="Rice and Plantain":
#     print ("Olawale will eat his food")
# else:
#     print ("Olawale will not touch the food")


# age = int(input("Kindly enter your age:"))

# if age < 18:
#     print("You are a minor.")
# elif 18 <= age <= 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")

# **************************************************** ARITH. CALC. ********************************************************88
# x = int(input("Kindly input value for x:"))
# y = int(input("Kindly input value for y:"))

# def f(x,y):
#     return x+y

# # # x = int(input("Kindly input value for x:"))
# # # y = int(input("Kindly input value for y:"))

# # def calculate_addition (x,y):
# #     return x+y

# # def f(x,y):
# #     return x*y
# # # # def calculate_multiply (x,y):
# # # #     return x*y

# # def f(x,y):
# #     return x-y
# # # # def calculate_subtract (x,y):
# # # #     return x-y

# # def f(x,y):
# #     if y!= 0:
# #         return x/y
# #     else:
# #         return ("Zero Division Error")
# # # # def calculate_divide (x,y):
# # # #     return x/y

# result = f(x,y)
# print(result)

# # len ("olawale")

# welcome_note = "hello world".upper ()
# print (welcome_note)

# fav_musician = ["2Baba", "Burna boy", "T.I", "Rihanna", "Wande Coal"]
# fav_musician.append ("Davido")
# fav_musician.append ("Olamide")
# fav_musician.append ("Dbanj")
# fav_musician.pop ()
# fav_musician.remove ("Rihanna")
# no_of_musician = len (fav_musician)
# print (no_of_musician)


# # places_visited = []
# year1 = input("Kindly input the name and coordinates of city visited in year 1: ")
# year2 = input("Kindly input the name and coordinates of city visited in year 2: ")
# year3 = input("Kindly input the name and coordinates of city visited in year 3: ")
# year4 = input("Kindly input the name and coordinates of city visited in year 4: ")

# # year1 = ["Lagos : 6.4541° N, 3.3947° E"]
# # year2 = ["Istanbul : 41.0151° N, 28.9795° E"]
# # year3 = ["London : 51.5074° N, 0.1278° W"]
# # year4 = ["Barcelona : 41.3851° N, 2.1734° E"]

# places_visited_overtime = [year1,year2,year3,year4]
# # places_visited_overtime = ((year1+year2+year3+year4))

# print (places_visited_overtime)

# start = input("Is that you Olawale Aturu(yes/no): ")
# def f(start):
#     if start == "yes":
#         age = input ("Kindly confirm your age: ")
#         height = input ("Kindly confirm your height: ")
#         color = input ("Kindly confirm your colour: ")
#         DOB = input ("kindly input your DOB: ")
#         olawale_attributes = {
#             "age": age,
#             "height": height,
#             "color": color,
#             "DOB": DOB
#         }
#         return olawale_attributes
#     else:
#         return "Access Denied"

# print(f(start))

# fav_songs = {
#     "Olamide": ["Baddoo", "WOTS", "Eniduro"],
#     "2Baba": ["African Queen", "Implication", "For Instance"],
#     "Burna Boy": ["Ye", "On the Low", "Anybody"],
#     "T.I": ["Whatever You Like", "Live Your Life", "No Mediocre"],
#     "Rihanna": ["Umbrella", "Diamonds", "We Found Love"],
#     "Wande Coal": ["Bumper to Bumper", "Ololufe", "Iskaba"],
#     "Davido": ["Fall", "If", "FEM"],
#     "Dbanj": ["Oliver Twist", "Fall in Love", "Suddenly"]
# }

# # song_list = list(fav_songs.keys())
# # print (fav_songs[song_list[3]])
# # print (fav_songs)

# for artist, songs in fav_songs.items():
#     new_songs = (f"{artist}: {',  '.join(songs)}")
#     print (new_songs)

# name =('Olawale ' + 'loves ' + 'His Mummy ')
# for i in range (5):
#     print (name)

# name = input ("Kindly enter your name: ")
# d_o_b = input ("Kindly enter your date of birth: ")
# origin = input ("Kindly enter your country of origin: ")

# status = "{} happens to be the country of origin of {}, born in {} " . format (origin, name, d_o_b)

# for i in range (5):
#     print (status)


# x = "CAMUS"
# print (x[0],x[1],x[2],x[3],x[4])

# write = input ("What did you write yesterday: ")
# to_who = input ("Who did you send it to: ")

# action = "Yesterday I wrote {}, I sent it to {}" . format (write, to_who)

# print (action)

# xy = "aldous huxley was born in 1984"
# xyz = xy .capitalize ()
# print (xyz)

# action = ("Where now? . Who now? . When now? . How now?")
# action_s = action .split (".")
# print (action_s)

# j = ["The", "fox",
#             "jumped", "over", "the", "fence"
#             "."
#             ]
# join_a = " ". join(j)
# print(join_a)

aturu_fam = {"Taiwo" : ["Father", "70", "Strict and Academician"], 
            "Grace" : ["Mother", "60", "Prayerful and Ambitious"], 
            "Vicky" : ["1st Child", "40", "Mature and Intelligent"], 
            "Olu" : ["2nd Child", "37", "Ambitious and Calm"], 
            "B'Femi" : ["3rd Child", "31", "Brilliant and Empathetic"], 
            "Enny" : ["4th Child", "29", "Caring and Decisive"]
}  
for names, xteristics in aturu_fam.items():
    aturu_fam_sum = (f"{names.upper()} : {', '.join(xteristics)}")
    print(aturu_fam_sum)

# aturu_fam =["Taiwo", 
#             "Grace" , 
#             "Vicky" , 
#             "Olu" , 
#             "BFemi" , 
#             "Enny" 
# ] 

# i = 0
# for names in aturu_fam:
    # # s_name = aturu_fam [i]
    # # aturu_fam [i] = s_name
    # i +=1
# print (aturu_fam)

