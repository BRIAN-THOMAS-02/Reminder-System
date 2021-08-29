import speech_recognition as sr
import playsound
import time
import pyaudio
import pyttsx3
import win10toast
from win10toast import ToastNotifier
import time
from datetime import datetime
from datetime import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("")
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get_audio():
    import speech_recognition as sr
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(" ")
        print("Listening...")
        audio = rObject.listen(source, phrase_time_limit=5)

        try:
            text = rObject.recognize_google(audio, language='en-us')
            print("You said... :", str.capitalize(text))
            print(" ")
            return text

        except:
            print(" ")
            print("Could not understand you Brian, PLease try again !")
            speak("Could not understand you Brian, PLease try again !")
            print(" ")
            return 0


def reminder_seconds():
    global reminder_sec
    import win10toast
    from win10toast import ToastNotifier
    import time
    from datetime import datetime

    print("What should I remind you...?")
    speak("What should I remind you...?")
    reason1 = get_audio()
    now = datetime.now()
    q = [int(i) for i in g.split() if i.isdigit()]
    r = 60
    for r in range(0, r):
        if r in q:
            print("I have set a reminder for ", r, "secs")
            current_sec = (now.second)
            current_min = (now.minute)
            current_hour = (now.hour)
            print("Current Time = ", current_hour, ":", current_min, ":", current_sec)
            reminder_sec = current_sec + r
            if reminder_sec <= 60:
                print("Notify at...", current_hour, ":", current_min, ":", reminder_sec)
                # speak("Notify at " + reminder_sec)
                time.sleep(r - 0.6)
                z = 1
                while z < 5:
                    z = z + 1
                    print("I'm reminding you to " + str(reason1))
                    speak("I'm reminding you to"), speak(str(reason1))
                    toaster = ToastNotifier()
                    toaster.show_toast("Brian " + str.upper(reason1), duration=5)
                    print("Have you done it...?")
                    speak("Have you done it...?")
                    y_n = get_audio()
                    if "no" in str(y_n).lower():
                        print("I'm reminding you again in 10 secs")
                        speak("I'm reminding you again in 10 seconds")
                        fine = get_audio()
                        if ("okay" or "fine" or "yes" in str(fine).lower()):
                            time.sleep(10)
                        if "no" in str(fine).lower():
                            print("In how many seconds should I remind you...?")
                            speak("In how many seconds should I remind you...?")
                            secs_dur = get_audio()
                            dur = int(secs_dur)
                            print("Okay I'm reminding you again in " + dur + "secs")
                            speak("Okay I'm reminding you again in "), speak(secs_dur), speak("seconds")
                            time.sleep(dur)
                        continue
                    if "yes":
                        print("Good")
                        speak("Good")
                    break

            else:
                extra_sec = reminder_sec - 60
                extra_seconds = extra_sec + 0
                print("Notify at...", current_hour, ":", current_min, ":", extra_seconds)
                time.sleep(r - 0.6)
                print("I'm reminding you to " + str(reason1))
                speak("I'm reminding you to"), speak(str(reason1))
                toaster = ToastNotifier()
                toaster.show_toast("Brian" + str.upper(reason1), duration=10)


