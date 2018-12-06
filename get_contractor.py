def get_contractor(industry, hourly_rate):
    '''
    Returns info from materials.txt and vendors.txt
    files (hard coded) that meet the industry and
    hourly_rate criterion.
    
    Inputs:
    =======
    industry : string, desired industry (i.e. 'electrical', 'plumbing')
    hourly_rate : float, maximum hourly_rate to be returned
    
    Returns:
    ========
    prints to stdout, row(s) information meeting input criterion
    
    '''     
    import pandas as pd

    # read in (statically) the materials and vendors csv files
    m = pd.read_csv('./materials.txt')
    v = pd.read_csv('./vendors.txt')
    
    # inner join the two files on vendor_id
    mv = pd.merge(m, v, how='inner', left_on='vendor_id', right_on='vendor_id')
    
    # create 'hourly_rate_parsed' column, which is the
    # float representation of 'hourly_rate'
    # NOTE: this assumes hourly_rate ALWAYS has a leading '$'
    mv['hourly_rate_parsed'] = mv['hourly_rate'].apply(lambda x: float(x[1:]))
    
    # could be cleaner, find a way to avoid duplication
    if hourly_rate == None:
        output_df = mv[ (mv['industry'] == industry) ][['name', 'address', 'phone']]
        for row in output_df.values:
            sep = ' '
            print(sep.join(row))
    else:
        output_df = mv[ (mv['industry'] == industry) & (mv['hourly_rate_parsed'] < hourly_rate) ][['name', 'address', 'phone']]
        for row in output_df.values:
            sep = ' '
            print(sep.join(row))


if __name__ == '__main__':
    get_contractor('electrical', None)
