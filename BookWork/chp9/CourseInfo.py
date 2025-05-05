
#courseNumber: [classRoom, teacher, time]
courseInfo = {
    'CS101': [3004, 'Haynes', '8:00 a.m.'],
    'CS102': [4501, 'Alvarado', '9:00 a.m.'],
    'CS103': [6755, 'Rich', '10:00 a.m.'],
    'NT110': [1244, 'Burke', '11:00 a.m.'],
    'CM241': [1411, 'Lee', '1:00 p.m.'],
}

def main():
    while True:
        #makes sure they put in an actual course
        course = input("Enter course number: ").upper()
        if course in courseInfo:
            #prints everything
            print(courseInfo[course][0])
            print(courseInfo[course][1])
            print(courseInfo[course][2])
            #ends loop
            break

main()