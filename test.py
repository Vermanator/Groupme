import girth_puller
import json
import collector
import sys
messages = collector.get_messages()
favorites_received = collector.get_fav_rec()
favorites_given = collector.get_fav_giv()
user_count = collector.get_user_count()
users = collector.get_users()
user_favorites = collector.get_user_fav()
user_time_messages = collector.get_user_time()
name = collector.get_name()
sys.stdout.reconfigure(encoding='utf-8')
new_user_times = {}
with open("times.txt", "w") as f:
    for user_id in user_time_messages:
        new_user_times[users[user_id]] = user_time_messages[user_id]
    f.write(str(new_user_times))
