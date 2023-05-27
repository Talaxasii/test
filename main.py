import tkinter.messagebox
from tkinter import *
import datetime
import time
import winsound
import random


def validateInputTime(receivedTime):
    invalid = True
    alarmTime = [int(receivedTime[0]), int(receivedTime[1])]
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False
    return invalid


def convertTimeToSeconds(receivedTime):
    alarmTime = getEntriesValues(receivedTime)
    secondsMultiplier = [3600, 60, 1]
    currentTime = datetime.datetime.now()
    currentTimeInSeconds = sum(
        [a * b for a, b in (zip(secondsMultiplier, [currentTime.hour, currentTime.minute, currentTime.second]))])
    totalSeconds = sum([a * b for a, b in (zip(secondsMultiplier[:len(alarmTime)], alarmTime))])
    remainSeconds = totalSeconds - currentTimeInSeconds
    if remainSeconds < 0:
        remainSeconds += 86400
        return remainSeconds
    else:
        return remainSeconds


def alarm(entryData):
    time.sleep(convertTimeToSeconds(entryData))
    shutDown()


def shutDown():
    def shutdown():
        answer = answerEntry.get()
        if answer == question[1]:
            tkinter.messagebox.showinfo(message="Хорошего дня")
            shutdownWindow.destroy()
        else:
            tkinter.messagebox.showinfo(message="Неверный ответ")

    shutdownWindow = Tk()
    shutdownWindow.lift()
    shutdownWindow.geometry("400x200")
    shutdownWindow.title("Будильник")
    f = open("tasks.txt", "r", encoding="UTF8").read().splitlines()
    targetLine = random.choice(f)
    question = targetLine.split("=")
    answer = StringVar()
    welcomeLabel = Label(text="Будильник", font=("Arial", 14))
    equalsLabel = Label(shutdownWindow, text=question[0] + " = ")
    answerEntry = Entry(shutdownWindow, textvariable=answer, width=5)
    shutdownButton = Button(shutdownWindow, text="Выключить", command=lambda: shutdown())
    welcomeLabel.place(x=155, y=30)
    equalsLabel.place(x=160, y=75)
    answerEntry.place(x=200, y=75)
    shutdownButton.place(x=190, y=145)


def getEntriesValues(entryValues):
    if validateInputTime([entryValues[0], entryValues[1]]):
        tkinter.messagebox.showerror(title="Ошибка", text="Введены некорректные данные")
    else:
        entriesValue = [int(entryValues[0]), int(entryValues[1])]
        return entriesValue


def alarmDisplay():
    clock = Tk()
    clock.resizable(False, False)
    hour = IntVar()
    minute = IntVar()
    clock.title("Будильник")
    clock.geometry("400x200")
    hoursEntry = Entry(clock, textvariable=hour, width=5)
    minutesEntry = Entry(clock, textvariable=minute, width=5)
    btn = Button(clock, text="запуск", command=lambda: alarm([hoursEntry.get(), minutesEntry.get()]))
    welcomeLabel = Label(text="Будильник", font=("Arial", 14))
    hoursLabel = Label(text="часы", font=("Arial", 9))
    minutesLabel = Label(text="минуты", font=("Arial", 9))
    welcomeLabel.place(x=155, y=30)
    hoursLabel.place(x=160, y=75)
    minutesLabel.place(x=203, y=75)
    hoursEntry.place(x=165, y=100)
    minutesEntry.place(x=205, y=100)
    btn.place(x=180, y=145)
    clock.mainloop()


alarmDisplay()
