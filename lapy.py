#!/usr/bin/python3
import requests
import threading
from colorama import Fore, Back, Style
import argparse
import sys


class s3:

    def __init__(self, domain):
        self.domain = domain
        self.s3_url = "http://{}.s3.amazonaws.com".format(domain)


    def url_handler(self):
        try:
            r = requests.get(self.s3_url, timeout=5)
            status = r.status_code
            if status != 404:
                print(Fore.RED + "[*] Found: {} status code:{}".format(self.s3_url, r.status_code))
        
        except Exception as e:
            pass
            print(e)



class Permutations():

    def __init__(self, domain):
        self.domain = domain
        self.enviroments = ['dev', 'development', 'stage', 's3', 'prod', 'homol', 'hml', 'test', 'teste', 'homolog', 'amazonaws']


    def permutations_with_dot(self):
        try:
            with open('common_bucket_prefixes.txt', 'r') as f:
                lines_file = f.readlines()
                lines = [lines.rstrip() for lines in lines_file]
                for line in lines:
                    for enva in self.enviroments:
                    # domain.admin.dev.s3.amazon.com.br
                        permute_domain = "{}.{}.{}".format(self.domain,line,enva)
                        s3_objt = s3(permute_domain)
                        s3_objt.url_handler()
        finally:
            f.close()


    def permutations_with_dash(self):
        try:
            with open('common_bucket_prefixes.txt', 'r') as f:
                lines_file = f.readlines()
                lines = [lines.rstrip() for lines in lines_file]
                for line in lines:
                    for enva in self.enviroments:
                        # domain.admin.dev.s3.amazon.com.br
                        permute_domain = "{}-{}-{}".format(self.domain,line,enva)
                        s3_objt = s3(permute_domain)
                        s3_objt.url_handler()
        finally:
            f.close()

    
    def permutations_with_dash_dot(self):
        try:
            with open('common_bucket_prefixes.txt', 'r') as f:
                lines_file = f.readlines()
                lines = [lines.rstrip() for lines in lines_file]
                for line in lines:
                    for enva in self.enviroments:
                        # domain.admin.dev.s3.amazon.com.br
                        permute_domain = "{}-{}.{}".format(self.domain,line,enva)
                        s3_objt = s3(permute_domain)
                        s3_objt.url_handler()
        finally:
            f.close()

    def permutations_dash(self):
        try:
            with open('common_bucket_prefixes.txt', 'r') as f:
                lines_file = f.readlines()
                lines = [lines.rstrip() for lines in lines_file]
                for line in lines:
                    for enva in self.enviroments:
                    # domain.admin.dev.s3.amazon.com.br
                        #permute_domain = str(self.domain) + "-" + str(line) + str(enva)
                        permute_domain = "{}-{}{}".format(self.domain,line,enva)
                        s3_objt = s3(permute_domain)
                        s3_objt.url_handler()
        finally:
            f.close()

    def permutations_dot_dash(self):
        try:
            with open('common_bucket_prefixes.txt', 'r') as f:
                lines_file = f.readlines()
                lines = [lines.rstrip() for lines in lines_file]
                for line in lines:
                    for enva in self.enviroments:
                    # domain.admin.dev.s3.amazon.com.br
                        permute_domain = "{}.{}-{}".format(self.domain,line,enva)
                        s3_objt = s3(permute_domain)
                        s3_objt.url_handler()
        finally:
            f.close()

    def permutations_single_dot(self):
        try:
            for enva in self.enviroments:
                # domain.admin.dev.s3.amazon.com.br
                permute_domain = "{}.{}".format(self.domain,enva)
                s3_objt = s3(permute_domain)
                s3_objt.url_handler()
        except Exception as e:
            print(e)
        

    def permutations_single_dash(self):
        try:
            for enva in self.enviroments:
                # domain.admin.dev.s3.amazon.com.br
                permute_domain = "{}-{}".format(self.domain,enva)
                s3_objt = s3(permute_domain)
                s3_objt.url_handler()
        except Exception as e:
            print(e)

    def permutations_single_together(self):
        try:
            for enva in self.enviroments:
                # domain.admin.dev.s3.amazon.com.br
                permute_domain = "{}{}".format(self.domain,enva)
                s3_objt = s3(permute_domain)
                s3_objt.url_handler()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    
    menu = argparse.ArgumentParser()
    menu.add_argument('-n', '--name', help='name of the target to be permuted ex: facebook')
    m = menu.parse_args()
    target = m.name

    if target == None or target == "":
        print("[*] usage: python3 lapy.py facebook")
        sys.exit()

    s1 = Permutations(target)
    threads_list =[]
    t1 = threading.Thread(target=s1.permutations_dash)
    t2 = threading.Thread(target=s1.permutations_with_dot)
    t3 = threading.Thread(target=s1.permutations_with_dash)
    t4 = threading.Thread(target=s1.permutations_with_dash_dot)
    t5 = threading.Thread(target=s1.permutations_dot_dash)
    t6 = threading.Thread(target=s1.permutations_single_dot)
    t7 = threading.Thread(target=s1.permutations_single_dash)
    t8 = threading.Thread(target=s1.permutations_single_together)


    threads_list.append(t1)
    threads_list.append(t2)
    threads_list.append(t3)
    threads_list.append(t4)
    threads_list.append(t5)
    threads_list.append(t6)
    threads_list.append(t7)
    threads_list.append(t8)


    for thr in threads_list:
        thr.start()
