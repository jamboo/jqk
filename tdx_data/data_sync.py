__author__ = 'Winface'

from struct import *
from constants.constants import *
from util.util import iterate_file_names


def get_output_filename(filename):
    if 'sz' in filename:
        return sz_data_directory+'\\'+filename
    if 'sh' in filename:
        return sh_data_directory+'\\'+filename

def get_input_filename(filename):
    if 'sz' in filename:
        return processed_sz_data_directory +'\\'+ filename.replace('.day', '.csv')
    if 'sh' in filename:
        return processed_sh_data_directory +'\\'+ filename.replace('.day', '.csv')

def convert_to_text(filename):
    output_filename = get_output_filename(filename)
    ofile=open(output_filename,'rb')
    buf=ofile.read()
    ofile.close()

    input_filename = get_input_filename(filename)
    ifile=open(input_filename,'w')
    num=len(buf)
    no=num/32
    b=0
    e=32
    line=''

    for i in xrange(no):
       a=unpack('IIIIIfII',buf[b:e])
       line=str(a[0])+', '+str(a[1]/100.0)+', '+str(a[2]/100.0)+', '+str(a[3]/100.0)+', '+str(a[4]/100.0)+', '+str(a[5])+', '+str(a[6])+', '+str(a[7])+' '+'\n'
       # print line
       ifile.write(line)
       b=b+32
       e=e+32
    ifile.close()


def generate_file_data():
    files = iterate_file_names()
    for filename in files:
        try:
            convert_to_text(filename)
        except:
            print 'failed for ' +filename
            pass
    print 'data generation is completed'


def test():
    convert_to_text('C:\\new_tdx\\vipdoc\\sz\\lday\\sz000680')

if __name__ == '__main__':
   #test()
    generate_file_data()
