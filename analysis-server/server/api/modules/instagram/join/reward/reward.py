import server.secret.config as config
from .reward_user import reward_user
from .reward_post import reward_post
from .reward_prev import reward_maintain
from .reward_prev import reward_er


class JoinReward:
    def __init__(self, join_collection_list, pk):
        self.join_collection_list = join_collection_list
        self.pk = pk

    @staticmethod
    def get_reward_point(join_collection) -> int:
        user_point = reward_user(join_collection['join_user']['follow_count']) * config.InstagramReward.CONSTANT_USER

        hashtag_list = []
        for hashtag_hashtag in join_collection['event']['hashtag']['hashtag_hashtags']:
            hashtag_list.append(hashtag_hashtag['hashtags'])
        post_point = reward_post(join_collection['hashtags'], hashtag_list)

        maintain_point = reward_maintain(join_collection['upload_date'],
                                         join_collection['delete_date']) * config.InstagramReward.CONSTANT_PREV

        er_point = reward_er(join_collection['like_count'], join_collection['comment_count']) * config.InstagramReward.CONSTANT_PREV

        reward_point = post_point + user_point + maintain_point + er_point

        return reward_point

    def get_reward_point_dict(self) -> dict:
        reward_point_dict = {}
        for join_collection in self.join_collection_list:
            reward_point_dict[join_collection['id']] = self.get_reward_point(join_collection)
        return reward_point_dict

    def get_reward_rate_list(self):
        reward_rate_list = []
        reward_count_sum = 0
        for item in self.join_collection_list:
            # print(item['event'])
            print(item['event']['rewards'])
            if item['id'] == self.pk:
                for event_rewards in item['event']['event_rewards']:
                    reward_rate_list.append(event_rewards['rewards']['count'])
                    reward_count_sum += event_rewards['rewards']['count']

        for key, val in enumerate(reward_rate_list):
            reward_rate_list[key] = val / reward_count_sum

        return reward_rate_list

    def get_reward_point_rate(self):
        reward_point_dict = self.get_reward_point_dict()
        reward_point_list = []

        for key, val in reward_point_dict.items():
            reward_point_list.append(val)

        reward_point_list.sort()
        reward_point_rate = 0
        cnt = 0
        for key, val in reward_point_dict.items():
            cnt += 1
            if key == self.pk:
                reward_point_rate = 1 - (reward_point_list.index(val) + 1) / len(reward_point_dict)
        print(reward_point_dict)
        return reward_point_rate

    def get_reward_level(self) -> int:
        reward_rate_list = self.get_reward_rate_list()
        reward_point_rate = self.get_reward_point_rate()

        reward_level = 1
        for key, val in enumerate(reward_rate_list):
            if val > reward_point_rate:
                reward_level = key + 1

        print(reward_rate_list)
        print(reward_point_rate)
        print(reward_level)
        return reward_level



