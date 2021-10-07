[![Build Status](https://travis-ci.com/ptrstn/lets-plagiarize.svg?branch=master)](https://travis-ci.com/ptrstn/lets-plagiarize)
[![codecov](https://codecov.io/gh/ptrstn/lets-plagiarize/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/lets-plagiarize)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Lets Plagiarize!

## Installation 

```bash
pip install git+https://github.com/ptrstn/deepl-translate
pip install git+https://github.com/ptrstn/lets-plagiarize
```

## Usage

```bash
plagiarize --help
```

```bash
usage: plagiarize [-h] [--version] [--language LANGUAGE] [--by BY [BY ...]] [--silent] text

Conceal your plagiarism by translating your groundbreaking dissertation multiple times

positional arguments:
  text                 Text to be plagiarized

optional arguments:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  --language LANGUAGE  Language of your text. Default: English
  --by BY [BY ...]     Bypass languages. Default: Chinese, German, Russian
  --silent             Do not display bypass texts.
```

### Example 1

```bash
plagiarize "The 1986 Chernobyl accident was the result of a awry reactor design"
```

```
EN -> ZH: 1986年的切尔诺贝利事故是一个错误的反应堆设计造成的。
ZH -> DE: Der Unfall von Tschernobyl im Jahr 1986 war das Ergebnis einer fehlerhaften Reaktorkonstruktion.
DE -> RU: Авария на Чернобыльской АЭС в 1986 году стала результатом неправильной конструкции реактора.
The Chernobyl accident in 1986 was the result of improper reactor design.
```

### Example 2

```bash
plagiarize "Wer reitet so spät durch Nacht und Wind? Es ist der Vater mit seinem Kind" --language DE --by EN DE RU DE NL
```

```
DE -> EN: Who rides so late through night and wind? It is the father with his child
EN -> DE: Wer reitet so spät durch Nacht und Wind? Es ist der Vater mit seinem Kind
DE -> RU: Кто едет так поздно, сквозь ночь и ветер? Это отец со своим ребенком
RU -> DE: Wer fährt so spät noch durch die Nacht und den Wind? Es ist ein Vater mit seinem Kind
DE -> NL: Wie rijdt er nog zo laat door de nacht en de wind? Het is een vader met zijn kind
Wer fährt so spät in der Nacht und bei Wind? Es ist ein Vater mit seinem Kind
```

### Example 3

```bash
plagiarize "I'm gonna make him an offer he can't refuse." --silent
```

```
I'll make him an offer he can't refuse.
```
