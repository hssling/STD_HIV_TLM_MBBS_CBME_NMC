import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
import warnings
warnings.filterwarnings('ignore')

# Set style for matplotlib
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Color scheme: Medical blue, Indian saffron, white backgrounds
colors = {
    'primary': '#0066CC',
    'secondary': '#FF9933',
    'accent': '#138808',
    'background': 'white',
    'text': '#333333'
}

def create_std_classification_pyramid():
    """Create STD Classification Pyramid visualization"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Define pyramid levels
    levels = [
        {'name': 'Fungal STDs\n(Candidiasis)', 'y': 1, 'width': 2, 'color': '#FFD700', 'examples': 'Candida albicans'},
        {'name': 'Parasitic STDs\n(Trichomoniasis, Pubic lice)', 'y': 3, 'width': 4, 'color': '#32CD32', 'examples': 'Trichomonas vaginalis\nPhthirus pubis'},
        {'name': 'Viral STDs\n(HIV, HSV, HPV, Hepatitis B)', 'y': 5, 'width': 6, 'color': '#FF4444', 'examples': 'HIV, HSV-1/2, HPV 16/18\nHBV'},
        {'name': 'Bacterial STDs\n(Gonorrhea, Syphilis, Chlamydia)', 'y': 7, 'width': 8, 'color': '#4169E1', 'examples': 'Neisseria gonorrhoeae\nTreponema pallidum\nChlamydia trachomatis'}
    ]

    for level in levels:
        # Create trapezoid for each level
        x_left = (10 - level['width']) / 2
        x_right = x_left + level['width']

        # Bottom of trapezoid
        bottom_points = [(x_left, level['y']), (x_right, level['y']),
                        (x_right, level['y'] + 1), (x_left, level['y'] + 1)]

        # Top of trapezoid (next level or top)
        if level['y'] < 7:  # Not the top level
            next_width = next(l['width'] for l in levels if l['y'] == level['y'] + 2)
            x_left_top = (10 - next_width) / 2
            x_right_top = x_left_top + next_width
            top_points = [(x_left_top, level['y'] + 1), (x_right_top, level['y'] + 1),
                         (x_right_top, level['y'] + 2), (x_left_top, level['y'] + 2)]
        else:
            top_points = [(x_left, level['y'] + 1), (x_right, level['y'] + 1),
                         (x_right, level['y'] + 1.5), (x_left, level['y'] + 1.5)]

        # Create polygon
        poly_points = bottom_points + top_points
        polygon = Polygon(poly_points, facecolor=level['color'], edgecolor='black', alpha=0.8)
        ax.add_patch(polygon)

        # Add text
        ax.text(5, level['y'] + 0.5, level['name'], ha='center', va='center',
                fontsize=10, fontweight='bold', color='black')
        ax.text(5, level['y'] + 0.2, level['examples'], ha='center', va='center',
                fontsize=8, color='black')

    ax.set_title('STD Classification Pyramid\nCommunity Medicine Perspective', fontsize=16, fontweight='bold', color=colors['primary'])
    ax.set_xlabel('Classification Hierarchy', fontsize=12)
    ax.set_ylabel('Level of Complexity', fontsize=12)
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.tight_layout()
    plt.savefig('std_classification_pyramid.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_indian_hiv_prevalence_map():
    """Create Indian HIV Prevalence Map using choropleth"""
    # Indian states data (simplified for demonstration)
    states_data = {
        'State': ['Maharashtra', 'Karnataka', 'Andhra Pradesh', 'Telangana', 'Tamil Nadu',
                 'Kerala', 'Delhi', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'West Bengal',
                 'Nagaland', 'Manipur', 'Mizoram', 'Arunachal Pradesh'],
        'HIV_Prevalence': [0.25, 0.22, 0.18, 0.20, 0.15, 0.12, 0.28, 0.14, 0.11, 0.08, 0.09,
                          1.5, 1.4, 1.2, 0.9],
        'Population_Lakhs': [125.7, 67.6, 52.2, 39.5, 77.8, 35.7, 2.1, 63.9, 81.0, 225.0, 100.9,
                           2.1, 3.2, 1.2, 1.6]
    }

    df = pd.DataFrame(states_data)

    # Create choropleth map using plotly
    fig = px.choropleth(
        df,
        locations='State',
        locationmode='country names',
        color='HIV_Prevalence',
        hover_name='State',
        hover_data=['HIV_Prevalence', 'Population_Lakhs'],
        color_continuous_scale='Reds',
        title='HIV Prevalence in Indian States (2023)<br>NACP Data',
        labels={'HIV_Prevalence': 'HIV Prevalence (%)'}
    )

    fig.update_geos(
        visible=False,
        resolution=50,
        showcountries=True,
        countrycolor="Black",
        showsubunits=True,
        subunitcolor="Black",
        fitbounds="locations"
    )

    fig.update_layout(
        title_font_size=16,
        font_color=colors['text'],
        paper_bgcolor=colors['background']
    )

    fig.write_image('indian_hiv_prevalence_map.png', width=800, height=600)
    fig.write_html('indian_hiv_prevalence_map.html')

def create_syphilis_staging_timeline():
    """Create Syphilis Staging Timeline"""
    fig, ax = plt.subplots(figsize=(14, 6))

    # Timeline data
    stages = [
        {'name': 'Primary Syphilis', 'duration': '2-12 weeks', 'description': 'Painless chancre\nRegional lymphadenopathy'},
        {'name': 'Secondary Syphilis', 'duration': '6-24 weeks', 'description': 'Generalized rash\nMucous patches\nCondylomata lata'},
        {'name': 'Latent Syphilis', 'duration': 'Asymptomatic', 'description': 'Seropositive\nNo clinical symptoms\nPotential reactivation'},
        {'name': 'Tertiary Syphilis', 'duration': '>2 years', 'description': 'Cardiovascular\nNeurosyphilis\nGummatous lesions'}
    ]

    colors_stages = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']

    # Create timeline
    x_positions = [0, 3, 6, 9]
    y_position = 2

    for i, stage in enumerate(stages):
        # Draw stage box
        rect = patches.Rectangle((x_positions[i], y_position-0.5), 2.5, 1,
                               linewidth=2, edgecolor='black', facecolor=colors_stages[i], alpha=0.7)
        ax.add_patch(rect)

        # Add stage name
        ax.text(x_positions[i] + 1.25, y_position + 0.8, stage['name'],
                ha='center', va='center', fontsize=12, fontweight='bold')

        # Add duration
        ax.text(x_positions[i] + 1.25, y_position + 0.3, stage['duration'],
                ha='center', va='center', fontsize=10, style='italic')

        # Add description
        ax.text(x_positions[i] + 1.25, y_position - 0.1, stage['description'],
                ha='center', va='center', fontsize=9, wrap=True)

        # Draw arrow to next stage (except last)
        if i < len(stages) - 1:
            ax.arrow(x_positions[i] + 2.5, y_position, 0.5, 0, head_width=0.1, head_length=0.1,
                    fc='black', ec='black', alpha=0.7)

    # Add timeline axis
    ax.plot([0, 11.5], [y_position-0.5, y_position-0.5], 'k-', linewidth=2)
    ax.text(11.5, y_position-0.7, 'Time →', ha='right', fontsize=12, fontweight='bold')

    ax.set_xlim(-0.5, 12)
    ax.set_ylim(0.5, 4)
    ax.set_title('Natural History of Syphilis\nStaging and Clinical Features',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('syphilis_staging_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_condom_effectiveness_chart():
    """Create Condom Use Effectiveness Chart"""
    stds = ['HIV/AIDS', 'Gonorrhea', 'Chlamydia', 'Syphilis', 'HPV', 'Herpes']
    effectiveness = [95, 85, 85, 70, 70, 55]

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.barh(stds, effectiveness, color=[colors['primary'] if x >= 85 else colors['secondary'] for x in effectiveness],
                   alpha=0.8, edgecolor='black', linewidth=1)

    # Add percentage labels on bars
    for bar, eff in zip(bars, effectiveness):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{eff}%', ha='left', va='center', fontweight='bold', fontsize=10)

    ax.set_xlabel('Prevention Effectiveness (%)', fontsize=12)
    ax.set_title('Condom Effectiveness for STD Prevention\nConsistent and Correct Use',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.set_xlim(0, 100)
    ax.grid(axis='x', alpha=0.3)

    # Add footnote
    ax.text(0, -0.5, '*Based on consistent and correct condom use. Effectiveness varies with usage patterns.',
            fontsize=9, style='italic', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig('condom_effectiveness_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_naco_program_timeline():
    """Create NACO Program Impact Timeline"""
    fig, ax = plt.subplots(figsize=(14, 8))

    # Timeline data
    events = [
        {'year': 2007, 'event': 'NACP-III Launch', 'impact': '66% reduction in new infections'},
        {'year': 2012, 'event': 'Free ART initiation', 'impact': '80% ART coverage achieved'},
        {'year': 2017, 'event': 'NACP-IV (2017-2021)', 'impact': '23.1 lakh PLHIV identified'},
        {'year': 2021, 'event': 'NACP-V (2021-2026)', 'impact': '90% viral suppression target'},
        {'year': 2023, 'event': 'Current achievements', 'impact': '800 million condoms distributed'}
    ]

    y_positions = [6, 4, 2, 1, 0]

    # Draw timeline
    ax.plot([2007, 2023], [3, 3], 'k-', linewidth=3, alpha=0.7)

    for i, event in enumerate(events):
        # Draw event marker
        ax.scatter(event['year'], 3, s=200, c=colors['primary'], edgecolor='black', zorder=5)

        # Add year label
        ax.text(event['year'], 3.3, str(event['year']), ha='center', va='bottom',
                fontsize=10, fontweight='bold')

        # Add event description
        ax.text(event['year'], y_positions[i], event['event'], ha='center', va='center',
                fontsize=11, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

        # Add impact description
        ax.text(event['year'], y_positions[i] - 0.8, event['impact'], ha='center', va='center',
                fontsize=9, style='italic', color=colors['accent'])

    ax.set_xlim(2005, 2025)
    ax.set_ylim(-2, 7)
    ax.set_title('NACO Program Impact Timeline\nHIV/AIDS Control in India (2007-2023)',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('naco_program_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_high_risk_groups_chart():
    """Create High-Risk Groups Prevalence Comparison"""
    groups = ['Men who have sex\nwith men', 'Female sex workers', 'Injecting drug users',
              'Migrant laborers', 'General population']
    prevalence = [17.0, 2.8, 2.1, 1.5, 0.22]

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.barh(groups, prevalence, color=colors['primary'], alpha=0.8,
                   edgecolor='black', linewidth=1)

    # Add percentage labels
    for bar, prev in zip(bars, prevalence):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
                f'{prev}%', ha='left', va='center', fontweight='bold', fontsize=10)

    ax.set_xlabel('HIV Prevalence (%)', fontsize=12)
    ax.set_title('HIV Prevalence in High-Risk Groups vs General Population\nIndia (NACO 2023)',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.grid(axis='x', alpha=0.3)

    # Highlight MSM bar
    bars[0].set_color(colors['secondary'])

    plt.tight_layout()
    plt.savefig('high_risk_groups_prevalence.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_prevention_pyramid():
    """Create Prevention Strategy Pyramid"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Pyramid levels
    levels = [
        {'name': 'Population Level', 'strategies': ['Comprehensive Sexuality\nEducation', 'Policy and Legal\nFrameworks', 'Healthcare System\nStrengthening'], 'y': 6, 'width': 8, 'color': '#E8F4F8'},
        {'name': 'Community Level', 'strategies': ['Targeted Interventions', 'Condom Distribution\nPrograms', 'Community Awareness\nCampaigns'], 'y': 3, 'width': 6, 'color': '#D1ECF1'},
        {'name': 'Individual Level', 'strategies': ['Safe Sex Practices', 'Regular STI Screening', 'Vaccination (HPV, Hep B)'], 'y': 0, 'width': 4, 'color': '#B8DAFF'}
    ]

    for level in levels:
        # Create trapezoid
        x_left = (10 - level['width']) / 2
        x_right = x_left + level['width']

        # Calculate top width for next level
        if level['y'] > 0:
            next_level = next(l for l in levels if l['y'] == level['y'] - 3)
            x_left_top = (10 - next_level['width']) / 2
            x_right_top = x_left_top + next_level['width']
        else:
            x_left_top = x_left + 1
            x_right_top = x_right - 1

        # Create polygon
        poly_points = [(x_left, level['y']), (x_right, level['y']),
                      (x_right, level['y'] + 2), (x_left, level['y'] + 2),
                      (x_left_top, level['y'] + 2), (x_right_top, level['y'] + 2),
                      (x_right_top, level['y'] + 3), (x_left_top, level['y'] + 3)]
        polygon = Polygon(poly_points, facecolor=level['color'], edgecolor='black', alpha=0.8)
        ax.add_patch(polygon)

        # Add level name
        ax.text(5, level['y'] + 2.5, level['name'], ha='center', va='center',
                fontsize=12, fontweight='bold', color=colors['text'])

        # Add strategies
        for i, strategy in enumerate(level['strategies']):
            ax.text(5, level['y'] + 1.8 - i*0.4, strategy, ha='center', va='center',
                    fontsize=9, color=colors['text'])

    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 9)
    ax.set_title('Prevention Strategy Pyramid\nMulti-level Approach to STD Control',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('prevention_strategy_pyramid.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_std_complications_infographic():
    """Create STD Complications Infographic"""
    fig, ax = plt.subplots(figsize=(14, 10))

    # Complications data
    complications = {
        'PID/Infertility': {'std': 'Chlamydia/Gonorrhea', 'pos': (2, 8)},
        'Ectopic Pregnancy': {'std': 'Chlamydia/Gonorrhea', 'pos': (4, 6)},
        'Chronic Pelvic Pain': {'std': 'Chlamydia/Gonorrhea', 'pos': (8, 6)},
        'Neonatal Infections': {'std': 'Syphilis/HIV/Hepatitis B', 'pos': (6, 4)},
        'Cervical Cancer': {'std': 'HPV', 'pos': (4, 2)},
        'Liver Cirrhosis': {'std': 'Hepatitis B', 'pos': (8, 2)},
        'Neurosyphilis/Gummas': {'std': 'Syphilis', 'pos': (6, 0)}
    }

    # Draw connecting arrows
    connections = [
        ((2, 8), (4, 6)), ((4, 6), (8, 6)), ((8, 6), (6, 4)),
        ((6, 4), (4, 2)), ((6, 4), (8, 2)), ((8, 2), (6, 0))
    ]

    for start, end in connections:
        ax.arrow(start[0], start[1], end[0]-start[0], end[1]-start[1],
                head_width=0.2, head_length=0.2, fc='gray', ec='gray', alpha=0.6)

    # Draw complication boxes
    for comp, data in complications.items():
        rect = patches.Rectangle((data['pos'][0]-1.5, data['pos'][1]-0.5), 3, 1,
                               linewidth=2, edgecolor='black', facecolor=colors['secondary'], alpha=0.8)
        ax.add_patch(rect)

        # Add text
        ax.text(data['pos'][0], data['pos'][1], comp, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')
        ax.text(data['pos'][0], data['pos'][1]-0.2, f'({data["std"]})', ha='center', va='center',
                fontsize=8, color='white')

    ax.set_xlim(0, 12)
    ax.set_ylim(-1, 10)
    ax.set_title('STD Complications: From Infection to Severe Outcomes\nPrevention Through Early Treatment',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('std_complications_infographic.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_drug_resistance_trends():
    """Create Drug Resistance Trends Line Graph"""
    years = list(range(2010, 2023))
    resistance_data = {
        'Gonorrhea': {
            'Ciprofloxacin': [85, 87, 89, 91, 93, 94, 95, 95, 95, 95, 95, 95, 95],
            'Penicillin': [70, 72, 74, 76, 78, 80, 82, 84, 85, 85, 85, 85, 85],
            'Tetracycline': [65, 67, 69, 71, 73, 75, 75, 75, 75, 75, 75, 75],
            'Azithromycin': [5, 7, 9, 11, 13, 15, 15, 15, 15, 15, 15, 15],
            'Ceftriaxone': [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
        }
    }

    fig, ax = plt.subplots(figsize=(12, 6))

    colors_resistance = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#F7DC6F']

    for i, (drug, resistance) in enumerate(resistance_data['Gonorrhea'].items()):
        ax.plot(years, resistance, marker='o', linewidth=2, label=drug,
                color=colors_resistance[i], markersize=6)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Resistance Percentage (%)', fontsize=12)
    ax.set_title('Antibiotic Resistance Trends in Gonorrhea\nIndia (2010-2022)',
                fontsize=16, fontweight='bold', color=colors['primary'])
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(alpha=0.3)
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig('drug_resistance_trends.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_success_metrics_dashboard():
    """Create Success Metrics Dashboard"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Metric 1: New Infections Reduction
    ax1.bar(['2007', '2023'], [100, 34], color=colors['primary'], alpha=0.8)
    ax1.set_title('New HIV Infections\n(66% Reduction)', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Relative Index')
    ax1.grid(axis='y', alpha=0.3)

    # Metric 2: ART Coverage
    ax2.pie([80, 20], labels=['On ART', 'Not on ART'], colors=[colors['primary'], '#E8E8E8'],
            autopct='%1.0f%%', startangle=90)
    ax2.set_title('ART Coverage\n(80% of PLHIV)', fontsize=12, fontweight='bold')

    # Metric 3: Viral Suppression
    ax3.barh(['Target', 'Achieved'], [90, 90], color=colors['accent'], alpha=0.8)
    ax3.set_title('Viral Suppression\n(90% Target Met)', fontsize=12, fontweight='bold')
    ax3.set_xlabel('Percentage (%)')

    # Metric 4: Condom Distribution
    years = ['2019', '2020', '2021', '2022', '2023']
    condoms = [750, 780, 790, 795, 800]
    ax4.plot(years, condoms, marker='o', linewidth=2, color=colors['secondary'])
    ax4.set_title('Condom Distribution\n(800 Million Annually)', fontsize=12, fontweight='bold')
    ax4.set_ylabel('Millions')
    ax4.grid(alpha=0.3)

    fig.suptitle('NACP Success Metrics Dashboard\nHIV/AIDS Control Program Achievements',
                fontsize=16, fontweight='bold', color=colors['primary'])
    plt.tight_layout()
    plt.savefig('success_metrics_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all STD visualizations"""
    print("Creating STD visualizations for community medicine...")

    # Create all visualizations
    create_std_classification_pyramid()
    print("✓ STD Classification Pyramid created")

    create_indian_hiv_prevalence_map()
    print("✓ Indian HIV Prevalence Map created")

    create_syphilis_staging_timeline()
    print("✓ Syphilis Staging Timeline created")

    create_condom_effectiveness_chart()
    print("✓ Condom Effectiveness Chart created")

    create_naco_program_timeline()
    print("✓ NACO Program Impact Timeline created")

    create_high_risk_groups_chart()
    print("✓ High-Risk Groups Prevalence Chart created")

    create_prevention_pyramid()
    print("✓ Prevention Strategy Pyramid created")

    create_std_complications_infographic()
    print("✓ STD Complications Infographic created")

    create_drug_resistance_trends()
    print("✓ Drug Resistance Trends created")

    create_success_metrics_dashboard()
    print("✓ Success Metrics Dashboard created")

    print("\nAll visualizations saved as PNG files!")
    print("\nSummary of Visualizations Created:")
    print("1. STD Classification Pyramid - Hierarchical classification of STDs")
    print("2. Indian HIV Prevalence Map - State-wise HIV prevalence choropleth")
    print("3. Syphilis Staging Timeline - Natural history of syphilis infection")
    print("4. Condom Effectiveness Chart - Prevention effectiveness by STD type")
    print("5. NACO Program Impact Timeline - Key achievements since 2007")
    print("6. High-Risk Groups Prevalence - HIV prevalence comparison")
    print("7. Prevention Strategy Pyramid - Multi-level prevention approach")
    print("8. STD Complications Infographic - Disease progression and outcomes")
    print("9. Drug Resistance Trends - Antibiotic resistance in gonorrhea")
    print("10. Success Metrics Dashboard - NACP program achievements")

if __name__ == "__main__":
    main()