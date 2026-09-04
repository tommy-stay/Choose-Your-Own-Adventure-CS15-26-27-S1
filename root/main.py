user_choice = None

story = """Mr. Forsyth is teaching a computer science class when an alarm suddenly begins blaring throughout the school.

A voice comes over the intercom:

"Attention. This is not a drill. We are short one astronaut."

The classroom falls silent.

A few seconds later, another announcement follows:

"Correction. We are short one astronaut who knows how to troubleshoot technology."

Every student in the room slowly turns to look at Mr. Forsyth.

Five minutes later, he finds himself being escorted onto a rocket.

The rocket launches successfully and reaches orbit.

Mission Control contacts Mr. Forsyth.

"Astronaut Forsyth, we have two important tasks for you."

"Which would you like to investigate first?"

A : A mysterious signal coming from the Moon.
OR
B : A satellite that has suddenly stopped responding.
"""

print(story)

user_choice = input().lower()

if user_choice == "a":
    story = """Mr. Forsyth lands near the source of the signal.

The signal leads him to a giant metal door built into the surface of the Moon.

The door has a keypad.

A message flashes:

HUMAN DETECTED

Then:

FINALLY

The door slowly opens.

Inside is a brightly lit hallway.

At the far end sits an alien drinking coffee.

A : Introduce yourself.
OR
B : Ask why the alien is on the Moon.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """The alien seems relieved.

"Excellent. You're the first visitor in 2,000 years."

The alien hands Mr. Forsyth a tablet.

"Can you help me? The station's computer isn't working."

After twenty minutes of troubleshooting, Mr. Forsyth discovers the issue.

Someone accidentally unplugged the entire station.

The alien is embarrassed.

A : Fix the station.
OR
B : Leave it unplugged.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The station powers back on.

The alien reveals it is actually an intergalactic amusement park.

Mr. Forsyth receives a lifetime pass and becomes the first human to ride a roller coaster around Saturn.

THE END
"""
            print(story)
        else:
            story = """Mr. Forsyth leaves.

Three days later, the alien accidentally drifts the Moon six kilometers off course.

Earth scientists are extremely confused.

THE END
"""
            print(story)

    else:
        story = """The alien sighs.

"I'm the caretaker."

It gestures toward a giant warehouse.

Inside are millions of boxes.

Each one is labeled:

SPARE MOON

A : Ask why there are spare moons.
OR
B : Open one of the boxes.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The caretaker explains that moons occasionally wear out and must be replaced.

Mr. Forsyth spends the afternoon learning things humanity was never supposed to know.

THE END
"""
            print(story)
        else:
            story = """Inside the box is a tiny moon.

It immediately escapes and begins orbiting Mr. Forsyth's helmet.

Scientists later name it Forsyth Minor.

THE END
"""
            print(story)

else:
    story = """Mr. Forsyth docks with the satellite.

A maintenance hatch is hanging open.

Inside he discovers a raccoon wearing a space suit.

The raccoon is eating wires.

A : Attempt to communicate with the raccoon.
OR
B : Chase the raccoon.
"""
    print(story)

    user_choice = input().lower()

    if user_choice == "a":
        story = """Surprisingly, the raccoon responds.

"Finally. Someone reasonable."

The raccoon explains that it accidentally launched into space while hiding in a supply crate.

A : Help the raccoon return home.
OR
B : Let the raccoon stay.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The raccoon safely returns to Earth and becomes an international celebrity.

Its autobiography becomes a bestseller.

THE END
"""
            print(story)
        else:
            story = """The raccoon remains in orbit and eventually starts the Solar System's first orbital snack company.

THE END
"""
            print(story)

    else:
        story = """The raccoon flees through the satellite.

During the chase, Mr. Forsyth discovers a hidden room.

Inside is a glowing red button.

A sign reads:

ABSOLUTELY DO NOT PRESS

The raccoon immediately points at the button.

A : Press the button.
OR
B : Stop the raccoon from pressing it.
"""
        print(story)

        user_choice = input().lower()

        if user_choice == "a":
            story = """The button activates a giant holographic sign visible from Earth.

It simply says:

HELLO

Humanity spends decades debating who sent the message.

THE END
"""
            print(story)
        else:
            story = """Mr. Forsyth successfully stops the raccoon.

Later inspection reveals the button would have released ten thousand rubber ducks into orbit.

Earth narrowly avoids a very unusual space age.

THE END
"""
            print(story)