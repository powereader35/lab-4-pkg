from geometry import shapes



def area_stats(shapes):
    if shapes == ():
        raise ValueError
    
    areas = [shape.area() for shape in shapes]
    return {
    "n": len(areas),
    "total": sum(areas),
    "mean": sum(areas) / len(areas),
    "min": sorted(areas)[0],
    "max": sorted(areas)[-1] }
