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

with open("times.txt", "w") as f:
    f.write(str(user_time_messages))
