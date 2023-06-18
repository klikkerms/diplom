# coding = utf-8
# Copyright 2020 Helga Svala Sigurðardóttir helgas@ru.is
# In this file, unprocessed text is taken and processed
# according to the methods in Punctuator 2 ©.
# It is split and saved to a train, test and validation files
from process_text import process_line
from sklearn.model_selection import train_test_split
import sys

# We process the input text according to the processing script

try:
    if len(sys.argv) > 1:
        float(sys.argv[1])
        print("Указанный текст для обработки отсутствует")
        sys.exit(0)
except ValueError:
    with open(sys.argv[1], "r", encoding='utf-8') as file:
        lines = file.read()
    file_string = lines.split("\n")

if not isinstance(file_string[0], str):
    print("Входной текст должен представлять собой список строк")
    sys.exit(0)

print(f"Number of rows in file: {len(file_string)}")

# Punctuation marks processed
processed_text = [process_line(elem) for elem in file_string]
print("Завершена обработка текста")

# Write it to train, dev, and test files.
if len(sys.argv) > 3:
    train_text, tmp_text = train_test_split(
        processed_text, test_size=float(sys.argv[3]), random_state=42
    )
    dev_text, test_text = train_test_split(
        tmp_text, test_size=float(sys.argv[4]), random_state=42
    )
else:
    train_text, tmp_text = train_test_split(
        processed_text, test_size=0.2, random_state=42
    )
    dev_text, test_text = train_test_split(tmp_text, test_size=0.5, random_state=42)

with open(sys.argv[2] + "/processed_text.train.txt", "w", encoding="utf-8") as train_file:
    for item in train_text:
        train_file.write("%s\n" % item)

with open(sys.argv[2] + "/processed_text.dev.txt", "w", encoding="utf-8") as dev_file:
    for item in dev_text:
        dev_file.write("%s\n" % item)

with open(sys.argv[2] + "/processed_text.test.txt", "w", encoding="utf-8") as test_file:
    for item in test_text:
        test_file.write("%s\n" % item)

print("Завершено сохранение файлов в каталог данных")




# import sys
# import os
# import random
# from process_text import process_line
#
# if len(sys.argv) < 3:
#     print("Usage: python write_to_file.py input_file output_dir [test_size] [val_size]")
#     sys.exit(1)
#
# input_filename = sys.argv[1]
# output_dirname = sys.argv[2]
#
# if not os.path.isfile(input_filename):
#     print("Input file not found")
#     sys.exit(1)
#
# if not os.path.exists(output_dirname):
#     os.makedirs(output_dirname)
#
# test_size = 0.2
# if len(sys.argv) > 3:
#     test_size = float(sys.argv[3])
#
# val_size = 0.5
# if len(sys.argv) > 4:
#     val_size = float(sys.argv[4])
#
#
# def write_to_file(data, filename):
#     with open(filename, 'w', encoding='utf-8') as f:
#         for d in data:
#             f.write(d + '\n')
#
#
# # Читаем все строки из файла
# with open(input_filename, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
# # Обрабатываем каждую строку
# lines = [process_line(line.strip()) for line in lines]
#
# # Разбиваем на тренировочный, тестовый и валидационный датасеты
# num_lines = len(lines)
# test_idx = int(num_lines * test_size)
# val_idx = int(num_lines * (test_size + val_size))
#
# indices = list(range(num_lines))  # Определяем индексы строк
# random.shuffle(indices)  # перемешиваем индексы
#
# train_indices = set(indices[val_idx:])  # Определяем индексы для тренировочного датасета
# test_indices = set(indices[:test_idx])  # Определяем индексы для тестового датасета
# val_indices = set(indices[test_idx:val_idx])  # Определяем индексы для валидационного датасета
#
# train_data = [lines[i] for i in train_indices]
# test_data = [lines[i] for i in test_indices]
# val_data = [lines[i] for i in val_indices]
#
# # Сохраняем данные в файлы
# write_to_file(train_data, os.path.join(output_dirname, 'train.txt'))
# write_to_file(test_data, os.path.join(output_dirname, 'test.txt'))
# write_to_file(val_data, os.path.join(output_dirname, 'val.txt'))
#
# print("Done!")


# import sys
# import os
# import random
# from process_text import process_line
#
# if len(sys.argv) < 3:
#     print("Usage: python write_to_file.py input_file output_dir [test_size] [val_size]")
#     sys.exit(1)
#
# input_filename = sys.argv[1]
# output_dirname = sys.argv[2]
#
# if not os.path.isfile(input_filename):
#     print("Input file not found")
#     sys.exit(1)
#
# if not os.path.exists(output_dirname):
#     os.makedirs(output_dirname)
#
# test_size = 0.2
# if len(sys.argv) > 3:
#     test_size = float(sys.argv[3])
#
# val_size = 0.5
# if len(sys.argv) > 4:
#     val_size = float(sys.argv[4])
#
#
# def write_to_file(data, filename):
#     with open(filename, 'w', encoding='utf-8') as f:
#         for d in data:
#             f.write(d + '\n')
#
#
# # Читаем все строки из файла
# with open(input_filename, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
# # Обрабатываем каждую строку
# lines = [process_line(line.strip()) for line in lines]
#
# # Разбиваем на тренировочный, тестовый и валидационный датасеты
# num_lines = len(lines)
# test_idx = int(num_lines * test_size)
# val_idx = int(num_lines * (test_size + val_size))
#
# indices = list(range(num_lines))  # Определяем индексы строк
# random.shuffle(indices)  # перемешиваем индексы
#
# train_indices = set(indices[val_idx:])  # Определяем индексы для тренировочного датасета
# test_indices = set(indices[:test_idx])  # Определяем индексы для тестового датасета
# val_indices = set(indices[test_idx:val_idx])  # Определяем индексы для валидационного датасета
#
# train_data = [lines[i] for i in train_indices]
# test_data = [lines[i] for i in test_indices]
# val_data = [lines[i] for i in val_indices]
#
# # Обрабатываем каждую строку перед записью в файлы
# train_data = [process_line(line) for line in train_data]
# test_data = [process_line(line) for line in test_data]
# val_data = [process_line(line) for line in val_data]
#
# write_to_file(train_data, os.path.join(output_dirname, 'train.txt'))
# write_to_file(test_data, os.path.join(output_dirname, 'test.txt'))
# write_to_file(val_data, os.path.join(output_dirname, 'val.txt'))
#
# print("Data files generated successfully!")