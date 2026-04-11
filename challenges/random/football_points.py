def football_points(wins, draws, losses):
    return (wins * 3) + (draws) + (losses * 0)


tests = ((3, 4, 2), (5, 0, 2), (0, 0, 1))
for wins, draws, losses in tests:
    print(
        f"with {wins} wins, {draws} draws and {losses} losses, you have: {football_points(wins, draws, losses)} points"
    )
