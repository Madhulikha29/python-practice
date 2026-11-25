word = "automation"
print(word[4:7])
print(word[::-1])
print(word[::2])

alert = "  ERROR: disk full on server-01  "
cleaned = alert.strip().lower()
print(cleaned)
words = cleaned.split()
print(words)

hostname = "server-01"
error_count = 5
print(f'Alert: {hostname} has {error_count} errors')