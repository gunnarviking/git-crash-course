def dm_to_meter(dm):

    return dm / 10

def cm_to_meter(cm):

    return cm / 100



def main():

    # calculate area of square
    cm_calc = cm_to_meter(190)
    print(f"Cm to meters: {cm_calc}")


    dm_calc = dm_to_meter(18)
    print(f"dm to meters: {dm_calc}")

    

if __name__ == '__main__':
    main()