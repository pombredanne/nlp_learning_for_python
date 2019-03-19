import os


_LOG_DIR_2 = 'C:/Users/tsukuda/var/data/recipe/weekcook/procedure_2'
_LOG_DIR_4_2 = 'C:/Users/tsukuda/var/data/recipe/weekcook/procedure_4_2'
_DST_DIR = 'C:/Users/tsukuda/var/data/recipe/weekcook/combined'


def main():
    if os.path.isdir(_DST_DIR) is False:
        os.makedirs(_DST_DIR)
    else:
        pass

    proc_2_files = os.listdir(_LOG_DIR_2)
    proc_4_2_files = os.listdir(_LOG_DIR_4_2)
    print('proc_2_files')
    print(proc_2_files)
    print('proc_4_2_files')
    print(proc_4_2_files)

    print(len(proc_2_files))

    for i in range(1, len(proc_2_files) + 1):
        proc_2_fname = f'weekcook_{i:08}_proc2.txt'
        proc_4_2_fname = f'weekcook_{i:08}_proc4_2.txt'
        output_fname = f'weekcook_{i:08}_combined.tsv'
        proc_2_path = os.path.join(_LOG_DIR_2, proc_2_fname)
        proc_4_2_path = os.path.join(_LOG_DIR_4_2, proc_4_2_fname)
        output_path = os.path.join(_DST_DIR, output_fname)
        with open(proc_2_path, 'r', encoding='utf-8') as r_2:
            lines1 = []
            for l in r_2.readlines():
                if l == '\n': # delete empty line
                    pass
                else:
                    lines1.append(l)
        with open(proc_4_2_path, 'r', encoding='utf-8') as r_4_2:
            lines2 = r_4_2.readlines()
        with open(output_path, 'w', encoding='utf-8') as w:
            print(proc_2_fname.split('_')[1])
            print('lines1')
            print(lines1)
            print('lines2')
            print(lines2)
            word_num = 0
            for proc_idx, (line1, line2) in enumerate(zip(lines1, lines2)):
                proc_idx = f'{proc_idx:03}'
                print(proc_idx)
                line1 = line1.replace('\n', '')
                # line2 = line2.replace('\n', '')
                line1 = line1.split(' ')
                line2 = line2.split(' ')
                print(line1)
                print(line2)
                sentences_idx = 0
                for word_idx, (word1, word2) in enumerate(zip(line1, line2)):
                    print('word1, word2')
                    print(word1, word2)
                    if word1 == '\n' or word2 == '\n':
                        pass
                    else:
                        sentences_num = f'{sentences_idx:02}'
                        word_num = f'{word_idx:03}'
                        proc_sentence_word_num = str(proc_idx) + '-' + str(sentences_num) + '-' + str(word_num)
                        # print(proc_sentence_word_num)
                        # print('word1')
                        # print(word1)
                        # print('word2')
                        # print(word2)
                        join_list = []
                        print(word2)
                        word = word2.split('/')[0]
                        tag = word2.split('/')[1]
                        join_list.append(proc_sentence_word_num)
                        join_list.append(word1)
                        join_list.append(tag)
                        data = '\t'.join(join_list)
                        print('data')
                        print(data)
                        w.write(data)
                        w.write('\n')
                        if word == '。':
                            sentences_idx += 1
                        else:
                            pass
                        


if __name__ == '__main__':
    main()
