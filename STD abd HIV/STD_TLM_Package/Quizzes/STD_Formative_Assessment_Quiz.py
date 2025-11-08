#!/usr/bin/env python3
"""
STD Formative Assessment MCQ Quiz
Comprehensive Multiple Choice Questions for STD Teaching Session
MBBS 3rd Year - Formative Assessment Quiz
Community Medicine Perspective with Indian Context

Author: Dr. Siddalingaiah H S
Professor, Community Medicine
SIMSRH, Tumkur
Email: hssling@yahoo.com
Phone: +91 8941087719

Educational content for medical students and healthcare professionals
"""

from typing import List, Dict, Union

class STDFormativeQuiz:
    def __init__(self):
        self.questions = self.load_questions()

    def load_questions(self) -> List[Dict]:
        """Load all STD-related MCQ questions for formative assessment"""
        return [
            # Types of STDs
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Types",
                "question": "Which of the following is classified as a bacterial STD?",
                "options": ["A) Genital herpes", "B) Gonorrhea", "C) Hepatitis B", "D) Human papillomavirus infection"],
                "answer": "B",
                "explanation": "Gonorrhea is caused by the bacterium Neisseria gonorrhoeae, making it a bacterial STD.",
                "reference": "Park's Textbook of Preventive and Social Medicine, 26th Edition"
            },
            {
                "type": "MRQ",
                "difficulty": "easy",
                "section": "Types",
                "question": "Which of the following are viral STDs? (Select all that apply)",
                "options": ["A) Syphilis", "B) Chlamydia", "C) Genital herpes", "D) Chancroid", "E) Human papillomavirus infection"],
                "answer": ["C", "E"],
                "explanation": "Genital herpes is caused by Herpes Simplex Virus (HSV), and HPV infection is caused by Human Papillomavirus, both viral pathogens.",
                "reference": "WHO Guidelines for the Management of Sexually Transmitted Infections, 2021"
            },

            # Etiology
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Etiology",
                "question": "What is the causative agent of syphilis?",
                "options": ["A) Neisseria gonorrhoeae", "B) Treponema pallidum", "C) Chlamydia trachomatis", "D) Haemophilus ducreyi"],
                "answer": "B",
                "explanation": "Syphilis is caused by the spirochete Treponema pallidum.",
                "reference": "Harrison's Principles of Internal Medicine, 21st Edition"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Etiology",
                "question": "Which serovars of Chlamydia trachomatis are responsible for lymphogranuloma venereum?",
                "options": ["A) A-C", "B) D-K", "C) L1-L3", "D) L4-L6"],
                "answer": "C",
                "explanation": "LGV is caused by serovars L1, L2, and L3 of Chlamydia trachomatis.",
                "reference": "CDC Sexually Transmitted Infections Treatment Guidelines, 2021"
            },

            # Epidemiology
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Epidemiology",
                "question": "According to NACO 2023 data, what is the estimated number of people living with HIV in India?",
                "options": ["A) 1.5 million", "B) 2.4 million", "C) 3.2 million", "D) 4.1 million"],
                "answer": "B",
                "explanation": "NACO estimates approximately 2.4 million people living with HIV in India as of 2023.",
                "reference": "NACO Annual Report 2022-23"
            },
            {
                "type": "SBA",
                "difficulty": "hard",
                "section": "Epidemiology",
                "question": "Which high-risk group in India has the highest HIV prevalence according to NACO?",
                "options": ["A) Female sex workers", "B) Injecting drug users", "C) Men who have sex with men", "D) Transgender persons"],
                "answer": "C",
                "explanation": "Men who have sex with men (MSM) have the highest HIV prevalence at 17% in India.",
                "reference": "NACO HIV Sentinel Surveillance 2022"
            },
            {
                "type": "MRQ",
                "difficulty": "medium",
                "section": "Epidemiology",
                "question": "Which states in India have HIV prevalence above 1%? (Select all that apply)",
                "options": ["A) Maharashtra", "B) Karnataka", "C) Nagaland", "D) Tamil Nadu", "E) Andhra Pradesh"],
                "answer": ["C"],
                "explanation": "Nagaland has the highest HIV prevalence in India at approximately 1.5%, while others are below 1%.",
                "reference": "NACO State-wise HIV Prevalence Data 2023"
            },

            # Transmission
            {
                "type": "MRQ",
                "difficulty": "easy",
                "section": "Transmission",
                "question": "Which of the following are modes of HIV transmission? (Select all that apply)",
                "options": ["A) Sexual contact", "B) Blood transfusion", "C) Mother-to-child", "D) Mosquito bites", "E) Sharing food"],
                "answer": ["A", "B", "C"],
                "explanation": "HIV is transmitted through sexual contact, blood exposure, and vertically from mother to child.",
                "reference": "WHO HIV Transmission Factsheet"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Transmission",
                "question": "What is the most common mode of transmission for Chlamydia trachomatis in India?",
                "options": ["A) Oral sex", "B) Vaginal intercourse", "C) Anal intercourse", "D) Vertical transmission"],
                "answer": "B",
                "explanation": "Vaginal intercourse is the most common mode, though other sexual practices can also transmit it.",
                "reference": "Indian Journal of Sexually Transmitted Diseases, 2022"
            },

            # Incubation Period
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Incubation Period",
                "question": "What is the typical incubation period for gonorrhea?",
                "options": ["A) 1-3 days", "B) 3-7 days", "C) 2-4 weeks", "D) 3-6 weeks"],
                "answer": "B",
                "explanation": "Gonorrhea has an incubation period of 2-7 days, with symptoms appearing within a week.",
                "reference": "CDC STI Guidelines"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Incubation Period",
                "question": "The incubation period for primary syphilis is:",
                "options": ["A) 1-2 weeks", "B) 3-6 weeks", "C) 2-3 months", "D) 6-12 months"],
                "answer": "B",
                "explanation": "Primary syphilis manifests 3-6 weeks after exposure with the chancre.",
                "reference": "NACO STI Management Guidelines 2021"
            },

            # Pathophysiology
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Pathophysiology",
                "question": "How does Chlamydia trachomatis cause pelvic inflammatory disease?",
                "options": ["A) Direct invasion of endometrium", "B) Toxin production", "C) Immune complex deposition", "D) Ascending infection from cervix"],
                "answer": "D",
                "explanation": "Chlamydia ascends from the cervix to cause endometritis, salpingitis, and PID.",
                "reference": "Williams Gynecology, 4th Edition"
            },
            {
                "type": "SBA",
                "difficulty": "hard",
                "section": "Pathophysiology",
                "question": "Which HPV oncoproteins are responsible for cervical carcinogenesis?",
                "options": ["A) E6 and E7", "B) E1 and E2", "C) L1 and L2", "D) E4 and E5"],
                "answer": "A",
                "explanation": "E6 and E7 proteins disrupt p53 and Rb tumor suppressor pathways, leading to malignancy.",
                "reference": "Journal of Clinical Oncology, HPV Review 2023"
            },

            # Clinical Features
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Clinical Features",
                "question": "Which symptom is characteristic of primary syphilis?",
                "options": ["A) Painful ulcer", "B) Painless chancre", "C) Rash with itching", "D) Fever and malaise"],
                "answer": "B",
                "explanation": "Primary syphilis presents with a painless, clean-based chancre at the inoculation site.",
                "reference": "Dermatology Atlas for STDs"
            },
            {
                "type": "MRQ",
                "difficulty": "medium",
                "section": "Clinical Features",
                "question": "Which clinical features are seen in secondary syphilis? (Select all that apply)",
                "options": ["A) Chancre", "B) Generalized rash", "C) Condyloma lata", "D) Alopecia", "E) Fever"],
                "answer": ["B", "C", "D", "E"],
                "explanation": "Secondary syphilis includes maculopapular rash, condyloma lata, alopecia, and constitutional symptoms.",
                "reference": "Harrison's Infectious Diseases"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Clinical Features",
                "question": "What percentage of chlamydial infections in women are asymptomatic?",
                "options": ["A) 20-30%", "B) 40-50%", "C) 70-80%", "D) 90-95%"],
                "answer": "C",
                "explanation": "70-80% of women with chlamydia are asymptomatic, highlighting the need for screening.",
                "reference": "American Journal of Obstetrics and Gynecology"
            },

            # Complications
            {
                "type": "MRQ",
                "difficulty": "medium",
                "section": "Complications",
                "question": "Which complications can result from untreated chlamydial infection? (Select all that apply)",
                "options": ["A) Pelvic inflammatory disease", "B) Ectopic pregnancy", "C) Infertility", "D) Cervical cancer", "E) Ophthalmia neonatorum"],
                "answer": ["A", "B", "C", "E"],
                "explanation": "Untreated chlamydia can lead to PID, infertility, ectopic pregnancy, and neonatal eye infections.",
                "reference": "Fertility and Sterility Journal"
            },
            {
                "type": "SBA",
                "difficulty": "hard",
                "section": "Complications",
                "question": "Which STD is most strongly associated with increased risk of cervical cancer?",
                "options": ["A) Gonorrhea", "B) Syphilis", "C) Chlamydia", "D) HPV"],
                "answer": "D",
                "explanation": "HPV infection, especially high-risk types 16 and 18, is the primary cause of cervical cancer.",
                "reference": "IARC Monographs on HPV"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Complications",
                "question": "What is the most common complication of gonococcal infection in newborns?",
                "options": ["A) Pneumonia", "B) Ophthalmia neonatorum", "C) Meningitis", "D) Arthritis"],
                "answer": "B",
                "explanation": "Gonococcal ophthalmia neonatorum can cause blindness if untreated.",
                "reference": "Pediatric Infectious Diseases Journal"
            },

            # Diagnosis
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Diagnosis",
                "question": "What is the gold standard diagnostic test for Chlamydia trachomatis?",
                "options": ["A) Gram stain", "B) Culture", "C) PCR", "D) ELISA"],
                "answer": "C",
                "explanation": "Polymerase Chain Reaction (PCR) is the most sensitive and specific test for chlamydia.",
                "reference": "Journal of Clinical Microbiology"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Diagnosis",
                "question": "Which serological test is used for confirmation of syphilis?",
                "options": ["A) VDRL", "B) TPHA", "C) Both VDRL and TPHA", "D) Neither"],
                "answer": "C",
                "explanation": "VDRL is for screening, TPHA for confirmation; both are used in syphilis diagnosis.",
                "reference": "NACO Laboratory Guidelines for STI"
            },

            # Treatment
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Treatment",
                "question": "What is the first-line treatment for uncomplicated gonorrhea according to NACO?",
                "options": ["A) Azithromycin 1g single dose", "B) Ceftriaxone 500mg IM + Azithromycin 1g PO", "C) Doxycycline 100mg BD × 7 days", "D) Benzathine penicillin 2.4 MU IM"],
                "answer": "B",
                "explanation": "Dual therapy with ceftriaxone and azithromycin is recommended to prevent resistance.",
                "reference": "NACO STI Treatment Guidelines 2021"
            },
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "Treatment",
                "question": "Which antibiotic is contraindicated in pregnant women with syphilis?",
                "options": ["A) Penicillin", "B) Azithromycin", "C) Ceftriaxone", "D) Doxycycline"],
                "answer": "D",
                "explanation": "Doxycycline is contraindicated in pregnancy due to fetal harm; penicillin is the drug of choice.",
                "reference": "CDC Treatment Guidelines for Syphilis"
            },
            {
                "type": "MRQ",
                "difficulty": "hard",
                "section": "Treatment",
                "question": "Which antiretroviral drugs are used in first-line ART for HIV in India? (Select all that apply)",
                "options": ["A) Tenofovir", "B) Lamivudine", "C) Efavirenz", "D) Zidovudine", "E) Nevirapine"],
                "answer": ["A", "B", "C"],
                "explanation": "TLE (Tenofovir + Lamivudine + Efavirenz) is the standard first-line regimen in India.",
                "reference": "NACO ART Guidelines 2021"
            },

            # Control
            {
                "type": "SBA",
                "difficulty": "easy",
                "section": "Control",
                "question": "What does the ABC approach in HIV prevention stand for?",
                "options": ["A) Abstain, Be faithful, Condoms", "B) Awareness, Behavior change, Cure", "C) Abstain, Behavior change, Cure", "D) Awareness, Be faithful, Cure"],
                "answer": "A",
                "explanation": "ABC: Abstain from sex, Be faithful to one partner, use Condoms consistently.",
                "reference": "NACO HIV Prevention Strategies"
            },
            {
                "type": "MRQ",
                "difficulty": "medium",
                "section": "Control",
                "question": "Which are key components of STD control programs? (Select all that apply)",
                "options": ["A) Surveillance", "B) Contact tracing", "C) Health education", "D) Vaccine development", "E) Treatment access"],
                "answer": ["A", "B", "C", "E"],
                "explanation": "STD control involves surveillance, contact tracing, education, and ensuring treatment availability.",
                "reference": "WHO Global Health Sector Strategy on STIs"
            },

            # National Programme Linkage
            {
                "type": "SBA",
                "difficulty": "medium",
                "section": "National Programme Linkage",
                "question": "Which national programme in India addresses HIV/AIDS?",
                "options": ["A) National AIDS Control Programme (NACP)", "B) National Programme for Control of Blindness", "C) National Vector Borne Disease Control Programme", "D) National Cancer Control Programme"],
                "answer": "A",
                "explanation": "NACP is the flagship programme for HIV/AIDS prevention and control in India.",
                "reference": "Ministry of Health and Family Welfare, India"
            },
            {
                "type": "SBA",
                "difficulty": "hard",
                "section": "National Programme Linkage",
                "question": "How many phases has the National AIDS Control Programme completed as of 2023?",
                "options": ["A) 2", "B) 3", "C) 4", "D) 5"],
                "answer": "C",
                "explanation": "NACP has completed four phases: NACP-I (1992-1999), II (1999-2006), III (2007-2012), IV (2012-2017), with NACP V ongoing.",
                "reference": "NACO Official Website"
            },
            {
                "type": "MRQ",
                "difficulty": "medium",
                "section": "National Programme Linkage",
                "question": "Which services are provided under NACP for STI management? (Select all that apply)",
                "options": ["A) Free testing", "B) ART centers", "C) Condom distribution", "D) IEC campaigns", "E) STI clinics"],
                "answer": ["A", "C", "D", "E"],
                "explanation": "NACP provides free STI testing, condoms, information campaigns, and dedicated STI clinics.",
                "reference": "NACO STI Services Framework"
            }
        ]

    def print_quiz(self) -> None:
        """Print the complete formative assessment quiz"""
        print("🎓 STD Formative Assessment MCQ Quiz")
        print("=" * 60)
        print("Community Medicine Perspective - MBBS 3rd Year")
        print("Total Questions: 28")
        print("Format: SBA (Single Best Answer), MRQ (Multiple Response Question)")
        print("Difficulty Levels: Easy, Medium, Hard")
        print("=" * 60)
        print()

        for i, q in enumerate(self.questions, 1):
            print(f"Question {i} ({q['difficulty'].capitalize()}, {q['type']}, Section: {q['section']}):")
            print(q['question'])
            print("\nOptions:")
            for opt in q['options']:
                print(f"  {opt}")
            print()
            if q['type'] == 'SBA':
                print(f"Correct Answer: {q['answer']}")
            else:
                print(f"Correct Answers: {', '.join(q['answer'])}")
            print(f"Explanation: {q['explanation']}")
            print(f"Reference: {q['reference']}")
            print("-" * 60)
            print()

    def get_summary(self) -> Dict:
        """Provide summary of quiz structure and coverage"""
        sections = {}
        difficulties = {"easy": 0, "medium": 0, "hard": 0}
        types = {"SBA": 0, "MRQ": 0}

        for q in self.questions:
            sections[q['section']] = sections.get(q['section'], 0) + 1
            difficulties[q['difficulty']] += 1
            types[q['type']] += 1

        return {
            "total_questions": len(self.questions),
            "sections_covered": sections,
            "difficulty_distribution": difficulties,
            "question_types": types
        }

def main():
    """Main function to run the formative assessment quiz"""
    quiz = STDFormativeQuiz()

    print("STD Formative Assessment Quiz")
    print("This quiz contains 28 questions covering all aspects of STDs from a community medicine perspective.")
    print("Questions include answers and explanations for formative learning.")
    print()

    quiz.print_quiz()

    summary = quiz.get_summary()
    print("\n" + "=" * 60)
    print("QUIZ SUMMARY")
    print("=" * 60)
    print(f"Total Questions: {summary['total_questions']}")
    print("\nSection Coverage:")
    for section, count in summary['sections_covered'].items():
        print(f"  {section}: {count} questions")
    print("\nDifficulty Distribution:")
    for diff, count in summary['difficulty_distribution'].items():
        print(f"  {diff.capitalize()}: {count} questions")
    print("\nQuestion Types:")
    for typ, count in summary['question_types'].items():
        print(f"  {typ}: {count} questions")
    print("\nThis quiz emphasizes clinical relevance, understanding over memorization,")
    print("and community medicine perspectives with Indian context (NACO guidelines).")
    print("Suitable for MBBS 3rd year formative assessment.")

if __name__ == "__main__":
    main()