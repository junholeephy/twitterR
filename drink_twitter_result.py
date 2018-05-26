import os,sys
sys.path.append("./func")
from read_as_list import str_list
from date_maker import DATE_MAKER

#Output_filename = "test_soomin_2018-05-07.txt"
REGION = "NY"
BEVERAGE = "beer"
DURATION = 1

pos_file = "python_positive.txt"
neg_file = "negative-words.txt"
pos_list = str_list(pos_file)
neg_list = str_list(neg_file)

year = 2018
day = 7
month = 5



for ijk in range(DURATION):
    soo_date = DATE_MAKER()
    DATE_input = soo_date.DATE_MAKER(year,month,day)
    DATE = soo_date.MAKE_DATE_STR(DATE_input)
    SOO_DATE = DATE[0]
    #print(SOO_DATE)
    FILE_NAME = REGION + "_" + BEVERAGE + "_" + SOO_DATE + ".txt"
    OUTFILE_NAME = REGION + "_" + "drink"+BEVERAGE + "_" + SOO_DATE + ".txt"
    print("Input file name : ",FILE_NAME)
    print("Generated file name : ",OUTFILE_NAME)
#    in_file = "NY_beer_2018-05-07.txt"
    in_file = FILE_NAME

    in_list = str_list(in_file)
    #test = in_list[100].split()
    FIRST_LINE = 0
    for SOOMIN in in_list:
        P_count = 0; N_count=0
        soo = SOOMIN.split()
        tot_word_soo = len(soo)
        for word_soo in range(tot_word_soo):
            if soo[word_soo].lower() in pos_list:
                P_count = P_count + 1
            if soo[word_soo] in neg_list:
                N_count = N_count + 1
        outfile = open(OUTFILE_NAME,"a+")
        if(FIRST_LINE == 0 ):
             outfile.write("v1 v2 v3\n")
             FIRST_LINE = 1
        outfile.write("%s " %str(tot_word_soo))
        outfile.write("%s " %str(P_count))
        outfile.write("%s" %str(N_count))
        outfile.write("\n")
        outfile.close()
    year= DATE_input[0]
    month = DATE_input[1]
    day = DATE_input[2]+1

