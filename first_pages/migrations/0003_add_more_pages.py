# Generated by Django 5.0.2 on 2025-03-14 14:56

from django.db import migrations

def add_more_pages(apps, schema_editor):
    BookPage = apps.get_model('first_pages', 'BookPage')
    
    # The Midnight Detective - Additional Pages
    BookPage.objects.create(
        book_title="The Midnight Detective",
        title="Chapter 1: The Investigation Begins",
        content="""Sarah pushed open the creaking door, her flashlight cutting through the darkness. The mansion's interior was exactly as she remembered from the crime scene photos - grand but neglected. The missing paintings had left ghostly outlines on the walls, pale rectangles where masterpieces once hung.""",
        page_number=2,
        purchase_link="https://example.com/midnight-detective"
    )
    BookPage.objects.create(
        book_title="The Midnight Detective",
        title="Chapter 1: The Clue",
        content="""A sound from upstairs made her freeze. Footsteps. She wasn't alone. The letter had been a trap after all. But as she turned to leave, her flashlight caught something glinting on the floor - a small brass key, engraved with the initials 'J.M.'""",
        page_number=3,
        purchase_link="https://example.com/midnight-detective"
    )
    BookPage.objects.create(
        book_title="The Midnight Detective",
        title="Chapter 1: The Confrontation",
        content="""The footsteps grew closer. Sarah's hand went to her service weapon. 'Show yourself!' she called out. A figure emerged from the shadows - an elderly man in a tattered suit. 'I've been waiting for you, Detective,' he said. 'The paintings are safe, but the truth about what happened here will change everything.'""",
        page_number=4,
        purchase_link="https://example.com/midnight-detective"
    )
    BookPage.objects.create(
        book_title="The Midnight Detective",
        title="Chapter 1: The Truth",
        content="""The old man's story unfolded like a nightmare. The paintings weren't stolen - they were hidden. Each one contained a secret message, a code that could expose a conspiracy reaching back decades. 'The key you found,' he said, 'opens a safe deposit box. Inside, you'll find proof of everything.'""",
        page_number=5,
        purchase_link="https://example.com/midnight-detective"
    )
    
    # The Dragon's Legacy - Additional Pages
    BookPage.objects.create(
        book_title="The Dragon's Legacy",
        title="Chapter 1: The Awakening",
        content="""The egg began to crack. Elara held her breath as a tiny claw emerged, followed by a snout and finally, a pair of brilliant sapphire eyes. The dragonet was no larger than a house cat, but its presence filled the cave with an ancient power.""",
        page_number=2,
        purchase_link="https://example.com/dragon-legacy"
    )
    BookPage.objects.create(
        book_title="The Dragon's Legacy",
        title="Chapter 1: The Bond",
        content="""The dragonet nuzzled against Elara's hand, and she felt a surge of warmth through their connection. 'I'll call you Sapphire,' she whispered. The dragonet purred, sending ripples of blue light through the cave walls.""",
        page_number=3,
        purchase_link="https://example.com/dragon-legacy"
    )
    BookPage.objects.create(
        book_title="The Dragon's Legacy",
        title="Chapter 1: The Warning",
        content="""Suddenly, Sapphire tensed. A distant roar echoed through the caves. 'Others are coming,' Elara realized. The dragon hunters had found them. Sapphire spread her tiny wings, already growing stronger by the minute.""",
        page_number=4,
        purchase_link="https://example.com/dragon-legacy"
    )
    BookPage.objects.create(
        book_title="The Dragon's Legacy",
        title="Chapter 1: The Choice",
        content="""'We have to leave,' Elara said, gathering Sapphire in her arms. The dragonet's eyes glowed with determination. Together, they would face whatever came next. The legacy of the dragons would not end here.""",
        page_number=5,
        purchase_link="https://example.com/dragon-legacy"
    )
    
    # Beyond the Stars - Additional Pages
    BookPage.objects.create(
        book_title="Beyond the Stars",
        title="Chapter 1: The Launch Sequence",
        content="""The quantum drive's hum grew louder. James's hands flew over the control panel, running through the final checks. His crew of five specialists were strapped in, their faces a mix of excitement and apprehension.""",
        page_number=2,
        purchase_link="https://example.com/beyond-stars"
    )
    BookPage.objects.create(
        book_title="Beyond the Stars",
        title="Chapter 1: The Jump",
        content="""'Three... two... one...' The ship lurched forward, and the universe seemed to stretch around them. Colors shifted, stars became streaks of light, and for a moment, James felt as if he were everywhere and nowhere at once.""",
        page_number=3,
        purchase_link="https://example.com/beyond-stars"
    )
    BookPage.objects.create(
        book_title="Beyond the Stars",
        title="Chapter 1: The New World",
        content="""When the ship finally stabilized, they were in orbit around an unknown planet. Its surface was covered in swirling patterns of blue and green, unlike anything they'd seen before. 'We did it,' whispered Dr. Martinez, the ship's xenobiologist.""",
        page_number=4,
        purchase_link="https://example.com/beyond-stars"
    )
    BookPage.objects.create(
        book_title="Beyond the Stars",
        title="Chapter 1: The Discovery",
        content="""The scanners picked up something impossible - signs of intelligent life, but not just any life. The patterns on the planet's surface were moving, shifting, responding to their presence. 'This,' James said, 'changes everything.'""",
        page_number=5,
        purchase_link="https://example.com/beyond-stars"
    )
    
    # Love in Paris - Additional Pages
    BookPage.objects.create(
        book_title="Love in Paris",
        title="Chapter 1: The Artist",
        content="""The stranger's eyes met Marie's, and time seemed to stand still. He smiled, a warm, genuine smile that crinkled the corners of his eyes. 'May I?' he asked in French, gesturing to the empty chair across from her.""",
        page_number=2,
        purchase_link="https://example.com/love-paris"
    )
    BookPage.objects.create(
        book_title="Love in Paris",
        title="Chapter 1: The Sketch",
        content="""'I'm Pierre,' he said, opening his sketchbook. His pencil danced across the page, capturing the morning light and the way it played across Marie's face. 'You have the most extraordinary eyes,' he murmured.""",
        page_number=3,
        purchase_link="https://example.com/love-paris"
    )
    BookPage.objects.create(
        book_title="Love in Paris",
        title="Chapter 1: The Connection",
        content="""They talked for hours, about art, about life, about dreams. Marie learned that Pierre was a struggling artist who painted the city's hidden corners. He showed her his sketchbook, filled with moments of Paris that most people never noticed.""",
        page_number=4,
        purchase_link="https://example.com/love-paris"
    )
    BookPage.objects.create(
        book_title="Love in Paris",
        title="Chapter 1: The Promise",
        content="""As the café began to fill with the lunch crowd, Pierre closed his sketchbook. 'Would you like to see my studio?' he asked. Marie nodded, her heart racing. Sometimes, she thought, the best stories begin with a chance encounter in a Paris café.""",
        page_number=5,
        purchase_link="https://example.com/love-paris"
    )
    
    # The Queen's Secret - Additional Pages
    BookPage.objects.create(
        book_title="The Queen's Secret",
        title="Chapter 1: The Investigation",
        content="""Catherine moved through the court like a shadow, gathering whispers and rumors. The previous lady-in-waiting, Lady Margaret, had been found dead in her chambers, a single red rose clutched in her hand. The official report called it an accident.""",
        page_number=2,
        purchase_link="https://example.com/queen-secret"
    )
    BookPage.objects.create(
        book_title="The Queen's Secret",
        title="Chapter 1: The Discovery",
        content="""In the dead of night, Catherine searched Lady Margaret's chambers. Beneath a loose floorboard, she found a diary. The last entry was dated the day of Margaret's death: 'I know the truth about the Queen's child. Tonight, I will confront her.'""",
        page_number=3,
        purchase_link="https://example.com/queen-secret"
    )
    BookPage.objects.create(
        book_title="The Queen's Secret",
        title="Chapter 1: The Confession",
        content="""The next morning, Catherine was summoned to the Queen's private chambers. Elizabeth's face was pale, her hands trembling. 'You know, don't you?' she asked. 'About my child?' Catherine nodded, the diary heavy in her pocket.""",
        page_number=4,
        purchase_link="https://example.com/queen-secret"
    )
    BookPage.objects.create(
        book_title="The Queen's Secret",
        title="Chapter 1: The Decision",
        content="""'The child lives,' Elizabeth whispered. 'Hidden away, protected. But there are those who would use this knowledge to destroy me, to destroy England.' Catherine understood then - she wasn't just investigating a death. She was protecting a queen and a secret that could change history.""",
        page_number=5,
        purchase_link="https://example.com/queen-secret"
    )

def reverse_add_more_pages(apps, schema_editor):
    BookPage = apps.get_model('first_pages', 'BookPage')
    BookPage.objects.filter(page_number__gt=1).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('first_pages', '0002_populate_demo_books'),
    ]

    operations = [
        migrations.RunPython(add_more_pages, reverse_add_more_pages),
    ]
