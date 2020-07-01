from itertools import chain, combinations

VODKA = 1
KALUA = 2
BAILYS = 3
ICE_CREAM = 4
CHOCOLATE_SYRUP = 5
RUM = 6
MALIBU = 7
BLUE_CURACAO = 8
PINAPPLE_JUICE = 9
SPRITE = 10
TEQUILA = 11
RED_BULL = 12
LEMON_JUICE = 14
MARGARITA_MIX = LEMON_JUICE
FIREBALL = 15
PEACH_SCHNAPPS = 16
ICE_TEA = 17
LEMONADE = LEMON_JUICE
STRAWBERRY_VODKA = VODKA
HPNOTIQ = 20
CHAMBORD = 21
CRANBERRY_JUICE = 22
BOURBON = 23
COKE = SPRITE
ORANGE_JUICE = 25
PEPPERMINT_SCHNAPPS = 26
SODA_WATER = SPRITE
LIME_JUICE = 28
GINGER_ALE = SPRITE
MINT = PEPPERMINT_SCHNAPPS
CREAM = ICE_CREAM
STRAWBERRY_SYRUP = 29

ingredient_map = {
    1: 'VODKA', # ['VODKA', 'STRAWBERRY_VODKA', 'STRAWBERRY_SYRUP'],
    2: 'KALUA',
    3: 'BAILYS',
    4: 'ICE_CREAM', # ['ICE_CREAM', 'CREAM'],
    5: 'CHOCOLATE_SYRUP',
    6: 'RUM',
    7: 'MALIBU',
    8: 'BLUE_CURACAO',
    9: 'PINAPPLE_JUICE',
    10: 'SODA_WATER', # ['SPRITE', 'COKE', 'SODA_WATER', 'GINGER_ALE'],
    11: 'TEQUILA',
    12: 'RED_BULL',
    14: 'LEMON_JUICE', #['LEMON_JUICE', 'MARGARITA_MIX', 'LEMONADE'],
    15: 'FIREBALL',
    16: 'PEACH_SCHNAPPS',
    17 : 'ICE_TEA',
    20: 'HPNOTIQ',
    21: 'CHAMBORD',
    22: 'CRANBERRY_JUICE',
    23: 'BOURBON',
    25: 'ORANGE_JUICE',
    26: 'PEPPERMINT_SCHNAPPS', #['PEPPERMINT_SCHNAPPS', 'MINT'],
    28: 'LIME_JUICE',
    29: 'STRAWBERRY_SYRUP',
}

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

eevee = {VODKA, KALUA , BAILYS, ICE_CREAM, CHOCOLATE_SYRUP}
vaporeon = {RUM, MALIBU, BLUE_CURACAO, PINAPPLE_JUICE, SPRITE}
jolteon = {TEQUILA, RED_BULL, MARGARITA_MIX, LEMON_JUICE, SPRITE}
flareon = {FIREBALL, PEACH_SCHNAPPS, ICE_TEA, LEMONADE, STRAWBERRY_SYRUP}
espeon = {STRAWBERRY_VODKA, HPNOTIQ, CHAMBORD, CRANBERRY_JUICE, SPRITE}
umbreon = {BOURBON, COKE, LEMON_JUICE, ORANGE_JUICE}
glaceon = {RUM, BLUE_CURACAO, PEPPERMINT_SCHNAPPS, LEMONADE, SODA_WATER}
leafeon = {TEQUILA, PEACH_SCHNAPPS, LIME_JUICE, GINGER_ALE, MINT}
sylveon = {VODKA, STRAWBERRY_VODKA, BAILYS, ICE_CREAM, CREAM, STRAWBERRY_SYRUP}

evvee_graph = {
    'eevee': eevee,
    'vaporeon': vaporeon,
    'jolteon': jolteon,
    'flareon': flareon,
    'espeon': espeon,
    'umbreon': umbreon,
    'glaceon': glaceon,
    'leafeon': leafeon,
    'sylveon': sylveon,
}
reverse_eevee_graph = {tuple(v): k for k, v in evvee_graph.items()}

def find_eevee(eevee_ingredient_list):
    for eevee_ingredient in eevee_ingredient_list:
        yield reverse_eevee_graph[tuple(eevee_ingredient)]


ingredient_list = list({
    VODKA,
    KALUA,
    BAILYS,
    ICE_CREAM,
    CHOCOLATE_SYRUP,
    RUM,
    MALIBU,
    BLUE_CURACAO,
    PINAPPLE_JUICE,
    SPRITE,
    TEQUILA,
    RED_BULL,
    MARGARITA_MIX,
    LEMON_JUICE,
    FIREBALL,
    PEACH_SCHNAPPS,
    ICE_TEA,
    LEMONADE,
    STRAWBERRY_VODKA,
    HPNOTIQ,
    CHAMBORD,
    CRANBERRY_JUICE,
    BOURBON,
    COKE,
    ORANGE_JUICE,
    PEPPERMINT_SCHNAPPS,
    SODA_WATER,
    LIME_JUICE,
    GINGER_ALE,
    MINT,
    VODKA,
    CREAM,
    STRAWBERRY_SYRUP,
})
def make_ingredient_graph():
    ingredient_graph = {}
    for ingredient in ingredient_list:
        covered_eevees = set()
        for e, v in evvee_graph.items():
            if ingredient in v:
                covered_eevees.add(e)
        ingredient_graph[ingredient] = covered_eevees
    return ingredient_graph
ingredient_graph = make_ingredient_graph()


def heuristic_solve():
    evvee_list = list(evvee_graph.values())
    power_evvee_list = powerset(evvee_list)
    best_eevee_set = set()
    best_ingredient_union = set(ingredient_list)
    for eevee_list_set in power_evvee_list:
        if not eevee_list_set: continue
        # ingredient_interestion = set.intersection(*eevee_list_set)
        ingredient_union = set.union(*eevee_list_set)
        if (len(ingredient_union)) < len(best_ingredient_union) and len(eevee_list_set) > 3:
            best_ingredient_union = ingredient_union
            best_eevee_set = eevee_list_set
    print('Shopping List')
    print([ingredient_map[ing] for ing in best_ingredient_union])
    eevees = find_eevee(best_eevee_set)
    for e in eevees:
        print(e)
        eevee_ings = evvee_graph[e]
        print([ingredient_map[ing] for ing in eevee_ings])

eevee_matrix = [[0]*len(evvee_graph.values()) for _ in range(len(evvee_graph.values()))]
for i, x in enumerate(evvee_graph.values()):
    for j, y in enumerate(evvee_graph.values()):
        dist = len(x.intersection(y))
        eevee_matrix[i][j] = dist



heuristic_solve()