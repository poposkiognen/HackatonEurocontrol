
current_seek = 0
current_cat = ""
current_len = 0
current_fspec = ""
data_name = ""
import time

def print_by_eigth(arr):
    for i in range(0,len(arr),8):
            print(arr[i:i+8])

def get_entire_message(file_name):
    file = open(file_name + '.ast','r')
    message_text = ""
    file = file.read()
    print(len(file))
    message_text = "".join("{:08b}".format(ord(c),'b') for c in file)
    return message_text


def get_separate_messages(message_text):
    messages = []




def get_configuration_for_category():
    global current_cat
    configuration_file = open("conf\\" + str(current_cat) + ".conf")
    configuration_file = configuration_file.read()
    return configuration_file


def get_message_category():
    global current_len
    global current_cat
    global current_seek
    file = open(data_name ,"r")
    file.seek(current_seek)
    file = file.read(1)
    if(file != ""):
        current_cat = "".join("{:08b}".format(ord(c),'b') for c in file)
        current_cat = int(current_cat,2)
        return current_cat
    return ""

def get_message_length():
    global current_len
    global current_cat
    global current_seek
    file = open(data_name, "r")
    file.seek(current_seek+1)
    file = file.read(2)
    current_len_local = "".join("{:08b}".format(ord(c),'b') for c in file)
    current_len_local = int(current_len_local,2)
    current_len = current_len_local
    return current_len

def get_message():
    global current_len
    global current_cat
    global current_seek
    file = open(data_name, "r")
    file.seek(current_seek)
    file = file.read(current_len)
    message = "".join("{:08b}".format(ord(c), 'b') for c in file)
    current_seek += current_len
    return message


def get_fspec(message):
    global current_len
    global current_cat
    global current_seek
    global current_fspec
    i = 8
    current_fspec = ""
    current_fspec += message[0:i]
    while message[i+7] != 0:
        moment = message[i: i+8]
        current_fspec += moment
        i = i + 8
        if i >=len(message):
            break


    return current_fspec


get_fspec("11111111000000010000000111111100")




def main(file_name, number_of_cores):
    global data_name
    data_name = file_name

    x = time.time()
    print x
    message_cat = get_message_category()
    i = 1
    while message_cat != "":

        message_len = get_message_length()
        message = get_message()
        message_cat = get_message_category()

        i+=1
    print i
    print time.time()-x

main("Hackathon.ast",1)




    # while message_category != "":

