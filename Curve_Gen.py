from math import ceil


def creature_curve(cube_size, colour):
    if colour == ['W']:
        curve_limit = [0,
                       ceil(cube_size * 0.0093),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0204),
                       ceil(cube_size * 0.0093),
                       ceil(cube_size * 0.0093),
                       ceil(cube_size * 0.0056)]
    elif colour == ['U']:
        curve_limit = [0,
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0185),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0204),
                       ceil(cube_size * 0.0056),
                       ceil(cube_size * 0.0056)]
    elif colour == ['B']:
        curve_limit = [0,
                       ceil(cube_size * 0.0056),
                       ceil(cube_size * 0.0148),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0148),
                       ceil(cube_size * 0.0056),
                       ceil(cube_size * 0.0130)]
    elif colour == ['R']:
        curve_limit = [0,
                       ceil(cube_size * 0.0111),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0185),
                       ceil(cube_size * 0.0111),
                       ceil(cube_size * 0.0111),
                       ceil(cube_size * 0.0037)]
    elif colour == ["G"]:
        curve_limit = [0,
                       ceil(cube_size * 0.0130),
                       ceil(cube_size * 0.0185),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0093),
                       ceil(cube_size * 0.0167)]
    elif not colour:
        curve_limit = [ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0056),
                       ceil(cube_size * 0.0093)]
    else:
        curve_limit = [ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0037),
                       ceil(cube_size * 0.0111),
                       ceil(cube_size * 0.0185),
                       ceil(cube_size * 0.0167),
                       ceil(cube_size * 0.0148),
                       ceil(cube_size * 0.0074)]
    return curve_limit
