def check_line(Word):
    # with open ("practice.txt","w") as f:
    #     f.write("Hello! I'm Muhammad Ammar.\nI'm BS student at Air University.\nI started learning Python during my first summer break from university.")
    with open ('practice.txt','r') as f:
        word=Word
        j=1
        while True:
            line=f.readline()
            if word in line:
                print (f"word is in line {j}")
                break
            j+=1
            
check_line('University')