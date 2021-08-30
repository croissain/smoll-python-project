import random, os
from pygame import mixer
mixer.init()
os.system("cls")
print("Trò chơi đoán tên bài hát đơn giản")
print("By Ngọc Phát")
print()
print("Luật chơi: Trong trò chơi này, mỗi bài hát sẽ được phát trong 20s, bắt đầu tại 1 thời điểm ngẫu nhiên trong file nhạc. Nghe và chọn đáp án. Thời gian cho mỗi câu hỏi là 30s.")
print("Gõ chữ a để tua tới 5s. Enter để tiếp tục")
_ = input()
#Nạp file và câu hỏi
f = open("questions.honk", mode = "r")
questions = list()
for lines in f:
    questions.append(list(lines.split(";")))
f.close()
random.shuffle(questions)
i = 1
score = 0
answers = list()
#Bắt đầu
os.system("cls")
for song in questions:
    print("Câu hỏi thứ", i)
    #Nạp đáp án
    answers.append(song[0])
    while len(answers) < 4:
        j = random.randint(0, len(questions) - 1)
        if questions[j][0] not in answers:
            answers.append(questions[j][0])
    random.shuffle(answers)
    #Nạp file nhạc
    filename = "songfiles\\"+song[1]
    mixer.music.load(filename)
    mixer.music.play(0, float(random.randint(0,180)))
    #In câu hỏi và chờ đáp án
    for t in range(0,4):
        print(str(t+1) + ". " + answers[t])
    ans = "a"
    while (ans=="a"):
        ans = input("Câu trả lời: ")
        if ans == "a":
            os.system("cls")
            print("Câu hỏi thứ", i)
            for t in range(0,4): print(str(t+1) + ". " + answers[t])
            mixer.music.set_pos(5)
            print("Đã tua tới 5s\n")
        else:
            ans = int(ans) - 1
           
    #Ktra đáp án, dừng file nhạc
    if (answers[ans] == song[0]):
        print("\nChính xác!")
        print("Tên bài hát:",song[0])
        score += 1
    else:
        print("\nSai!")
        print("Đáp án đúng:",song[0])
    mixer.music.fadeout(1000)
    i+=1
    answers.clear()
    _ = input()
    os.system("cls")
 
i -=1
print("Điểm số: " + str(score*10) + "/" + str(i*10))
_ = input()