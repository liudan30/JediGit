# -*- coding: utf-8 -*-

import mechanize
import cookielib
from lxml import html
import urllib2
import sys
import shlex

from random import randint
from time import sleep
from lxml.etree import tostring
from bs4 import BeautifulSoup
import requests
import subprocess
import shlex
import os

import json
import pandas as pd
from pandas.io.json import json_normalize
import io
import imp

import ast


# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class DownStreamError(Error):
    """Raised when the retreived api response 'status' is 'ERROR'"""
    pass


class BrowserOpenReadError(Error):
    """Raised after execute br.oopen(website) if br.response()read().find(desire return keywords) is failed'"""
    pass


# start browser configuration
br = mechanize.Browser()

# Allow cookies
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# specify browser to emulate
br.addheaders = [('User-agent',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36')]


# method to get qualified repo name and thuse the gitlink
def get_repo(searchKey, pageUpperBound):
    """
    :param searchKey: repo that contains the desired key words
    :param pageUpperBound: scaped git repo, range[1, 100]
    :return: a List that contain # of pogeUpperBound scraping github websites
    """
    get_repo_list = []
    for page in xrange(1, pageUpperBound):
        query_form = 'https://github.com/search?p=' + str(page) + '&q=' + searchKey + '&type=Repositories&utf8=true'
        get_repo_list.append(query_form)
    return get_repo_list


def get_page_repo(get_repo_list, idx):
    """
    :param get_repo_list:
    :param idx:
    :return: A list with each ele is the repo name of this page
            the repo link would be 'https://github.com' + repo_name
    """
    query_form = get_repo_list[idx]
    sleep(randint(12, 43))  # wait for browing scraping
    query_br_tree = html.fromstring(br.open(query_form).get_data())
    repo_names = query_br_tree.xpath('//h3[@class="repo-list-name"]//a/@href')
    return repo_names


def getLib(repo_name, utf8, whatToFind):
    """
    # Given searched pom.xml is from advanced search format:  pom.xml in:path
    # how to call : getLib('/square/wire','true',['pom.xml', 'in:path'])
    :param repo_name: a string whose format is like : 'square/wire'
    :param utf8: 'true' or 'false' indicating the encoding utf8 enable status
    :param whatToFind: a list where recording advanced search syntax, whose format is like : ['pom.xml', 'in:path']
    :return: a HashMap, key is this repo_name, val is libs for this repo
            the val is also a hashmap, where every key is lib name (groupId), the vals for this key is formated:
            ('artifactId', 'version', 'scope')
    """
    repo_lib = {}

    if '/' not in repo_name:
        repo_lib.update({repo_name: 'Not a proper repo retreived name.'})
        print repo_lib
        return repo_lib

    query_repo_link = 'https://github.com/' + repo_name + '/'
    query_search_map = {'utf8': utf8, 'queryKey': whatToFind}
    search_postfix = _user_adv_keySearch(query_search_map)

    # this_repo_search looks like https://github.com/square/wire/search?utf=true&q=pom.xml+in:path+
    this_repo_search = query_repo_link + 'search?utf=true' + '&q=' + search_postfix

    # start to parse this_repo_search
    random_wait = randint(6, 21)
    print 'start to sleep for {} seconds'.format(random_wait)
    sleep(random_wait)  # wait for browing scraping

    repo_delay = 2
    long_wait_findRepo = False
    while True:
        if repo_delay >= 512:
            print 'Have been waiting up to {} seconds without proper response. Aborted on this repo.'.format(repo_delay)
            long_wait_findRepo = True
            break
        sleep(repo_delay)
        global this_repo_search_tree
        try:
            print 'Waiting up to {} seconds to retrieve pom.xml information from repo '.format(repo_delay) + repo_name
            this_repo_search_tree = html.fromstring(br.open(this_repo_search).get_data()).xpath(
                '//p[@class="title"]//a/@href')
        except Exception as e:
            repo_delay *= 2
            print e
        else:
            break

    if long_wait_findRepo == False and len(this_repo_search_tree) == 0:  # no xml found
        print 'No available target xml existed'
        repo_lib.update({repo_name: {}})
    elif long_wait_findRepo == True:
        repo_lib.update({repo_name: 'Not a proper repo retreived name.'})

    else:
        this_repo_xml_addr = 'https://raw.githubusercontent.com' + this_repo_search_tree[0][
                                                                   :this_repo_search_tree[0].index('blob') - 1] + \
                             this_repo_search_tree[0][this_repo_search_tree[0].index('blob') + len('blob'):]
        # start to find Lib
        lib_delay = 2
        while True:
            if lib_delay >= 512:
                print 'Have been waiting up to {} seconds without proper lib information response. Aborted on this repo.'.format(
                    lib_delay)
                break

            sleep(lib_delay)
            global soup
            try:
                print 'Waiting up to {} seconds to retrieve lib information from repo: '.format(lib_delay) + repo_name
                soup = BeautifulSoup(br.open(this_repo_xml_addr).get_data(), "html.parser")
            except Exception as e:
                lib_delay *= 2
                print e
            else:
                break

        libHashMap = {}
        if soup.findAll('dependency'):
            for node in soup.findAll('dependency'):
                this_groupId = node.find('groupId'.lower()).text.encode('utf-8') if node.find(
                    'groupId'.lower()) else None
                this_artifactId = node.find('artifactId'.lower()).text.encode('utf-8') if node.find(
                    'artifactId'.lower()) else None
                this_version = node.find('version'.lower()).text.encode('utf-8') if node.find(
                    'version'.lower()) else None
                this_scope = node.find('scope'.lower()).text.encode('utf-8') if node.find('scope'.lower()) else None
                libHashMap.update({this_groupId: (this_artifactId, this_version, this_scope)})
        else:
            print 'No available target xml existed'

        repo_lib.update({repo_name: libHashMap})

    print repo_lib

    return repo_lib


def _user_adv_keySearch(query_search_map):
    """
    :param query_search_map: format as {'utf8': utf8, 'queryKey': whatToFind}
    :return:
    """
    if query_search_map.get('queryKey') == False:
        return None
    res = ''
    for ele in query_search_map.get('queryKey'):
        res += (ele + '+')
    return res


def read_dataFiles():
    """
    :param :
    :return:List contains all data source file names in server
    """
    file_names = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            # if file.startswith("java_repo"):
            if file.startswith("x"):  # notice the data raw files name convertion may change later
                file_name = (os.path.join(root, file))
                file_names.append(file_name)
    return file_names


def writeOut(file_names_lst):
    for repo_file in file_names_lst:
        print repo_file
        with open(repo_file) as f:
            for line in f:
                line_tmp = line.split('\t')
                repo = line_tmp[0]
                print 'start to get Lib for repo: ', repo
                repo_libs = getLib(repo, 'true', ['pom.xml', 'in:path'])
                # start to write out
                print 'start to write to file'
                outfile_name = 'out_' + repo_file.split('/')[-1]
                if not os.path.isfile(outfile_name):
                    with open(outfile_name, "w") as this_out:
                        write_to = line.strip() + '\t' + str(repo_libs) + '\n'
                        this_out.write(write_to)
                else:
                    with open(outfile_name, "a") as this_out:
                        write_to = line.strip() + '\t' + str(repo_libs) + '\n'
                        this_out.write(write_to)
        print 'Results for file: ' + str(repo_file) + ' has been done.'
    print 'All files have done written.'


if __name__ == '__main__':
    file_names = read_dataFiles()
    writeOut(file_names)

    # with open('java_repo_3.txt_out.txt') as f:
    #     for line in f:
    #         tmp = line.strip('\n').split('\t')
    #         print ast.literal_eval(tmp[4])
