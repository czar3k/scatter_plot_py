# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:18:27 2017

@author: Maja Wojcik
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#ten plik musi sie znajdowac w tym samym folderze co pliki z behaview
import numpy as np
import pylab as plt
import csv
import os

def analize_experiment(name, interval):
    behaviors= {} 
    n_line = 0
    #with open(name+'.bvs','rb') as file:
    with open(wdir+name,'rb') as file:
        for line in file:
            if n_line == 0:
                print(line)
                n_line+=1
            else:
                line = str(line)
                hour = int(line[2:4])
                minute = int(line[5:7])+1
                minutes = int(line[5:7])
                miliseconds= int(line[8:10])+0.01*int(line[11:13])
                time = hour*3600+minutes*60+miliseconds 
                #print(line, minuta)
                #print(line[16:-5])
                behav = line[16:-5]
                n_line+=1
                if behav not in behaviors.keys():
                    behaviors[behav]=[time]
                else:
                    behaviors[behav].append(time)
    total_time = int(np.ceil(time/60)) 
    for behav in behaviors.keys():
        
        times = sorted(behaviors[behav])
        

   
    t = np.arange(interval,(total_time//interval+1)*interval+1,interval)
    
    behaviors_times = {}
    for key in behaviors.keys():
        behav = behaviors[key]
        print('###########',key,'###################################')
        print(behav)
        behaviors_times[key] = np.zeros(len(t))
        for i in range(int(len(behav)/2)):
            if behav[2*i]//60 == behav[2*i+1]//60:
                min_0 = int(behav[2*i]//60)
                duration_0 = behav[2*i+1]-behav[2*i]
                print('minute:',min_0+1, 'time',duration_0,'s' )
                behaviors_times[key][min_0//interval]+=duration_0
            else:
                print('nieoczywiste',behav[2*i],behav[2*i+1])
                min_1 = int(behav[2*i]//60)
                min_2 = int(behav[2*i+1]//60)
                duration_1 = (min_1+1)*60-behav[2*i]
                print('minute:',min_1+1, 'time',duration_1,'s')
                behaviors_times[key][min_1//interval]+=duration_1 
                for min_j in range(min_1+1, min_2):
                    print('minute:',min_j, 'time',60,'s')
                    behaviors_times[key][min_j//interval]+=60 
                duration_2 = behav[2*i+1]-min_2*60
                print('minute:',min_2+1, 'time',duration_2,'s')
                behaviors_times[key][min_2//interval]+=duration_2 
    return behaviors_times, total_time          

def draw_chart(behaviors_times, total_time, directory, interval): #tu robi pogladowe wykresy dla kazdego zachowania
    t = np.arange(interval,(total_time//interval+1)*interval+1,interval)
    for key in behaviors_times.keys():
        print(behaviors_times[key])
        print(t)
        plt.plot(t,behaviors_times[key],'ro-')
        plt.axis([1-0.1,total_time+0.1,-0.1,np.max(behaviors_times[key])+0.1])
        plt.xlabel('minute')
        plt.ylabel('time [$s$]')
        plt.xticks(t)
        plt.savefig(directory+key)
        plt.show()
        
        width = 1
        plt.bar(t, behaviors_times[key], width, color="pink", align='center')
        plt.axis([1-0.1,total_time+0.1,-0.1,np.max(behaviors_times[key])+0.1])
        plt.xlabel('minute')
        plt.ylabel('time [$s$]')
        plt.xticks(t)
       # plt.savefig('wynik/'+key) #tu mozesz sobie zapisac te wykresy, ale ja je robilam w czym innym wiec to zablokowalam
        plt.show()
    
#tu robisz podzial jaki sobie chcesz, ale musisz te same nazwy grup wprowadzic w data2csv
social = ['following', 'allogrooming', 'nose to butt', 'nose to head', 'pro-social', 'passing by', 'crawling', 'sniffing']
explor_social = [' nose to butt', 'nose to head', 'sniffing', 'following']
non_social = ['rearing', 'cage exploration', 'digging', 'self-grooming']
explor_non_social = ['rearing', 'cage exploration', 'digging']
others = ['self-grooming','crawling','passing by', 'pro-social']


def data2csv(name,behaviors_times, total_time, directory, interval): #tu definiujesz jak ma zapisywac dane w pliku, ktory pozniej mozna w excelu otworzyc
    t = np.arange(interval,(total_time//interval+1)*interval+1,interval)
    with open('%sczasy.csv'%directory, 'w') as csvfile:
        fieldnames = ['Nazwa_zachowania']
        fieldnames+= ['Czas_min%s[s]'%(i+1) for i in range(len(t))]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect=csv.excel_tab, lineterminator='\n')
        writer.writeheader()
        csvfile.write("Spoleczne\n")
        for key in behaviors_times.keys():
            if key in social:
                result = {'Nazwa_zachowania': key}
                for i in range(len(t)):
                    result['Czas_min%s[s]'%(i+1)] = behaviors_times[key][i]
                writer.writerow(result)
                print(result)
        csvfile.write("Społeczne eksploracyjne\n")
        for key in behaviors_times.keys():
            if key in explor_social:
                result = {'Nazwa_zachowania': key}
                for i in range(len(t)):
                    result['Czas_min%s[s]'%(i+1)] = behaviors_times[key][i]
                writer.writerow(result)
                print(result)
        csvfile.write("Niespoleczne\n")
        for key in behaviors_times.keys():
            if key in non_social:
                result = {'Nazwa_zachowania': key}
                for i in range(len(t)):
                    result['Czas_min%s[s]'%(i+1)] = behaviors_times[key][i]
                writer.writerow(result)
                print(result)
        csvfile.write("Eksploracyjne niespoleczne\n")
        for key in behaviors_times.keys():
            if key in explor_non_social:
                result = {'Nazwa_zachowania': key}
                for i in range(len(t)):
                    result['Czas_min%s[s]'%(i+1)] = behaviors_times[key][i]
                writer.writerow(result)
                print(result) 
        csvfile.write("Pozostale\n")
        for key in behaviors_times.keys():
            if key in others:
                result = {'Nazwa_zachowania': key}
                for i in range(len(t)):
                    result['Czas_min%s[s]'%(i+1)] = behaviors_times[key][i]
                writer.writerow(result)
                print(result)
                
        
#exp = ['nazwa_pliku', 'nazwa_pliku2' ] #można wiele na raz plikow analizowac
exp = os.listdir(os.getcwd()+"/do_analizy");
wdir = os.getcwd()+"/do_analizy/";
interval = 3 #tu podział w jakich okresach czasu ma pokazywać wyniki
for name in exp:
    directory = 'results/%s_%s/'%(name,interval)
    if not os.path.exists(directory):
        os.makedirs(directory)
    behaviors_times, total_time = analize_experiment(name, interval)
    draw_chart(behaviors_times, total_time, directory, interval)
    data2csv(name,behaviors_times, total_time, directory, interval)
    print(behaviors_times)