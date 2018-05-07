import xml.etree.ElementTree as ET

print "1. Run test cases"
print "2. List test runs"
print "3.Show test results"
print "4. generate HTML test reports"
print "5. Exit"
option = int(input("enter an option"))
test_result = list()

if option  == 1 :
    f_num = int(raw_input("enter the number of files u want to run"))
    for i in range(f_num) :
        fname = raw_input("enter the filename")
        try :
            new = __import__(fname)
            test_result.append("passed")
        except :
            test_result.append("failed")
    test_passed = test_result.count("passed")
    test_failed = test_result.count("failed")

    root = ET.Element("testresult")
    doc = ET.SubElement(root, "result")
    for i in range(len(test_result)) :
        field = "testcase"+str(i+1)
        ET.SubElement(doc, field).text = test_result[i]
    ET.SubElement(doc, "testpassed").text = str(test_passed)
    ET.SubElement(doc, "testfailed").text = str(test_failed)
    tree = ET.ElementTree(root)

    import datetime
    now = datetime.datetime.now()
    f_name = now.strftime("%Y-%m-%d")+".xml"
    tree.write(f_name)


elif option == 2 :
    import glob
    files = glob.glob("*.xml")
    for i in files :
        print i

elif option == 3:
    f_name = raw_input("enter the file name")
    tree = ET.parse(f_name)
    root = tree.getroot()
    print "=="*10
    print root.tag+" "*8+f_name[:-4]
    print "=="*10
    for child in root.find("result") :
        print child.tag,child.text
    print "=="*10

elif option == 4:
    import HTML
    f_name = raw_input("enter the file name")
    tree = ET.parse(f_name)
    root = tree.getroot()
    head = root.tag+" "*8+f_name[:-4]
    html_list = HTML.List()
    for child in root.find("result") :
        html_list.lines.append("%s : %s" % (child.tag,child.text))
    
