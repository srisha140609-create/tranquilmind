def stress_score(sleep, screen, work, activity):
    score = 0
    if sleep < 6: score += 30
    if screen > 6: score += 25
    if work > 9: score += 25
    if activity < 30: score += 20
    return min(score, 100)
