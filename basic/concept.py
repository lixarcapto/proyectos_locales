


from basic.Basic import Basic

def main():
    print("init")
    r = ""
    #---------------------------------------

    tx = "ella corrio tres veces"
    count_is_ready = Basic.counter_call(30)
    while(not count_is_ready.is_end()):
        print(count_is_ready.get_percent())


    #----------------------------------------
    print(r)

main()
