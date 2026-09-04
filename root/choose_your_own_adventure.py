user_choice = None

story = """

THE LOST DUNGEON

You wake up inside a cold, dark dungeon with 100 Health.
At the end of the hall, you spot a giant locked gate—your only way out.

Before you lies two hallways.

A : Explore the dark, echoing passage to the left.
OR
B : Explore the quiet, cobblestone passage to the right.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """You creep down the dark passage. Suddenly, a wild Goblin jumps out from behind a pillar!

⚔️ A Goblin attacks you!

A : Fight the Goblin with your rusty sword.
OR
B : Try to dodge past it and run.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """You swing your sword and strike the Goblin down! 

 You defeat the enemy!
💰 You loot 30 Gold from the Goblin.
🗝️ In its pocket, you also find the Dungeon Key!

You now have the key to the exit, but you hear strange scraping noises ahead.

A : Head straight toward the locked gate to escape.
OR
B : Open a nearby side room to see if there is more loot.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """

YOU ESCAPED!

You rush to the main gate, slot the Dungeon Key into the lock, and turn it.
The gate heavy-swings open, revealing daylight!

You break out into the open world with 30 Gold in your pouch!

THE END
"""
            print(story)
        else:
            story = """You step into the side room searching for extra treasure.

🪤 TRAP! You step on a hidden pressure plate, triggering a wall dart!

You take massive damage and fall to the ground.

💀 GAME OVER
"""
            print(story)

    else:
        story = """You turn around and sprint as fast as you can.

You fail to escape! The Goblin strikes you in the back as you flee.

You tumble down a hidden staircase and land in a quiet, secluded alcove. 

❤️ Health remaining: 50

A : Rest in the alcove to heal your wounds.
OR
B : Push through the pain and keep walking.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """You take a rest and recover your strength.

While resting, you notice something shiny in the dirt.
🗝️ It's the Dungeon Key!

You take the key and head straight to the exit gate.

YOU ESCAPED!

You unlock the gate and escape into the wild!

THE END
"""
            print(story)
        else:
            story = """You ignore your injuries and stumble forward into the darkness.

Weakened and lost, you collapse in the underground maze.

💀 GAME OVER
"""
            print(story)

else:
    story = """You walk down the quiet passage. 

It opens up into a large, dusty chamber. In the center sits an old wooden chest.

A : Open the chest.
OR
B : Ignore the chest and inspect the glowing runes on the wall.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """💎 You open the chest! Inside, you find 50 Gold and a shiny Dungeon Key!

As you grab the key, a hidden door behind the chest opens up, revealing a staircase leading up to the gate.

A : Go up the stairs and unlock the exit gate.
OR
B : Go down a secondary tunnel to look for more gold.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """
            
        YOU ESCAPED!
You walk up the stairs, insert your key into the ancient gate, and push it open.

You escape with 50 Gold!

THE END
"""
            print(story)
        else:
            story = """Greed gets the better of you!

You head down the secondary tunnel looking for extra gold, but step straight into a pit trap.

💀 GAME OVER
"""
            print(story)

    else:
        story = """You inspect the glowing runes on the wall. 

Suddenly, a trapdoor opens beneath your feet! You slide down a steep chute.

At the bottom of the chute, a giant Goblin Guard stands over you.

A : Fight the Goblin Guard.
OR
B : Offer the Goblin a bribe.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """Without your full strength, the Goblin Guard overpowers you in battle.

💀 GAME OVER
"""
            print(story)
        else:
            story = """You pull out your empty pockets and offer to help the Goblin with dungeon duties.

The Goblin accepts your offer and hands you a broom.

You spend the rest of your days as the official Dungeon Janitor.

THE END
"""
            print(story)