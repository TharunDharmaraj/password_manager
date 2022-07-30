# #====================================cartoonize image=================================
# import cv2
#
# img2 = cv2.imread(r'C:\Users\tharu\Dropbox\My PC (LAPTOP-DDCHP58Q)\Pictures\EVS\54830803.jpg')
#
# height, width = img2.shape[:2]
# max_height = 500
# max_width = 500
#
# # only shrink if img is bigger than required
# if max_height < height or max_width < width:
#     # get scaling factor
#     scaling_factor = max_height / float(height)
#     if max_width/float(width) < scaling_factor:
#         scaling_factor = max_width / float(width)
#     # resize image
#     img2 = cv2.resize(img2, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
#
# color = cv2.cvtColor(img2, cv2.COLOR_BGRA2GRAY)
# color = cv2.medianBlur(color, 5)
# edges = cv2.adaptiveThreshold(color, 500,
#                               cv2.ADAPTIVE_THRESH_MEAN_C,
#                               cv2.THRESH_BINARY, 9, 9)
#
# color = cv2.bilateralFilter(img2, 5, 250, 250)
# cartoon = cv2.bitwise_or(color, color,mask=edges)
#
# cv2.imshow("Image", img2)
# cv2.imshow("edges", edges)
# cv2.imshow("Cartoon", cartoon)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #========================To increase followers on instagram=================
# from instabot import Bot
#
# bot = Bot()
# bot.login(username="hd_images_only", password="Kishor#27")
# # # *****## upload a picture #******
# # bot.upload_photo(r"C:\Users\tharu\PycharmProjects\python 100 days code\password-manager-start\download.jpg",
# #                  caption="magnificient")
# # *****# follow someone
# bot.follow("hd_images_only")
# # # send a message #######
# # bot.send_message("Hello from hd_image", ['userl', 'user2'])
# # get follower info ##******
# # my_followers = bot.get_user_followers("codehub.py")
# # for follower in my_followers:
# #     print(follower)
# bot.unfollow_everyone()
#

# import subprocess
#
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', 'i','key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<30| {:<}".format(i, results[0]))
#     except IndexError:
#         print("{:30}| {:<}".format(i, ""))
#
# import scapy.all as scapy
# # We need to create regular expressions to ensure that the input is correctly formatted.
# import re
#
# # Basic user interface header
# print(r"""______            _     _  ______                 _           _
# |  _  \          (_)   | | | ___ \               | |         | |
# | | | |__ ___   ___  __| | | |_/ / ___  _ __ ___ | |__   __ _| |
# | | | / _` \ \ / / |/ _` | | ___ \/ _ \| '_ ` _ \| '_ \ / _` | |
# | |/ / (_| |\ V /| | (_| | | |_/ / (_) | | | | | | |_) | (_| | |
# |___/ \__,_| \_/ |_|\__,_| \____/ \___/|_| |_| |_|_.__/ \__,_|_|""")
# print("\n****************************************************************")
# print("\n* Copyright of David Bombal, 2021                              *")
# print("\n* https://www.davidbombal.com                                  *")
# print("\n* https://www.youtube.com/davidbombal                          *")
# print("\n****************************************************************")
#
# # Regular Expression Pattern to recognise IPv4 addresses.
# ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
#
# # Get the address range to ARP
# while True:
#     ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
#     if ip_add_range_pattern.search(ip_add_range_entered):
#         print(f"{ip_add_range_entered} is a valid ip address range")
#         break
#
#
# # Try ARPing the ip address range supplied by the user.
# # The arping() method in scapy creates a pakcet with an ARP message
# # and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
# # If a valid ip address range was supplied the program will return
# # the list of all results.
# arp_result = scapy.arping(ip_add_range_entered)
#
# import numpy as np
# import imageio
# import cv2
# import scipy.ndimage
#
# img = r'C:\Users\tharu\PycharmProjects\python 100 days code\password-manager-start\download.jpg'
#
#
# def grayscale(rgb):
#     return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
#
#
# def dodge(front, back):
#     result = front * 255 / (255 - back)
#     result[result > 255] = 255
#     result[back == 255] = 255
#     return result.astype('uint8')
#
#
# s = imageio.imread(img)
# g = grayscale(s)
# i = 255 - 9
# b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
# r = dodge(b, g)

# import pywhatkit
#
# # for i in range(1000):
# #     pywhatkit.sendwhatmsg_instantly(f"+91{9080604358}",f"Whatsapp? {i} Thank you {i} time",)
# pywhatkit.search("tce")
# pywhatkit.text_to_handwriting(
#
#     "Please help me Please help me Please help me Please help me Please help me"
#     "Please help me Please help me Please help me Please help me Please help me"
#     "Please help me Please help me Please help me Please help me Please help me"
#     "Please help me Please help me Please help me Please help me Please help me"
#     "Please help me Please help me Please help me Please help me Please help me"
#     "Please help me Please help me Please help me Please help me Please help me"
#     ". The obverse shows a bootprint on the lunar surface, and the reverse (pictured), based on a well-known photo by Armstrong, depicts the visor of Aldrin's space suit, reflecting Armstrong, the U.S. flag and the Lunar Module Eagle. The depiction of Aldrin made him the seventh individual depicted on a U.S. coin to be alive at the time it was struck. The program was the most successful U.S. commemorative coin issue since the 2014 National Baseball Hall of Fame coins, with more than 600,000 Apollo 11 coins sold. The larger silver dollar won the Coin of the Year Award for 2019-dated issues. The obverse shows a bootprint on the lunar surface, and the reverse (pictured), based on a well-known photo by Armstrong, depicts the visor of Aldrin's space suit, reflecting Armstrong, the U.S. flag and the Lunar Module Eagle. The depiction of Aldrin made him the seventh individual depicted on a U.S. coin to be alive at the time it was struck. The program was the most successful U.S. commemorative coin issue since the 2014 National Baseball Hall of Fame coins, with more than 600,000 Apollo 11 coins sold. The larger silver dollar won the Coin of the Year Award for 2019-dated issues"
#
#     ,r"C:\Users\tharu\Dropbox\My PC (LAPTOP-DDCHP58Q)\Pictures\EVS\new.jpg", rgb=[255,69,0])


# from gtts import gTTS
# # pip install gtts
# from playsound import playsound
#
# # pip install playsound
# audio = 'speech.mp3'
# language = 'en'
# sp = gTTS(text=input("ENter to be audio:"),
#           lang=language, slow=False)
# sp.save(audio)
# playsound(audio)

# #===========================profile downloader================
# import instaloader
# bot = instaloader.Instaloader()
# username = "tharun"
# print(bot.download_profile(username,profile_pic_only=True))

