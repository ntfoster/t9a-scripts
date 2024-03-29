import sys

from t9a.pdf import export_titles_to_json

def main(args):
    if len(args) > 0:
        filename = args[1]
        print(filename)
        try:
            print(export_titles_to_json(filename))
            sys.exit(0) # success
        except FileNotFoundError:
            print(f"{filename} does not exist", file=sys.stderr)
        except Exception as err:
            print(err, file=sys.stderr)
    else:
        print("No filename specified",file=sys.stderr)
    sys.exit(1) # only get here if there's an error

if __name__ == '__main__':
    main(sys.argv)
