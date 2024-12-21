import unittest
from unittest import skipIf, TestSuite, TextTestRunner


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Класс Tournament
class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = list(runners)

    def start(self):
        results = {}
        for runner in self.runners:
            while runner.distance < self.distance:
                runner.run()
            results[runner.distance] = runner.name
        return dict(sorted(results.items()))


# Тестовый класс TournamentTest
class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}  # Словарь для хранения результатов всех тестов

    def setUp(self):
        # Создаём бегунов
        self.runner_usain = Runner("Usain", speed=10)
        self.runner_andrei = Runner("Andrei", speed=9)
        self.runner_nik = Runner("Nik", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_usain_and_nik(self):
        # Забег Усэйна и Ника
        tournament = Tournament(90, self.runner_usain, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )

    def test_andrei_and_nik(self):
        # Забег Андрея и Ника
        tournament = Tournament(90, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_andrei_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )

    def test_usain_andrei_and_nik(self):
        # Забег Усэйна, Андрея и Ника
        tournament = Tournament(90, self.runner_usain, self.runner_andrei, self.runner_nik)
        results = tournament.start()
        TournamentTest.all_results["test_usain_andrei_and_nik"] = results
        self.assertTrue(
            list(results.values())[-1] == "Nik",
            "Nik should be the last runner"
        )


# Обновленные классы TestCase
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest2(unittest.TestCase):
    is_frozen = True

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_and_nik(self):
        tournament = Tournament(90, Runner("Usain", speed=10), Runner("Nik", speed=3))
        results = tournament.start()
        self.assertTrue(list(results.values())[-1] == "Nik")

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_andrei_and_nik(self):
        tournament = Tournament(90, Runner("Andrei", speed=9), Runner("Nik", speed=3))
        results = tournament.start()
        self.assertTrue(list(results.values())[-1] == "Nik")

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_usain_andrei_and_nik(self):
        tournament = Tournament(90, Runner("Usain", speed=10), Runner("Andrei", speed=9), Runner("Nik", speed=3))
        results = tournament.start()
        self.assertTrue(list(results.values())[-1] == "Nik")


# Создание TestSuite
suite = TestSuite()
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest2))

# Запуск TestSuite
if __name__ == "__main__":
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
