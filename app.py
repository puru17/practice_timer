import time
import winsound

def main():
    delays =  [2,0.1,2,0.1,2,0.1] #,2.5,6.5,5.5,3.5,1,6] # mins
    freq = 320 # Hz
    duration = 1500 # ms

    # startup
    time.sleep(4)
    winsound.Beep(500, 200)
    time.sleep(1)
    winsound.Beep(500, 200)
    time.sleep(1)
    winsound.Beep(500, 200)
    time.sleep(1)
    winsound.Beep(1300, 1000)


    for i in range(len(delays)):
        time.sleep(delays[i] * 60)
        winsound.Beep(freq, duration)
        print(delays[i], 'mins elapsed')

if __name__ == "__main__":
    main()