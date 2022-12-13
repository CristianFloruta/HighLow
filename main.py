from random import choice
from art import logo, vs
from game_data import data


COUNTER = 0

compare_A = choice(data)

game_on = True
while game_on:
    print(logo)
    against_B = choice(data)

    print(f"Compare A: {compare_A['name']}, {compare_A['description']}, from {compare_A['country']}")

    print(vs)

    print(f"Against B: {against_B['name']}, {against_B['description']}, from {against_B['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if compare_A["follower_count"] > against_B["follower_count"] and answer == "A":
        COUNTER += 1
        print("\n" * 100)

    elif compare_A["follower_count"] < against_B["follower_count"] and answer == "B":
        COUNTER += 1
        compare_A = against_B
        print("\n" * 100)

    else:
        game_on = False

print(f"You answer correctly {COUNTER} times!")





