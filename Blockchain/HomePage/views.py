from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from datetime import datetime
from django.core.files.storage import FileSystemStorage
import mysql.connector
import random
import smtplib
import subprocess
import rsa

# Create your views here.
from django.http import HttpResponse


def file_open(file):
    key_file = open(file, 'rb')
    key_data = key_file.read()
    key_file.close()
    return key_data


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def login(request):
    return render(request, 'login.html')


def verification(request):
    return render(request, 'verification.html')


def search(request):
    return render(request, 'search.html')


def afterloginpg(request):
    return render(request, 'afterloginpg.html')


def otp(request):
    return render(request, 'otp.html')


def forgot(request):
    return render(request, 'forgot.html')


def newpass(request):
    return render(request, 'newpass.html')


def record(request):
    return render(request, 'record.html')


def download(request):
    return render(request, 'F_Result.html')


def Ulogin(request):
    Email = request.POST["email"]
    Pass = request.POST["password"]
    d["email"] = Email
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1623", database="Blockchain")
    pointer = mydb.cursor()
    try:
        command = "select pass from login where name='" + Email + "';"
        pointer.execute(command)
        b = pointer.fetchall()
        if b[0][0] == Pass:
            c = 'Hi,' + d["email"]
            return render(request, 'afterloginpg.html', {'name': c})
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login.html')
    except:
        d["email"] = None
        messages.error(request, 'Invalid Credentials')
        return redirect('login.html')


def otp_send(request):
    Email = request.POST["email"]
    d["email"] = Email
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1623", database="Blockchain")
    pointer = mydb.cursor()
    try:
        command = "select * from login where name='" + Email + "';"
        pointer.execute(command)
        b = pointer.fetchall()
        print(b[0][0])
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("gadgetmania234@gmail.com", "Hello@1234")
        s.sendmail("gadgetmania234@gmail.com", Email, d["message"])
        print(d["message"])
        s.quit()
        return render(request, 'otp.html')

    except:
        messages.error(request, 'Invalid E-mail')
        return redirect('forgot.html')


def submit_record(request):
    file = open("hash.txt", "r")
    previoushash = file.read().rstrip()
    file.close()

    try:

        Candidate_Name = request.POST["Candidate_Name"]
        Gender = request.POST["Gender"]
        University = request.POST["University"]
        Institute_Name = request.POST["Institute_Name"]
        Course = request.POST["Course"]
        Branch = request.POST["Branch"]
        Roll_Number = request.POST["Roll_Number"]
        Result_Status = request.POST["Result_Status"]
        SGPA = request.POST["SGPA"]
        Address = request.POST["Address"]
        dt = datetime.now()

        f = open("message.txt", "w")
        print("Candidate_Name : ", Candidate_Name, file=f)
        print("Gender : ", Gender, file=f)
        print("University : ", University, file=f)
        print("Institute_Name : ", Institute_Name, file=f)
        print("Course : ", Course, file=f)
        print("Branch : ", Branch, file=f)
        print("Roll_Number : ", Roll_Number, file=f)
        print("Result_Status : ", Result_Status, file=f)
        print('SGPA : ', SGPA, file=f)
        print('Address : ', Address, file=f)
        print('', file=f)
        print('', file=f)
        print("Published By : ", d["email"], file=f)
        print(dt, file=f)

        f.close()

        privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))
        message = file_open('message.txt')
        signature = rsa.sign(message, privkey, 'SHA-512')
        s = open('signature_file', 'wb')
        s.write(signature)
        s.close()

        command = 'ipfs block put signature_file > sign_hash.txt'
        subprocess.run(command, shell=True)

        f = open('sign_hash.txt', 'r')
        signature = f.read()
        f.close()

        f = open('block.txt', 'w')
        print(previoushash, file=f)
        print(Roll_Number, file=f)
        print(Institute_Name, file=f)
        print(signature, file=f)
        print("Candidate_Name : ", Candidate_Name, file=f)
        print("Gender : ", Gender, file=f)
        print("University : ", University, file=f)
        print("Institute_Name : ", Institute_Name, file=f)
        print("Course : ", Course, file=f)
        print("Branch : ", Branch, file=f)
        print("Roll_Number : ", Roll_Number, file=f)
        print("Result_Status : ", Result_Status, file=f)
        print('SGPA : ', SGPA, file=f)
        print('Address : ', Address, file=f)
        print('', file=f)
        print('', file=f)
        print("Published By : ", d["email"], file=f)
        print(dt, file=f)

        f.close()

        subprocess.run('ipfs block put block.txt > hash.txt', shell=True)

        # file = open("hash.txt", "r")
        # currenthash = file.read()
        # command = 'ipfs pubsub pub block ' + currenthash
        # subprocess.run(command, shell=True)

        messages.error(request, 'Data Saved!!!')
        return redirect('record.html')


    except:
        f = open("hash.txt", "w")
        print(previoushash, file=f)
        f.close()
        messages.error(request, 'Data Not Saved.An error occured!!')
        return redirect('record.html')


