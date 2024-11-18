import except_system as excp
import logic as lgc
def main():
    file_path=input("Write the file path of the wordsearch: ")
    print(excp.structure_txt(file_path, lambda: lgc.check_results(file_path)))

if __name__ == "__main__":
    main()