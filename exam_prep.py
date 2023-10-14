my_logs = '''192.168.1.2 - - [17/Sep/2013:22:18:19 -0700] "GET /abc HTTP/1.1" 404 201
192.168.1.1 - - [17/Sep/2013:22:18:19 -0700] "GET /favicon.ico HTTP/1.1" 200 1406
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GETp/ /w HTTP/1.1" 200 5325
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GETp/ /w HTTP/1.1" 200 5325
192.168.1.1 - - [17/Sep/2013:22:18:19 -0700] "GET /favicon.ico HTTP/1.1" 200 1406
192.168.1.1 - - [17/Sep/2013:22:18:19 -0700] "GET /favicon.ico HTTP/1.1" 200 1406
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GETp/ /w HTTP/1.1" 200 5325
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GETp/ /w HTTP/1.1" 200 5325
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GETp/ /w HTTP/1.1" 200 5325
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve/style.css?ver=3.5.1 HTTP/1.1" 200 35292
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve/style.css?ver=3.5.1 HTTP/1.1" 200 35292
192.168.1.2 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve/style.css?ver=3.5.1 HTTP/1.1" 200 35292
192.168.1.3 - - [17/Sep/2013:22:18:27 -0700] "GET /wp/wp-content/themes/twentytwelve/js/navigation.js?ver=1.0 HTTP/1.1" 200 863'''

#print(my_logs)
my_lines = my_logs.split("\n")
#print(my_lines)
counter_dict = {}
for line in my_lines:
    if line == '':
        continue
    #print(line)
    my_ip = line.split(" ")[0]
    #print(my_ip)
    if my_ip in counter_dict:
        counter_dict[my_ip] +=1
    else:
        counter_dict[my_ip] = 1
print(counter_dict)
highest_value = max(counter_dict, key=counter_dict.get)
print("Most-occurances : " + str(highest_value))

lowest_value = min(counter_dict, key=counter_dict.get)
print("Least-occurances : " + str(lowest_value))
