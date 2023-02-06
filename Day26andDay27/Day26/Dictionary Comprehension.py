import random

# new_dict = {new_key : new_value for item in list}

# new_dict = {new_key : new_value for (key, value) in dict.items() if condition}

names = ['Manas', 'Shaily', 'Manoj', 'Suman', 'Anshi']

student_scores = {new_key: random.randint(1, 100) for new_key in names}
print(student_scores)
passed_student = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_student)

sentence = "What is the airspeed velocity of an unladen Swallow?"
list_of_words = sentence.split(" ")
words_length = {words: len(words) for words in list_of_words}
# or
words_length2 = {words: len(words) for words in sentence.split(" ")}
print(words_length)


def celcius_to_farenhite(num):
    return round(((num * (9 / 5)) + 32), 2)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: celcius_to_farenhite(tem) for (day, tem) in weather_c.items()}
print(weather_f)
