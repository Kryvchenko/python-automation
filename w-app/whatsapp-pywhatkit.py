import pywhatkit

# personal message
phone_number = input("Enter phone number: ")
pywhatkit.sendwhatmsg(phone_number, "Hello from Bermuda", 20, 30, 10, True, 3)


# group message
group_id = input("Enter group id: ")
pywhatkit.sendwhatmsg_to_group(
    group_id, "Hello from Bermuda", 20, 30, 10, True, 3)
