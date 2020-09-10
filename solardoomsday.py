def solution(area):
    '''
    A function which returns a list of areas of the largest squares '''

    if area == 0:
        return
        
    else:
        panel_area = (math.floor(math.sqrt(area)))**2
        new_area = area - panel_area
        panel_areas.append(panel_area)
        solution(new_area)

    return panel_areas