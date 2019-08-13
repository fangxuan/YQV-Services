def paginate_schema(params):
    try:
        page_index = int(params.get('page_index'))
    except:
        page_index = 1
    try:
        page_size = int(params.get('page_size'))
    except:
        page_size = 10
    return page_index, page_size
