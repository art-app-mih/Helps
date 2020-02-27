#!/usr/bin/env python

import os
import tempfile
import argparse
import json
from collections import defaultdict

#Задаём аргументы для командной строки (-- означает, что они необязательны)
parser = argparse.ArgumentParser()
parser.add_argument('--key', help='please, write your key')
parser.add_argument('--value', help='provide an integer (default: None)')
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
args = parser.parse_args()

#Проверяем существование файла
if os.path.exists(storage_path) is False:
    with open(storage_path, 'w', encoding='utf-8') as f:
        ...


if args.key and args.value:
    with open(storage_path, 'r',  encoding='utf-8') as f:
        r = f.read()
        if r == '':
            #Делаем оригинальный ход - записываем все наши значения в список
            D = {}
            D.setdefault(args.key, [])
            D[args.key].append(args.value)
            with open(storage_path, 'w', encoding='utf-8') as f:
                f.write(json.dumps({args.key: D[args.key]}, sort_keys=True))
                f.close()
        #Записываем в файл json формат
        else:
            data = json.loads(r)
            if args.key in data:
                D = {}
                D.setdefault(args.key, [])
                s = ' '.join(map(str, data.get(args.key)))
                D[args.key].append(s)
                D[args.key].append(args.value)
                with open(storage_path, 'w', encoding='utf-8') as f:
                    f.write(json.dumps({args.key: D[args.key]}, sort_keys=True))
                    f.close()
elif args.key:
    with open(storage_path, 'r',  encoding='utf-8') as f:
        #Считываем файл в json формате
        data = json.loads(f.read())
        if args.key:
            ans = ' '.join(map(str, data.get(args.key)))
            print(ans)
else:
    print('Error! Please input your key to get value', end=' ')
    print('or input pair key/value to make new pairs.')
