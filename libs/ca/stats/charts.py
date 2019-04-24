def histogram(freq, **kwargs):
    '''
    Plots a textual horizonatal histogram for given frequency data
    Arguments:
       * freq: 
           A dictionary containing frequency distribution, 
           each key represent item and value corresponding frequency
           {1:4, 2:2, 8:7, 3:1 }
           
        * kwargs: optional configuration parameters
            * design [===] : design of bar
            * showLabel[True] : if to show the frequency value as label
            * align[False]: if frequency label should be aligned. 
            
    >>> histogram({1:4, 2:2, 8:7, 3:1 })
    1 |============ 4
    2 |====== 2
    8 |===================== 7
    3 |=== 1
    
    >>> histogram({1:4, 2:2, 8:7, 3:1 },design=' ::::')
    1 | :::: :::: :::: :::: 4
    2 | :::: :::: 2
    8 | :::: :::: :::: :::: :::: :::: :::: 7
    3 | :::: 1
    
    >>> histogram({1:4, 2:2, 8:7, 3:1 },showLabel=False)
    1 |============ 
    2 |====== 
    8 |===================== 
    3 |===
    
    >>> histogram({1:4, 2:2, 8:7, 3:1 }, align=True, design=' ++++')
    1 | ++++ ++++ ++++ ++++                4
    2 | ++++ ++++                          2
    8 | ++++ ++++ ++++ ++++ ++++ ++++ ++++ 7
    3 | ++++                               1
    
    '''
    design=kwargs.get('design','===')
    showLabel=kwargs.get('showLabel',True)
    align=kwargs.get('align',False) if showLabel else False
    
    if align:
        width=max(freq.values()) * len(design)
    
    for key,value in freq.items():
        bar=design * value
        if align:
            bar=bar.ljust(width)
        label= value if showLabel else ''
        print('{} |{} {}'.format(key,bar,label))