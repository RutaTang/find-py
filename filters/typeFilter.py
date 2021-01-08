
#Type filter
def typeFilter(**kwargs):
    args = kwargs["args"]
    full_ffname = kwargs["full_ffname"]
    fftype = args.type
    if fftype == "all":
        return True
    if fftype == "foler" and os.path.isdir(full_ffname):
        return True
    elif fftype == "file" and os.path.isfile(full_ffname):
        return True
    else:
        return False
