def hanoi(n,start,auxiliary,end):
    if n == 1:
        print(f"move disk 1 from {start} to {end}")
        return
    hanoi(n-1,start,end,auxiliary)
    print(f"move disk {n} from {start} to {end}")
    hanoi(n-1,auxiliary,end,start)

hanoi(3,'A','B','C')