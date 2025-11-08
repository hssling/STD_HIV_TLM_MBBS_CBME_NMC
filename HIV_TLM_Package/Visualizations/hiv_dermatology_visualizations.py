#!/usr/bin/env python3
"""
HIV Dermatology Integration Visualizations
Creates educational visualizations for HIV dermatology class

Author: Dr. Siddalingaiah H S
Professor, Community Medicine
SIMSRH, Tumkur

Focus: Dermatological aspects of HIV, epidemiology, transmission, clinical features,
treatment regimens, and national programme data for MBBS 3rd year students
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Polygon
import matplotlib.patches as patches
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import matplotlib.patheffects as path_effects

# Set matplotlib style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def create_indian_hiv_epidemiology():
    """Create Indian HIV epidemiology bar chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    states = ['Nagaland', 'Manipur', 'Mizoram', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Tamil Nadu', 'National Average']
    prevalence = [1.5, 1.4, 0.8, 0.4, 0.3, 0.3, 0.2, 0.22]

    bars = ax.bar(states, prevalence, color='#FF6B6B', edgecolor='black', linewidth=1.5, width=0.6)

    ax.set_title('HIV Prevalence in India by State (2023)', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Prevalence (%)', fontsize=14)
    ax.set_xlabel('States/Regions', fontsize=14)

    # Add value labels
    for bar, prev in zip(bars, prevalence):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{prev}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('indian_hiv_epidemiology.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Indian HIV epidemiology chart created")

def create_hiv_transmission_routes():
    """Create HIV transmission routes pie chart"""
    fig, ax = plt.subplots(figsize=(10, 8))

    routes = ['Heterosexual', 'Men who have sex\nwith men', 'Injecting drug use', 'Mother-to-child', 'Blood transfusion']
    percentages = [87, 2.1, 3.2, 0.9, 0.1]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

    wedges, texts, autotexts = ax.pie(percentages, labels=routes, autopct='%1.1f%%',
                                     colors=colors, startangle=90,
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 1.5})

    ax.set_title('HIV Transmission Routes in India (2023)', fontsize=16, fontweight='bold', pad=20)

    # Style the percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_fontweight('bold')

    plt.tight_layout()
    plt.savefig('hiv_transmission_routes.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("HIV transmission routes pie chart created")

def create_hiv_progression_timeline():
    """Create HIV disease progression timeline with dermatological aspects"""
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Timeline line
    ax.plot([1, 13], [4, 4], 'k-', linewidth=3)

    # Stages with dermatological focus
    stages = [
        ('Acute HIV\n(2-4 weeks)', 2, 'High viral load\nMaculopapular rash\nFever, lymphadenopathy'),
        ('Clinical Latency\n(8-10 years)', 5, 'Asymptomatic\nSeborrheic dermatitis\nTinea infections'),
        ('Symptomatic HIV\n(CD4 200-500)', 8, 'Kaposi sarcoma\nHerpes zoster\nOral candidiasis'),
        ('AIDS\n(CD4 <200)', 11, 'Disseminated herpes\nCryptococcal lesions\nBacillary angiomatosis')
    ]

    colors = ['#FF6B6B', '#FFD93D', '#6BCF7F', '#4D96FF']

    for i, (stage, x_pos, desc) in enumerate(stages):
        # Stage circle
        circle = Circle((x_pos, 4), 0.8, facecolor=colors[i],
                       edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        # Stage text
        ax.text(x_pos, 4, str(i+1), ha='center', va='center',
                fontsize=16, fontweight='bold', color='white')

        # Stage title
        ax.text(x_pos, 5.5, stage, ha='center', va='center',
                fontsize=12, fontweight='bold', color='#2E4057')

        # Description
        ax.text(x_pos, 2.5, desc, ha='center', va='center',
                fontsize=10, color='#2E4057')

    # Timeline labels
    ax.text(1, 3.3, 'Exposure', ha='center', fontsize=10, color='#666666')
    ax.text(13, 3.3, 'Death if untreated', ha='center', fontsize=10, color='#666666')

    plt.title('HIV Disease Progression with Dermatological Manifestations', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('hiv_progression_dermatology_timeline.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("HIV progression timeline with dermatology created")

def create_dermatological_manifestations_spectrum():
    """Create dermatological manifestations spectrum by CD4 count"""
    fig, ax = plt.subplots(figsize=(12, 8))

    cd4_ranges = ['CD4 > 500', 'CD4 200-500', 'CD4 < 200']
    conditions = {
        'Seborrheic Dermatitis': [3, 2, 1],
        'Kaposi Sarcoma': [1, 3, 2],
        'Herpes Infections': [1, 2, 3],
        'Fungal Infections': [2, 2, 3],
        'Bacterial Infections': [1, 2, 3],
        'Drug Reactions': [2, 1, 1]
    }

    x = np.arange(len(cd4_ranges))
    width = 0.15
    multiplier = 0

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']

    for condition, values in conditions.items():
        offset = width * multiplier
        bars = ax.bar(x + offset, values, width, label=condition, color=colors[multiplier], edgecolor='black', linewidth=1)
        multiplier += 1

    ax.set_title('Dermatological Manifestations by CD4 Count', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Frequency/Prevalence Score', fontsize=14)
    ax.set_xlabel('CD4 Count Ranges', fontsize=14)
    ax.set_xticks(x + width * 2.5)
    ax.set_xticklabels(cd4_ranges)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('dermatological_manifestations_spectrum.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("Dermatological manifestations spectrum created")

def create_hiv_skin_conditions_infographic():
    """Create HIV skin conditions infographic"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Common Dermatological Conditions in HIV', ha='center', va='center',
            fontsize=18, fontweight='bold', color='#2E4057')

    conditions = [
        ('Seborrheic Dermatitis', 'Greasy, scaly patches\nScalp, face, chest\nMalassezia overgrowth', 2, 8, '#FF6B6B'),
        ('Kaposi Sarcoma', 'Purple/red patches\nOral involvement\nHHV-8 associated', 6, 8, '#4ECDC4'),
        ('Oral Hairy Leukoplakia', 'White patches on tongue\nEBV-associated\nCannot be scraped', 10, 8, '#45B7D1'),
        ('Herpes Infections', 'Chronic ulcers\nDisseminated infection\nHSV/VZV', 2, 5, '#FFA07A'),
        ('Fungal Infections', 'Oral thrush\nExtensive tinea\nCryptococcal lesions', 6, 5, '#98D8C8'),
        ('Bacterial Infections', 'Staphylococcal folliculitis\nBacillary angiomatosis\nImpetigo', 10, 5, '#F7DC6F'),
        ('Drug Reactions', 'Sulfa hypersensitivity\nNevirapine rash\nStevens-Johnson syndrome', 2, 2, '#BB8FCE'),
        ('Molluscum Contagiosum', 'Pearly papules\nWidespread in advanced HIV\nPoxvirus', 6, 2, '#85C1E9')
    ]

    for condition, desc, x, y, color in conditions:
        # Condition box
        rect = FancyBboxPatch((x-1.5, y-0.8), 3, 1.2,
                            boxstyle="round,pad=0.1",
                            facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(rect)

        # Condition title
        ax.text(x, y-0.3, condition, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        # Description
        ax.text(x, y-0.7, desc, ha='center', va='center',
                fontsize=8, color='white')

    plt.savefig('hiv_skin_conditions_infographic.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("HIV skin conditions infographic created")

def create_art_regimens_comparison():
    """Create ART regimens comparison chart"""
    fig, ax = plt.subplots(figsize=(12, 8))

    regimens = ['TLD\n(Tenofovir + Lamivudine + Dolutegravir)',
                'TLE\n(Tenofovir + Lamivudine + Efavirenz)',
                'AZT-based\n(Zidovudine + Lamivudine + Efavirenz)']

    # Scores (higher = better)
    efficacy = [5, 4, 3]
    tolerability = [5, 3, 4]
    adherence = [5, 4, 3]
    cost_effectiveness = [4, 5, 5]

    x = np.arange(len(regimens))
    width = 0.2

    bars1 = ax.bar(x - 1.5*width, efficacy, width, label='Efficacy',
                   color='#4ECDC4', edgecolor='black', linewidth=1)
    bars2 = ax.bar(x - 0.5*width, tolerability, width, label='Tolerability',
                   color='#FF6B6B', edgecolor='black', linewidth=1)
    bars3 = ax.bar(x + 0.5*width, adherence, width, label='Adherence',
                   color='#45B7D1', edgecolor='black', linewidth=1)
    bars4 = ax.bar(x + 1.5*width, cost_effectiveness, width, label='Cost-Effectiveness',
                   color='#FFA07A', edgecolor='black', linewidth=1)

    ax.set_title('ART Regimen Comparison (NACO Recommended)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(regimens, fontsize=10)
    ax.legend()
    ax.set_ylabel('Score (1-5, Higher = Better)', fontsize=12)
    ax.set_ylim(0, 6)

    # Add value labels
    for bars in [bars1, bars2, bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig('art_regimens_comparison.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("ART regimens comparison created")

def create_naco_95_95_95_targets():
    """Create NACO 95-95-95 targets progress chart"""
    fig, ax = plt.subplots(figsize=(10, 6))

    targets = ['95% know status', '95% on ART', '95% viral suppression']
    current = [86, 80, 87]  # Approximate 2023 figures
    target = [95, 95, 95]

    x = np.arange(len(targets))
    width = 0.35

    bars1 = ax.bar(x - width/2, current, width, label='Current (2023)',
                   color='#FF6B6B', edgecolor='black', linewidth=1)
    bars2 = ax.bar(x + width/2, target, width, label='Target (2030)',
                   color='#4ECDC4', edgecolor='black', linewidth=1)

    ax.set_title('NACO 95-95-95 Targets Progress', fontsize=16, fontweight='bold', pad=20)
    ax.set_ylabel('Percentage (%)', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(targets, fontsize=10)
    ax.legend()
    ax.set_ylim(0, 100)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 2,
                    f'{int(height)}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig('naco_95_95_95_targets.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("NACO 95-95-95 targets chart created")

def create_hiv_prevention_pyramid():
    """Create HIV prevention pyramid diagram"""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Pyramid levels (from bottom to top - most effective at top)
    levels = [
        ('Tertiary Prevention', 'ART, opportunistic infection management', 1, '#FF6B6B'),
        ('Secondary Prevention', 'Early diagnosis, PPTCT, PEP', 3, '#FFD93D'),
        ('Primary Prevention', 'Condoms, PrEP, vaccines', 5, '#6BCF7F'),
        ('Structural Prevention', 'Education, stigma reduction, policy', 7, '#4D96FF')
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

    plt.title('HIV Prevention Pyramid in Indian Context', fontsize=16, fontweight='bold', pad=20)
    plt.savefig('hiv_prevention_pyramid.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("HIV prevention pyramid created")

def create_cd4_skin_manifestation_correlation():
    """Create CD4 count correlation with skin manifestations"""
    fig, ax = plt.subplots(figsize=(12, 8))

    cd4_counts = [800, 600, 400, 200, 100]
    seborrheic = [80, 60, 40, 20, 10]
    kaposi = [5, 20, 40, 60, 70]
    herpes = [10, 30, 50, 70, 85]
    fungal = [15, 35, 55, 75, 90]

    ax.plot(cd4_counts, seborrheic, 'o-', linewidth=3, markersize=8, label='Seborrheic Dermatitis', color='#FF6B6B')
    ax.plot(cd4_counts, kaposi, 's-', linewidth=3, markersize=8, label='Kaposi Sarcoma', color='#4ECDC4')
    ax.plot(cd4_counts, herpes, '^-', linewidth=3, markersize=8, label='Herpes Infections', color='#45B7D1')
    ax.plot(cd4_counts, fungal, 'd-', linewidth=3, markersize=8, label='Fungal Infections', color='#FFA07A')

    ax.set_title('CD4 Count Correlation with Skin Manifestations', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('CD4 Count (cells/μL)', fontsize=14)
    ax.set_ylabel('Prevalence (%)', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.invert_xaxis()  # Higher CD4 on left

    # Add threshold lines
    ax.axvline(x=500, color='orange', linestyle='--', alpha=0.7, label='Symptomatic HIV threshold')
    ax.axvline(x=200, color='red', linestyle='--', alpha=0.7, label='AIDS threshold')

    plt.tight_layout()
    plt.savefig('cd4_skin_correlation.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("CD4-skin manifestation correlation chart created")

def create_hiv_dermatology_diagnostic_clues():
    """Create diagnostic clues infographic for HIV dermatology"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Title
    ax.text(6, 7.5, 'Diagnostic Clues for HIV in Dermatology Practice', ha='center', va='center',
            fontsize=16, fontweight='bold', color='#2E4057')

    clues = [
        ('Multiple concurrent\nskin conditions', 'Seborrheic dermatitis +\noral candidiasis +\nherpes zoster', 2, 6),
        ('Atypical presentations', 'Extensive tinea\nChronic ulcers\nWidespread molluscum', 6, 6),
        ('Poor response to\ntreatment', 'Recalcitrant infections\nFrequent relapses\nSevere reactions', 10, 6),
        ('Systemic symptoms', 'Weight loss\nFever\nLymphadenopathy', 2, 3),
        ('High-risk groups', 'MSM, IDU, FSW\nMultiple partners\nHistory of STIs', 6, 3),
        ('CD4 correlation', 'Onset with declining\nimmune function\nProgression with\nCD4 drop', 10, 3)
    ]

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']

    for i, (clue, examples, x, y) in enumerate(clues):
        # Clue box
        rect = FancyBboxPatch((x-1.8, y-1.2), 3.6, 1.8,
                            boxstyle="round,pad=0.1",
                            facecolor=colors[i], edgecolor='black', linewidth=2)
        ax.add_patch(rect)

        # Clue title
        ax.text(x, y-0.3, clue, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        # Examples
        ax.text(x, y-0.8, examples, ha='center', va='center',
                fontsize=9, color='white')

    plt.savefig('hiv_dermatology_diagnostic_clues.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close()
    print("HIV dermatology diagnostic clues infographic created")

def create_interactive_hiv_epidemiology_plotly():
    """Create interactive HIV epidemiology chart using Plotly"""
    # Indian states HIV data
    states = ['Nagaland', 'Manipur', 'Mizoram', 'Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Tamil Nadu', 'National']
    prevalence = [1.5, 1.4, 0.8, 0.4, 0.3, 0.3, 0.2, 0.22]
    population = [1.6, 2.9, 1.1, 49.4, 61.1, 112.4, 72.1, 1380]  # Million

    fig = px.bar(x=states, y=prevalence,
                 title='HIV Prevalence in India by State (2023)',
                 labels={'x': 'States/Regions', 'y': 'Prevalence (%)'},
                 color=prevalence,
                 color_continuous_scale='Reds')

    fig.update_layout(
        font=dict(size=12),
        title_font_size=16
    )

    fig.write_image('interactive_hiv_epidemiology.png', width=800, height=600)
    print("Interactive HIV epidemiology chart created")

if __name__ == "__main__":
    print("Creating HIV dermatology integration visualizations...")

    create_indian_hiv_epidemiology()
    create_hiv_transmission_routes()
    create_hiv_progression_timeline()
    create_dermatological_manifestations_spectrum()
    create_hiv_skin_conditions_infographic()
    create_art_regimens_comparison()
    create_naco_95_95_95_targets()
    create_hiv_prevention_pyramid()
    create_cd4_skin_manifestation_correlation()
    create_hiv_dermatology_diagnostic_clues()
    create_interactive_hiv_epidemiology_plotly()

    print("All HIV dermatology visualizations created successfully!")