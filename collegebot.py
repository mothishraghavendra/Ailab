print("------Welcome to JNTUA assistant------");
while(True):
    you = input("YOU :");
    lis = you.lower().split()
    if "course" in lis or "courses" in lis:
        print("BOT: We offer various courses which include B Tech , M Tech , MBA , MCA")
    elif "department" in lis or "departments" in lis:
        print("BOT: we have CSE,ECE,EEE,MECH,CHEM,CIVIL")
    elif "exit" in lis or "bye" in lis:
        print("BOT:bye")
        break;
    elif "hi" in lis or "hello" in lis:
        print("BOT: Hello welcome to JNTUCEA, how can i help you?")
    else:
        print("BOT: sorry i didnt recoginze you")