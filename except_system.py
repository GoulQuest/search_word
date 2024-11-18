import information_organizer as inf
def structure_txt(file_path, function):
    """This function will see if the file_path exist, and if it achieve the conditions to be executed with the wordsearch solver.

    Args:
        file_path (str): Is the name of the file that we want to open.
        function (Callable): Is a function that we want to execute.

    Returns:
        str: a message error or a message with a confirmation.
    """
    try:
        if  not file_path.endswith(".txt"):
            raise ValueError ("is not a txt document")
        
        with open(file_path, "r") as f:
            info=str(f.readlines())
            information=inf.get_f_info(file_path)
            
            if "---" not in info:
                raise ValueError ("doesn't have the specific structure: '---' is missing")
            
            if 0<len(information[0])<2:
                raise ValueError ("doesn't have the specific structure: the wordsearch has to have more than 2 lines")
            elif len(information[0])<=0:
                raise ValueError ("doesn't have the specific structure: There are no wordsearch")
            
            len_line= len(information[0][0])

            for lines in information[0]:
                if len (lines)!=len_line:
                    raise ValueError ("doesn't have the specific structure: the wordsearch has some lines with more length than others")
                elif len (lines) <=2:
                    raise ValueError ("doesn't have the specific structure: the wordsearch has to have more than 1 letter in a position")
                
                for letter in lines:
                    if int(len(letter)) < 1:
                        raise ValueError ("doesn't have the specific structure: the wordsearch has more than 1 letter in a position")
                    
            if len(information[1])<1:
                raise ValueError ("doesn't have the specific structure: There has to be at least 1 word")
    
    except FileNotFoundError as e:
        return f"Error: the file '{file_path}' doesn't exist." 
        

    except ValueError as e:
        return f"Error: ValueError the file '{file_path}' {e}." 

    except UnicodeDecodeError as e:
        return f"Error: the file '{file_path}' has unwanted characters."
    
    except Exception as e:
        return f"Error: something went wrong {e}."
    else:
        return function()