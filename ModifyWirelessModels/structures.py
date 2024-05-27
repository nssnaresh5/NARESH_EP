import base64
from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from wsdiscovery.publishing import ThreadedWSPublishing as WSPublishing
import re


def __find_in_dictionary(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in __find_in_dictionary(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in __find_in_dictionary(key, d):
                        yield result


def __find_in_iterator(key, iterator):
    for item in iterator:
        if key in item:
            return item


def get_flipped_dict(initial_dict):
    flipped_dict = {}
    for key, value in initial_dict.items():
        if value not in flipped_dict:
            flipped_dict[value] = [key]
        else:
            flipped_dict[value].append(key)
    return flipped_dict


def compare_lists(old_list, new_list):
    added = [item for item in new_list if item not in old_list]
    removed = [item for item in old_list if item not in new_list]
    return added, removed


# data = {
#     "version": "0.18.7",
#     "_timeToLive": 30,
#     "dataExpiryRatioVsTimeToLive": {
#         'aa': 1,
#         'b': 2,
#         'c': {
#             'aa': 11
#         }
#     }
# }


def findKeyvalue(obj, path):
    def extract_element_from_json(obj, path):
        def extract(obj, path, ind, arr):
            key = path[ind]
            if ind + 1 < len(path):
                if isinstance(obj, dict):
                    if key in obj.keys():
                        extract(obj.get(key), path, ind + 1, arr)
                    else:
                        arr.append(None)
                elif isinstance(obj, list):
                    if not obj:
                        arr.append(None)
                    else:
                        for item in obj:
                            extract(item, path, ind, arr)
                else:
                    arr.append(None)
            if ind + 1 == len(path):
                if isinstance(obj, list):
                    if not obj:
                        arr.append(None)
                    else:
                        for item in obj:
                            arr.append(item.get(key, None))
                elif isinstance(obj, dict):
                    arr.append(obj.get(key, None))
                else:
                    arr.append(None)
            return arr

        if isinstance(obj, dict):
            return extract(obj, path, 0, [])
        elif isinstance(obj, list):
            outer_arr = []
            for item in obj:
                outer_arr.append(extract(item, path, 0, []))
            return outer_arr

    path = path.split(".")
    txt = extract_element_from_json(obj, path)
    if txt is not None:
        return txt
    else:
        return ""


def convertb64(passwordstring):
    pwdascii = passwordstring.encode('ascii')
    pwdb = base64.b64encode(pwdascii)
    pwdbase64 = pwdb.decode('ascii')
    return pwdbase64


def time_me(*arg):
    import time
    if len(arg) != 0:
        elapsedTime = time.time() - arg[0]
        import math
        hours = math.floor(elapsedTime / (60 * 60))
        elapsedTime = elapsedTime - hours * (60 * 60)
        minutes = math.floor(elapsedTime / 60)
        elapsedTime = elapsedTime - minutes * (60)
        seconds = math.floor(elapsedTime)
        elapsedTime = elapsedTime - seconds
        ms = elapsedTime * 1000
        if (hours != 0):
            # print ("%d hours %d minutes %d seconds" % (hours, minutes, seconds))
            print("%d hours %d minutes %d seconds" % (hours, minutes, seconds))
        elif (minutes != 0):
            # print ("%d minutes %d seconds" % (minutes, seconds))
            print("%d minutes %d seconds" % (minutes, seconds))
        else:
            # print ("%d seconds %0.3f ms" % (seconds, ms))
            print("%d sec %0.0f ms" % (seconds, ms))
    else:
        # print ('does not exist. here you go.');
        return time.time()


def getid(data):
    if type(data) is dict:
        return findKeyvalue('_id', data)


def log(txt):
    print(txt)
    import datetime
    ct4 = datetime.datetime.now()
    ct = str(ct4).split(" ")[1]
    dt1 = str(ct4).split(" ")[0]
    dt2 = dt1.split("-")
    ct1 = ct.split(".")[0]
    ct2 = ct.split(".")[1][:3]
    ct3 = dt2[2] + '-' + dt2[1] + '-' + dt2[0] + '#' + ct1 + "." + ct2 + '==>'
    with open('filename.log', 'a') as fhandle:
        fhandle.write(ct3 + txt + '\n')


def ping(host):
    """
    :param host
    :return Returns True if host responds to a ping request
    """
    import subprocess, platform, sys
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if platform.system().lower() == "windows" else True
    # sys.stdout.flush()
    return subprocess.call(args, shell=need_sh, stdout=need_sh, stderr=subprocess.STDOUT) == 0


def multithread(function_name, argumentlist):
    import time
    t1 = time.perf_counter()
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        result = executor.map(function_name, argumentlist)
    returnresult = []
    for i in result:
        returnresult.append(i)
    # print(returnResult)
    t2 = time.perf_counter()
    print(str(int(t2 - t1)) + ' sec(s)')
    return returnresult


def findDPWSIP():
    # Publish the service
    wsp = WSPublishing()
    wsp.start()
    wsd = WSDiscovery()
    wsd.start()
    services = wsd.searchServices()
    ip = []
    for service in services:
        # print(service.getXAddrs()[0])
        ipstr = service.getXAddrs()[0]
        print(ipstr)
        ips = re.findall(r"//.*:", ipstr)[0]
        ipst = ips.replace("//", "").replace(":", "")
        # print(ipst)
        ip.append(ipst)
    wsd.stop()
    return ip


def Modbus_43_14(IP, slaveaddress=255, objectType=1):
    from pymodbus.mei_message import ReadDeviceInformationRequest
    from pymodbus.client import ModbusTcpClient
    try:
        client = ModbusTcpClient(IP, port=502)
        client.connect()
        rq = ReadDeviceInformationRequest(unit=slaveaddress, read_code=objectType)
        rr = client.execute(rq)
        data1 = [IP]
        for i in dict(rr.information).items():
            data1.append(i[1].decode("utf-8").rstrip('\x00'))
        client.close()
        print(data1)
    except:
        pass


def printdict(data):
    import json
    print(json.dumps(data, indent=2))


# Modbus_43_14('10.179.247.187',255,3)


def readResponse(obj, path):
    """
    It takes a JSON object and a path to a value in that object, and returns the value

    :param obj: The object to read from
    :param path: The path to the value you want to extract from the response
    :return: The value of the path in the response
    """
    try:
        if path == '':
            return obj
        else:
            p = path.split(".")
            if isinstance(obj, dict):
                return readResponse(obj[p[0]], ".".join(p[1:]))
            if isinstance(obj, list):
                for i in obj:
                    if isinstance(i, dict):
                        return readResponse(i[p[0]], ".".join(p[1:]))
            if isinstance(obj, str) and path == '':
                return obj
            else:
                raise TypeError("Bad Path")
    except Exception as e:
        e.add_note('Please check path')
        raise
