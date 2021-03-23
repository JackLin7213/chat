#將對話記錄轉換格式
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #sig把奇怪的符號去掉
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None #為了怕沒有person會當掉
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:   #如果person有值的話
            new.append(person + ': '+ line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()