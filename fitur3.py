def main():
    run = True
    print("*****Quiz Game*****")
    print("Apa rumus dari BMI(Body Mass Index)?")
    print("A. Berat Badan / (Tinggi Badan)^2 ")
    print("B. Berat Badan / Tinggi Badan ")
    print("C. (Tinggi Badan)^2 / Berat Badan ")
    print("D. (Berat Badan)^2 / Tinggi Badan ")
    x = input("Masukkan jawaban: ")
    if x == "A":
        print("Anda Benar!")
    elif x == "B" or x == "C" or x == "D":
        print("Anda Salah!")
    else:
        print("Masukkan huruf A, B, C, atau D")

if __name__ == "__main__":
    main()
