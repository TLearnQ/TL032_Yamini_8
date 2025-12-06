def csv_data():
    l = [45,67,89,23,56]
    t = sum(l)
    avg = t // len(l)
    print(avg)
    if avg >= 80 and avg <= 100:
        print("Overloaded")
    elif avg >= 60 and avg < 80:
        print("Busy")
    elif avg >= 40 and avg < 60:
        print("Normal")
    elif avg >= 20 and avg < 40:
        print("Idle")
    else:
        print("invalid")
csv_data()