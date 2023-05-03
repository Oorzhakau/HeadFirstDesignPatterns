import typing


class Event(list):
    def __call__(self, *args, **kwargs) -> None:
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.events: "Event" = Event()

    def fire(self, args: typing.Any) -> None:
        self.events(args)


class GoalScoredInfo:
    def __init__(self, who_scored: str, goals_scored: int) -> None:
        self.who_scored = who_scored
        self.goals_scored = goals_scored


class Player:
    def __init__(self, name: str, game: "Game") -> None:
        self.name = name
        self.game = game
        self.goals_scored: int = 0

    def score(self) -> None:
        self.goals_scored += 1
        args: "GoalScoredInfo" = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)


class Coach:
    def __init__(self, game: "Game") -> None:
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args: typing.Any):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done, {args.who_scored}")


if __name__ == "__main__":
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)

    for _ in range(3):
        player.score()
