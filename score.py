score = int(input())

if score == 100:
  print('Perfect Score')
elif score < 100 and score >= 80:
  print('Almost perfect score')
elif score < 80:
  print('Nice Try')