def resetpass(request):
    OTP = request.POST["otp"]
    if OTP == d["message"]:
        return render(request, 'newpass.html')
    else:
        messages.error(request, 'Invalid OTP')
        return redirect('otp.html')


def newpass(request):
    password = request.POST['password']

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="1623", database="Blockchain")
    pointer = mydb.cursor()
    try:
            command = 'update login set pass = "' + password + '" where name = "' + d["email"] + '";'
            pointer.execute(command)
            mydb.commit()
            return render(request, 'login.html')


    except:
        messages.error(request, 'Error!!')
        return redirect('newpass.html')


def search_submit(request):
    searchroll = request.POST['roll']
    searchcollege = request.POST['university']
    try:
        f = open('block.txt', 'w')
        f.write('')
        f.close()

        f = open('hash.txt', 'r')
        hash = f.readline().rstrip()
        f.close()
        print(hash)
        flag=0

        while (hash != 'NULL'):
            flag = 0
            command = 'ipfs block get ' + hash + ' >Result.txt'
            subprocess.run(command, shell=True)

            file = open('Result.txt', 'r')
            hash = file.readline().rstrip()
            roll = file.readline().rstrip()
            university =file.readline().rstrip()
            if (roll == searchroll and university == searchcollege):
                flag =1
                f = open('block.txt', 'w')

                #i = file.readline()
                i = file.readline()
                i = file.readline()

                while (i):
                    f.write(i)
                    i = file.readline()

                f.close()
                file.close()
                break

                # f = open('block.txt', 'r')
                # col = f.read(17)
                # col = f.readline().strip()
                # f.close()
                # if (university == searchcollege):
                #     flag = 1
                #     break

        if (flag == 1):
            return render(request, 'F_Result.html',{'name':roll})
        else:
            messages.error(request, 'Not Found!!')
            return redirect('search.html')


    # pdf = FPDF()
    # pdf.add_page()
    # pdf.set_font("Arial", size=15)
    # f = open("Verification\static\block.txt", "r")
    # for x in f:
    #     pdf.cell(200, 10, txt=x, ln=1, align='L')
    # pdf.output("Verification\static\certificate.txt")
    except:
        messages.error(request, 'Not Found!!')
        return redirect('search.html')

def verify(request):
    if request.method == 'POST':
        sroll = request.POST['roll']
        scollege = request.POST['university']
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        c = "media\\"+str(uploaded_file)
        print(c)
        try:
            f = open('hash.txt', 'r')
            hash = f.readline().rstrip()
            f.close()
            print(hash)
            flag = 0
            while (hash != 'NULL'):
                flag = 0
                command = 'ipfs block get ' + hash + ' >Result.txt'
                subprocess.run(command, shell=True)

                file = open('Result.txt', 'r')
                hash = file.readline().rstrip()
                roll = file.readline().rstrip()
                university = file.readline().rstrip()
                signhash=file.readline().rstrip()
                print(hash,roll,university,signhash)
                if (roll == sroll and university == scollege):
                    flag = 1
                    break

            if (flag == 1):
                print("i am here")
                command = 'ipfs block get ' + signhash + ' > signature_file2'
                subprocess.run(command, shell=True)
                print("i am here2")
                pubkey = rsa.PublicKey.load_pkcs1(file_open('publickey.key'))
                print("i am here3")
                signature = file_open('signature_file2')
                print("i am here4")
                message = file_open(c)
                try:
                    rsa.verify(message, signature, pubkey)
                    return render(request, 'F_Result.html')

                except:
                    return render(request, 'N_Result.html')


            else:
                messages.error(request, 'Not Found!!')
                return redirect('verification.html')
        except:
            messages.error(request, '1ERROR!')
            return redirect('verification.html')

    else:
        messages.error(request, '2ERROR!!')
        return redirect('verification.html')


d = {"email": 'None', "message": 000, "Pass": 'None'}
d["message"] = str(random.randint(1, 999999))
