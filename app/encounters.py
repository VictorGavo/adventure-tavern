import random

desert_encounter = [
    "As you step out of the tavern, you're immediately hit by a wave of heat. The sun beats down relentlessly, casting long shadows across the sand dunes. Suddenly, a pack of gnolls emerges from behind a nearby dune, eager for a fight.",
    "The sandstorm that had been brewing on the horizon has now arrived, and visibility is almost zero. You can barely see a group of giant scorpions until they're almost upon you.",
    "A mirage of an oasis appears in the distance, but as you approach, you realize it's a trap. A group of bandits has set up camp there, waiting for unwary travelers to stumble into their clutches.",
    "The desert at night is eerily silent, save for the occasional hoot of an owl or the hiss of a snake. Suddenly, a group of jackalweres emerge from the darkness, eager for a fight.",
    "You come across a caravan that has been attacked by a group of fire elementals. The air shimmers with heat as the elementals dance and leap, setting everything around them ablaze."
]

forest_encounter = [
    "You step out of the tavern and into the cool, green shade of the forest. The air is thick with the scent of pine and moss, and the only sounds are the chirping of birds and the rustling of leaves. Suddenly, a group of goblins emerges from behind a nearby tree, armed with crude weapons.",
    "The forest is alive with magic, and you can feel the energy coursing through the trees and the earth. But that energy is attracting all manner of dangerous creatures, including a pack of hungry wolves.",
    "The forest floor is littered with fallen leaves and branches, making it hard to move quietly. Suddenly, a group of twig blights emerge from the underbrush, their sharp claws and teeth gleaming in the dappled sunlight.",
    "You come across a clearing where a group of druids is holding a ritual. But before you can decide whether to approach or avoid them, a swarm of giant bees descends on the clearing, buzzing angrily.",
    "The forest is home to all kinds of strange and wondrous creatures, but also to some that are decidedly less friendly. You come across a group of trolls, their skin tough and their claws sharp."
]

jungle_encounter = [
    "As you step out of the tavern and into the jungle, the humidity hits you like a wall. The air is thick with the scent of damp earth and rotting vegetation, and the trees loom tall and dark above you. Suddenly, a group of kobolds emerges from the underbrush, armed with spears.",
    "The jungle is home to all manner of dangerous beasts, including a group of giant snakes that slither out from behind a nearby tree, their tongues flicking hungrily.",
    "You come across a ruined temple, its walls and pillars overgrown with vines and moss. But as you step inside, you realize it's been occupied by a group of yuan-ti, who are none too pleased to see you.",
    "The jungle is alive with the sound of buzzing insects and chirping birds, but it's also home to some creatures that are decidedly less friendly. You come across a group of giant spiders, their eight legs skittering across the jungle floor.",
    "The jungle floor is slick with mud and leaves, making it hard to keep your footing. Suddenly, a group of lizardfolk emerges from the underbrush, their eyes glittering in the dappled sunlight."
]

mountain_encounter = [
    "As you step out of the tavern and into the mountains, the air grows thin and cold. The sun beats down on the rocky terrain, casting deep shadows across the valleys. Suddenly, a group of mountain goats stampede down the slope, knocking you off balance.",
    "The mountains are home to all manner of dangerous creatures, including a group of harpies that swoop down from the sky, their sharp claws and beaks gleaming in the sunlight.",
    "You come across a group of dwarves, hard at work in a mine. But before you can exchange greetings, a group of goblins emerges from the darkness, eager to steal the dwarves' hard-earned treasure.",
    "The mountains are home to all manner of strange and wondrous creatures, including a group of giant eagles that swoop down from their aerie, keen to defend their territory.",
    "The mountain pass you're traversing is narrow and treacherous, with steep cliffs on either side. Suddenly, a group of bandits emerges from the rocks, their blades glinting in the sun."
]

swamp_encounter = [
    "As you step out of the tavern and into the swamp, the air grows thick and sticky. The ground squelches underfoot, and the only sounds are the croaking of frogs and the buzzing of insects. Suddenly, a group of bullywugs emerges from the murky water, their eyes fixed on you.",
    "The swamp is home to all manner of dangerous creatures, including a group of giant mosquitoes that swarm around you, their proboscises thirsting for blood.",
    "You come across a ruined temple, its walls and pillars half-submerged in the murky water. But as you step inside, you realize it's been occupied by a group of lizardfolk, who are none too pleased to see you.",
    "The swamp is home to all manner of strange and wondrous creatures, including a group of giant frogs that leap out of the water, their tongues darting hungrily.",
    "The swamp is treacherous and full of hidden dangers, including a group of trolls that emerge from a nearby cave, their skin slick with swamp water."
]

encounters = {
    1: desert_encounter,
    2: forest_encounter,
    3: jungle_encounter,
    4: mountain_encounter,
    5: swamp_encounter
}

try:
    encounter = random.choices(random.choices(encounters)[0])[0]
except KeyError:
    encounter = "You open the door leading out of the tavern and find yourself in the darkness. A slow drip echoes off the stone floor and a small light is coming through the boards that make up the wooden door in front of you."



''' BRAIN DUMP
Player logs in
makes a character
chooses a character
leaves the tavern
random encounter.exe
    pick a random terrain
    pick a random encounter from that terrain
    
    create an image from the prompt (Dalle 2 API)
    Load the encounter and character options (dnd API)
    start combat
    resolve encounter
get rewards (xp, items, lore)
come back to the tavern

Actions: 
- Combat:       Fight, Flee, Parley, Inventory


TODO
Secrets:
For each encounter, have 1 or 2 secrets that can become revealed if the character has a high enough stat (str, dex, con, wis, int, cha)
'''


