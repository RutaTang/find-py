# find-py functions:
# 1. find folder or file
# 2. by size
# 3. by durations
#       by create with durations
#       by modified with durations
# 4. by suffix, like .js, .rs, .json

from argparse import ArgumentParser
import sys
import os
import datetime

__author__ = "Ruta"
__version__ = "1.0.0"
__license__ = "MIT"

def _cli_parse(args):
    parser = ArgumentParser(prog="find-py",usage="%(prog)s [options]")
    opt = parser.add_argument
    opt("-v","--version",action="store_true",help="show version number")
    opt("-f","--fpath",help="path to user filters.json")
    opt("-p","--path",default=".",help="where to begin: .") #require: default: .
    opt("-n","--name",help="file or folder name") #require: default: ""
    opt("-r","--regex",action="store_true",help="whether support regex")
    opt("-t","--type",default="all",choices=['folder', 'file','all'],help="find folder or file: all")
    opt("-s","--size",default="all", help= "size(Bytes) of file (only for file): lt,gt,le,ge,eq,ne [num]; ne200")
    args = parser.parse_args()
    print(type(args))
    return args

# BFS
#iter all file and folders
#if all filters return true, then this file or folder is target
def ffFind(args,filters):
    """
    docstring
    """
    if not os.path.exists(args.path):
        raise FileNotFoundError("Can not find {} path to begin".format(args.path))
    if args.type not in ("folder","file","all"):
        raise TypeError("{} is not one of (\"foler\",\"file\")".format(args.type))
    if not filters:
        raise SyntaxError("there is no filter defined")

    #target_sequence
    target_sequence= []

    #folder_queue
    folder_queue = [args.path]

    while folder_queue:
        current_path = folder_queue.pop(0)
        for ffname in os.listdir(current_path):
            full_ffname = os.path.join(current_path,ffname)
            if os.path.isdir(full_ffname):
                folder_queue.append(full_ffname)

            #all filters apply to filter targets
            for i,mfilter in enumerate(filters):
                result = mfilter(args=args,ffname = ffname,full_ffname = full_ffname)
                if not result:
                    break
                if i == len(filters)-1 and result:
                    target_sequence.append(full_ffname)
    return target_sequence


def display(target_sequence):
    for fpath in target_sequence:
        print(fpath)



if __name__ == "__main__":
    args = _cli_parse(sys.argv)
    if args.version:
        print("find-py",__version__)
        exit(0)
    
    #buildin filters 
    import filters
    allfilters = [eval("filters.{}".format(el)) for el in filters.__all__]

    #user filters: -f must have value
    if args.fpath:
        #import user filters from json
        with open(args.fpath,"r") as f:
            import json
            json_text = ""
            for line in f:
                json_text+= line
        json_dict = json.loads(json_text)
        user_filters = json_dict["user_filters"]

        #load modle by name and abspath
        for user_filter in user_filters:
            name = user_filter['name']
            fpath = user_filter['path']
            from importlib.machinery import SourceFileLoader as SFL
            m = SFL(name,fpath).load_module()
            for el in m.__all__:
                expression = "m.{}".format(el)
                allfilters.append(eval(expression))

    # print(allfilters)
    target_sequence = ffFind(args,allfilters)
    display(target_sequence)
    
 
    
