import collector
with open(file_name,'a', encoding='utf-8') as outfile:
    outfile.seek(0)
    outfile.truncate()
    outfile.write("\n" + "Favortes Given" + "\n")
    for key in favorites_given:
        outfile.write(users[key] + " " + str(favorites_given[key]) +"\n")
    outfile.write("\n" + "Favorites Received" + "\n")
    for key in favorites_received:
        outfile.write(users[key] + " " + str(favorites_received[key]) +"\n")
    outfile.write("\n" + "Ratio" + "\n")
    for key in favorites_received:
        if not (user_count[key] == 0):
            outfile.write(users[key] + " " + str(float(favorites_received[key])/float(user_count[key])) +"\n")
    outfile.write("\n" + "Messages sent" + "\n")
    for key in user_count:
        outfile.write(users[key] + " " + str(user_count[key]) +"\n")
    outfile.write("\n" + "Favorites by person" + "\n")
    for key in user_favorites:
        outfile.write("\n" +  "USER: " + users[key] +"\n")
        for key2 in user_favorites[key]:
            outfile.write(users[key2] + " " + str(user_favorites[key][key2]) +"\n")
print("done")

x = []
ratio = []
names = []
counter = 1
for key in favorites_received:
        if not (user_count[key] == 0):
            x.append(counter)
            counter = counter + 1
            ratio.append(round(float(favorites_given[key])/float(favorites_received[key]),3))
            names.append(users[key])
names = [x for _,x in sorted(zip(ratio,names),reverse=True)]
fig = plt.figure()
ax = fig.add_subplot(111)
print(names)
ratio = sorted(ratio,reverse=True)
print(ratio)

# plotting the points  
plt.bar(x, ratio, tick_label = names, width = .6, color = ['red','blue']) 
rects = ax.patches
# Make some labels.

for rect, rat in zip(rects, ratio):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height + .3, rat,
            ha='center', va='bottom')
# naming the x axis 
plt.xlabel('Nicknames') 
# naming the y axis 
plt.ylabel('Ratio') 
plt.xticks(x,names,rotation=90)
# giving a title to my graph 
plt.title('Likes Given over Likes Received') 
# Set the x-axis limit
plt.savefig('totallikesratio.jpg',bbox_inches = 'tight')
# function to show the plot 
plt.show() 

import matplotlib.pyplot as plt
x = []

likes = []
names = []
i = 1
plt.subplots_adjust(wspace = .5)
plt.rcParams.update({'font.size': 22})
fig = plt.gcf()
fig.set_size_inches(100.5, 100.5)
for key in user_favorites:
    likes = []
    names = []
    ax = plt.subplot(5,6,i)
    ax.title.set_text(users[key] + " Likes Given " + str(favorites_received[key]))
    for key2 in user_favorites[key]:
            if(isinstance(user_favorites[key][key2],int)):
                if(not favorites_received[key] == 0):
                    likes.append(user_favorites[key][key2]/favorites_received[key])
                    names.append(users[key2] + ' ' + str(user_favorites[key][key2]))
    i = i + 1
    ax.pie(likes, labels=names, autopct='%.0f%%',
        shadow=True, radius = 10000000, startangle=90)
    ax.axis('equal') 

print(names)
print(likes)
#plt.savefig('totallikesratio.jpg',bbox_inches = 'tight')
# function to show the plot 
plt.savefig('likesreceived.pdf',bbox_inches = 'tight')
plt.show() 