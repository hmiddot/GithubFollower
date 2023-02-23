import requests

j = 1
i = 1
print("Welcome to GithubFollower V.0.1")
print("To Start Following Create a Github access-token")
username = "hmddrz"
access_token = "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"
user_to_follow_followers = "facebook"


def follow():
    global i
    global j
    global username
    global user_to_follow_followers
    headers = {
        "Authorization": f"token " + access_token,
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(
        f"https://api.github.com/users/" + user_to_follow_followers + "/followers?per_page=100&page=" + str(j),
        headers=headers)
    if response.status_code == 200:
        followers = response.json()
        for follower in followers:
            z = str(i + (j - 1) * 100) + "."
            response = requests.get(f"https://api.github.com/user/following/" + follower['login'] + "", headers=headers)
            if response.status_code == 204:
                print(z + f"You are already following " + follower['login'] + "!")
            elif response.status_code == 404:
                response = requests.put(f"https://api.github.com/user/following/" + follower['login'] + "",
                                        headers=headers)
                if response.status_code == 204:
                    print(z + f"You are now following " + follower['login'] + "!")
                else:
                    print(z + f"Failed to follow " + follower['login'] + ".")
            else:
                print(z + f"Failed to check if you are following " + follower['login'] + ".")
            i += 1
            if i == 101:
                i -= 100
                j += 1
                follow()
    else:
        print(f"Failed to retrieve followers for " + user_to_follow_followers + ".")


follow()
print('Following Ended Successfully !')
