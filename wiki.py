import wikipedia;

while True:
    query = input("Enter :")
    if query.lower() == 'exit':
        print("Exiting...")
        break
    ans = wikipedia.summary(query,sentences=2)
    print("Wikipedia:",ans)
