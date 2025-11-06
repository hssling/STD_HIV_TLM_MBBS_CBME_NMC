from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

def create_story_book_pdf():
    # Create PDF document
    doc = SimpleDocTemplate("Jathin_Kethan_Story_Book_final.pdf", pagesize=A4)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#FF6B6B'),
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor('#666666'),
        alignment=TA_CENTER,
        italic=True,
        spaceAfter=30
    )

    story_text_style = ParagraphStyle(
        'StoryText',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#333333'),
        alignment=TA_LEFT,
        spaceAfter=12,
        leading=16
    )

    moral_style = ParagraphStyle(
        'Moral',
        parent=styles['Normal'],
        fontSize=14,
        textColor=HexColor('#FFFFFF'),
        alignment=TA_CENTER,
        backColor=HexColor('#4FACFE'),
        borderColor=HexColor('#00F2FE'),
        borderWidth=2,
        borderPadding=10,
        spaceAfter=20
    )

    toc_title_style = ParagraphStyle(
        'TOCTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=HexColor('#FFFFFF'),
        alignment=TA_CENTER,
        backColor=HexColor('#667EEA'),
        borderColor=HexColor('#764BA2'),
        borderWidth=2,
        borderPadding=10,
        spaceAfter=20
    )

    toc_item_style = ParagraphStyle(
        'TOCItem',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#FFFFFF'),
        backColor=HexColor('#764BA2'),
        borderColor=HexColor('#FFFFFF'),
        borderWidth=1,
        borderPadding=8,
        spaceAfter=8
    )

    # Build the story content
    story = []

    # Title page
    story.append(Paragraph("🌟 Jathin and Kethan Story Book 🌟", title_style))
    story.append(Spacer(1, 20))
    story.append(Paragraph("10 Magical Adventures for Young Dreamers!", subtitle_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph("✨📚✨", ParagraphStyle('Center', alignment=TA_CENTER, fontSize=18)))
    story.append(PageBreak())

    # Table of Contents
    story.append(Paragraph("📖 Table of Contents 🎭", toc_title_style))
    story.append(Spacer(1, 20))

    toc_items = [
        "Story 1: The Hidden Treasure Adventure 🏴‍☠️\nJathin and Kethan discover a treasure map leading to family memories!",
        "Story 2: The Friendly Dragon 🐉\nThe brothers befriend a lonely dragon and help him overcome his fear!",
        "Story 3: The Magical Forest 🌳\nAn enchanted forest where trees talk and animals dance!",
        "Story 4: The Superhero Siblings 🦸‍♂️\nMagical capes give the brothers superpowers!",
        "Story 5: The Time-Traveling Clock ⏰\nA magical clock takes them through time!",
        "Story 6: The Underwater Kingdom 🐠\nA magical shell lets them explore the ocean depths!",
        "Story 7: The Cloud Castle ☁️\nA rainbow ladder leads to a castle in the clouds!",
        "Story 8: The Animal Orchestra 🎵\nAnimals form a musical orchestra!",
        "Story 9: The Wish-Granting Star ⭐\nA shooting star grants wishes!",
        "Story 10: The Garden of Dreams 🌸\nA magical garden where dreams bloom like flowers!"
    ]

    for item in toc_items:
        story.append(Paragraph(item, toc_item_style))

    story.append(PageBreak())

    # Story 1: The Hidden Treasure Adventure
    story.append(Paragraph("Story 1: The Hidden Treasure Adventure 🏴‍☠️", title_style))
    story.append(Paragraph("A thrilling tale of discovery and family treasures!", subtitle_style))

    # Add illustration placeholder
    try:
        img_path = "images/story1_illustration1.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 1: The Discovery]", story_text_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Once upon a time, in a cozy house at the edge of a sunny town, lived two brave brothers named Jathin and Kethan. Jathin was ten years old and loved solving puzzles, while Kethan was eight and always ready for an adventure.", story_text_style))
    story.append(Paragraph("One rainy afternoon, while exploring their grandpa's old attic, they stumbled upon a dusty chest hidden behind some forgotten boxes. \"Look what I found!\" Jathin exclaimed, pulling out a yellowed parchment. It was a treasure map!", story_text_style))
    story.append(Paragraph("The map showed their town with winding paths, a sparkling river, and a big red X at the top of Mystery Hill. \"This must lead to buried treasure!\" Kethan shouted, his eyes shining with excitement.", story_text_style))

    # Continue with more illustrations and text for Story 1
    try:
        img_path = "images/story1_illustration2.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 2: Crossing the River]", story_text_style))

    story.append(Paragraph("Their parents gave them permission to explore, but warned them to be careful and return before sunset. Armed with a backpack of snacks, a compass, and the map, the brothers set off on their grand adventure.", story_text_style))
    story.append(Paragraph("Their first challenge was crossing the Sparkling River. The water rushed swiftly, but they found large stepping stones that formed a natural bridge. Jathin went first, testing each stone to make sure it was steady. \"It's safe!\" he called back to Kethan. Kethan followed carefully, using a long stick for balance. As they crossed, they spotted rainbow-colored fish jumping in the water and dragonflies dancing in the air.", story_text_style))

    # Add more illustrations and continue the story
    try:
        img_path = "images/story1_illustration3.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 3: The Riddle Stone]", story_text_style))

    story.append(Paragraph("Next, they climbed the gentle slope of Mystery Hill. At the halfway point, they found a large stone covered in moss. Carved into the stone were these words:", story_text_style))
    story.append(Paragraph("\"I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\"", story_text_style))
    story.append(Paragraph("Jathin read the riddle aloud. \"What could it be?\" he wondered. Kethan looked around the forest. \"Maybe it's a tree? No, trees have bodies.\" Suddenly, Kethan pointed to the treetops. \"Look! The leaves are rustling in the wind!\" They realized the answer was \"the wind.\" The stone slid aside, revealing a hidden path.", story_text_style))

    try:
        img_path = "images/story1_illustration4.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 4: The Treasure Chest]", story_text_style))

    story.append(Paragraph("Following the path to the top of Mystery Hill, they found the spot marked with the red X. They dug carefully and soon uncovered a small wooden chest. With trembling hands, they opened it. Inside wasn't piles of gold or jewels, but old photographs, letters, and small keepsakes from their family's past.", story_text_style))
    story.append(Paragraph("\"This is the real treasure,\" Jathin said softly, holding up a photo of their grandparents as children. \"It's our family's memories.\"", story_text_style))
    story.append(Paragraph("Kethan nodded, tears of joy in his eyes. \"The best adventures aren't about finding gold, but discovering what really matters.\"", story_text_style))
    story.append(Paragraph("As the sun set behind them, painting the sky in beautiful colors, the brothers carried their treasure home, knowing they had found something far more valuable than any buried gold.", story_text_style))

    story.append(Paragraph("💝 Remember, little adventurers: The greatest treasures in life are the memories we make with the people we love! 💝", moral_style))

    story.append(PageBreak())

    # Story 2: The Friendly Dragon
    story.append(Paragraph("Story 2: The Friendly Dragon 🐉", title_style))
    story.append(Paragraph("A tale of friendship and overcoming fears!", subtitle_style))

    # Add illustrations for Story 2
    try:
        img_path = "images/story2_illustration1.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 1: The Mysterious Cave]", story_text_style))

    story.append(Paragraph("Once upon a time, Jathin and Kethan decided to explore the Whispering Woods behind their house. These woods were said to be magical, filled with secrets and wonders. Jathin, being the older brother, carried a flashlight, while Kethan clutched his favorite stuffed bear for courage.", story_text_style))
    story.append(Paragraph("As they wandered deeper into the woods, they heard strange noises - not scary ones, but sad-sounding sighs and gentle rumbles. \"What could that be?\" Kethan whispered. Following the sounds, they came upon a huge cave hidden behind a waterfall of vines.", story_text_style))
    story.append(Paragraph("Peeking inside, they saw something amazing: a dragon! But this wasn't a fierce, fire-breathing dragon from storybooks. This dragon was green and scaly, with kind eyes and droopy wings. He looked lonely and a little sad.", story_text_style))

    try:
        img_path = "images/story2_illustration2.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 2: Meeting the Dragon]", story_text_style))

    story.append(Paragraph("\"Hello,\" Jathin said bravely. \"We're Jathin and Kethan. What's your name?\"", story_text_style))
    story.append(Paragraph("The dragon blinked his large eyes. \"I am Ember,\" he replied in a deep but gentle voice. \"I've been alone for a very long time. Dragons like me are supposed to fly and breathe fire, but... I can't fly. My wings are too heavy, and I'm afraid of heights.\"", story_text_style))
    story.append(Paragraph("Kethan stepped forward, his fear forgotten. \"That's okay! We can be your friends. Maybe we can help you learn to fly!\"", story_text_style))
    story.append(Paragraph("Ember's eyes lit up. \"Really? You would do that for me?\"", story_text_style))

    try:
        img_path = "images/story2_illustration3.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 3: Playing Games]", story_text_style))

    story.append(Paragraph("For the next few days, Jathin and Kethan visited Ember every afternoon. They brought him fruits from their garden and told him stories about their adventures. Ember shared tales of ancient times when dragons roamed freely.", story_text_style))
    story.append(Paragraph("One day, they decided to help Ember overcome his fear. \"Flying isn't just about wings,\" Jathin explained. \"It's about believing you can do it.\" They started small - teaching Ember to jump over small rocks, then bigger ones.", story_text_style))
    story.append(Paragraph("They played games in the cave: tag, where Ember used his long tail to gently tag them; hide and seek, where Ember counted to one hundred (dragons count very slowly); and storytelling, where each shared their dreams.", story_text_style))

    try:
        img_path = "images/story2_illustration4.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 4: The First Flight]", story_text_style))

    story.append(Paragraph("Finally, the big day came. They led Ember to a gentle hill overlooking the valley. \"You can do this,\" Kethan encouraged. \"We're right here with you.\"", story_text_style))
    story.append(Paragraph("Ember took a deep breath, spread his wings, and jumped. For a moment, nothing happened. Then, with a mighty flap, he caught the wind! He didn't soar high like other dragons, but he flew - gliding just above the ground, circling the hill.", story_text_style))
    story.append(Paragraph("Jathin and Kethan cheered and clapped. \"You did it! You're flying!\"", story_text_style))
    story.append(Paragraph("Ember landed gently, his eyes sparkling with joy. \"Thank you, my friends. You taught me that friendship gives you wings stronger than any dragon could have alone.\"", story_text_style))
    story.append(Paragraph("From that day on, Ember became the guardian of the Whispering Woods, and Jathin and Kethan had a dragon friend who would always be there for them.", story_text_style))

    story.append(Paragraph("🌟 Remember, children: True friends help each other overcome fears and reach new heights! 🌟", moral_style))
    story.append(PageBreak())

    # Story 3: The Magical Forest
    story.append(Paragraph("Story 3: The Magical Forest 🌳", title_style))
    story.append(Paragraph("An enchanted forest where trees talk and animals dance!", subtitle_style))

    try:
        img_path = "images/story3_illustration1.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 1: The Secret Entrance]", story_text_style))

    story.append(Paragraph("Once upon a time, Jathin and Kethan discovered a secret path in their backyard that led to a magical forest. This wasn't an ordinary forest - it was alive with wonder and filled with talking trees, singing flowers, and dancing animals.", story_text_style))
    story.append(Paragraph("The brothers had been playing in the garden when Kethan noticed a narrow opening between two old oak trees. \"Look, Jathin! There's a path we never saw before!\" As they stepped through, the trees seemed to whisper greetings.", story_text_style))
    story.append(Paragraph("\"Welcome, young explorers,\" said a tall oak tree with a wise face in its bark. \"You have entered the Enchanted Grove, where nature comes alive.\"", story_text_style))

    try:
        img_path = "images/story3_illustration2.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 2: Meeting the Animals]", story_text_style))

    story.append(Paragraph("As they walked deeper, they met all sorts of friendly creatures. A wise old owl named Oliver greeted them from his branch. \"Hello, children! What brings you to our magical home?\"", story_text_style))
    story.append(Paragraph("\"We're exploring,\" Jathin replied. \"This place is amazing!\"", story_text_style))
    story.append(Paragraph("Oliver introduced them to his friends: Benny the Bunny, who could hop incredibly high; Squeaky the Squirrel, who collected the shiniest acorns; and Daisy the Deer, who was as graceful as a dancer.", story_text_style))
    story.append(Paragraph("The animals showed the boys around. They visited a meadow where flowers sang sweet songs, and a pond where fish performed acrobatic jumps.", story_text_style))

    try:
        img_path = "images/story3_illustration3.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 3: The Tree Council]", story_text_style))

    story.append(Paragraph("The brothers were invited to the Great Tree Council, where the oldest trees shared their wisdom. \"We trees have stood here for hundreds of years,\" said Grandmother Willow, the eldest oak. \"We have seen many changes in the world.\"", story_text_style))
    story.append(Paragraph("\"We protect the forest and teach lessons to those who listen,\" added another tree.", story_text_style))
    story.append(Paragraph("The animals joined in, sharing their stories. Benny told how he learned to share his carrots with friends, and Squeaky explained how storing food for winter taught patience.", story_text_style))
    story.append(Paragraph("Jathin and Kethan listened carefully, learning that every creature in the forest had a role to play.", story_text_style))

    try:
        img_path = "images/story3_illustration4.png"
        if os.path.exists(img_path):
            img = Image(img_path, 6*inch, 4.5*inch)
            story.append(img)
    except:
        story.append(Paragraph("[Illustration 4: The Forest Song]", story_text_style))

    story.append(Paragraph("As evening fell, the forest came alive with music. All the creatures joined in a grand song - trees rustled their leaves, flowers hummed melodies, and animals danced in circles.", story_text_style))
    story.append(Paragraph("Jathin and Kethan joined the song, their voices blending with the forest's magic. They learned the Forest Song, which celebrated friendship, nature, and the beauty of working together.", story_text_style))
    story.append(Paragraph("When it was time to go home, Grandmother Willow gave them each a small acorn. \"Plant these in your garden,\" she said. \"They will remind you of the magic within nature.\"", story_text_style))
    story.append(Paragraph("Back home, the brothers planted the acorns and watched as tiny sprouts appeared. They knew that magic wasn't just in faraway forests - it was everywhere, if you knew how to look.", story_text_style))

    story.append(Paragraph("🌸 Remember, little ones: Nature is full of wonders. Listen to the trees, watch the animals, and you'll discover magic in the world around you! 🌸", moral_style))
    story.append(PageBreak())

    # Continue with Stories 4-10 in similar detail
    # Story 4: The Superhero Siblings
    story.append(Paragraph("Story 4: The Superhero Siblings 🦸‍♂️", title_style))
    story.append(Paragraph("Magical capes give the brothers superpowers!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story4_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("Once upon a time, Jathin and Kethan were playing in their bedroom when they discovered something extraordinary. While tidying up their toys, Kethan opened their old wooden wardrobe that had been in the family for generations.", story_text_style))
    story.append(Paragraph("\"Whoa! Look at this!\" Kethan exclaimed. Instead of their usual clothes, the wardrobe was filled with two magnificent capes. One was bright red with a lightning bolt symbol, and the other was deep blue with a star emblem. The capes glowed softly, as if they were alive.", story_text_style))
    story.append(Paragraph("Jathin touched the red cape. Instantly, he felt stronger and braver. Kethan tried the blue one and felt faster and smarter. \"We're superheroes!\" they shouted together.", story_text_style))
    story.append(Paragraph("The capes gave them special abilities. Jathin's red cape made him incredibly strong and able to jump very high. Kethan's blue cape made him super fast and able to solve problems quickly.", story_text_style))
    story.append(Paragraph("They spent the afternoon practicing their powers in the backyard. Jathin lifted heavy rocks and jumped over the fence. Kethan ran around the house three times in seconds and figured out how to fix their broken swing.", story_text_style))
    story.append(Paragraph("Their little dog, Spot, watched with wagging tail, barking excitedly.", story_text_style))
    story.append(Paragraph("Just then, they heard cries for help from the town square. An elderly neighbor, Mrs. Jenkins, was struggling with her heavy grocery bags. One bag tore, and groceries started rolling everywhere.", story_text_style))
    story.append(Paragraph("\"Super Siblings to the rescue!\" Jathin shouted. With his super strength, he caught flying apples and oranges in mid-air. Kethan, using his super speed, gathered the rolling items before they went too far.", story_text_style))
    story.append(Paragraph("Mrs. Jenkins was amazed. \"Thank you, young heroes! How did you do that?\"", story_text_style))
    story.append(Paragraph("\"We're just helping out,\" Kethan said with a wink.", story_text_style))
    story.append(Paragraph("Their biggest challenge came when they heard a child's cries from the park. Little Sarah had climbed too high in an old oak tree and was too scared to come down.", story_text_style))
    story.append(Paragraph("\"Don't worry, Sarah!\" Jathin called. Using his super strength, he climbed the tree quickly and safely brought her down. Kethan comforted her with kind words and made sure she was okay.", story_text_style))
    story.append(Paragraph("Sarah's parents were so grateful. \"You saved our daughter! You're real heroes!\"", story_text_style))
    story.append(Paragraph("As the sun set, the brothers returned home, tired but happy. They hung up their capes in the wardrobe, knowing they could use them again whenever someone needed help.", story_text_style))

    story.append(Paragraph("⭐ Remember, brave ones: You don't need capes to be a superhero. Being kind, helpful, and brave makes you a hero every day! ⭐", moral_style))
    story.append(PageBreak())

    # Story 5: The Time-Traveling Clock
    story.append(Paragraph("Story 5: The Time-Traveling Clock ⏰", title_style))
    story.append(Paragraph("A magical clock takes them through time!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story5_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("Once upon a time, while cleaning out their grandpa's old attic, Jathin and Kethan found a peculiar clock. It wasn't an ordinary timepiece - this clock was made of shimmering crystal with golden gears that seemed to move on their own.", story_text_style))
    story.append(Paragraph("\"Look at this!\" Jathin said, carefully picking it up. The clock had twelve numbers, but instead of 1-12, they were strange symbols. The hands glowed softly, and when they touched it, they felt a tingling sensation.", story_text_style))
    story.append(Paragraph("Suddenly, the clock chimed, and a gentle voice spoke: \"Time travelers, state your destination.\"", story_text_style))
    story.append(Paragraph("The boys looked at each other in amazement. \"Can we really travel through time?\" Kethan asked.", story_text_style))
    story.append(Paragraph("Curious, they said, \"Take us to see dinosaurs!\" In a swirl of colors and sounds, they were transported to a time long ago, when dinosaurs ruled the Earth.", story_text_style))
    story.append(Paragraph("They found themselves in a lush valley with giant ferns and distant volcanoes. A friendly stegosaurus with plates on its back was eating leaves nearby. \"Hello!\" Kethan whispered. The dinosaur looked at them curiously but didn't seem afraid.", story_text_style))
    story.append(Paragraph("They learned that not all dinosaurs were scary - many were gentle giants who just wanted to eat and play.", story_text_style))
    story.append(Paragraph("Next, they asked to see the future. Whoosh! They arrived in a amazing city where buildings touched the clouds and cars flew through the air like birds.", story_text_style))
    story.append(Paragraph("People wore clothes that changed colors, and friendly robots helped with everyday tasks. \"This is incredible!\" Jathin exclaimed. They saw floating gardens where fruits grew without soil, and schools where children learned by playing games.", story_text_style))
    story.append(Paragraph("A kind robot guide explained how people in the future cared for the environment and worked together to solve problems.", story_text_style))
    story.append(Paragraph("When they returned home, the clock taught them an important lesson: \"Time is precious. Learn from the past, live in the present, and dream of the future.\"", story_text_style))
    story.append(Paragraph("Jathin and Kethan promised to make every moment count. They started a \"Time Treasure\" journal where they wrote down special moments and things they were grateful for.", story_text_style))
    story.append(Paragraph("The clock became their special friend, reminding them that adventure and learning could happen anytime, anywhere.", story_text_style))

    story.append(Paragraph("⏳ Remember, young time travelers: Every moment is a treasure. Make the most of your time by learning, loving, and living fully! ⏳", moral_style))
    story.append(PageBreak())

    # Story 6: The Underwater Kingdom
    story.append(Paragraph("Story 6: The Underwater Kingdom 🐠", title_style))
    story.append(Paragraph("A magical shell lets them explore the ocean depths!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story6_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("One sunny afternoon, Jathin and Kethan went to the beach to play. While building the biggest sandcastle ever, Kethan dug up something extraordinary - a beautiful seashell that glowed with all the colors of the rainbow.", story_text_style))
    story.append(Paragraph("\"Look what I found!\" Kethan shouted. As Jathin examined it, they noticed a perfect pearl inside that seemed to pulse with light.", story_text_style))
    story.append(Paragraph("When they held the shell to their ears, instead of the usual ocean sounds, they heard a clear voice: \"Brave explorers of the sea, hold the pearl and make a wish to visit the deep.\"", story_text_style))
    story.append(Paragraph("Excited, they wished together: \"We wish to explore the underwater world!\"", story_text_style))
    story.append(Paragraph("Suddenly, they felt a tingling sensation. Their legs became fins, gills appeared on their necks, and they could breathe underwater! Holding hands, they dove into the sparkling ocean.", story_text_style))
    story.append(Paragraph("The underwater world was more beautiful than they imagined. Colorful fish swam in schools, coral reefs looked like underwater gardens, and sunlight danced through the water in golden beams.", story_text_style))
    story.append(Paragraph("A friendly dolphin named Finley greeted them. \"Welcome to the Sea Kingdom! I'm Finley, your guide.\"", story_text_style))
    story.append(Paragraph("Finley led them to the Coral Palace, home of Princess Marina, a beautiful mermaid with flowing blue hair and a crown of seashells.", story_text_style))
    story.append(Paragraph("\"Welcome, surface dwellers,\" Princess Marina said warmly. \"What brings you to our watery home?\"", story_text_style))
    story.append(Paragraph("\"We're explorers!\" Jathin replied. \"We want to learn about the ocean.\"", story_text_style))
    story.append(Paragraph("The princess introduced them to her friends: Ollie the Octopus, who could change colors; Shelly the Turtle, who was very wise; and Sammy the Seahorse, who could swim backwards.", story_text_style))
    story.append(Paragraph("The princess took them on a grand tour. They explored a sunken pirate ship filled with treasures, swam through underwater caves glowing with bioluminescent algae, and played hide-and-seek with schools of fish.", story_text_style))
    story.append(Paragraph("They learned important lessons: how to protect the ocean from pollution, why coral reefs are important, and how all sea creatures work together.", story_text_style))
    story.append(Paragraph("When it was time to return, Princess Marina gave them each a small pearl. \"Remember,\" she said, \"the ocean is our shared home. Take care of it.\"", story_text_style))
    story.append(Paragraph("Back on the beach, the boys returned to normal, but their hearts were forever changed. They became ocean protectors, picking up litter and telling others about the wonders beneath the waves.", story_text_style))

    story.append(Paragraph("🌊 Remember, ocean explorers: The sea is full of amazing creatures and treasures. Help keep our oceans clean and beautiful for everyone! 🌊", moral_style))
    story.append(PageBreak())

    # Story 7: The Cloud Castle
    story.append(Paragraph("Story 7: The Cloud Castle ☁️", title_style))
    story.append(Paragraph("A rainbow ladder leads to a castle in the clouds!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story7_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("Once upon a time, after a big rainstorm, Jathin and Kethan saw the most amazing rainbow they had ever seen. But this wasn't an ordinary rainbow - it seemed to form a ladder reaching up into the sky!", story_text_style))
    story.append(Paragraph("\"Look!\" Kethan pointed. \"It's like a ladder to the clouds!\"", story_text_style))
    story.append(Paragraph("Curious, they climbed the rainbow ladder. Each step was soft and bouncy, like walking on cotton candy. Higher and higher they went, until they reached a fluffy white cloud.", story_text_style))
    story.append(Paragraph("At the top, they found themselves in front of a magnificent castle made entirely of clouds, with towers of whipped cream and walls of mist.", story_text_style))
    story.append(Paragraph("The castle door opened by itself, and they were greeted by the Cloud King, a wise figure made of swirling mist with a crown of tiny lightning bolts.", story_text_style))
    story.append(Paragraph("\"Welcome, earth visitors!\" the Cloud King boomed gently. \"I am Nimbus, ruler of the Sky Kingdom.\"", story_text_style))
    story.append(Paragraph("He introduced them to his cloud subjects: Fluffy the Cloud Bunny, who hopped on soft clouds; Sparkle the Cloud Bird, who sang songs that made rainbows; and Misty the Cloud Fairy, who painted pictures with morning dew.", story_text_style))
    story.append(Paragraph("Nimbus took them to the Weather Workshop, where clouds created all kinds of weather. \"We make rain to water the flowers, sunshine to help plants grow, and wind to carry seeds,\" he explained.", story_text_style))
    story.append(Paragraph("The boys helped mix a batch of gentle spring rain. Jathin stirred sunshine into the mix, while Kethan added just the right amount of wind. The result was perfect weather for a picnic!", story_text_style))
    story.append(Paragraph("They learned that every type of weather had a purpose and that balance was important.", story_text_style))
    story.append(Paragraph("For their grand adventure, Nimbus gave them cloud chariots pulled by magical cloud horses. They soared through the sky, visiting fluffy cloud islands and racing with the wind.", story_text_style))
    story.append(Paragraph("They saw how clouds changed shapes, learned about different types of clouds, and discovered that the sky was full of wonders.", story_text_style))
    story.append(Paragraph("As the sun began to set, painting the sky in beautiful colors, it was time to return home. \"Remember,\" Nimbus said, \"the sky watches over you. Look up and dream big!\"", story_text_style))
    story.append(Paragraph("Back on the ground, Jathin and Kethan often gazed at the clouds, seeing shapes and remembering their sky adventure. They knew that imagination could take them anywhere.", story_text_style))

    story.append(Paragraph("☁️ Remember, sky dreamers: Look up at the clouds and let your imagination soar. The world is full of wonders waiting to be discovered! ☁️", moral_style))
    story.append(PageBreak())

    # Story 8: The Animal Orchestra
    story.append(Paragraph("Story 8: The Animal Orchestra 🎵", title_style))
    story.append(Paragraph("Animals form a musical orchestra!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story8_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("One beautiful spring morning, Jathin and Kethan were walking through Sunny Meadow when they heard the most wonderful music. It wasn't just any music - it was a full orchestra playing a cheerful symphony!", story_text_style))
    story.append(Paragraph("Following the sounds, they discovered a group of animals performing together. There was Leo the Lion playing drums on a hollow log, Bella the Bird playing flute with her beak, Freddy the Frog playing violin on a blade of grass, and many others.", story_text_style))
    story.append(Paragraph("Standing on a tree stump conducting was Ollie the Wise Owl. \"Welcome to the Animal Orchestra!\" he hooted.", story_text_style))
    story.append(Paragraph("The animals welcomed the boys warmly. \"We play music to celebrate nature's beauty,\" explained Ollie. \"Each animal brings their own special sound.\"", story_text_style))
    story.append(Paragraph("They met the talented musicians: Cricket Charlie played tiny cymbals that went \"ting-ting-ting\", Beaver Benny played a xylophone made from smooth river stones, Elephant Ellie played a deep tuba made from a giant leaf, Monkey Max played fast rhythms on coconut shells.", story_text_style))
    story.append(Paragraph("Jathin and Kethan were amazed at how each animal used their natural abilities to create music.", story_text_style))
    story.append(Paragraph("\"Would you like to join our orchestra?\" Ollie asked. The boys were thrilled!", story_text_style))
    story.append(Paragraph("Jathin learned to play the drums from Leo, discovering that rhythm was like a heartbeat. Kethan learned the flute from Bella, finding that music could express feelings like joy and peace.", story_text_style))
    story.append(Paragraph("They practiced every day. At first, their notes were wobbly, but with patience and practice, they improved. The animals taught them that making music was about listening to each other and playing together.", story_text_style))
    story.append(Paragraph("Finally, it was time for the Grand Meadow Concert. All the animals and the boys performed together under the setting sun.", story_text_style))
    story.append(Paragraph("Jathin played a powerful drum solo that made the ground shake gently. Kethan played a beautiful flute melody that soared like a bird. Together, they created a symphony that celebrated friendship, nature, and harmony.", story_text_style))
    story.append(Paragraph("The forest audience cheered with hoots, barks, and claps. Even the trees seemed to sway in rhythm!", story_text_style))
    story.append(Paragraph("After the concert, Ollie said, \"Music brings us all together. Remember, everyone has a special song inside them.\"", story_text_style))
    story.append(Paragraph("Jathin and Kethan continued to visit the Animal Orchestra, knowing that music could turn ordinary moments into magical ones.", story_text_style))

    story.append(Paragraph("🎼 Remember, young musicians: Everyone has music in their heart. Listen, practice, and create beautiful sounds with your friends! 🎼", moral_style))
    story.append(PageBreak())

    # Story 9: The Wish-Granting Star
    story.append(Paragraph("Story 9: The Wish-Granting Star ⭐", title_style))
    story.append(Paragraph("A shooting star grants wishes!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story9_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("One magical summer night, Jathin and Kethan were stargazing in their backyard. The sky was like a blanket of diamonds, with millions of stars twinkling above.", story_text_style))
    story.append(Paragraph("\"Look!\" Kethan shouted. \"A shooting star!\"", story_text_style))
    story.append(Paragraph("As the bright star streaked across the sky, leaving a trail of sparkling light, they remembered the old saying: \"Star light, star bright, first star I see tonight...\"", story_text_style))
    story.append(Paragraph("They closed their eyes and made their wishes. Jathin wished for endless adventures, while Kethan wished for the ability to help others.", story_text_style))
    story.append(Paragraph("Suddenly, a soft voice echoed in their minds: \"Your wishes are heard. But remember, true magic comes from within.\"", story_text_style))
    story.append(Paragraph("The next morning, they found a beautiful star-shaped pendant on each of their pillows. The pendants glowed softly and felt warm to the touch.", story_text_style))
    story.append(Paragraph("\"What are these?\" Jathin wondered.", story_text_style))
    story.append(Paragraph("As they held the pendants, they felt a surge of energy. The star's voice returned: \"These are Wish Stones. They will help your wishes come true, but you must work for them.\"", story_text_style))
    story.append(Paragraph("The boys learned that the pendants gave them special abilities to make their wishes happen.", story_text_style))
    story.append(Paragraph("Jathin's pendant helped him discover amazing adventures everywhere. He found secret trails in the woods, hidden caves, and mysterious old books that told incredible stories.", story_text_style))
    story.append(Paragraph("Kethan's pendant helped him find ways to help others. He organized a neighborhood cleanup, helped his teacher with class projects, and started a kindness club at school.", story_text_style))
    story.append(Paragraph("They learned that wishes don't just happen - you have to work to make them come true.", story_text_style))
    story.append(Paragraph("One night, as they looked up at the stars again, they realized their greatest wish had already come true - they had each other as brothers and best friends.", story_text_style))
    story.append(Paragraph("The star's voice returned: \"You have learned the most important lesson. The best wishes come from the heart, and the greatest magic is love and friendship.\"", story_text_style))
    story.append(Paragraph("The pendants glowed brighter than ever, reminding them that they had the power to make their own magic every day.", story_text_style))
    story.append(Paragraph("From then on, Jathin and Kethan knew that wishing upon a star was just the beginning. The real magic happened when they worked hard and cared for others.", story_text_style))

    story.append(Paragraph("✨ Remember, wish makers: Stars can guide your dreams, but you have the power to make them come true through hard work and kindness! ✨", moral_style))
    story.append(PageBreak())

    # Story 10: The Garden of Dreams
    story.append(Paragraph("Story 10: The Garden of Dreams 🌸", title_style))
    story.append(Paragraph("A magical garden where dreams bloom like flowers!", subtitle_style))

    for i in range(1, 5):
        try:
            img_path = f"images/story10_illustration{i}.png"
            if os.path.exists(img_path):
                img = Image(img_path, 6*inch, 4.5*inch)
                story.append(img)
        except:
            story.append(Paragraph(f"[Illustration {i}]", story_text_style))

    story.append(Paragraph("Once upon a time, while exploring their neighborhood, Jathin and Kethan discovered an old stone wall covered in ivy and flowers. Behind the wall, they could hear soft whispers and see a gentle glow.", story_text_style))
    story.append(Paragraph("\"Let's see what's back there,\" Kethan said curiously.", story_text_style))
    story.append(Paragraph("Pushing through the ivy, they found a hidden gate with a beautiful dreamcatcher symbol carved into the stone. As they touched the symbol, the gate swung open, revealing the most magical garden they had ever seen.", story_text_style))
    story.append(Paragraph("The Garden of Dreams was filled with flowers that glowed with inner light, trees with leaves that whispered secrets, and paths that seemed to lead to anywhere you imagined.", story_text_style))
    story.append(Paragraph("A gentle figure made of soft light appeared - the Dream Keeper. \"Welcome to my garden,\" she said. \"Here, dreams bloom like flowers. What dreams do you wish to grow?\"", story_text_style))
    story.append(Paragraph("The boys learned that each flower represented a different dream. Red flowers for brave adventures, blue for peaceful moments, yellow for joyful laughter, and purple for kind deeds.", story_text_style))
    story.append(Paragraph("The Dream Keeper taught them how to plant dream seeds. \"Dreams need care to grow,\" she explained. \"You must water them with belief, shine sunlight of hope on them, and protect them from doubt.\"", story_text_style))
    story.append(Paragraph("Jathin planted a seed of adventure, watching it sprout into a tree with leaves shaped like treasure maps. Kethan planted a seed of kindness, which bloomed into flowers that smiled and waved.", story_text_style))
    story.append(Paragraph("They learned that the most beautiful dreams were those that helped others and brought joy to the world.", story_text_style))
    story.append(Paragraph("As their dreams grew, amazing things happened. Jathin's adventure tree led him on safe explorations, finding beautiful shells and interesting rocks. Kethan's kindness flowers helped him notice ways to help - carrying water for thirsty plants, sharing snacks with hungry birds.", story_text_style))
    story.append(Paragraph("The Dream Keeper smiled. \"You see? Dreams don't just happen. You make them real through your actions every day.\"", story_text_style))
    story.append(Paragraph("The garden taught them that imagination was powerful, but combining it with hard work and kindness made dreams come true.", story_text_style))

    story.append(Paragraph("🌱 Remember, dreamers: Plant your dreams with care, water them with belief, and watch them grow into beautiful realities! 🌱", moral_style))

    # Footer
    story.append(Spacer(1, 30))
    story.append(Paragraph("🎉 The End of Our Magical Adventures! 🎉", title_style))
    story.append(Paragraph("This story book is dedicated to Jathin and Kethan - may your adventures be filled with wonder, your hearts with kindness, and your dreams with magic! ✨📚💫", story_text_style))
    story.append(Paragraph("🌟 Keep dreaming and exploring! 🌟", ParagraphStyle('Center', alignment=TA_CENTER, fontSize=16, textColor=HexColor('#FF6B6B'))))

    # Build the PDF
    doc.build(story)
    print("PDF created successfully: Jathin_Kethan_Story_Book.pdf")

if __name__ == "__main__":
    create_story_book_pdf()
