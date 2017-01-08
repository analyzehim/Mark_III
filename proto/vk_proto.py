import requests
import json
SIZE = 20
offset = 0

class VkMessage:
    def __init__(self, mes_json):
        self.body = mes_json['body'].encode('utf8')
        self.read_state = mes_json["read_state"]
        self.date = mes_json["date"]
        self.author = mes_json["uid"]

    def __str__(self):
        return self.body

    def __len__(self):
        return len(self.body)

class VkUser:
    def __init__(self, mes_json):
        self.last_name = mes_json['last_name']
        self.first_name = mes_json["first_name"]
        self.uid = mes_json["uid"]
        try:
            self.bdate = mes_json["bdate"]
        except:
            pass

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

def vk_getuserslist(VK_TOKEN, id_list):
    r = requests.get('https://api.vk.com/method/users.get?out=18&user_ids=' +
                             str(id_list)[1:-1] + '&fields=bdate' +
                             '&access_token=' + VK_TOKEN)
    ans = json.loads(r.content)
    users_list = []
    for line in ans["response"]:
        users_list.append(VkUser(line))
    return users_list

def vk_getfriendlist(VK_TOKEN, user_id):

    r = requests.get('https://api.vk.com/method/friends.get?out=18' +
                     '&user_id={0}'.format(user_id) +
                     '&orders=hints' +
                     '&fields=bdate' +
                     '&access_token={0}'.format(VK_TOKEN))
    ans = json.loads(r.content)
    friends_list = []
    for line in ans["response"]:
        friends_list.append(VkUser(line))
    return friends_list




def vk_ping(VK_TOKEN):
    r = requests.get('https://api.vk.com/method/messages.get?out=18&count=' +
                             str(SIZE) + '&offset=' + str(offset) + '&out=0' +
                             '&access_token=' + VK_TOKEN)
    ans = json.loads(r.content)
    print ans, type(ans)
    return ans


def vk_getmeslist(VK_TOKEN, SIZE):
        r = requests.get('https://api.vk.com/method/messages.get?out=18&count=' +
                         str(SIZE) + '&offset=' + str(0) + '&out=0' +
                         '&access_token=' + VK_TOKEN)
        ans = json.loads(r.content)
        mes_list = []
        for line in ans["response"][1:]:
            mes = VkMessage(line)
            mes_list.append(mes)
        return mes_list


def vk_checklist(mes_list):
    return mes_list[:2]