def reminder_minute():
    global reminder_sec
    import win10toast
    from win10toast import ToastNotifier
    import time
    from datetime import datetime

    print("What should I remind you...?")
    speak("What should I remind you...?")
    reason = get_audio()
    now = datetime.now()
    q1 = [int(i) for i in h.split() if i.isdigit()]
    r1 = 60
    for r1 in range(0, r1):
        if r1 in q1:
            current_sec = (now.second)
            current_min = (now.minute)
            current_hour = (now.hour)
            print("Current time = ", current_hour, ":", current_min, ":", current_sec)
            reminder_min = current_min + r1
            if reminder_min <= 60 and current_sec <= 60:
                print("Reminding at... ", current_hour, ":", reminder_min, ":", current_sec)
                speak("Reminding at "), speak(current_hour), speak(reminder_min)  # current_hour, current_min, current_sec)
                time.sleep(r1 * 60)
                z1 = 1
                while z1 < 5:
                    z1 = z1 + 1
                    print("I'm reminding you to " + str(reason))
                    speak("I'm reminding you to"), speak(str(reason))
                    toaster = ToastNotifier()
                    toaster.show_toast("Brian " + str.upper(reason), duration=5)
                    print("Have you done it...?")
                    speak("Have you done it...?")
                    y_n1 = get_audio()
                    if "no" in str(y_n1).lower():
                        print("I'm reminding you again in 10 minutes")
                        speak("I'm reminding you again in 10 minutes")
                        fine1 = get_audio()
                        if (("okay" or "fine" or "yes") in str(fine1).lower()):
                            print("")
                            #time.sleep(10 * 60)
                        if "no" in str(fine1).lower() or "don't" in str(fine1).lower():
                            print("In how many minutes should I remind you again...?")
                            speak("In how many minutes should I remind you again...?")
                            min_dur = get_audio()
                            dur1 = int(min_dur)
                            print("Okay I'm reminding you again in ", dur1, " minutes")
                            speak("Okay I'm reminding you again in"), speak(min_dur), speak("minutes")
                            time.sleep(dur1 * 60)
                        continue
                    if "doing" in str(y_n1).lower() or "completing" in str(y_n1).lower():
                        print("Good, but do it fast...")
                        speak("Good, but do it fast...")
                        print("I'm still gonna remind you...")
                        speak("I'm still gonna remind you...")
                        should_remind = get_audio()
                        if "fine" in str(should_remind).lower():
                            print("I'm reminding you again in 10 minutes")
                            speak("I'm reminding you again in 10 minutes")
                            #time.sleep(10 * 60)
                            print("I'm reminding you to " + str(reason))
                            speak("I'm reminding you to"), speak(str(reason))
                            toaster = ToastNotifier()
                            toaster.show_toast("Brian " + str.upper(reason), duration=5)
                    if "yes":
                        print("Good")
                        speak("Good")
                    break
            else:
                extra_min = reminder_min - 60
                extra_minutes = extra_min + 0
                extra_sec = current_sec - 60
                extra_seconds = extra_sec + 0
                print("Notify at...", current_hour, ":" + current_min, ":", extra_seconds)
                speak("Notify at: " + current_hour + current_min + current_sec)
                time.sleep(r1 * 60)
                print("I'm reminding you to " + str(reason))
                speak("I'm reminding you to")
                toaster = ToastNotifier()
                toaster.show_toast("Brian" + str(reason), duration=10)


def alarm_reminder():
    global reminder_sec
    import win10toast
    from win10toast import ToastNotifier
    import time
    from datetime import datetime
    from datetime import date

    print("What should I remind you...?")
    speak("What should I remind you...?")
    remind = get_audio()
    print("What time should I set the reminder...?")
    speak("What time should I set the reminder...?")
    reminder_time = get_audio()
    now = datetime.now()
    current_hour1 = now.hour
    current_min1 = now.minute
    current_sec1 = now.second
    a = str(reminder_time).lower()
    z = a.replace(":", " ")
    f = [int(i) for i in z.split() if i.isdigit()]
    v = (f[0])
    x = (f[1])

    curr_time = now.strftime("%I %M %S")
    n = [int(i) for i in curr_time.split() if i.isdigit()]
    h1 = (n[0])
    m1 = (n[1])

    k1 = v - h1
    l1 = x - m1

    print("Current time: ", h1, ":", current_min1, ":", current_sec1)
    print("Notify at: ", v, ":", x, ":", now.second)

    time.sleep((l1 * 60) - 10)
    toaster = ToastNotifier()
    speak("This is you're reminder Brian to " + remind)
    toaster.show_toast(remind, duration=7)


