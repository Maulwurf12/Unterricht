#1.1 Unittests
#1.1.1
'''import unittest
from circle import calculateArea, calculateCircumference
from math import pi

class TestCircle(unittest.TestCase):
    # Test für korrekte Berechnungen
    def test_calculate_area(self):
        self.assertAlmostEqual(calculateArea(0), 0)  # Randfall: Null
        self.assertAlmostEqual(calculateArea(1), pi)  # Basisfall: Radius = 1
        self.assertAlmostEqual(calculateArea(2.5), pi * (2.5**2))  # Dezimalzahl
        self.assertAlmostEqual(calculateArea(10), pi * (10**2))  # Größere Zahl
        self.assertAlmostEqual(calculateArea(0.1), pi * (0.1**2))  # Sehr kleiner Wert

    def test_calculate_circumference(self):
        self.assertAlmostEqual(calculateCircumference(0), 0)  # Randfall: Null
        self.assertAlmostEqual(calculateCircumference(1), 2 * pi)  # Basisfall
        self.assertAlmostEqual(calculateCircumference(2.5), 2 * pi * 2.5)  # Dezimalzahl
        self.assertAlmostEqual(calculateCircumference(10), 2 * pi * 10)  # Größerer Wert
        self.assertAlmostEqual(calculateCircumference(0.1), 2 * pi * 0.1)  # Sehr kleiner Wert

    # Testfälle, die fehlschlagen sollten (wenn keine Fehlerbehandlung implementiert ist)
    def test_calculate_area_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculateArea("string")  # String als Input

        with self.assertRaises(ValueError):
            calculateArea(None)  # None als Input

        with self.assertRaises(ValueError):
            calculateArea([])  # Liste als Input

        with self.assertRaises(TypeError):
            calculateArea(-5)  # Negativer Wert

    def test_calculate_circumference_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculateCircumference("text")  # String als Input

        with self.assertRaises(ValueError):
            calculateCircumference(None)  # None als Input

        with self.assertRaises(ValueError):
            calculateCircumference({})  # Dictionary als Input

        with self.assertRaises(TypeError):
            calculateCircumference(-10)  # Negativer Wert

if __name__ == '__main__':
    unittest.main()'''

#1.1.2
#see in circle.py
#1.1.3
'''import unittest
from unittest.mock import patch
from game import main

class TestGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["q"])  # Sofort beenden
    def test_quit_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Bye")

    @patch('builtins.input', side_effect=["1", "q"])  # Pokemon erstellen, dann beenden
    def test_create_pokemon(self, mock_input):
        with patch('builtins.print') as mock_print:
            with patch('game.createNewPokemon', return_value="Pikachu"):
                main()
                mock_print.assert_any_call("Create Pokemon")

    @patch('builtins.input', side_effect=["2", "q"])  # Pokemon angreifen, dann beenden
    def test_attack_pokemon(self, mock_input):
        with patch('builtins.print') as mock_print:
            with patch('game.attackPokemon'):
                main()
                mock_print.assert_any_call("Attack Pokemon")

    @patch('builtins.input', side_effect=["x", "q"])  # Ungültige Eingabe, dann beenden
    def test_invalid_option(self, mock_input):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Invalid option")

    @patch('builtins.input', side_effect=["1", "2", "x", "q"])  # Mehrere Befehle testen
    def test_multiple_inputs(self, mock_input):
        with patch('builtins.print') as mock_print:
            with patch('game.createNewPokemon', return_value="Pikachu"):
                with patch('game.attackPokemon'):
                    main()
                    mock_print.assert_any_call("Create Pokemon")
                    mock_print.assert_any_call("Attack Pokemon")
                    mock_print.assert_any_call("Invalid option")
                    mock_print.assert_any_call("Bye")

if __name__ == '__main__':
    unittest.main()
'''
#1.2.1
'''import random

class Pokemon:
    def __init__(self, name: str, number: int, pokeType: str) -> None:
        self._name: str = name
        self._number: int = number
        self._pokeType: str = pokeType
        self._health: int = 100
        self._maxHealth: int = 100
        self._level: int = 1
        self._levelProgress: int = 0
        self._isAlive: bool = True
        self._strength: int = random.randint(1, 30)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pokemon):
            return NotImplemented
        return self._name == other.getName()

    def __str__(self) -> str:
        return f"Name: {self._name}\nType: {self._pokeType}\nLevel: {self._level}\nHealth: {self._health}"

    def _levelUp(self) -> None:
        self._level += 1
        print(f"Pokemon {self._name} is now level {self._level}!")
        self._maxHealth += 10
        self._health += 10

    def attack(self, opponent: "Pokemon") -> None:
        if not self._isAlive:
            print("Pokemon is dead already!")
        elif not opponent.getIsAlive():
            print("Opponent is dead already!")
        else:
            print(f"{self._name} attacks {opponent.getName()}!")
            attackFactor = self.getAttackFactor(self._pokeType, opponent.getPokeType())
            attackDamage = self._strength * attackFactor
            if attackFactor == 2:
                print("Effective")
            elif attackFactor == 1:
                print("Not very effective")
            elif attackFactor == 4:
                print("Very effective")
            opponent.receiveDamage(attackDamage)
            self.earnXp(attackDamage)

    def receiveDamage(self, damage: int) -> None:
        print(f"{self._name} looses {damage} health!")
        self._health -= damage
        if self._health <= 0:
            self._isAlive = False
            print(f"Pokemon {self._name} is dead!")

    def earnXp(self, xp: int) -> None:
        self._levelProgress += xp
        while self._levelProgress >= 100:
            self._levelProgress -= 100
            self._levelUp()

    def useHealthPotion(self) -> None:
        self._health = self._maxHealth
        print(f"Pokemon {self._name} was healed.")

    def getName(self) -> str:
        return self._name

    def getPokeType(self) -> str:
        return self._pokeType

    def getHealth(self) -> int:
        return self._health

    def getLevel(self) -> int:
        return self._level

    def getIsAlive(self) -> bool:
        return self._isAlive

    def getStrength(self) -> int:
        return self._strength

    @staticmethod
    def getAttackFactor(attackType: str, defendType: str) -> int:
        attackTypes = {
            ("Water", "Fire"): 4,
            ("Fire", "Water"): 1,
            ("Plant", "Water"): 4,
            ("Water", "Plant"): 1,
            ("Fire", "Plant"): 4,
            ("Plant", "Fire"): 1,
        }
        return attackTypes.get((attackType, defendType), 2)
'''
