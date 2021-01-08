#Name filter
def nameFilter(**kwargs):
    args = kwargs["args"]
    ffname = kwargs["ffname"]
    re = args.regex
    target_name = args.name
    if not re:
        return ffname == target_name
    else:
        import re
        pattern = re.compile(target_name)
        match = pattern.match(ffname)
        return match != None