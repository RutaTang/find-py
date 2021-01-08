#Size filter
import os
def sizeFilter(**kwargs):
    args = kwargs["args"]
    full_ffname = kwargs["full_ffname"]
    size = args.size
    if size == "all":
        return True
    ops = ['lt','gt','le','ge','eq','ne']
    ops_e = ['<','>','<=','>=','==','!=']
    op = size[:2]
    num = size[2:]
    if op not in ops:
        raise SyntaxError("{} is not in {}",op,ops)
    if not all(map(str.isdigit,num)):
        raise SyntaxError("{} is not digits",num)
    if os.path.isfile(full_ffname):
        op = ops_e[ops.index(op)]
        ffsize = os.path.getsize(full_ffname)
        expression = "{} {} {}".format(ffsize,op,num)
        return eval(expression)
    else:
        return True