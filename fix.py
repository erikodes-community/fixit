def fix_economy(people):
    return { p:(0 if p != "erikodes" else (sum(people.values()) + people["erikodes"])) for p in people }
