import time as t
import threading
import random

# Commands list:
# Stats
# Start

cmdude = True
life = 0
life_level_1 = 'You have acheived life! You now generate humans every three seconds. Once you reach a certain ammount of humans you will start generating life faster, until you run out of room on your home world.'

# Function to handle the life loop
def life_loop():
    global life
    while True:
        life += random.randint(1, 3) # Randomly generate 1 to 3 humans
        t.sleep(3)

# Function to handle the stats command
def stats():
    global cmd
    global life

    while True:
        if cmd == 'Stats' or cmd == 'stats':
            print(f'Your life count is: {life}.')
            cmd = None
            t.sleep(1)
            
def event():
    global life

    while True:
        event_number = random.randint(1, 60)  # Randomly select an event
        t.sleep(random.randint(50, 400))  # Wait for a random time between events

        if event_number == 1:
            print("A neighboring tribe attacks! You lose 10 humans.")
            life -= 10
        elif event_number == 2:
            print("A deadly disease spreads through the tribe. You lose 15 humans.")
            life -= 15
        elif event_number == 3:
            print("A volcanic eruption destroys part of your settlement. You lose 20 humans.")
            life -= 20
        elif event_number == 4:
            print("A harsh winter causes famine. You lose 12 humans.")
            life -= 12
        elif event_number == 5:
            print("A wild animal attack claims 8 humans.")
            life -= 8
        elif event_number == 6:
            print("A rival tribe steals resources, but no humans are lost.")
        elif event_number == 7:
            print("A new hunting technique is discovered! You gain 10 humans.")
            life += 10
        elif event_number == 8:
            print("A fire breaks out in the settlement. You lose 5 humans.")
            life -= 5
        elif event_number == 9:
            print("A flood washes away part of the settlement. You lose 7 humans.")
            life -= 7
        elif event_number == 10:
            print("A meteorite lands nearby, scaring the tribe but causing no harm.")
        elif event_number == 11:
            print("A neighboring tribe forms an alliance. You gain 5 humans.")
            life += 5
        elif event_number == 12:
            print("A drought reduces food supplies. You lose 6 humans.")
            life -= 6
        elif event_number == 13:
            print("A new tool is invented, improving productivity. You gain 8 humans.")
            life += 8
        elif event_number == 14:
            print("A mysterious illness spreads, but the tribe recovers quickly.")
        elif event_number == 15:
            print("A large herd of animals is found nearby. You gain 12 humans.")
            life += 12
        elif event_number == 16:
            print("A tribal war breaks out. You lose 18 humans.")
            life -= 18
        elif event_number == 17:
            print("A cave collapse traps some members. You lose 9 humans.")
            life -= 9
        elif event_number == 18:
            print("A new leader emerges, uniting the tribe. You gain 15 humans.")
            life += 15
        elif event_number == 19:
            print("A lightning strike causes a fire. You lose 4 humans.")
            life -= 4
        elif event_number == 20:
            print("A neighboring tribe teaches you new survival skills. You gain 7 humans.")
            life += 7
        elif event_number == 21:
            print("A plague devastates the tribe. You lose 25 humans.")
            life -= 25
        elif event_number == 22:
            print("A fertile valley is discovered. You gain 10 humans.")
            life += 10
        elif event_number == 23:
            print("A predator stalks the tribe, but no one is harmed.")
        elif event_number == 24:
            print("A tribal festival boosts morale. You gain 5 humans.")
            life += 5
        elif event_number == 25:
            print("A neighboring tribe raids your settlement. You lose 14 humans.")
            life -= 14
        elif event_number == 26:
            print("A new fishing technique is developed. You gain 8 humans.")
            life += 8
        elif event_number == 27:
            print("A massive earthquake shakes the land. You lose 20 humans.")
            life -= 20
        elif event_number == 28:
            print("A rare fruit is discovered, improving health. You gain 6 humans.")
            life += 6
        elif event_number == 29:
            print("A rival tribe challenges you to a battle. You lose 10 humans.")
            life -= 10
        elif event_number == 30:
            print("A forest fire destroys resources. You lose 8 humans.")
            life -= 8
        elif event_number == 31:
            print("A new cave is found, providing better shelter. You gain 10 humans.")
            life += 10
        elif event_number == 32:
            print("A strange illness wipes out part of the tribe. You lose 12 humans.")
            life -= 12
        elif event_number == 33:
            print("A neighboring tribe shares food. You gain 5 humans.")
            life += 5
        elif event_number == 34:
            print("A massive storm destroys part of the settlement. You lose 9 humans.")
            life -= 9
        elif event_number == 35:
            print("A new hunting ground is discovered. You gain 15 humans.")
            life += 15
        elif event_number == 36:
            print("A predator attacks during the night. You lose 6 humans.")
            life -= 6
        elif event_number == 37:
            print("A tribal conflict is resolved peacefully. You gain 8 humans.")
            life += 8
        elif event_number == 38:
            print("A rare mineral is found, boosting morale. You gain 3 humans.")
            life += 3
        elif event_number == 39:
            print("A neighboring tribe spreads disease. You lose 10 humans.")
            life -= 10
        elif event_number == 40:
            print("A new fire-starting technique is discovered. You gain 7 humans.")
            life += 7
        elif event_number == 41:
            print("A predator is hunted successfully. You gain 5 humans.")
            life += 5
        elif event_number == 42:
            print("A neighboring tribe offers a trade. You gain 4 humans.")
            life += 4
        elif event_number == 43:
            print("A famine strikes the land. You lose 15 humans.")
            life -= 15
        elif event_number == 44:
            print("A new type of weapon is invented. You gain 10 humans.")
            life += 10
        elif event_number == 45:
            print("A neighboring tribe attacks during the night. You lose 12 humans.")
            life -= 12
        elif event_number == 46:
            print("A large migration brings new members. You gain 20 humans.")
            life += 20
        elif event_number == 47:
            print("A predator stalks the tribe, causing fear but no harm.")
        elif event_number == 48:
            print("A new source of water is discovered. You gain 8 humans.")
            life += 8
        elif event_number == 49:
            print("A neighboring tribe teaches you farming. You gain 15 humans.")
            life += 15
        elif event_number == 50:
            print("A massive landslide destroys part of the settlement. You lose 18 humans.")
            life -= 18
        elif event_number == 51:
            print("A new type of clothing is invented, improving survival. You gain 6 humans.")
            life += 6
        elif event_number == 52:
            print("A predator attacks during a hunt. You lose 7 humans.")
            life -= 7
        elif event_number == 53:
            print("A neighboring tribe forms an alliance. You gain 10 humans.")
            life += 10
        elif event_number == 54:
            print("A drought causes food shortages. You lose 8 humans.")
            life -= 8
        elif event_number == 55:
            print("A new type of shelter is built. You gain 12 humans.")
            life += 12
        elif event_number == 56:
            print("A tribal war breaks out. You lose 20 humans.")
            life -= 20
        elif event_number == 57:
            print("A rare animal is hunted successfully. You gain 10 humans.")
            life += 10
        elif event_number == 58:
            print("A neighboring tribe spreads rumors, causing unrest.")
        elif event_number == 59:
            print("A new type of trap is invented, improving hunting. You gain 8 humans.")
            life += 8
        elif event_number == 60:
            print("A massive earthquake destroys part of the settlement. You lose 25 humans.")
            life -= 25

print('Hello. Welcome to Life.')
while cmdude == True:
    cmd = input('What command would you like to run?\n')
    cmdad = False
    cmd_stats_thread = threading.Thread(target=stats, daemon=True)
    cmd_stats_thread.start()
    if cmd is not None:
        if cmd == 'Stats' or cmd == 'stats':
            print(f'Your life count is: {life}.')
            t.sleep(5)
        elif cmd == 'Start' or cmd == 'start':
            print('Starting simulation...')
            t.sleep(2)
            print('Simulation started.')
            print(life_level_1)
            # Start the life loop in a separate thread
            life_thread = threading.Thread(target=life_loop, daemon=True)
            life_thread.start()
            # Start the event loop in a separate thread
            event_thread = threading.Thread(target=event, daemon=True)
            event_thread.start()
            cmdad = True
        while cmdad == True:
            cmd = input('What command would you like to run?\n')