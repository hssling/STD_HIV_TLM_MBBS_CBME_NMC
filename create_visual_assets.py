import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import matplotlib.patches as patches
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import matplotlib.patheffects as path_effects

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_std_classification_diagram():
    """Create STD classification diagram"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(5, 7.5, 'STD Classification', ha='center', va='center',
            fontsize=20, fontweight='bold', color='#2E4057')

    # Main categories
    categories = [
        ('Bacterial STDs', ['Gonorrhea', 'Syphilis', 'Chlamydia'], '#FF6B6B'),
        ('Viral STDs', ['HIV', 'HSV', 'HPV', 'Hepatitis B'], '#4ECDC4'),
        ('Parasitic STDs', ['Trichomoniasis', 'Pubic lice'], '#45B7D1'),
        ('Fungal STDs', ['Candidiasis'], '#FFA07A')
    ]

    y_pos = 6
    for category, subitems, color in categories:
        # Category box
        rect = FancyBboxPatch((1, y_pos-0.8), 8, 0.6,
                            boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)

        # Category title
        ax.text(5, y_pos-0.5, category, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')

        # Subitems
        sub_y = y_pos - 1.2
        for subitem in subitems:
            ax.text(5, sub_y, f'• {subitem}', ha='center', va='center',
                   fontsize=12, color='#2E4057')
            sub_y -= 0.3

        y_pos -= 2.5

    plt.savefig('std_classification.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("STD classification diagram created")

def create_global_std_epidemiology_chart():
    """Create global STD epidemiology bar chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    stds = ['Chlamydia', 'Gonorrhea', 'Syphilis', 'Trichomoniasis']
    cases = [129, 82, 7.1, 156]  # Million cases

    bars = ax.bar(stds, cases, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'],
                  edgecolor='black', linewidth=1.5, width=0.6)

    ax.set_title('Global STD Burden (2022)', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('New Cases (Millions)', fontsize=14)
    ax.set_xlabel('Sexually Transmitted Diseases', fontsize=14)

    # Add value labels on bars
    for bar, case in zip(bars, cases):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{case}M', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('global_std_epidemiology.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Global STD epidemiology chart created")

def create_indian_hiv_transmission_pie():
    """Create Indian HIV transmission routes pie chart"""
    fig, ax = plt.subplots(figsize=(10, 8))

    routes = ['Heterosexual', 'MSM', 'IDU', 'Mother-to-Child']
    percentages = [85, 2, 7, 6]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

    wedges, texts, autotexts = ax.pie(percentages, labels=routes, autopct='%1.1f%%',
                                     colors=colors, startangle=90,
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

    ax.set_title('HIV Transmission Routes in India', fontsize=16, fontweight='bold', pad=20)

    # Style the percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    plt.tight_layout()
    plt.savefig('indian_hiv_transmission_pie.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Indian HIV transmission pie chart created")

def create_hiv_progression_timeline():
    """Create HIV disease progression timeline"""
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Timeline line
    ax.plot([1, 13], [3, 3], 'k-', linewidth=3)

    # Stages
    stages = [
        ('Acute HIV\n(2-4 weeks)', 2, 'High viral replication\nFlu-like symptoms'),
        ('Clinical Latency\n(8-10 years)', 5, 'CD4 decline\nAsymptomatic'),
        ('Symptomatic HIV\n(CD4 <500)', 8, 'Persistent infections\nWeight loss'),
        ('AIDS\n(CD4 <200)', 11, 'Opportunistic infections\nDeath if untreated')
    ]

    colors = ['#FF6B6B', '#FFD93D', '#6BCF7F', '#4D96FF']

    for i, (stage, x_pos, desc) in enumerate(stages):
        # Stage circle
        circle = Circle((x_pos, 3), 0.8, facecolor=colors[i],
                       edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        # Stage text
        ax.text(x_pos, 3, str(i+1), ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')

        # Stage title
        ax.text(x_pos, 4.5, stage, ha='center', va='center',
                fontsize=12, fontweight='bold', color='#2E4057')

        # Description
        ax.text(x_pos, 1.5, desc, ha='center', va='center',
                fontsize=10, color='#2E4057', wrap=True)

    # Timeline labels
    ax.text(1, 2.3, 'Exposure', ha='center', fontsize=10, color='#666666')
    ax.text(13, 2.3, 'Death', ha='center', fontsize=10, color='#666666')

    plt.title('HIV Disease Progression Timeline', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('hiv_progression_timeline.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("HIV progression timeline created")

def create_art_regimen_comparison():
    """Create ART regimen comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 6))

    regimens = ['TLD\n(Tenofovir + Lamivudine + Dolutegravir)',
                'TLE\n(Tenofovir + Lamivudine + Efavirenz)',
                'AZT-based\n(Zidovudine + Lamivudine + Efavirenz)']

    advantages = [3, 2, 1]  # TLD best, then TLE, then AZT
    side_effects = [1, 3, 2]  # TLD least, AZT moderate, TLE most
    adherence = [3, 2, 1]  # TLD easiest, then TLE, then AZT

    x = np.arange(len(regimens))
    width = 0.25

    bars1 = ax.bar(x - width, advantages, width, label='Advantages',
                   color='#4ECDC4', edgecolor='black', linewidth=1)
    bars2 = ax.bar(x, side_effects, width, label='Side Effects (lower better)',
                   color='#FF6B6B', edgecolor='black', linewidth=1)
    bars3 = ax.bar(x + width, adherence, width, label='Adherence Ease',
                   color='#45B7D1', edgecolor='black', linewidth=1)

    ax.set_title('ART Regimen Comparison', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(regimens, fontsize=10)
    ax.legend()
    ax.set_ylabel('Score (Higher = Better)', fontsize=12)

    # Add value labels
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig('art_regimen_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("ART regimen comparison chart created")

def create_prevention_pyramid():
    """Create prevention pyramid diagram"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Pyramid levels (from bottom to top - most effective at top)
    levels = [
        ('Tertiary Prevention', 'Treatment & Support', 1, '#FF6B6B'),
        ('Secondary Prevention', 'Screening & Early Treatment', 3, '#FFD93D'),
        ('Primary Prevention', 'Vaccines & PrEP', 5, '#6BCF7F'),
        ('Structural Prevention', 'Education & Policy', 7, '#4D96FF')
    ]

    for level_name, description, y_pos, color in levels:
        # Level triangle section
        triangle = patches.Polygon([[2, y_pos], [8, y_pos], [5, y_pos+1.5]],
                                 facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(triangle)

        # Level text
        ax.text(5, y_pos+0.8, level_name, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white')
        ax.text(5, y_pos+0.4, description, ha='center', va='center',
                fontsize=10, color='white')

    # Effectiveness arrow
    ax.arrow(9, 1, 0, 6, head_width=0.2, head_length=0.3,
             fc='black', ec='black', linewidth=2)
    ax.text(9.5, 4, 'Increasing\nEffectiveness', ha='left', va='center',
            fontsize=10, fontweight='bold', color='#2E4057')

    plt.title('HIV Prevention Pyramid', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('prevention_pyramid.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("Prevention pyramid created")

def create_u_equals_u_symbol():
    """Create U=U symbol for undetectable equals untransmittable"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # U=U text
    ax.text(4, 4, 'U', fontsize=72, fontweight='bold', color='#FF6B6B',
            ha='center', va='center')
    ax.text(4, 3, '=', fontsize=48, fontweight='bold', color='#2E4057',
            ha='center', va='center')
    ax.text(4, 2, 'U', fontsize=72, fontweight='bold', color='#4ECDC4',
            ha='center', va='center')

    # Explanatory text
    ax.text(4, 5, 'Undetectable', fontsize=16, fontweight='bold',
            color='#FF6B6B', ha='center', va='center')
    ax.text(4, 1, 'Untransmittable', fontsize=16, fontweight='bold',
            color='#4ECDC4', ha='center', va='center')

    # Subtitle
    ax.text(4, 0.5, 'Viral suppression prevents sexual transmission of HIV',
            fontsize=12, color='#2E4057', ha='center', va='center')

    plt.savefig('u_equals_u_symbol.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("U=U symbol created")

def create_abc_icons():
    """Create ABC approach icons"""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis('off')

    approaches = [
        ('A', 'Abstain', 'Avoid sex or delay sexual debut'),
        ('B', 'Be faithful', 'Mutual monogamy with uninfected partner'),
        ('C', 'Condoms', 'Consistent and correct condom use')
    ]

    for i, (letter, title, desc) in enumerate(approaches):
        x_pos = 2 + i * 3.5

        # Letter circle
        circle = Circle((x_pos, 2.5), 0.8, facecolor='#4ECDC4',
                       edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        # Letter text
        ax.text(x_pos, 2.5, letter, ha='center', va='center',
                fontsize=24, fontweight='bold', color='white')

        # Title
        ax.text(x_pos, 1.8, title, ha='center', va='center',
                fontsize=14, fontweight='bold', color='#2E4057')

        # Description
        ax.text(x_pos, 1.2, desc, ha='center', va='center',
                fontsize=10, color='#666666', wrap=True)

    plt.title('ABC Approach to HIV Prevention', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('abc_approach_icons.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("ABC approach icons created")

def create_cd4_monitoring_chart():
    """Create CD4 monitoring chart"""
    fig, ax = plt.subplots(figsize=(10, 6))

    months = ['Baseline', '3 months', '6 months', '12 months', '18 months', '24 months']
    cd4_normal = [800, 850, 900, 950, 1000, 1050]
    cd4_hiv = [350, 400, 450, 500, 550, 600]

    ax.plot(months, cd4_normal, 'g-', marker='o', linewidth=3, markersize=8,
            label='Normal Range', color='#4ECDC4')
    ax.plot(months, cd4_hiv, 'r-', marker='s', linewidth=3, markersize=8,
            label='HIV Patient on ART', color='#FF6B6B')

    ax.set_title('CD4 Count Monitoring in HIV Treatment', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('CD4 Count (cells/μL)', fontsize=14)
    ax.set_xlabel('Time on ART', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Add threshold lines
    ax.axhline(y=500, color='orange', linestyle='--', alpha=0.7, label='Symptomatic HIV')
    ax.axhline(y=200, color='red', linestyle='--', alpha=0.7, label='AIDS')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('cd4_monitoring_chart.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("CD4 monitoring chart created")

if __name__ == "__main__":
    print("Creating visual assets...")

    create_std_classification_diagram()
    create_global_std_epidemiology_chart()
    create_indian_hiv_transmission_pie()
    create_hiv_progression_timeline()
    create_art_regimen_comparison()
    create_prevention_pyramid()
    create_u_equals_u_symbol()
    create_abc_icons()
    create_cd4_monitoring_chart()

    print("All visual assets created successfully!")
