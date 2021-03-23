#將對話記錄轉換格式2

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f: #sig把奇怪的符號去掉
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    s = []
    person = None #當作預設值，為了怕沒有person會當掉
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_pic_count = 0
    viki_pic_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_pic_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_pic_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了', allen_word_count , '傳了', allen_sticker_count, '個貼圖', allen_pic_count, '張圖片')
    print('Viki說了', viki_word_count, '傳了', viki_sticker_count, '個貼圖', viki_pic_count, '張圖片')
     

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()