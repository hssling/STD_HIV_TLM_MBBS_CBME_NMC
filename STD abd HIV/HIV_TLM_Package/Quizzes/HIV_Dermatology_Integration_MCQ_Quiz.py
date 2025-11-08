#!/usr/bin/env python3
"""
HIV Dermatology Integration MCQ Quiz Script
Comprehensive Multiple Choice Questions for HIV Teaching Session with Dermatology Focus
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
from typing import List, Dict, Union

class HIVDermatologyQuiz:
    def __init__(self):
        self.questions = self.load_questions()
        self.score = 0
        self.total_questions = len(self.questions)
        self.time_limit = 45  # seconds per question (increased for dermatology focus)

    def load_questions(self) -> List[Dict]:
        """Load all HIV dermatology integration MCQ questions"""
        return [
            # Etiology - Easy
            {
                "question": "Which of the following is the primary causative agent of HIV infection?",
                "options": ["A) Hepatitis B virus", "B) Human Immunodeficiency Virus", "C) Human Papillomavirus", "D) Cytomegalovirus"],
                "answer": "B",
                "type": "single",
                "difficulty": "easy",
                "explanation": "HIV (Human Immunodeficiency Virus) is the causative agent of AIDS.",
                "reference": "HIV Dermatology Integration Handouts, Section 1: Etiology"
            },
            {
                "question": "HIV belongs to which family of viruses?",
                "options": ["A) Flaviviridae", "B) Retroviridae", "C) Herpesviridae", "D) Poxviridae"],
                "answer": "B",
                "type": "single",
                "difficulty": "easy",
                "explanation": "HIV is a retrovirus belonging to the Lentivirus subfamily of Retroviridae family.",
                "reference": "HIV Dermatology Integration Handouts, Section 1: Etiology"
            },

            # Epidemiology - Medium
            {
                "question": "According to NACO 2023, what is the adult HIV prevalence in India?",
                "options": ["A) 0.05%", "B) 0.22%", "C) 0.50%", "D) 1.20%"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "India's adult HIV prevalence is 0.22% with 23.1 lakh people living with HIV.",
                "reference": "HIV Dermatology Integration Handouts, Section 2: Epidemiology"
            },
            {
                "question": "Which Indian state has the highest HIV prevalence?",
                "options": ["A) Maharashtra", "B) Karnataka", "C) Nagaland", "D) Tamil Nadu"],
                "answer": "C",
                "type": "single",
                "difficulty": "medium",
                "explanation": "Nagaland has the highest HIV prevalence at 1.5% in India.",
                "reference": "HIV Dermatology Integration Handouts, Section 2: Epidemiology"
            },

            # Transmission - Easy
            {
                "question": "What is the most common mode of HIV transmission in India?",
                "options": ["A) Homosexual contact", "B) Injecting drug use", "C) Heterosexual contact", "D) Blood transfusion"],
                "answer": "C",
                "type": "single",
                "difficulty": "easy",
                "explanation": "Heterosexual transmission accounts for 87% of HIV infections in India.",
                "reference": "HIV Dermatology Integration Handouts, Section 3: Transmission"
            },
            {
                "question": "Which of the following is NOT a mode of HIV transmission?",
                "options": ["A) Sharing contaminated needles", "B) Mother-to-child transmission", "C) Casual contact like hugging", "D) Unprotected sexual intercourse"],
                "answer": "C",
                "type": "single",
                "difficulty": "easy",
                "explanation": "HIV is not transmitted through casual contact, saliva, or insect bites.",
                "reference": "HIV Dermatology Integration Handouts, Section 3: Transmission"
            },

            # Incubation Period - Medium
            {
                "question": "What is the typical window period for HIV antibody tests?",
                "options": ["A) 1-2 weeks", "B) 2-12 weeks", "C) 6-12 months", "D) 2-3 years"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "The window period for HIV antibody tests is 2-12 weeks post-exposure.",
                "reference": "HIV Dermatology Integration Handouts, Section 4: Incubation Period"
            },

            # Pathophysiology - Hard
            {
                "question": "Which enzyme is responsible for converting HIV RNA to DNA?",
                "options": ["A) Protease", "B) Integrase", "C) Reverse transcriptase", "D) Helicase"],
                "answer": "C",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Reverse transcriptase converts single-stranded viral RNA into double-stranded DNA.",
                "reference": "HIV Dermatology Integration Handouts, Section 5: Pathophysiology"
            },
            {
                "question": "What is the primary target cell for HIV infection?",
                "options": ["A) B lymphocytes", "B) CD4+ T lymphocytes", "C) Neutrophils", "D) Platelets"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "HIV primarily infects CD4+ T helper lymphocytes, leading to their depletion.",
                "reference": "HIV Dermatology Integration Handouts, Section 5: Pathophysiology"
            },

            # Clinical Features - Dermatological Emphasis - Multiple questions
            {
                "question": "Which dermatological condition is most commonly associated with HIV infection?",
                "options": ["A) Psoriasis", "B) Seborrheic dermatitis", "C) Acne vulgaris", "D) Vitiligo"],
                "answer": "B",
                "type": "single",
                "difficulty": "easy",
                "explanation": "Seborrheic dermatitis is the most common HIV-associated dermatosis, presenting with greasy, scaly patches.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "Kaposi sarcoma in HIV patients is associated with which virus?",
                "options": ["A) EBV", "B) CMV", "C) HHV-8", "D) HPV"],
                "answer": "C",
                "type": "single",
                "difficulty": "medium",
                "explanation": "Kaposi sarcoma is caused by Human Herpesvirus 8 (HHV-8) and is more aggressive in HIV patients.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "Which of the following is a marker of immunosuppression in HIV patients?",
                "options": ["A) Oral candidiasis", "B) Oral hairy leukoplakia", "C) Angular cheilitis", "D) All of the above"],
                "answer": "D",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Oral candidiasis, hairy leukoplakia, and angular cheilitis are all markers of immunosuppression in HIV.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "In HIV patients, herpes zoster typically presents as:",
                "options": ["A) Localized single dermatome", "B) Multidermatomal involvement", "C) Disseminated infection", "D) Oral ulcers only"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "In HIV patients, herpes zoster often presents with multidermatomal involvement due to immunosuppression.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "Which CD4 count range is associated with Kaposi sarcoma?",
                "options": ["A) CD4 >500 cells/μL", "B) CD4 200-500 cells/μL", "C) CD4 <200 cells/μL", "D) Any CD4 count"],
                "answer": "B",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Kaposi sarcoma typically occurs when CD4 count is between 200-500 cells/μL.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "Multiple Response: Which dermatological conditions are commonly seen in HIV patients? (Select all that apply)",
                "options": ["A) Seborrheic dermatitis", "B) Kaposi sarcoma", "C) Oral hairy leukoplakia", "D) Herpes zoster", "E) Psoriasis"],
                "answer": ["A", "B", "C", "D"],
                "type": "multiple",
                "difficulty": "medium",
                "explanation": "Seborrheic dermatitis, Kaposi sarcoma, oral hairy leukoplakia, and herpes zoster are common in HIV patients.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },

            # Complications - Medium
            {
                "question": "What is the most common opportunistic infection in HIV patients in India?",
                "options": ["A) Pneumocystis pneumonia", "B) Tuberculosis", "C) Cryptococcal meningitis", "D) Toxoplasmosis"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "Tuberculosis is the most common opportunistic infection in HIV patients in India.",
                "reference": "HIV Dermatology Integration Handouts, Section 7: Complications"
            },
            {
                "question": "Which malignancy is most commonly associated with HIV infection?",
                "options": ["A) Lung cancer", "B) Kaposi sarcoma", "C) Breast cancer", "D) Colorectal cancer"],
                "answer": "B",
                "type": "single",
                "difficulty": "easy",
                "explanation": "Kaposi sarcoma is the most common HIV-associated malignancy.",
                "reference": "HIV Dermatology Integration Handouts, Section 7: Complications"
            },

            # Diagnosis - Hard
            {
                "question": "Which test can detect HIV infection as early as 10-14 days post-exposure?",
                "options": ["A) ELISA", "B) Western blot", "C) HIV RNA PCR", "D) CD4 count"],
                "answer": "C",
                "type": "single",
                "difficulty": "hard",
                "explanation": "HIV RNA PCR can detect infection within 10-14 days of exposure.",
                "reference": "HIV Dermatology Integration Handouts, Section 8: Diagnosis"
            },
            {
                "question": "According to WHO clinical staging, AIDS is defined as CD4 count:",
                "options": ["A) <500 cells/μL", "B) <350 cells/μL", "C) <200 cells/μL", "D) <50 cells/μL"],
                "answer": "C",
                "type": "single",
                "difficulty": "medium",
                "explanation": "AIDS is defined by CD4 count <200 cells/μL or presence of AIDS-defining illnesses.",
                "reference": "HIV Dermatology Integration Handouts, Section 8: Diagnosis"
            },

            # Treatment - Medium
            {
                "question": "According to NACO 2023 guidelines, when should ART be initiated?",
                "options": ["A) CD4 <500 cells/μL", "B) CD4 <350 cells/μL", "C) CD4 <200 cells/μL", "D) All PLHIV regardless of CD4 count"],
                "answer": "D",
                "type": "single",
                "difficulty": "medium",
                "explanation": "NACO recommends ART initiation for all people living with HIV regardless of CD4 count.",
                "reference": "HIV Dermatology Integration Handouts, Section 9: Treatment"
            },
            {
                "question": "What is the preferred first-line ART regimen in India?",
                "options": ["A) AZT + 3TC + EFV", "B) TDF + 3TC + DTG", "C) TDF + FTC + RPV", "D) ABC + 3TC + EFV"],
                "answer": "B",
                "type": "single",
                "difficulty": "medium",
                "explanation": "Tenofovir + Lamivudine + Dolutegravir (TLD) is the preferred first-line regimen.",
                "reference": "HIV Dermatology Integration Handouts, Section 9: Treatment"
            },
            {
                "question": "What level of ART adherence is required for optimal viral suppression?",
                "options": ["A) >80%", "B) >90%", "C) >95%", "D) >99%"],
                "answer": "C",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Greater than 95% adherence is required for optimal viral suppression and prevention of resistance.",
                "reference": "HIV Dermatology Integration Handouts, Section 9: Treatment"
            },

            # Control and National Programme - Easy to Hard
            {
                "question": "What does U=U stand for in HIV prevention?",
                "options": ["A) Universal Use of condoms", "B) Undetectable equals Untransmittable", "C) Urgent Use of antiretrovirals", "D) Unified Understanding of HIV"],
                "answer": "B",
                "type": "single",
                "difficulty": "easy",
                "explanation": "U=U means Undetectable equals Untransmittable - people with undetectable viral load cannot transmit HIV sexually.",
                "reference": "HIV Dermatology Integration Handouts, Section 10: Control and Prevention"
            },
            {
                "question": "What is the timeframe for initiating post-exposure prophylaxis (PEP)?",
                "options": ["A) Within 24 hours", "B) Within 48 hours", "C) Within 72 hours", "D) Within 1 week"],
                "answer": "C",
                "type": "single",
                "difficulty": "medium",
                "explanation": "PEP should be initiated within 72 hours of HIV exposure for maximum effectiveness.",
                "reference": "HIV Dermatology Integration Handouts, Section 10: Control and Prevention"
            },
            {
                "question": "Multiple Response: What are the 95-95-95 targets of NACP-VI? (Select all that apply)",
                "options": ["A) 95% of PLHIV know their status", "B) 95% of diagnosed receive ART", "C) 95% of on ART achieve viral suppression", "D) 95% of population tested annually", "E) 95% reduction in new infections"],
                "answer": ["A", "B", "C"],
                "type": "multiple",
                "difficulty": "hard",
                "explanation": "The 95-95-95 targets are: 95% know status, 95% on ART, 95% virally suppressed.",
                "reference": "HIV Dermatology Integration Handouts, Section 10: Control and Prevention"
            },
            {
                "question": "What percentage reduction in new HIV infections was achieved in India from 2007-2017?",
                "options": ["A) 33%", "B) 50%", "C) 66%", "D) 80%"],
                "answer": "C",
                "type": "single",
                "difficulty": "medium",
                "explanation": "India achieved a 66% reduction in new HIV infections from 2007-2017 through NACP.",
                "reference": "HIV Dermatology Integration Handouts, Section 10: Control and Prevention"
            },
            {
                "question": "Which high-risk group in India has the highest HIV prevalence?",
                "options": ["A) Female sex workers", "B) Injecting drug users", "C) Men who have sex with men", "D) Migrant laborers"],
                "answer": "C",
                "type": "single",
                "difficulty": "easy",
                "explanation": "Men who have sex with men (MSM) have the highest HIV prevalence at 17% in India.",
                "reference": "HIV Dermatology Integration Handouts, Section 10: Control and Prevention"
            },

            # Additional Clinical Integration Questions
            {
                "question": "A patient presents with multiple skin conditions including seborrheic dermatitis, oral candidiasis, and Kaposi sarcoma. What CD4 count range is most likely?",
                "options": ["A) CD4 >500 cells/μL", "B) CD4 200-500 cells/μL", "C) CD4 <200 cells/μL", "D) Cannot determine from skin findings alone"],
                "answer": "B",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Multiple skin conditions with Kaposi sarcoma suggest moderate immunosuppression (CD4 200-500).",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            },
            {
                "question": "In HIV patients, which dermatological finding is considered a poor prognostic indicator?",
                "options": ["A) Seborrheic dermatitis", "B) Kaposi sarcoma", "C) Oral hairy leukoplakia", "D) Drug-induced rash"],
                "answer": "B",
                "type": "single",
                "difficulty": "hard",
                "explanation": "Kaposi sarcoma indicates significant immunosuppression and is associated with poorer prognosis.",
                "reference": "HIV Dermatology Integration Handouts, Section 6: Clinical Features"
            }
        ]

    def shuffle_questions(self) -> None:
        """Shuffle the questions for random order"""
        random.shuffle(self.questions)

    def ask_question(self, question_data: Dict, question_number: int) -> bool:
        """Present a single question and get user response"""
        print(f"\nQuestion {question_number}/{self.total_questions} ({question_data['difficulty'].title()} - {question_data['type'].title()})")
        print(question_data["question"])
        print("\nOptions:")
        for option in question_data["options"]:
            print(option)

        start_time = time.time()
        correct = False

        if question_data["type"] == "single":
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

        elif question_data["type"] == "multiple":
            print("\nFor multiple response questions, enter answers separated by commas (e.g., A,C,D)")
            while True:
                try:
                    user_input = input("Your answers: ").strip().upper()
                    user_answers = [ans.strip() for ans in user_input.split(',') if ans.strip()]
                    # Validate input
                    valid_options = ['A', 'B', 'C', 'D', 'E']
                    if all(ans in valid_options for ans in user_answers):
                        break
                    else:
                        print("Please enter valid options separated by commas.")
                except KeyboardInterrupt:
                    print("\nQuiz interrupted by user.")
                    return False

            elapsed_time = time.time() - start_time
            if elapsed_time > self.time_limit:
                print(f"Time's up! ({self.time_limit} seconds limit exceeded)")
                return False

            correct_answers = set(question_data["answer"])
            user_answers_set = set(user_answers)

            if user_answers_set == correct_answers:
                print("✅ Correct!")
                self.score += 1
                correct = True
            else:
                print(f"❌ Incorrect. The correct answers are {', '.join(correct_answers)}.")
                if len(user_answers_set - correct_answers) > 0:
                    print(f"You incorrectly selected: {', '.join(user_answers_set - correct_answers)}")
                if len(correct_answers - user_answers_set) > 0:
                    print(f"You missed: {', '.join(correct_answers - user_answers_set)}")

        print(f"Explanation: {question_data['explanation']}")
        print(f"Reference: {question_data['reference']}")
        return correct

    def run_quiz(self, num_questions: int = None) -> None:
        """Run the complete quiz"""
        if num_questions is None or num_questions > len(self.questions):
            num_questions = len(self.questions)

        self.shuffle_questions()
        selected_questions = self.questions[:num_questions]

        print("🩺 HIV Dermatology Integration MCQ Quiz")
        print("=" * 60)
        print(f"You will be asked {num_questions} questions.")
        print(f"Time limit: {self.time_limit} seconds per question.")
        print("Includes single best answer and multiple response questions.")
        print("Good luck!\n")

        input("Press Enter to start the quiz...")

        for i, question in enumerate(selected_questions, 1):
            if not self.ask_question(question, i):
                break

        self.show_results(num_questions)

    def show_results(self, total_asked: int) -> None:
        """Display final quiz results"""
        print("\n" + "=" * 60)
        print("🎯 QUIZ RESULTS - HIV Dermatology Integration")
        print("=" * 60)
        print(f"Questions answered: {total_asked}")
        print(f"Correct answers: {self.score}")
        percentage = (self.score / total_asked) * 100
        print(f"Percentage: {percentage:.1f}%")

        # Performance feedback
        if percentage >= 90:
            print("🌟 Excellent! Outstanding performance in HIV dermatology!")
        elif percentage >= 80:
            print("👍 Very Good! Strong understanding of HIV-dermatology integration!")
        elif percentage >= 70:
            print("👌 Good! Solid grasp of key concepts!")
        elif percentage >= 60:
            print("📚 Satisfactory! Review dermatological manifestations more.")
        else:
            print("📖 Needs improvement. Focus on HIV clinical features and dermatology.")

        print("\nThank you for taking the HIV Dermatology Integration Quiz!")
        print("Remember: Dermatological findings can be crucial clues in HIV diagnosis! 🩺")
        print("Integration with dermatology enhances clinical acumen!")

def main():
    """Main function to run the quiz"""
    quiz = HIVDermatologyQuiz()

    print("HIV Dermatology Integration Interactive MCQ Quiz")
    print("Focus: HIV with emphasis on dermatological aspects")
    print("Choose quiz mode:")
    print("1. Full Quiz (25 questions)")
    print("2. Quick Quiz (15 questions)")
    print("3. Practice Quiz (10 questions)")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                quiz.run_quiz(25)
            elif choice == 2:
                quiz.run_quiz(15)
            elif choice == 3:
                quiz.run_quiz(10)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (1-3).")

if __name__ == "__main__":
    main()