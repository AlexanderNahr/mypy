import os
import sys
def read_file(path):
    c = ""
    if os.path.isfile(path):
        f = open(path, 'r')
        c = f.read()
        f.close();

    return c

def append_file(path, content):
    f = open(path, 'a')
    f.write(content)
    f.close()

def create_file(path):
    f = open(path, 'w')
    f.close()

def get_base(path):
    b = os.path.splitext(path)[0]
    return b

# abc-cde
def split_string(string, delimiter):
    return string.split(delimiter) # e.g. [abc, cde]



def purcell_parser(inp, out):
    list_of_files = {}
    path = "" # input path
    fp_out = "" # file output path
    if inp == "":
        path = os.path.expanduser('~') + "\\.emacs.d\\lisp"
    else:
        path = inp
        
    if out == "":
        fp_out = os.sep.join([os.getcwd(), "result.org"])
    else:
        fp_out = out
        
    create_file(fp_out)

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if not (filename.startswith('.')):
                if not (filename.startswith('#')):
                    if filename.endswith('.el'):
                        fp_in = os.sep.join([dirpath, filename])
                        c = read_file(fp_in)
                        append_file(fp_out, "* " + get_base(filename) + "\n")
                        append_file(fp_out, "#+BEGIN_SRC emacs-lisp\n")
                        append_file(fp_out, c)
                        append_file(fp_out, "#+END_SRC\n")
                        list_of_files[filename] = os.sep.join([dirpath, filename])
    print("loop finished")



if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    inp = ""
    out = ""
    if len(sys.argv) == 2:
        inp = sys.argv[1]
        out = sys.argv[2]
    purcell_parser(inp, out)
