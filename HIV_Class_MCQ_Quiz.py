#!/usr/bin/env python3
"""
HIV Class MCQ Quiz Script
Comprehensive Multiple Choice Questions for HIV Teaching Session
MBBS 3rd Year - Interactive Quiz Application
"""

import random
import time
from typing import List, Dict

class HIVQuiz:
    def __init__(self):
        self.questions = self.load_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        self.time_limit = 30  # seconds per question

    def load_questions(self) -> List[Dict]:
        """Load all HIV-related MCQ questions"""
        return [
            # HIV Virology and Pathogenesis
            {
                "question": "Which enzyme is responsible for converting HIV RNA to DNA?",
                "options": ["A) Protease", "B) Integrase", "C) Reverse transcriptase", "D) Helicase"],
                "answer": "C",
                "explanation": "Reverse transcriptase converts single-stranded RNA into double-stranded DNA."
            },
            {
                "question": "What is the primary target cell for HIV infection?",
                "options": ["A) B lymphocytes", "B) CD4+ T lymphocytes", "C) Macrophages", "D) Neutrophils"],
                "answer": "B",
                "explanation": "HIV primarily infects CD4+ T helper lymphocytes, leading to their depletion."
            },

            # Natural History and Staging
            {
                "question": "Which stage of HIV infection is characterized by seroconversion illness?",
                "options": ["A) Acute HIV infection", "B) Clinical latency", "C) Symptomatic HIV", "D) AIDS"],
                "answer": "A",
                "explanation": "Acute HIV infection (2-4 weeks post-exposure) presents with seroconversion illness."
            },
            {
                "question": "According to WHO clinical staging, which of the following defines AIDS?",
                "options": ["A) CD4 count <500 cells/μL", "B) CD4 count <350 cells/μL", "C) CD4 count <200 cells/μL", "D) CD4 count <50 cells/μL"],
                "answer": "C",
                "explanation": "AIDS is defined by CD4 count <200 cells/μL or presence of AIDS-defining illnesses."
            },

            # Epidemiology in India
            {
                "question": "What is the adult HIV prevalence in India according to NACO 2023?",
                "options": ["A) 0.05%", "B) 0.22%", "C) 0.50%", "D) 1.20%"],
                "answer": "B",
                "explanation": "India's adult HIV prevalence is 0.22% with 23.1 lakh people living with HIV."
            },
            {
                "question": "Which high-risk group in India has the highest HIV prevalence?",
                "options": ["A) Female sex workers", "B) Injecting drug users", "C) Men who have sex with men", "D) Migrant laborers"],
                "answer": "C",
                "explanation": "Men who have sex with men (MSM) have the highest HIV prevalence at 17% in India."
            },

            # Diagnosis
            {
                "question": "What is the window period for HIV antibody tests?",
                "options": ["A) 1-2 weeks", "B) 4-12 weeks", "C) 6-12 months", "D) 2-3 years"],
                "answer": "B",
                "explanation": "HIV antibody tests have a window period of 4-12 weeks post-exposure."
            },
            {
                "question": "Which test is used for early HIV diagnosis within 10-14 days of exposure?",
                "options": ["A) ELISA", "B) Western blot", "C) HIV RNA PCR", "D) CD4 count"],
                "answer": "C",
                "explanation": "HIV RNA PCR can detect infection as early as 10-14 days post-exposure."
            },

            # ART Guidelines
            {
                "question": "According to NACO 2023 guidelines, when should ART be initiated?",
                "options": ["A) CD4 <500 cells/μL", "B) CD4 <350 cells/μL", "C) CD4 <200 cells/μL", "D) All PLHIV regardless of CD4 count"],
                "answer": "D",
                "explanation": "NACO recommends ART initiation for all people living with HIV regardless of CD4 count."
            },
            {
                "question": "Which is the preferred first-line ART regimen in India?",
                "options": ["A) AZT + 3TC + EFV", "B) TDF + 3TC + DTG", "C) TDF + FTC + RPV", "D) ABC + 3TC + EFV"],
                "answer": "B",
                "explanation": "Tenofovir + Lamivudine + Dolutegravir (TLD) is the preferred first-line regimen."
            },

            # ART Management
            {
                "question": "What level of adherence is required for optimal viral suppression?",
                "options": ["A) >80%", "B) >90%", "C) >95%", "D) >99%"],
                "answer": "C",
                "explanation": "Greater than 95% adherence is required for optimal viral suppression and prevention of resistance."
            },
            {
                "question": "Which ART drug is contraindicated in the first trimester of pregnancy?",
                "options": ["A) Tenofovir", "B) Lamivudine", "C) Efavirenz", "D) Dolutegravir"],
                "answer": "C",
                "explanation": "Efavirenz is teratogenic and contraindicated in the first trimester of pregnancy."
            },

            # Opportunistic Infections
            {
                "question": "What is the most common opportunistic infection in HIV patients in India?",
                "options": ["A) Pneumocystis pneumonia", "B) Tuberculosis", "C) Cryptococcal meningitis", "D) Toxoplasmosis"],
                "answer": "B",
                "explanation": "Tuberculosis is the most common opportunistic infection in HIV patients in India."
            },
            {
                "question": "For which opportunistic infection is cotrimoxazole used as prophylaxis?",
                "options": ["A) Tuberculosis", "B) Cryptococcal meningitis", "C) Pneumocystis pneumonia", "D) Cytomegalovirus"],
                "answer": "C",
                "explanation": "Cotrimoxazole is used for prophylaxis against Pneumocystis pneumonia and Toxoplasma gondii."
            },

            # Prevention Strategies
            {
                "question": "What does U=U stand for in HIV prevention?",
                "options": ["A) Universal Use of condoms", "B) Undetectable equals Untransmittable", "C) Urgent Use of antiretrovirals", "D) Unified Understanding of HIV"],
                "answer": "B",
                "explanation": "U=U means Undetectable equals Untransmittable - people with undetectable viral load cannot transmit HIV sexually."
            },
            {
                "question": "What is the timeframe for initiating post-exposure prophylaxis (PEP)?",
                "options": ["A) Within 24 hours", "B) Within 48 hours", "C) Within 72 hours", "D) Within 1 week"],
                "answer": "C",
                "explanation": "PEP should be initiated within 72 hours of HIV exposure for maximum effectiveness."
            },

            # PMTCT
            {
                "question": "What is the success rate of PMTCT programs in preventing mother-to-child transmission?",
                "options": ["A) 50-60%", "B) 70-80%", "C) 90-95%", "D) 99-100%"],
                "answer": "C",
                "explanation": "Comprehensive PMTCT programs can prevent 90-95% of mother-to-child HIV transmission."
            },
            {
                "question": "When should HIV testing be done in pregnant women?",
                "options": ["A) Only if symptomatic", "B) First trimester", "C) Third trimester", "D) At delivery"],
                "answer": "B",
                "explanation": "HIV testing should be done in the first trimester of pregnancy for all women."
            },

            # Special Populations
            {
                "question": "What is the main challenge in pediatric HIV management?",
                "options": ["A) Drug resistance", "B) Adherence to medication", "C) Lack of pediatric formulations", "D) All of the above"],
                "answer": "D",
                "explanation": "Pediatric HIV management faces challenges with drug resistance, adherence, and availability of appropriate formulations."
            },
            {
                "question": "Which mental health condition is commonly associated with HIV diagnosis?",
                "options": ["A) Schizophrenia", "B) Bipolar disorder", "C) Depression", "D) Obsessive-compulsive disorder"],
                "answer": "C",
                "explanation": "Depression is commonly associated with HIV diagnosis due to stigma, lifestyle changes, and disease burden."
            },

            # Drug Resistance
            {
                "question": "What is the main cause of acquired HIV drug resistance?",
                "options": ["A) Primary infection", "B) Poor adherence", "C) Drug interactions", "D) Viral mutations"],
                "answer": "B",
                "explanation": "Poor adherence to ART regimens is the main cause of acquired HIV drug resistance."
            },
            {
                "question": "When should viral load monitoring be done after ART initiation?",
                "options": ["A) 1 month", "B) 3 months", "C) 6 months", "D) 12 months"],
                "answer": "C",
                "explanation": "Viral load should be checked at 6 months after ART initiation to assess treatment response."
            },

            # Monitoring and Follow-up
            {
                "question": "What is the target viral load for successful ART?",
                "options": ["A) <10,000 copies/mL", "B) <1,000 copies/mL", "C) <100 copies/mL", "D) Undetectable"],
                "answer": "B",
                "explanation": "Viral load <1,000 copies/mL indicates successful ART response."
            },
            {
                "question": "How often should CD4 count be monitored in patients on ART?",
                "options": ["A) Monthly", "B) Every 3 months", "C) Every 6 months", "D) Annually"],
                "answer": "C",
                "explanation": "CD4 count should be monitored every 6 months in patients on ART."
            },

            # Program Achievements
            {
                "question": "What percentage reduction in new HIV infections was achieved in India from 2007-2017?",
                "options": ["A) 33%", "B) 50%", "C) 66%", "D) 80%"],
                "answer": "C",
                "explanation": "India achieved a 66% reduction in new HIV infections from 2007-2017 through NACP."
            },
            {
                "question": "What is the current ART coverage in India?",
                "options": ["A) 50%", "B) 60%", "C) 70%", "D) 80%"],
                "answer": "D",
                "explanation": "India has achieved 80% ART coverage among people living with HIV."
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

        print("🩺 HIV Class MCQ Quiz")
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

        print("\nThank you for taking the HIV Quiz!")
        print("Remember: Knowledge about HIV saves lives! 🩺")

def main():
    """Main function to run the quiz"""
    quiz = HIVQuiz()

    print("HIV Class Interactive MCQ Quiz")
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
