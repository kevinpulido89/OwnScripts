def describe(element):
    try:
        return print('Type:',type(element),'|| Size:', element.shape)
    except:
        return print('Type:',type(element),'|| Size:', len(element))
