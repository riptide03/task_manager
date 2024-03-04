import argparse
import sqlite3
import sys

DB_NAME = 'task_manager'
DESCRIPTION = 'example description'
IN_DEBUG_MODE = False

def runQuery(outfilename: str, infile: str):
    query = infile.read()

    if IN_DEBUG_MODE:
        print(query)
        return
    
    connection = sqlite3.connect(f'./{outfilename}')
    cursor = connection.cursor()
    
    try:
        cursor.execute(query)
        connection.commit()
    except:
        print("invalid query")
        
    connection.close()


def main():
    parser = argparse.ArgumentParser(
        prog=DB_NAME,
        description=DESCRIPTION
    )

    parser.add_argument('-o', '--output_file')
    parser.add_argument('-f', '--input_file')

    args = parser.parse_args()

    if args.output_file is None:
        outfilename = f'./{DB_NAME}.db'

    if args.input_file is None:
        infile = sys.stdin
    else:
        infile = open(args.input_file, 'r')
    
    runQuery(outfilename, infile)
    if infile != sys.stdin:
        infile.close()


if __name__ == '__main__':
    main()
