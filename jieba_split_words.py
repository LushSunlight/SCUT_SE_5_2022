import jieba
import os

# TODO: 结合新词构建的词典，进一步加载，
#  input: new_Dicts文件夹下的每个子文件夹（一个子文件夹代表一次迭代，一次迭代以天为单位）下的各个新词典


def loadMyDicts():
    dict_root_path = "./Dicts"
    file_list = os.listdir(dict_root_path)
    # TODO: sougou不是utf-8没有加入
    # TODO: 地名词典太大了，没有加入
    for file in file_list[1:]:
        # print(file)
        if file != "THUOCL_diming.txt":
            abs_path = os.path.join(dict_root_path, file)
            jieba.load_userdict(abs_path)



# 对文件进行分词
def splitFile(inputFile,outputFile):
    fin = open(inputFile,'r',encoding='utf-8')
    fout = open(outputFile,'w',encoding='utf-8')
    for line in fin:
        line = line.strip()
        line = jieba.cut(line) #采用“精确模式进行切词”
        outstr = " ".join(line)
        print(outstr)
        fout.write(outstr + '\n')
    fin.close()
    fout.close()

# TODO: 后面把迭代的过程加入
def mySplitWords():
    text_root_path = "./TXTs/2022年06月01日"
    output_split_words_root_path = "./output_split_words/2022年06月01日"
    if not os.path.exists(output_split_words_root_path):
        os.makedirs(output_split_words_root_path)
    text_file_list = os.listdir(text_root_path)
    for text_file in text_file_list:
        fr = os.path.join(text_root_path, text_file)
        fw = os.path.join(output_split_words_root_path, text_file)
        splitFile(fr,fw)

if __name__ == '__main__':
    loadMyDicts()
    mySplitWords()