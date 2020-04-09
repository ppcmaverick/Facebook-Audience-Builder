
import re
import numpy
import array
import requests
from bs4 import BeautifulSoup


class PhaseOne:
    # start and get data
    def promptAndGetData():
        
        '''
        # read raw data from file
        print("\nStart working the file")
        print("Process start:")

        Inf = open(r"input.txt","r")
        print("\nInput file opened successfully")

        print("\nStart reading from input file")

        Data = Inf.read()
        print(Data)

        print("\nReading complete, please wait")

        Inf.close()
        '''
        
        # get raw data from facebook
        print("What keyword would you like to search?")
        keyword = input("Keyword: ")
        
        # reading api key
        with open("key.txt", "r") as keyfile:
            key = keyfile.readlines()
            keyfile.close()
        
        url_p1 = "https://graph.facebook.com/search?type=adinterest&q=["
        url_p2 = "]&limit=10000&locale=en_US&access_token=" + key[0]
        
        url = url_p1 + str(keyword) + url_p2

        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        page = requests.get(url, headers = headers)
        Data = BeautifulSoup(page.content, 'html.parser')
        Data = str(Data)

        # Processing data
        i = 0
        for i in Data:
            inofdata = Data.count("\"name\"")

        print(inofdata, "data sets in the input file")

        # Counting positions of datae
        print("\nInstances of name:")
        i = 0
        posname = []
        while i < len(Data):
            i = Data.find("name", i)
            if i == -1:
                break
            print("name found at", i)
            posname.append(i + len("name :  "))
            i += len("name :  ")
            i = Data.find("\"", i)
            print("name ends at", i)
            posname.append(i)
        print(posname)

        print("\nInstances of audience_size:")
        i = 0
        posaudsize = []
        while i < len(Data):
            i = Data.find("audience_size", i)
            if i == -1:
                break
            print("aud_size found at", i)
            posaudsize.append(i + len("audience_size : "))
            i += len("audience_size :  ")
            i = Data.find(",", i)
            print("aud_size ends at", i)
            posaudsize.append(i)
        print(posaudsize)

        # Getting the data itself
        print("\nData for audience names:")
        i = 0
        j = 0
        dtname = []
        while i != inofdata * 2:
            tempstr = ""
            for j in range(posname[i], posname[i+1]):
                print(j, end = ' ')
                tempstr += (Data[j])
            dtname.append(tempstr)
            i += 2
        print("\n", dtname)

        print("\nData for audience size:")
        i = 0
        j = 0
        dtsize = []
        while i != inofdata * 2:
            tempstr = ""
            j = posaudsize[i]
            chk = posaudsize[i + 1]
            for j in range(posaudsize[i], posaudsize[i+1]):
                print(j, end = ' ')
                tempstr += (Data[j])
            dtsize.append(int(tempstr))
            i += 2

        print("\n", dtsize)

        return inofdata, dtname, dtsize


    # building audience the sets
    def sets(Data):
        inofdata = Data[0]
        dtname = Data[1]
        dtsize = Data[2]
        # Start building the sets
        audsum = 0
        i = 0
        while i < Data[0]:
            audsum = audsum + Data[2][i]
            i += 1
        print(audsum)

        numpy.array(Data[2]).astype(numpy.float)
        audavg = numpy.median(Data[2])
        print(audavg)

        '''
        print("\n\n\nHow many sets would you like to have?")
        setsnr = int(input("setsnr = "))
        setsindex = []
        i = 0
        while i < setsnr:
            if i == (setsnr - 1):
                setsindex.append((Data[0] // setsnr) + (Data[0] % setsnr))
                break
            setsindex.append(Data[0] // setsnr)
            i += 1

        print(setsindex)

        i = 0
        j = 0
        while i < setsnr:
            while j < setsindex[i]:
                j += 1

            i += 1
        '''

        # Writing to output file
        Opf = open("output.txt", "w")
        print("Output file created successfully")

        i = 0
        while i != Data[0]:
            Opf.write(Data[1][i])
            Opf.write(" -- ")
            Opf.write(str(Data[2][i]))
            Opf.write("\n")
            i += 1

        # close output file    
        print("\nClosing files")
        Opf.close()