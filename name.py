#!/usr/bin/env python
#coding=utf-8
import numpy as np

#===============
#81个数字吉凶定义
t_num_ji = np.array([1,3,5,6,7,8,11,13,15,16,17,18,21,23,24,25,29,31,32,33,35,37,39,41,45,47,48,52,55,57,61,63,65,67,68,81])#共36个
t_num_xiong = np.array([2,4,9,10,12,14,19,20,22,26,27,28,30,34,36,38,40,42,43,44,46,49,50,51,53,54,56,58,59,60,62,64,66,69,70,71,72,73,74,75,76,77,78,79,80])#共45个

#=======================================================
#t_Three_cai 三才搭配表
#t_Three_cai[0]: 1木 2火 3土 4金 5水
#t_Three_cai[1]: 1大吉 2中吉 3吉多凶少 4凶多吉少 5凶 6大凶
t_Three_cai = np.array([
            [[1,1,1],1], 
            [[1,1,2],1], 
            [[1,1,3],1], 
            [[1,1,4],4], 
            [[1,1,5],3],
            [[1,2,1],1], 
            [[1,2,2],2], 
            [[1,2,3],1], 
            [[1,2,4],4], 
            [[1,2,5],6],
            [[1,3,1],6], 
            [[1,3,2],2], 
            [[1,3,3],2], 
            [[1,3,4],3], 
            [[1,3,5],6],
            [[1,4,1],6], 
            [[1,4,2],6], 
            [[1,4,3],4], 
            [[1,4,4],6], 
            [[1,4,5],5],
            [[1,5,1],1], 
            [[1,5,2],4], 
            [[1,5,3],4], 
            [[1,5,4],1], 
            [[1,5,5],1],
            
            [[2,1,1],1], 
            [[2,1,2],1], 
            [[2,1,3],1], 
            [[2,1,4],4], 
            [[2,1,5],2],
            [[2,2,1],1], 
            [[2,2,2],2], 
            [[2,2,3],1], 
            [[2,2,4],6], 
            [[2,2,5],6],
            [[2,3,1],3], 
            [[2,3,2],1], 
            [[2,3,3],1], 
            [[2,3,4],1], 
            [[2,3,5],3],
            [[2,4,1],6], 
            [[2,4,2],6], 
            [[2,4,3],3.5], 
            [[2,4,4],6], 
            [[2,4,5],6],
            [[2,5,1],4], 
            [[2,5,2],6], 
            [[2,5,3],6], 
            [[2,5,4],6], 
            [[2,5,5],6],
            
            [[3,1,1],2], 
            [[3,1,2],2], 
            [[3,1,3],4], 
            [[3,1,4],6], 
            [[3,1,5],4],
            [[3,2,1],1], 
            [[3,2,2],1], 
            [[3,2,3],1], 
            [[3,2,4],3], 
            [[3,2,5],6],
            [[3,3,1],2], 
            [[3,3,2],1], 
            [[3,3,3],1], 
            [[3,3,4],1], 
            [[3,3,5],4],
            [[3,4,1],4], 
            [[3,4,2],4], 
            [[3,4,3],1], 
            [[3,4,4],1], 
            [[3,4,5],1],
            [[3,5,1],4], 
            [[3,5,2],6], 
            [[3,5,3],6], 
            [[3,5,4],3.5], 
            [[3,5,5],6],
            
            [[4,1,1],4], 
            [[4,1,2],4], 
            [[4,1,3],4], 
            [[4,1,4],6], 
            [[4,1,5],4],
            [[4,2,1],4], 
            [[4,2,2],3.5], 
            [[4,2,3],3.5], 
            [[4,2,4],6], 
            [[4,2,5],6],
            [[4,3,1],2], 
            [[4,3,2],1], 
            [[4,3,3],1], 
            [[4,3,4],1], 
            [[4,3,5],3],
            [[4,4,1],6], 
            [[4,4,2],6], 
            [[4,4,3],1], 
            [[4,4,4],2], 
            [[4,4,5],2],
            [[4,5,1],1], 
            [[4,5,2],4], 
            [[4,5,3],2], 
            [[4,5,4],1], 
            [[4,5,5],2],
            
            [[5,1,1],1], 
            [[5,1,2],1], 
            [[5,1,3],1], 
            [[5,1,4],4], 
            [[5,1,5],1],
            [[5,2,1],2], 
            [[5,2,2],6], 
            [[5,2,3],4], 
            [[5,2,4],6], 
            [[5,2,5],6],
            [[5,3,1],6], 
            [[5,3,2],2], 
            [[5,3,3],2], 
            [[5,3,4],2], 
            [[5,3,5],6],
            [[5,4,1],4], 
            [[5,4,2],4], 
            [[5,4,3],1], 
            [[5,4,4],2], 
            [[5,4,5],1],
            [[5,5,1],1], 
            [[5,5,2],6], 
            [[5,5,3],6], 
            [[5,5,4],1], 
            [[5,5,5],2],
            ])


#根据三才搭配查表定凶吉，例如：木木木=>大吉
def table_check_3cai(a,b,c):
    ret = 0
    t=np.array([ [a,b,c],0 ])
    for index in range(125):
        if t[0]==t_Three_cai[index][0]:
            ret = t_Three_cai[index][1]  
    return ret

#根据笔画数计算三才五格，例如：10,2,4 => 三才1,1,3(木木土) 五格11,12,6,5,39  
def count_3cai_5ge(x,y,z):
    c1=1+x
    c2=x+y
    c3=y+z
    c4=z+1
    c5=c1+c2+c3
    three_cai = round(c1%10/2.0,1),round(c2%10/2.0),round(c3%10/2.0)
    five_ge = c1,c2,c3,c4,c5
    return three_cai,five_ge
    
#根据数字吉凶表计算五格吉数    
def tabel_check_5ge(c1,c2,c3,c4,c5):
    ji =0
    for index in range(len(t_num_ji)):   
        if c1==t_num_ji[index]:
            ji = ji+1
        if c2==t_num_ji[index]:
            ji = ji+1
        if c3==t_num_ji[index]:
            ji = ji+1    
        if c4==t_num_ji[index]:
            ji = ji+1
        if c5==t_num_ji[index]:
            ji = ji+1            
    return ji        
             
            
def main():

    family_name = 11 #姓氏的笔画数：张11画【请安实际修改】
    
    for i in range(1,25):
        for j in range(1,25):
            three_cai,five_ge = count_3cai_5ge(family_name,i,j)
            #print("天格人格地格:%d %d %d"%three_cai) #12木 34火 56土 78金 90水

            three_cai_ret = table_check_3cai(three_cai[0],three_cai[1],three_cai[2])
            #print("三才搭配结果:%d"%three_cai_ret) #1大吉 2中吉 3吉多凶少 4凶多吉少 5凶 6大凶
    
            five_ge_ret = tabel_check_5ge(five_ge[0],five_ge[1],five_ge[2],five_ge[3],five_ge[4])
            #print("五格吉数：%d"%five_ge_ret)
    
            if three_cai_ret==1 and five_ge_ret>=4: #筛选出三才大吉+五格4吉以上组合【请安实际修改】
                print("笔画数：%d %d；五格吉数%d"%(i,j,five_ge_ret))

if __name__ == '__main__':
    main()
