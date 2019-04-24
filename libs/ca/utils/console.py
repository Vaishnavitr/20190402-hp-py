

def read_string(prompt, default=None,suffix=':'):

    if default!=None:
        prompt='{} [{}] {}'.format(prompt,default,suffix)
    str=input(prompt)
    if str=='' and default!=None:
        return default
    else:
        return str

def read_int(prompt,default=None,suffix=':'):
    if default==None:
        s=read_string(prompt)
    else:
        s=read_string(prompt,default,suffix)

    return int(s)

def read_float(prompt,default=None,suffix=':'):
    if default==None:
        s=read_string(prompt)
    else:
        s=read_string(prompt,default,suffix)

    return float(s)

def read_bool(prompt,default=None,suffix=':'):
    if default==None:
        s=read_string(prompt)
    else:
        s=read_string(prompt,default,suffix)

    trues={'y','yes','true','ok','t','fine'}
    s=s.lower()

    return s in trues



