# Moduł obsługujący logikę zadań (questów) w grze

class Quest:
    def __init__(self, quest_id, description, target, reward):
        self.quest_id = quest_id
        self.description = description
        self.target = target  # np. liczba przeciwników do zabicia
        self.progress = 0
        self.completed = False
        self.reward = reward  # nagroda za wykonanie zadania

    def update_progress(self, amount=1):
        """Aktualizuje postęp zadania."""
        if not self.completed:
            self.progress += amount
            if self.progress >= self.target:
                self.completed = True
                return True  # Zadanie wykonane
        return False

    def get_state(self):
        """Zwraca stan zadania jako słownik."""
        return {
            "quest_id": self.quest_id,
            "description": self.description,
            "target": self.target,
            "progress": self.progress,
            "completed": self.completed,
            "reward": self.reward
        }

    def set_state(self, state):
        """Ustawia stan zadania na podstawie wczytanego słownika."""
        self.quest_id = state["quest_id"]
        self.description = state["description"]
        self.target = state["target"]
        self.progress = state["progress"]
        self.completed = state["completed"]
        self.reward = state["reward"]


class QuestManager:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        """Dodaje nowe zadanie."""
        self.quests.append(quest)

    def update_quest(self, quest_id, amount=1):
        """Aktualizuje postęp zadania o zadanym ID."""
        for quest in self.quests:
            if quest.quest_id == quest_id:
                if quest.update_progress(amount):
                    print(f"Zadanie '{quest.description}' wykonane! Nagroda: {quest.reward}")
                    return quest.reward
        return None

    def get_state(self):
        """Zwraca stany wszystkich zadań."""
        return [quest.get_state() for quest in self.quests]

    def set_state(self, quests_state):
        """Przywraca stany zadań z odczytanego słownika."""
        self.quests = []
        for state in quests_state:
            quest = Quest(state["quest_id"], state["description"], state["target"], state["reward"])
            quest.set_state(state)
            self.quests.append(quest)