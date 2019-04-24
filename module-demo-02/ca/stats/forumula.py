
def freq(values):
    result=dict()
        
    for value in values:
        result[value]=result.get(value,0)+1
    
    return result