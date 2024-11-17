import json
import background_word_search as bws
file_path="input.txt"
results_file_path="results.json"
def get_f_info(file_path):
    with open(file_path) as f:
        info=f.read().split("---") 
    return info

def get_words():
    global file_path
    info=get_f_info(file_path)

    words=info[1].strip().splitlines()
    return words

def get_letters():
    global file_path
    info=get_f_info(file_path)

    new_letters=[]
    letters=info[0].strip().splitlines()
    for row in letters:
        new_letters.append(row.split(" "))
    return new_letters

def vertical_lines(letters, m):
        lines=[]
        for x in range(0, m):
            y_total=[]
            for y in letters:
                y_total.append(y[x])

            lines.append("".join(y_total))
            y_total.reverse()
            lines.append("".join(y_total))
        return lines
                     
def horizontal_lines(letters):
    lines=[]
    for y in letters:
        lines.append("".join(y))
        y.reverse()
        lines.append("".join(y))
    return lines

#[['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10'], ['11', '12', '13', '14', '15'], ['16', '17', '18', '19', '20'], ['21', '22', '23', '24', '25']]

def left_diagonal_lines(letters):
    lines=[]
    counter=0
    flag=True
    flag_2=True
    letters_2=letters
    while flag:
        d_total=[]

        for y in range(0, len(letters),1):
            x= letters[y]

            if counter <5:
                d_total.append(x[counter])

            counter+=1

        if len(letters)==0:
            flag=False

        else:
            lines.append("".join(d_total))
            d_total.reverse()
            lines.append("".join(d_total))
            letters.pop(0)
        counter=0
    
    while flag_2:
        d_total=[]
        print(letters_2)
        for w in range(0, len(letters),1):
            x= letters_2[w]
            
            if counter <5:
                print(x[counter])
                d_total.append(x[counter])

            counter+=1
        lines.append("".join(d_total))
        d_total.reverse()
        lines.append("".join(d_total))
        counter-=4
        
        if 0>=counter:
            flag_2=False
        
    print(lines)

    


left_diagonal_lines(get_letters())


def right_diagonal_lines():
    x=0
    return ["",""]

def possible_lines():
    letters=get_letters()
    m=len(letters[0])
    n=len(letters)
    total=[]

    h=horizontal_lines(letters)
    v=vertical_lines(letters, m)
    d_l=left_diagonal_lines()
    d_r=right_diagonal_lines()
    
    total=h+v+d_l+d_r
    return total

def check_results():
    total= possible_lines()
    words= get_words()
    results= {}
    for word in words:
        flag=True
        for line in total:
            if word in line:
                results[word]=True
                flag= False
        if flag:
            results[word]=False
    return results