def goals_to_win(first_match_score, current_match_score, location):
    g1, g2 = map(int, first_match_score.split(':'))
    g3, g4 = map(int, current_match_score.split(':'))
    if 0 <= g1 <= 5 and 0 <= g2 <= 5 and 0 <= g3 <= 5 and 0 <= g4 <= 5:
        # Проверка
        if (g2 + g4) - (g1 + g3) < 0:
            return 0
        elif (g2 + g4) - (g1 + g3) == 0:
            if location == 1:
                if g3 > g2:
                    return 0
                elif g3 <= g2:
                    return 1
            if location == 2:
                if g1 > g4:
                    return 0
                elif g1 <= g4:
                    return 1
        elif (g2 + g4) - (g1 + g3) > 0:
            if location == 1:
                if (g2 + g4) - (g1 + g3) + g3 > g2:
                    return (g2 + g4) - (g1 + g3)
                elif (g2 + g4) - (g1 + g3) + g3 <= g2:
                    return (g2 + g4) - (g1 + g3) + 1
            if location == 2:
                if g1 > g4:
                    return (g2 + g4) - (g1 + g3)
                elif g1 <= g4:
                    return (g2 + g4) - (g1 + g3) + 1

    else:
        return -1


# Считывание ввода
first_match_score = input().strip()
current_match_score = input().strip()
location = int(input().strip())

# Вызов функции
result = goals_to_win(first_match_score, current_match_score, location)

# Вывод
print(result)

# ok
