import streamlit as st
import os
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="🌟 Jathin & Kethan Story Book",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .story-title {
        font-size: 2rem;
        color: #667EEA;
        margin: 1rem 0;
    }
    .story-text {
        font-size: 1.1rem;
        line-height: 1.6;
        margin: 1rem 0;
    }
    .moral-text {
        font-size: 1.2rem;
        color: #4FACFE;
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #4FACFE;
        margin: 1rem 0;
    }
    .sidebar-content {
        padding: 1rem;
    }
    .book-icon {
        font-size: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Story data
STORIES = {
    1: {
        "title": "🏴‍☠️ The Hidden Treasure Adventure",
        "subtitle": "A thrilling tale of discovery and family treasures!",
        "moral": "💝 Remember, little adventurers: The greatest treasures in life are the memories we make with the people we love! 💝"
    },
    2: {
        "title": "🐉 The Friendly Dragon",
        "subtitle": "A tale of friendship and overcoming fears!",
        "moral": "🌟 Remember, children: True friends help each other overcome fears and reach new heights! 🌟"
    },
    3: {
        "title": "🌳 The Magical Forest",
        "subtitle": "An enchanted forest where trees talk and animals dance!",
        "moral": "🌸 Remember, little ones: Nature is full of wonders. Listen to the trees, watch the animals, and you'll discover magic in the world around you! 🌸"
    },
    4: {
        "title": "🦸‍♂️ The Superhero Siblings",
        "subtitle": "Magical capes give the brothers superpowers!",
        "moral": "⭐ Remember, brave ones: You don't need capes to be a superhero. Being kind, helpful, and brave makes you a hero every day! ⭐"
    },
    5: {
        "title": "⏰ The Time-Traveling Clock",
        "subtitle": "A magical clock takes them through time!",
        "moral": "⏳ Remember, young time travelers: Every moment is a treasure. Make the most of your time by learning, loving, and living fully! ⏳"
    },
    6: {
        "title": "🐠 The Underwater Kingdom",
        "subtitle": "A magical shell lets them explore the ocean depths!",
        "moral": "🌊 Remember, ocean explorers: The sea is full of amazing creatures and treasures. Help keep our oceans clean and beautiful for everyone! 🌊"
    },
    7: {
        "title": "☁️ The Cloud Castle",
        "subtitle": "A rainbow ladder leads to a castle in the clouds!",
        "moral": "☁️ Remember, sky dreamers: Look up at the clouds and let your imagination soar. The world is full of wonders waiting to be discovered! ☁️"
    },
    8: {
        "title": "🎵 The Animal Orchestra",
        "subtitle": "Animals form a musical orchestra!",
        "moral": "🎼 Remember, young musicians: Everyone has music in their heart. Listen, practice, and create beautiful sounds with your friends! 🎼"
    },
    9: {
        "title": "⭐ The Wish-Granting Star",
        "subtitle": "A shooting star grants wishes!",
        "moral": "✨ Remember, wish makers: Stars can guide your dreams, but you have the power to make them come true through hard work and kindness! ✨"
    },
    10: {
        "title": "🌸 The Garden of Dreams",
        "subtitle": "A magical garden where dreams bloom like flowers!",
        "moral": "🌱 Remember, dreamers: Plant your dreams with care, water them with belief, and watch them grow into beautiful realities! 🌱"
    }
}

def load_story_text(story_num):
    """Load story text from file"""
    filename = f"story{story_num}.txt"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split content by illustrations
        parts = content.split("## Illustration")
        if len(parts) > 1:
            # Remove the title part and keep the story content
            story_content = parts[1:]
            # Clean up the content
            cleaned_parts = []
            for part in story_content:
                # Remove illustration headers and clean text
                lines = part.split('\n')
                # Skip the illustration description line and keep the story text
                story_lines = []
                in_story = False
                for line in lines[1:]:  # Skip illustration title
                    line = line.strip()
                    if line and not line.startswith('*') and not line.startswith('#'):
                        in_story = True
                        story_lines.append(line)
                    elif line.startswith('*') and in_story:
                        # This is the moral, stop here
                        break
                if story_lines:
                    cleaned_parts.append(' '.join(story_lines))

            return cleaned_parts
    return []

def get_story_illustrations(story_num):
    """Get illustration paths for a story"""
    illustrations = []
    for i in range(1, 5):
        img_path = f"images/story{story_num}_illustration{i}.png"
        if os.path.exists(img_path):
            illustrations.append(img_path)
    return illustrations

def main():
    # Header
    st.markdown('<h1 class="main-header">🌟 Jathin and Kethan Story Book 🌟</h1>', unsafe_allow_html=True)
    st.markdown("### *10 Magical Adventures for Young Dreamers*")
    st.markdown("---")

    # Sidebar for navigation
    st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.sidebar.markdown("## 📖 Story Navigation")
    st.sidebar.markdown("Choose a story to read:")

    # Story selection
    story_options = [f"Story {i}: {STORIES[i]['title'].split(' ', 1)[1]}" for i in range(1, 11)]
    selected_story = st.sidebar.selectbox("Select a Story:", story_options)

    # Extract story number
    story_num = int(selected_story.split(":")[0].replace("Story ", ""))

    # Download options
    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📥 Downloads")

    if st.sidebar.button("📄 Download PDF"):
        if os.path.exists("Jathin_Kethan_Story_Book_final.pdf"):
            with open("Jathin_Kethan_Story_Book_final.pdf", "rb") as f:
                st.sidebar.download_button(
                    label="Click to Download PDF",
                    data=f,
                    file_name="Jathin_Kethan_Story_Book.pdf",
                    mime="application/pdf"
                )
        else:
            st.sidebar.error("PDF not found")

    if st.sidebar.button("🌐 Download HTML"):
        if os.path.exists("Jathin_Kethan_story_book.html"):
            with open("Jathin_Kethan_story_book.html", "rb") as f:
                st.sidebar.download_button(
                    label="Click to Download HTML",
                    data=f,
                    file_name="Jathin_Kethan_story_book.html",
                    mime="text/html"
                )
        else:
            st.sidebar.error("HTML not found")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 🎨 About")
    st.sidebar.markdown("This interactive story book features:")
    st.sidebar.markdown("- 10 enchanting tales")
    st.sidebar.markdown("- Beautiful illustrations")
    st.sidebar.markdown("- Valuable life lessons")
    st.sidebar.markdown("- Perfect for ages 5-12")

    st.sidebar.markdown("---")
    st.sidebar.markdown("## 📧 Contact")
    st.sidebar.markdown("Created with ❤️ for young dreamers everywhere!")

    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f'<h2 class="story-title">{STORIES[story_num]["title"]}</h2>', unsafe_allow_html=True)
        st.markdown(f"*{STORIES[story_num]['subtitle']}*")
        st.markdown("---")

        # Load and display story content
        story_parts = load_story_text(story_num)
        illustrations = get_story_illustrations(story_num)

        # Display story with illustrations
        for i, (part, img_path) in enumerate(zip(story_parts, illustrations)):
            if os.path.exists(img_path):
                try:
                    img = Image.open(img_path)
                    st.image(img, caption=f"Illustration {i+1}", use_column_width=True)
                except Exception as e:
                    st.warning(f"Could not load illustration {i+1}")

            st.markdown(f'<div class="story-text">{part}</div>', unsafe_allow_html=True)

            if i < len(story_parts) - 1:  # Don't add spacer after last part
                st.markdown("---")

        # Display moral
        st.markdown(f'<div class="moral-text">{STORIES[story_num]["moral"]}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("## 🎭 Story Overview")
        st.markdown(f"**Story {story_num} of 10**")
        st.markdown(f"**Theme:** {STORIES[story_num]['title'].split()[1]}")
        st.markdown(f"**Main Characters:** Jathin (10) and Kethan (8)")

        # Story navigation
        st.markdown("### 📚 Quick Navigation")
        nav_cols = st.columns(2)
        for i in range(1, 11):
            if i <= 5:
                with nav_cols[0]:
                    if st.button(f"Story {i}", key=f"nav_{i}"):
                        st.experimental_rerun()
            else:
                with nav_cols[1]:
                    if st.button(f"Story {i}", key=f"nav_{i}"):
                        st.experimental_rerun()

        # Educational value
        st.markdown("### 🎓 Learning Value")
        if story_num == 1:
            st.markdown("• Family bonds and memories")
            st.markdown("• Following directions")
            st.markdown("• Problem-solving skills")
        elif story_num == 2:
            st.markdown("• Overcoming fears")
            st.markdown("• Friendship and trust")
            st.markdown("• Helping others")
        elif story_num == 3:
            st.markdown("• Nature appreciation")
            st.markdown("• Animal behavior")
            st.markdown("• Environmental awareness")
        elif story_num == 4:
            st.markdown("• Kindness and helping")
            st.markdown("• Teamwork")
            st.markdown("• Responsibility")
        elif story_num == 5:
            st.markdown("• Time management")
            st.markdown("• Historical awareness")
            st.markdown("• Future thinking")
        elif story_num == 6:
            st.markdown("• Ocean conservation")
            st.markdown("• Marine life")
            st.markdown("• Exploration")
        elif story_num == 7:
            st.markdown("• Weather science")
            st.markdown("• Imagination")
            st.markdown("• Perspective")
        elif story_num == 8:
            st.markdown("• Music appreciation")
            st.markdown("• Cooperation")
            st.markdown("• Creativity")
        elif story_num == 9:
            st.markdown("• Goal setting")
            st.markdown("• Hard work")
            st.markdown("• Self-reliance")
        elif story_num == 10:
            st.markdown("• Dream cultivation")
            st.markdown("• Patience")
            st.markdown("• Personal growth")

    # Footer
    st.markdown("---")
    st.markdown("### 🌟 Thank you for reading!")
    st.markdown("This story book was created with love for Jathin and Kethan, and dedicated to all young dreamers around the world.")
    st.markdown("📚 *Keep reading, keep dreaming, keep exploring!* 📚")

if __name__ == "__main__":
    main()
