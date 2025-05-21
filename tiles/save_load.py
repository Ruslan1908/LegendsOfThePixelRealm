import json


def save_game(player, enemy_manager, inventory, door_manager=None, trap_manager=None, quest_manager=None,
              filename="savegame.json"):
    """
    Zapisuje stan gry do pliku JSON.
    Zawiera stan gracza, ekwipunek, przeciwników oraz (opcjonalnie) stan drzwi, pułapek i questów.
    """
    game_state = {
        "player": {
            "position": list(player.rect.topleft),
            "health": player.health,
            "mana": player.mana,
            "experience": player.experience
        },
        "inventory": inventory.items,
        "enemies": [
            {
                "type": enemy.__class__.__name__,
                "position": list(enemy.rect.topleft),
                "health": enemy.health,
                "state": enemy.state
            } for enemy in enemy_manager.enemies
        ]
    }
    if door_manager:
        game_state["doors"] = door_manager.get_state()
    if trap_manager:
        game_state["traps"] = trap_manager.get_state()
    if quest_manager:
        game_state["quests"] = quest_manager.get_state()

    with open(filename, "w") as f:
        json.dump(game_state, f)
    print("Gra została zapisana.")


def load_game(player, enemy_manager, inventory, door_manager=None, trap_manager=None, quest_manager=None,
              filename="savegame.json"):
    """
    Ładuje stan gry z pliku JSON i przywraca dane gracza, ekwipunek, przeciwników
    oraz (opcjonalnie) stan drzwi, pułapek i questów.
    """
    with open(filename, "r") as f:
        game_state = json.load(f)

    player.rect.topleft = tuple(game_state["player"]["position"])
    player.health = game_state["player"]["health"]
    player.mana = game_state["player"]["mana"]
    player.experience = game_state["player"]["experience"]

    inventory.items = game_state["inventory"]

    enemy_manager.enemies.empty()
    from enemy.skeleton import Skeleton
    from enemy.goblin import Goblin
    from enemy.werewolf import Werewolf
    enemy_map = {
        "Skeleton": Skeleton,
        "Goblin": Goblin,
        "Werewolf": Werewolf
    }
    for data in game_state["enemies"]:
        enemy_type = enemy_map.get(data["type"])
        if enemy_type:
            enemy = enemy_type(tuple(data["position"]))
            enemy.health = data["health"]
            enemy.state = data["state"]
            enemy_manager.enemies.add(enemy)

    if door_manager and "doors" in game_state:
        door_manager.set_state(game_state["doors"])
    if trap_manager and "traps" in game_state:
        trap_manager.set_state(game_state["traps"])
    if quest_manager and "quests" in game_state:
        quest_manager.set_state(game_state["quests"])

    print("Gra została załadowana.")