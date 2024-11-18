import json

def get_f_info(file_path):
    """It would upload the information with a certain file path.

    Args:
        file_path (str): Is the name of the file that we want to open.

    Returns:
        List [str, str]: The first position of the list will be the letters of the wordsearch and the second postion will be the words that we want to search.
    """
    new_letters=[]
    with open(file_path) as f:
        info=f.read().split("---") 

        words=info[1].strip().splitlines()

        letters=info[0].strip().splitlines()
        for row in letters:
            new_letters.append(row.split(" "))

    return [new_letters, words]

def write_json(results):
    """This will create a .json that we wanna use it to upload the information of the results.

    Args:
        results (dict): Will contain the result of the wordsearch.

    Returns:
        str: A messages of confirmation.
    """
    with open("result.json", "w") as f:
        json.dump(results,f, indent=4)
    return "The result.json was created"