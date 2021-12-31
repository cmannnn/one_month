import random

forward = ["Leroy Sane",
           "Ryad Marez",
           "Son Heung-min",
           "Christian Pulisic",
           "Lucas Moura",
           "Harry Kane",
           "Dane Scarlett"]

midfield = ["Oliver Skipp",
            "Tanguy Ndombele",
            "Pierre-Emile Hojbjerg",
            "Dele Alli",
            "Bryan Gil",
            "Giovani Lo Celso",
            "Steven Bergwijn",
            "Jack Clarke"]

defence = ["Eric Dier",
           "Alphonso Davies",
           "Sergio Reguilon",
           "Ben Davies",
           "Davdson Sanchez",
           "Japhet Tanganga",
           "Cristian Romero",
           "Emerson Royal",
           "Joe Rodon"]

goalie = ["Neuer",
          "Lloris",
          "Kepa",
          "Allison",
          "Buffon",
          "Jan Oblak",
          "David de Gea",
          "Pierluigi Gollini"]

random_forward_one = random.choice(forward)
random_forward_two = random.choice(forward)
random_midfield_one = random.choice(midfield)
random_midfield_two = random.choice(midfield)
random_midfield_three = random.choice(midfield)
random_midfield_four = random.choice(midfield)
random_defence_one = random.choice(defence)
random_defence_two = random.choice(defence)
random_defence_three = random.choice(defence)
random_defence_four = random.choice(defence)
random_goalie = random.choice(goalie)

print(f"Here is your starting 11:\n \
\t\t\t{random_forward_one}\t{random_forward_two}\t\n\
{random_midfield_one}\t{random_midfield_two}\t{random_midfield_three}\t{random_midfield_four}\n\
{random_defence_one}\t{random_defence_two}\t{random_defence_three}\t{random_defence_four}\n\
\t\t\t{random_goalie}")























