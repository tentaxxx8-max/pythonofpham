def calculate(total,tip):
    tipresult = (total * tip)/100
    total = total + tipresult 
    print(f"tip:{tipresult}")
    print(f"total:{total}")

def totalandtip():
    raw_total = input("Please type how much total").strip().replace("$", "")
    raw_tip = input("type percentage of tip you want to tip").strip().replace("%", "")
    total = float(raw_total)
    tip = float(raw_tip)
    calculate(total,tip)

if __name__=="__main__":
    totalandtip()