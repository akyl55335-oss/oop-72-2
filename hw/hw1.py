import keyword

PASS_MARK = 5

scores = {}

for kw in keyword.kwlist:
    while True:
        try:
            answer = int(input(f'Оцените {kw} от 1-10: '))
        except ValueError:
            print('  Ошибка: нужно целое число от 1 до 10.')
            continue
        if not 1 <= answer <= 10:
            print('  Ошибка: оценка должна быть от 1 до 10.')
            continue
        break
    scores[kw] = answer

total = len(scores)

passed = sum(1 for mark in scores.values() if mark >= PASS_MARK)
not_passed = total - passed
passed_percent = passed / total * 100 if total else 0.0
not_passed_percent = not_passed / total * 100 if total else 0.0

excellent = [kw for kw in keyword.kwlist if scores[kw] >= 9]

print()
print('=' * 55)
print(f'1) Всего слов: {total}')
print(f'2) Пройдено: {passed} ({passed_percent:.1f}%), '
      f'не пройдено: {not_passed} ({not_passed_percent:.1f}%)')
print('3) Слова с оценкой >= 9:')
if excellent:
    for kw in excellent:
        print(f'   {kw} — {scores[kw]}')
else:
    print('   таких слов нет')