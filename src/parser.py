import crc

''' GLOBALS '''
KEY = '1001'
FILE = 'text.txt'
MAX_LINES = 100
FILES = []

f = open(FILE,'r')
file_lines = (sum(1 for line in open('text.txt')))

print("Max lines: %d, File lines: %d"% (MAX_LINES, file_lines))

def file_parse():
    file_cnt = 0
    line_cnt = 0
    f = open(FILE,'r')
    while True:
        line_cnt = 0
        new_file_name = 't' + str(file_cnt) + '.txt'
        new_file = open(new_file_name, 'a')
        FILES.append(new_file_name)
        while line_cnt < MAX_LINES:
            data = f.readline()
            if not data:
                return
            ans = crc.encode(data, KEY)
            c = ans[-(len(KEY)-1):]
            new_file.write(data.rstrip() + ' ' + c + '\n')
            line_cnt += 1
        new_file.close()
        file_cnt += 1
    f.close()

def file_bind():
    with open('crc_text.txt', 'w') as outfile:
        for fname in FILES:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

file_parse()
file_bind()
