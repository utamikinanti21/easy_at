import random

def quiz_diet():
    questions = [
        {
            "question": "Berapa gelas air yang disarankan diminum setiap hari?",
            "options": ["A. 2-3 gelas", "B. 5-6 gelas", "C. 8 gelas", "D. 12 gelas"],
            "answer": "C"
        },
        {
            "question": "Makanan mana yang paling tinggi kandungan proteinnya?",
            "options": ["A. Roti", "B. Telur", "C. Nasi", "D. Pisang"],
            "answer": "B"
        },
        {
            "question": "Untuk diet sehat, sarapan sebaiknya dilakukan jam?",
            "options": ["A. 6-9 pagi", "B. 10-12 siang", "C. Tidak perlu sarapan", "D. Sore hari"],
            "answer": "A"
        }
    ]

    print("=== QUIZ DIET SEHAT ===")
    random.shuffle(questions)
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        ans = input("Jawaban kamu (A/B/C/D): ").upper()
        if ans == q["answer"]:
            print("✅ Benar!")
            score += 1
        else:
            print(f"❌ Salah! Jawaban yang benar: {q['answer']}")
    print(f"\nSkor akhir kamu: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_diet()
