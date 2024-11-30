def findSearchSpace(category, subcategory, subsubcategory, kannada_medium, rural_reservation):
    search_space = []

    # General Merit category
    if category == 'General Merit':
        if kannada_medium == 'Yes':
            search_space.append('GMK')  
        if rural_reservation == 'Yes':
            search_space.append('GMR')  
        search_space.append('GMG') 

    # OBC category handling
    elif category == 'OBC':
        # Category 1
        if subcategory == '1':
            if kannada_medium == 'Yes':
                search_space.append('1K')
            if rural_reservation == 'Yes':
                search_space.append('1R')
            search_space.append('1G')
        # Category 2
        elif subcategory == '2':
            if subsubcategory == 'A':
                if kannada_medium == 'Yes':
                    search_space.append('2AK')
                if rural_reservation == 'Yes':
                    search_space.append('2AR')
                search_space.append('2AG')
            elif subsubcategory == 'B':
                if kannada_medium == 'Yes':
                    search_space.append('2BK')
                if rural_reservation == 'Yes':
                    search_space.append('2BR')
                search_space.append('2BG')
        # Category 3
        elif subcategory == '3':
            if subsubcategory == 'A':
                if kannada_medium == 'Yes':
                    search_space.append('3AK')
                if rural_reservation == 'Yes':
                    search_space.append('3AR')
                search_space.append('3AG')
            elif subsubcategory == 'B':
                if kannada_medium == 'Yes':
                    search_space.append('3BK')
                if rural_reservation == 'Yes':
                    search_space.append('3BR')
                search_space.append('3BG')

    # SC category handling
    elif category == 'SC':
        if kannada_medium == 'Yes':
            search_space.append('SCK')  # Kannada Medium
        if rural_reservation == 'Yes':
            search_space.append('SCR')  # Rural Reservation
        search_space.append('SCG')  # General SC

    # ST category handling
    elif category == 'ST':
        if kannada_medium == 'Yes':
            search_space.append('STK')  # Kannada Medium
        if rural_reservation == 'Yes':
            search_space.append('STR')  # Rural Reservation
        search_space.append('STG')  # General ST

    return search_space
