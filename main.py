import os

input_path = './input/'

if __name__ == "__main__":
    if not os.path.isdir(input_path):
        os.makedirs(input_path)

    file_list = os.listdir(input_path)  # 경로 입력

    for i in file_list:
        if i.split(".")[-1] == 'txt':
            with open(input_path + i, 'r', encoding='utf-8') as f:
                txt = f.readlines()
                a = txt[0]
                s = a[0]
                s = s.replace('3', '4')
                d = s + a[1:len(a)-1] + '\n'
                z = list(d)
                x =''.join(d)
                c = []
                c.append(x)

                with open(input_path + i, 'w', encoding='utf-8') as f:
                    f.writelines(c)