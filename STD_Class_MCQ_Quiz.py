#!/usr/bin/env python3
"""
STD Class MCQ Quiz Script
Comprehensive Multiple Choice Questions for STD Teaching Session
MBBS 3rd Year - Interactive Quiz Application

Author: Dr. Siddalingaiah H S
Professor, Community Medicine
SIMSRH, Tumkur
Email: hssling@yahoo.com
Phone: +91 8941087719

Educational content for medical students and healthcare professionals
"""

import random
import time
from typing import List, Dict, Tuple

class STDQuiz:
    def __init__(self):
        self.questions = self.load_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        self.time_limit = 30  # seconds per question

    def load_questions(self) -> List[Dict]:
        """Load all STD-related MCQ questions"""
        return [
            # Basic Concepts
            {
                "question": "Which of the following is NOT classified as a sexually transmitted disease?",
                "options": ["A) Gonorrhea", "B) Hepatitis A", "C) Syphilis", "D) Chlamydia"],
                "answer": "B",
                "explanation": "Hepatitis A is primarily transmitted through fecal-oral route, not sexual contact."
            },
            {
                "question": "What is the estimated annual burden of STD cases in India according to NACO 2023?",
                "options": ["A) 5-10 million", "B) 10-20 million", "C) 30-40 million", "D) 50-60 million"],
                "answer": "C",
                "explanation": "NACO estimates 30-40 million STD cases annually in India."
            },

            # Gonorrhea
            {
                "question": "Which Gram stain finding is characteristic of gonococcal urethritis?",
                "options": ["A) Gram-positive cocci in chains", "B) Gram-negative intracellular diplococci", "C) Gram-positive rods", "D) Acid-fast bacilli"],
                "answer": "B",
                "explanation": "Neisseria gonorrhoeae appears as gram-negative intracellular diplococci."
            },
            {
                "question": "What is the first-line treatment for uncomplicated gonorrhea according to NACO guidelines?",
                "options": ["A) Azithromycin 1g single dose", "B) Ceftriaxone 500mg IM + Azithromycin 1g PO", "C) Doxycycline 100mg twice daily × 7 days", "D) Benzathine penicillin 2.4 MU IM"],
                "answer": "B",
                "explanation": "Dual therapy with ceftriaxone and azithromycin is recommended to cover chlamydia co-infection."
            },

            # Syphilis
            {
                "question": "Which stage of syphilis is characterized by a painless genital ulcer called chancre?",
                "options": ["A) Primary syphilis", "B) Secondary syphilis", "C) Latent syphilis", "D) Tertiary syphilis"],
                "answer": "A",
                "explanation": "Primary syphilis presents with a chancre - a painless, clean-based ulcer at the site of inoculation."
            },
            {
                "question": "Which serological test is used for confirmation of syphilis infection?",
                "options": ["A) VDRL", "B) TPHA", "C) FTA-ABS", "D) Both B and C"],
                "answer": "D",
                "explanation": "TPHA and FTA-ABS are confirmatory tests for syphilis. VDRL is used for screening."
            },

            # Chlamydia
            {
                "question": "What percentage of chlamydial infections in women are asymptomatic?",
                "options": ["A) 20-30%", "B) 40-50%", "C) 70-80%", "D) 90-95%"],
                "answer": "C",
                "explanation": "70-80% of chlamydial infections in women are asymptomatic, making screening crucial."
            },
            {
                "question": "Which is the gold standard diagnostic test for Chlamydia trachomatis?",
                "options": ["A) Gram stain", "B) Culture", "C) PCR", "D) ELISA"],
                "answer": "C",
                "explanation": "Polymerase Chain Reaction (PCR) is the most sensitive and specific test for chlamydia."
            },

            # Viral STDs
            {
                "question": "Which HPV types are considered high-risk for cervical cancer?",
                "options": ["A) 6 and 11", "B) 16 and 18", "C) 31 and 33", "D) Both B and C"],
                "answer": "D",
                "explanation": "HPV 16, 18, 31, and 33 are high-risk types associated with cervical cancer."
            },
            {
                "question": "Which antiviral medication is used for episodic treatment of genital herpes?",
                "options": ["A) Acyclovir", "B) Zidovudine", "C) Lamivudine", "D) Efavirenz"],
                "answer": "A",
                "explanation": "Acyclovir is the first-line treatment for genital herpes simplex virus infection."
            },

            # Clinical Approach
            {
                "question": "What does the '5 Ps' approach in sexual history taking stand for?",
                "options": ["A) Partners, Practices, Protection, Past STDs, Pregnancy", "B) People, Places, Protection, Prevention, Planning", "C) Partners, Places, Protection, Past infections, Planning", "D) People, Practices, Protection, Prevention, Pregnancy"],
                "answer": "A",
                "explanation": "5 Ps: Partners, Practices, Protection, Past STDs, Pregnancy intentions."
            },
            {
                "question": "Which specimen collection method is preferred for diagnosing chlamydial cervicitis?",
                "options": ["A) Vaginal swab", "B) Endocervical swab/brush", "C) Urine sample", "D) Blood sample"],
                "answer": "B",
                "explanation": "Endocervical swab or brush provides the best sample for chlamydia diagnosis."
            },

            # Prevention
            {
                "question": "What is the ABC approach to HIV prevention?",
                "options": ["A) Abstain, Be faithful, Condoms", "B) Awareness, Behavior change, Condoms", "C) Abstain, Behavior change, Cure", "D) Awareness, Be faithful, Cure"],
                "answer": "A",
                "explanation": "ABC stands for Abstain from sex, Be faithful to one partner, use Condoms consistently."
            },
            {
                "question": "How many condoms does NACO distribute annually in India?",
                "options": ["A) 200 million", "B) 400 million", "C) 600 million", "D) 800 million"],
                "answer": "D",
                "explanation": "NACO distributes approximately 800 million condoms annually through various programs."
            },

            # Epidemiology
            {
                "question": "Which Indian state has the highest HIV prevalence according to NACO data?",
                "options": ["A) Maharashtra", "B) Karnataka", "C) Nagaland", "D) Tamil Nadu"],
                "answer": "C",
                "explanation": "Nagaland has the highest HIV prevalence in India at approximately 1.5%."
            },
            {
                "question": "Which high-risk group has the highest HIV prevalence in India?",
                "options": ["A) Female sex workers", "B) Injecting drug users", "C) Men who have sex with men", "D) Migrant laborers"],
                "answer": "C",
                "explanation": "Men who have sex with men (MSM) have the highest HIV prevalence at 17% in India."
            },

            # Treatment
            {
                "question": "What is the recommended treatment duration for latent syphilis?",
                "options": ["A) Single dose", "B) 7 days", "C) 14 days", "D) 3 weekly doses"],
                "answer": "D",
                "explanation": "Latent syphilis requires benzathine penicillin 2.4 MU IM weekly for 3 doses."
            },
            {
                "question": "Which antibiotic should be avoided in pregnant women with chlamydia?",
                "options": ["A) Azithromycin", "B) Amoxicillin", "C) Doxycycline", "D) Erythromycin"],
                "answer": "C",
                "explanation": "Doxycycline is contraindicated in pregnancy due to risk of fetal harm."
            },

            # Complications
            {
                "question": "Which complication is most commonly associated with untreated chlamydial infection in women?",
                "options": ["A) Endometritis", "B) Pelvic inflammatory disease", "C) Ectopic pregnancy", "D) All of the above"],
                "answer": "D",
                "explanation": "Untreated chlamydia can lead to PID, infertility, and ectopic pregnancy."
            },
            {
                "question": "What is the most common cause of infectious blindness worldwide?",
                "options": ["A) Gonococcal ophthalmia", "B) Chlamydial trachoma", "C) Syphilitic interstitial keratitis", "D) Herpetic keratitis"],
                "answer": "B",
                "explanation": "Chlamydia trachomatis causes trachoma, the leading infectious cause of blindness."
            },

            # Special Situations
            {
                "question": "In which trimester should syphilis screening be done in pregnant women?",
                "options": ["A) First trimester only", "B) Second trimester only", "C) Third trimester only", "D) First trimester, then as needed"],
                "answer": "A",
                "explanation": "Syphilis screening is mandatory in the first trimester of pregnancy."
            },
            {
                "question": "Which STD is particularly associated with increased risk of cervical cancer?",
                "options": ["A) Gonorrhea", "B) Syphilis", "C) Chlamydia", "D) HPV"],
                "answer": "D",
                "explanation": "Human Papillomavirus (HPV) infection is the primary risk factor for cervical cancer."
            }
        ]

    def shuffle_questions(self) -> None:
        """Shuffle the questions for random order"""
        random.shuffle(self.questions)

    def ask_question(self, question_data: Dict, question_number: int) -> bool:
        """Present a single question and get user response"""
        print(f"\nQuestion {question_number}/{self.total_questions}:")
        print(question_data["question"])
        print("\nOptions:")
        for option in question_data["options"]:
            print(option)

        start_time = time.time()
        while True:
            try:
                user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
                if user_answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Please enter A, B, C, or D.")
            except KeyboardInterrupt:
                print("\nQuiz interrupted by user.")
                return False

        elapsed_time = time.time() - start_time
        if elapsed_time > self.time_limit:
            print(f"Time's up! ({self.time_limit} seconds limit exceeded)")
            return False

        correct = user_answer == question_data["answer"]
        if correct:
            print("✅ Correct!")
            self.score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {question_data['answer']}.")

        print(f"Explanation: {question_data['explanation']}")
        return correct

    def run_quiz(self, num_questions: int = None) -> None:
        """Run the complete quiz"""
        if num_questions is None or num_questions > len(self.questions):
            num_questions = len(self.questions)

        self.shuffle_questions()
        selected_questions = self.questions[:num_questions]

        print("🎓 STD Class MCQ Quiz")
        print("=" * 50)
        print(f"You will be asked {num_questions} questions.")
        print(f"Time limit: {self.time_limit} seconds per question.")
        print("Good luck!\n")

        input("Press Enter to start the quiz...")

        for i, question in enumerate(selected_questions, 1):
            if not self.ask_question(question, i):
                break

        self.show_results(num_questions)

    def show_results(self, total_asked: int) -> None:
        """Display final quiz results"""
        print("\n" + "=" * 50)
        print("🎯 QUIZ RESULTS")
        print("=" * 50)
        print(f"Questions answered: {total_asked}")
        print(f"Correct answers: {self.score}")
        percentage = (self.score / total_asked) * 100
        print(f"Percentage: {percentage:.1f}%")
        # Performance feedback
        if percentage >= 90:
            print("🌟 Excellent! Outstanding performance!")
        elif percentage >= 80:
            print("👍 Very Good! Well done!")
        elif percentage >= 70:
            print("👌 Good! Keep studying!")
        elif percentage >= 60:
            print("📚 Satisfactory! Review the material again.")
        else:
            print("📖 Needs improvement. Focus on key concepts.")

        print("\nThank you for taking the STD Quiz!")
        print("Remember: STD knowledge saves lives! 🩺")

def main():
    """Main function to run the quiz"""
    quiz = STDQuiz()

    print("STD Class Interactive MCQ Quiz")
    print("Choose quiz mode:")
    print("1. Full Quiz (20 questions)")
    print("2. Quick Quiz (10 questions)")
    print("3. Practice Quiz (5 questions)")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                quiz.run_quiz(20)
            elif choice == 2:
                quiz.run_quiz(10)
            elif choice == 3:
                quiz.run_quiz(5)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (1-3).")

if __name__ == "__main__":
    main()
