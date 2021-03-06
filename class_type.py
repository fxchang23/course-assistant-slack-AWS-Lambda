import pymysql.cursors
import sys

coursenum = sys.argv[1]
dept = sys.argv[2]

connection = pymysql.connect(host='uvaclasses.martyhumphrey.info',
                                 user='UVAClasses',
                                 password='WR6V2vxjBbqNqbts',
                                 db='uvaclasses',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `Type` FROM `CompSci1178Data` WHERE `ClassNumber`=%s and `Mnemonic`=%s"
        cursor.execute(sql,(coursenum, dept))
        result = cursor.fetchone()

        if dept == "CS" or dept == "cs":
            if result != None:
                print "The type of course " + coursenum + " in " + dept + " is " + result['Type']
            else: print "I am not aware of that course at the University of Virginia"
        else: print "I am not aware of that department at the University of Virginia"


finally:
    connection.close()
