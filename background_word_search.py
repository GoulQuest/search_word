import json
results_file_path="results.json"
file_path="input.txt"
def get_f_info(file_path):
    with open(file_path) as f:
        info=f.read().split("---") 
    return info

def write_json(results):
    with open(results_file_path, "w") as f:
        json.dump(results,f, indent=4)


def left_diagonal_lines(letters, m, n):
    lines=[]
    counter=0
    flag_t=True
    while flag_t:
        if letters!=[]:
            for y in range(0, len(letters),1):
                x= letters[y]
                if counter <5:
                    print(x[counter])
                counter+=1
            counter-=4
            letters.pop(0)
        
        
        counter=0
