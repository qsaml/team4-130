from flask import Flask, render_template, request
from flask_table import Table, Col
import urllib.request
import json
import random
import queue

app = Flask(__name__)

@app.route('/')
def student():
	return render_template('index.html')

class ObjTable(Table):
	title_song = Col('Title of Song')
	singer = Col('Singer')

class Obj(object):
	def __init__(self, title_song, singer):
		self.title_song =  title_song
		self.singer = singer

class Singer:
	def __init__(self, name_singer, rate_singer):
		self.name_singer = name_singer
		self.rate_singer = rate_singer

class Song:
	def __init__(self, title_song, rate_song):
		self.title_song = title_song
		self.rate_song = rate_song

###############
class Stack:
	def __init__(self):
		self.items = []

def push(self,item):
	self.items.append(item)


def pop(self):
        return self.items.pop()

def size(self):
        return len(self.items)

def check_recent(self, victim):
        if victim in self.items:
            return True
        else: 
            return False
    
def print_items(self):
        for i in self.items:
            print(i)


#helper function for quicksort
def partition(list_song, start, end):
	i = (start-1)
	pivot=list_song[end][1].rate_song

	for j  in range(start, end):
		if list_song[j][1].rate_song <= pivot:
			i=i+1   #increment index
			list_song[i], list_song[j] = list_song[j], list_song[i]

	list_song[i+1], list_song[end] = list_Song[end], list_song[i+1]
	return (i+1)

###api part

#quicksort function
def quickSort(list_song, start, end):
	if start<end:
		p = partition(list_song, start, end)  #partition at index at aspecific point
		#sorting elemns before and after partition
		quickSort(list_song, start, p-1)
		quickSort(list_song, p+1, end)

def get_sorted_songs(list_song):
	res = []
	ordered_song=Stack()
	for song in list_song:
		ordered_song.push(song)
	for i, x in enumerate(list_Song):
		res.append(ordered_song.pop())

	return res

def sort_shuffle(list_song):
	queue_song=queue.Queue()
	added_recently=Stack()
	increment_count=0

	while(increment_count<20):
		end=(len(list_song)-1)
		print(end)
		rand_index=random.randint(0,end)
		print(rand_index)

		if added_recently.check_recent(list_song[rand_index][0].name_singer):
			increment_count=increment_count +1
			pass
		else:
			increment_count=0
			queue_song.put(list_song[rand_index])
			added_recently.push(list_song[rand_index][0].name_singer)
			list_song.remove(list_song[rand_index])
			added_recently.print_items()
			if added_recently.size()>4:
				added_recently.pop()

	while (len(list_song) != 0):
		end=(len(list_song)-1)
		rand_index=random.randint(0,end)
		queue_song.put(list_song[rand_index])
		list_song.remove(list_song[rand_index])

	list_final=[]
	while(queue_song.empty() != True):
		list_final.append(queue_song.get())

	for singer in list_final:
		print(singer[0].name_singer)
	print(len(list_final))

	return list_final

def table_generate(list_song):
	items=[]
	for song in list_song:
		items.append(Item(song[1].title_song, song[0].name_singer))

	#populating the table
	table = ObjTable(items)

	return table

def parse_multi_form(form):
    data = {}
    for url_k in form:
        v = form[url_k]
        ks = []
        while url_k:
            if '[' in url_k:
                k, r = url_k.split('[', 1)
                ks.append(k)
                if r[0] == ']':
                    ks.append('')
                url_k = r.replace(']', '', 1)
            else:
                ks.append(url_k)
                break
        sub_data = data
        for i, k in enumerate(ks):
            if k.isdigit():
                k = int(k)
            if i+1 < len(ks):
                if not isinstance(sub_data, dict):
                    break
                if k in sub_data:
                    sub_data = sub_data[k]
                else:
                    sub_data[k] = {}
                    sub_data = sub_data[k]
            else:
                if isinstance(sub_data, dict):
                    sub_data[k] = v
    data_l = []
    for key, val in data.items(): 
        data_l.append(val)


list_singer=[]
for i in range(0,10):
	singer=data_l[0][i]
	processed_text=singer.replace(" ", "")
	list_singer.append(singer)

info_singer=[]
for value in form.items():
	info_singer.append(value)
print(info_singer)

ratings_singer=[]
for value in info_singer:
	if value[1].isdigit():
		ratings_singer.append(value[1])
print(ratings_singer)

list_info=[]
for i, singer in enumerate(list_singer):
	#line 214 api part
	#line 215 ^

result = []

sorted_songs = list_info.copy()
shuffled = list_info.copy()

end=len(sorted_songs)-1
quickSort(sorted_songs, 0, end)

shuffled = shuffle_sort(shuffled)

temp = get_sorted_songs(sorted_Songs)
table_sorted = table_generate(temp)
table_shuffled = table_generate(shuffled)

result.append(table_sorted)
result.append(table_shuffled)

return result


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = parse_multi_form(request.form)
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)



