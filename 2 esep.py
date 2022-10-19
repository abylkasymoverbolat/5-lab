""""Напишите программу, в которой предлагается вводить учащихся различных груп, 
посещающих секции по программированию. Требуется упорядочить список по возрастанию классов. Распечатать список фамилий и классов."""
students = [
        ('abylkasyov Erbolat', 10),
        ('Auezov Abzal', 4),
        ('Kanagatov Murat', 2),
        ('Aitkali Azamat', 1)
    ]
print(sorted(students, key=lambda v: (v[1])))
[('abylkasymov erbolat', 3), ('Auezov Abzal', 4), ('Kanagatov Murat', 2), ('Aitkali Azamat', 1)]
