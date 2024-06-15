


from basic.Basic import Basic

T_RANGES:dict = {
        "freeze":[0, 1],
        "cold":[2,3],
        "warm":[4,5],
        "hot":[6,7],
        "ardent":[8, 10]
    }

def whats_ranges(ranges_named:dict, 
            number:int)->list[str]:
        range_keys_arr:list = []
        result:bool = False
        for k in ranges_named:
            result = Basic.in_range(
                number,
                ranges_named[k])
            if(result):
                range_keys_arr.append(k)
        return range_keys_arr

def main():
    print("init")
    r = ""
    #---------------------------------------

    
    r = whats_ranges(T_RANGES, 5)
            
    
    #----------------------------------------
    print(r)

main()
