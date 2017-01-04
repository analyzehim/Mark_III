import requests
import json
SIZE = 20
offset = 0


def vk_ping(VK_TOKEN):
    r = requests.get('https://api.vk.com/method/messages.get?out=18&count=' +
                             str(SIZE) + '&offset=' + str(offset) + '&out=0' +
                             '&access_token=' + VK_TOKEN)
    ans = json.loads(r.content)
    print ans, type(ans)
    return ans


    '''

            if ans['response'][1]['read_state'] != 1:
                return ans
    except:
        pass
    '''
