class Head:
    def __init__(self, eyes, ears, nose, mouth):
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.mouth = mouth

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Hand:
    def __init__(self, fingers):
        self.fingers = fingers

class Leg:
    def __init__(self, foot):
        self.foot = foot

class Feet:
    def __init__(self, toes):
        self.toes = toes

class Human:
    def __init__(self, head, torso):
        self.head = head
        self.torso = torso

eyes = 2
ears = 2
nose = 1
mouth = 1
head = Head(eyes, ears, nose, mouth)

righ_fingers = 5
left_fingers = 5
right_hand = Hand(righ_fingers)
left_hand =  Hand(left_fingers)

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_toes = 5
left_toes = 5
right_feet = Feet(right_toes)
left_feet = Feet(left_toes)

right_leg = Leg(right_feet)
left_leg = Leg(left_feet)

torso = Torso(head, left_arm, right_arm, left_leg, right_leg)

human = Human(head, torso)

print(f'El humano tiene: {human.head.eyes} ojos, {human.head.ears} oidos, {human.head.nose} nariz, {human.head.mouth} boca.')
print(f'El brazo derecho tiene {human.torso.right_arm.hand.fingers} dedos en su mano derecha, y el brazo izquierdo tiene: {human.torso.left_arm.hand.fingers} dedos en su mano izquieda.')
print(f'Tambien tiene en su pierna derecha {human.torso.right_leg.foot.toes} dedos en su pie derecho y la pierna izquierda tiene {human.torso.right_leg.foot.toes} dedos en su pie izquierdo')