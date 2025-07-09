def mol_to_per(a, m, d):
    return (a*m)/10*d

def per_to_mol(a, w, d):
    return w/(10*a*d)

menu = input("무엇을 찾으시겠습니까?\n1. 퍼센트 농도   2. 몰 농도\n")
if menu == "1":
    a, m, d = map(float, input("화학식량, 몰 농도, 밀도를 순서대로 입력하세요(각각 띄어쓰기로 구분)").split())
    print(mol_to_per(a, m, d))

elif menu == "2":
    a, w, d = map(float, input("화학식량, 퍼센트 농도, 밀도를 순서대로 입력하세요(각각 띄어쓰기로 구분)").split())
    print(per_to_mol(a,w,d))

