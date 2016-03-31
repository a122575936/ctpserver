import os

def convert(src, dst):
    with open(src, 'r') as sf:
        lines = sf.readlines()
        ret = ['Date,Open,High,Low,Close,Volume,OpenInterest\n']
        for line in lines:
            srcarr = line.split(',')
            srcarr[0] = srcarr[0].replace('/', '-')
            srcarr[1] = srcarr[1] + ':00'
            ret.append(','.join(srcarr))

        with open(dst, 'w') as df:
            df.writelines(ret)

def main():
    fl = os.listdir('c:/datas')
    for f in fl:
        convert('c:/datas/' + f, 'c:/btdatas/' + f)

main()