def multiple_alarm_reminder():
    global reminder_sec
    import win10toast
    from win10toast import ToastNotifier
    import time
    from datetime import datetime
    from datetime import date

    print("How many reminders...?")
    speak("How many reminders...?")
    num_reminders = get_audio()
    j = [int(i) for i in num_reminders.split() if i.isdigit()]
    j1 = j[1]
    # print(j)

    i1 = 0
    while i1 < j1:
        i1 = i1 + 1
        # print("")
        # print(i1)
        # print("")
        if (i1 == 1):
            print("What should I remind you for the 1st reminder...?")
            speak("What should I remind you for the first reminder...?")
        if (i1 == 2):
            print("")
            print("What should I remind you for the 2nd reminder...?")
            speak("What should I remind you for the second reminder...?")
        if (i1 == 3):
            print("")
            print("What should I remind you for the 3rd reminder...?")
            speak("What should I remind you for the third reminder...?")
        if (i1 == 4):
            print("")
            print("What should I remind you for the 4th reminder...?")
            speak("What should I remind you for the fourth reminder...?")
        if (i1 == 5):
            print("")
            print("What should I remind you for the 5th reminder...?")
            speak("What should I remind you for the fifth reminder...?")
        remind = get_audio()
        now = datetime.now()
        current_hour1 = now.hour
        current_min1 = now.minute
        current_sec1 = now.second
        r1 = (i1 == 1)
        if r1:
            print("What time should I set the 1st reminder...?")
            speak("What time should I set the first reminder...?")
        r1 = (i1 == 2)
        if r1:
            print("What time should I set the 2nd reminder...?")
            speak("What time should I set the second reminder...?")
        r1 = (i1 == 3)
        if r1:
            print("What time should I set the 3rd reminder...?")
            speak("What time should I set the third reminder...?")
        r1 = (i1 == 4)
        if r1:
            print("What time should I set the 4th reminder...?")
            speak("What time should I set the fourth reminder...?")
        r1 = (i1 == 5)
        if r1:
            print("What time should I set the 5th reminder...?")
            speak("What time should I set the fifth reminder...?")
        print("Remember to say 'at' before specifying the time")
        speak("Remember to say, at , before specifying the time")
        reminder_time = get_audio()
        a = str(reminder_time).lower()
        z = a.replace(":", " ")
        f = [int(i) for i in z.split() if i.isdigit()]
        v = (f[0])
        x = (f[1])

        curr_time = now.strftime("%I %M %S")
        n = [int(i) for i in curr_time.split() if i.isdigit()]
        h1 = (n[0])
        m1 = (n[1])

        k1 = v - h1
        l1 = x - m1

        r7 = 1
        while r7 < j1:
            r7 = r7 + 1
            dd = l1
            print("Minutes : ", dd)

        print("Current time: ", h1, ":", current_min1, ":", current_sec1)
        print("Notify at: ", v, ":", x, ":", now.second)

        # time.sleep((l1*60)-10)
        # toaster = ToastNotifier()
        # speak("This is you're reminder Brian to " + remind)
        # toaster.show_toast(remind, duration=7)

    i1 = 0
    while i1 < j1:
        i1 = i1 + 1
        print("Minutes : ", dd)
        time.sleep((dd * 60) - 15)
        toaster = ToastNotifier()
        speak("This is you're reminder Brian to " + remind)
        toaster.show_toast(remind, duration=7)

        break


if __name__ == "__main__":

    while (1):
        text1 = get_audio()
        if text1 == 0:
            continue

        g = str(text1).lower()
        if "remind" in g and "second" in g:
            reminder_seconds()

        h = str(text1).lower()
        if "remind" in h and "minute" in h:
            reminder_minute()

        if "remind" in str(text1).lower() and "at" in str(text1).lower():
            alarm_reminder()

        b = str(text1).lower()
        if "multiple reminders" in b:
            multiple_alarm_reminder()

        break
