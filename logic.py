import information_organizer as inf

def vertical_lines(letters):
    """This funcion with the help of multiple loops will make all the possible vertical lines that the wordsearch has and it gonna put it in a list. 

    Args:
        letters (List): This will contain a matrix with the letters of the wordsearch.

    Returns:
        List: This will contain multiple strings with all the possible vertical lines in the wordsearch.
    """
    lines=[]
    for x in range(0, len (letters[0])):
        y_total=[]

        for y in letters:
            y_total.append(y[x])

        lines.append("".join(y_total))
        y_total.reverse()
        lines.append("".join(y_total))
    return lines
                
def horizontal_lines(letters):
    """This funcion with the help of a loop will make all the possible horizontal lines that the wordsearch has and it gonna put it in a list. 

    Args:
        letters (List): This will contain a matrix with the letters of the wordsearch.

    Returns:
        List: This will contain multiple strings with all the possible horizontal lines in the wordsearch.
    """
    lines=[]
    for y in letters:
        lines.append("".join(y))
        y.reverse()
        lines.append("".join(y))
    return lines

def left_diagonal_lines(letters):
    """This funcion with the help of multiple loops will make all the possible diagonals lines that initiate in the left part of the wordsearch and it gonna put it in a list. 

    Args:
        letters (List): This will contain a matrix with the letters of the wordsearch.

    Returns:
        List: This will contain multiple strings with all the possible diagonal left lines in the wordsearch.
    """
    lines=[]
    counter=0
    flag=True
    flag_2=True
    letters_2=[]
    letters_2+=letters
    
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

        for w in range(0, len(letters_2),1):
            x= letters_2[w]
            if counter <5:
                d_total.append(x[counter])
            counter+=1

        counter-=4

        if 0>=counter or counter>5:
            flag_2=False
        else:
            lines.append("".join(d_total))
            d_total.reverse()
            lines.append("".join(d_total))

    return lines

def right_diagonal_lines(letters):
    """This funcion with the help of a loop will change the orientation of the wordsearch and it gonna call the brother function 
    (left_diagonal_lines) to make all the possible diagonals lines that initiate in the right part of the wordsearch and it gonna 
    put it in a list. 

    Args:
        letters (List): This will contain a matrix with the letters of the wordsearch.

    Returns:
        List: This will contain multiple strings with all the possible diagonal right lines in the wordsearch.
    """
    r_letters=[]
    for lines in letters:
        lines.reverse()
        r_letters.append(lines)
    return left_diagonal_lines(r_letters)

def possible_lines(file_path):
    """This function will combine all the possible whether horizontal, vertical, diagonal left or diagonal right lines in an only list.

    Args:
        file_path (str): Is the name of the file that we want to open.

    Returns:
        List: This will be a list with multiple strings that will contain all the possible lines with the conditions that they will be an adjacent letters.
    """
    letters=inf.get_f_info(file_path)[0]
    total=[]

    h=horizontal_lines(letters)
    v=vertical_lines(letters)
    d_l=left_diagonal_lines(letters)
    d_r=right_diagonal_lines(letters)
    
    total=h+v+d_l+d_r
    return total

def check_results(file_path):
    """This function will see with all the possible lines, if any word that the file given is there or not.

    Args:
        words (list): The words that the code will see if they are in the word search.
        total (list): All the possible lines that the word search contain.

    Returns:
        Dictionary: This will contain the result with a estructure of (Word: True/False) if they are or not in the word search.
    """
    total= possible_lines(file_path)
    words= inf.get_f_info(file_path)[1]
    results= {}
    for word in words:
        flag=True
        for line in total:
            if word.upper() in line.upper():
                results[word.upper()]=True
                flag= False
        if flag:
            results[word.upper()]=False
    return inf.write_json(results)