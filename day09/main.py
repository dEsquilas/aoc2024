from collections import deque

def get_disk(filename):
	ddraw = open(filename).read().strip()

	# (id, size, space)
	dd = deque()
	id = 0

	for i in range(0, len(ddraw), 2):
		size = int(ddraw[i])
		space = int(ddraw[i + 1]) if i + 1 < len(ddraw) else 0
		dd.append((id, size, space))
		id += 1

	return dd

def day_9_p1(filename):

	dd = get_disk(filename)
	compact = deque()

	while dd:
		current_cluster = dd.popleft()
		current_cluster_id = current_cluster[0]
		current_cluster_size = current_cluster[1]
		remaining_space = current_cluster[2]

		compact.append((current_cluster_id, current_cluster_size, 0))

		while remaining_space > 0 and dd:
			last_cluster = dd.pop()
			last_cluster_id = last_cluster[0]
			last_cluster_size = last_cluster[1]
			last_cluster_space = last_cluster[2]

			if last_cluster_size <= remaining_space:
				compact.append((last_cluster_id, last_cluster_size, 0))
				remaining_space -= last_cluster_size
			else:
				new_cluster_id = last_cluster_id
				new_cluster_size = remaining_space
				new_cluster_space = 0

				compact.append((new_cluster_id, new_cluster_size, 0))

				re_add_cluster_id = last_cluster_id
				re_add_cluster_size = last_cluster_size - remaining_space
				re_add_cluster_space = last_cluster_space

				remaining_space = 0

				dd.append((re_add_cluster_id, re_add_cluster_size, re_add_cluster_space))


	pos = 0
	t = 0
	for cluster in compact:
		for i in range(cluster[1]):
			t += cluster[0] * pos
			pos += 1

	return t

# def day_9_p2(filename):
#
# 	compact = get_disk(filename)
#
# 	while not check_try_to_moved_all(compact):
#
#
# 		p = get_last_index_not_tried_to_move(compact)
# 		print(p)
#
# 		if p == -1:
# 			for c in compact:
# 				if not c[3]:
# 					print("Not moved", c)
# 			#print(compact)
# 			break
#
# 		if compact[p][3]:
# 			continue
#
# 		compact[p][3] = True
#
# 		for k in range(len(compact)):
#
# 			#print("Checking", compact[p], "with", compact[k])
#
# 			if k >= p:
# 				continue
#
# 			if compact[p][1] <= compact[k][2]:
#
# 				#print("Size found on", compact[k])
#
# 				cluster_to_move = compact[p]
# 				cluster_to_fill = compact[k]
#
# 				initial_space = cluster_to_fill[2]
# 				index_to_remove = compact.index(cluster_to_move)
# 				compact.pop(index_to_remove)
# 				compact[index_to_remove-1][2] += cluster_to_move[1] + cluster_to_move[2]
#
# 				cluster_to_fill[2] = 0
# 				cluster_to_move[2] = initial_space - cluster_to_move[1]
#
# 				compact.insert(k+1, cluster_to_move)
#
# 				break
#
#
#
# 		#debug(compact)
#
# 	t = 0
# 	pos = 0
# 	for cluster in compact:
# 		print(cluster)
# 		for i in range(cluster[1]):
# 			t += cluster[0] * pos
# 			pos += 1
# 		for i in range(cluster[2]):
# 			pos += 1
#
# 	return t


# def day_9_p2(filename):
#
# 	compact = get_disk(filename)
# 	Q = deque(reversed(compact))
#
# 	while Q:
#
# 		current = Q.popleft()
# 		index_to_move = compact.index(current)
# 	#	print("\t\t\t\t\t\t\t\t", current)
#
# 		#print(len(compact))
#
# 		for (index, c) in enumerate(compact):
#
# 			if index_to_move < index:
# 				break
#
# 			if current == c:
# 				continue
#
# 			if c[2] >= current[1]:
# 				space_left = c[2]
# 				c[2] = 0
#
# 				updated_current = compact[index_to_move]
#
# 				compact[index_to_move - 1][2] += updated_current[1] + updated_current[2]
#
# 				compact.remove(current)
# 				updated_current[2] = space_left - updated_current[1]
# 				updated_current[3] = True
#
# 				compact.insert(index+1, updated_current)
# 				break
# 	#	debug(compact)
#
# 	t = 0
# 	pos = 0
# 	for cluster in compact:
# 		print(cluster)
# 		for i in range(cluster[1]):
# 			t += cluster[0] * pos
# 			pos += 1
# 		pos += cluster[2]
#
# 	#print(t)
#
# 	return t
#
# def get_used_space(disk):
#
# 	t = 0
# 	for c in disk:
# 		t += c[1] + c[2]
#
# 	return t
#
#
#
# def check_try_to_moved_all(compact):
# 	print("r")
# 	for c in compact:
# 		if not c[3]:
# 			return False
#
# 	print('k')
# 	return True
#
# def get_last_index_not_tried_to_move(compact):
# 	for i in range(len(compact)-1, -1, -1):
# 		if not compact[i][3]:
# 			return i
#
# 	return False
#
#

#
#
# def has_all_ids(disk):
#
# 	for i in range(len(disk)-1):
# 		found = False
# 		for c in disk:
# 			if c[0] == i:
# 				found = True
# 				break
# 		if not found:
# 			print(i, " NOT FOUND")
# 			exit()

def load_disk(fileinput):

	content = open(fileinput).read()
	disk = []

	id = 0

	for i in range(len(content)):
		if i % 2 == 1:
			continue

		for _ in range(int(content[i])):
			disk.append(id)

		if len(content) > i + 1:
			for _ in range(int(content[i+1])):
				disk.append(".")

		id += 1

	return disk


def day_9_p2(fileinput):


	disk = load_disk(fileinput)

	ids_try_to_move = set()

	# debug2(disk)
	# print("")

	for offset in reversed(range(len(disk))):

		if disk[offset] in ids_try_to_move or disk[offset] == ".":
			continue

		# when starts, included
		# when ends, not included

		offset_end = offset + 1
		current_id = disk[offset]
		offset_start = -1

		if disk[offset] != ".":
			ids_try_to_move.add(current_id)

		for x in reversed(range(offset_end)):
			if disk[x] == current_id:
				offset_start = x
			else:
				break

		required_space = offset_end - offset_start
		offset_space_start = -1

		current_space = 0
		for x in range(len(disk)):

			if x >= offset_start:
				break

			if disk[x] == ".":
				if current_space == 0:
					offset_space_start = x
				current_space += 1
			else:
				offset_space_start = -1
				current_space = 0

			if current_space >= required_space:

				for j in range(offset_space_start, offset_space_start + required_space):
					disk[j] = current_id

				for j in range(offset_start, offset_end):
					disk[j] = "."
				break
	t = 0

	for _ in range(len(disk)):
		if disk[_] != ".":
			t += disk[_] * _

	return t


def debug2(disk):
	for _ in range(len(disk)):
		print(disk[_], end="")

def debug(dd):
	for d in dd:
		id = d[0]
		size = d[1]
		space = d[2]

		for i in range(size):
			print(id, end="")
		for i in range(space):
			print(".", end="")

	print("")

def test_day_9():
	assert day_9_p1("test.txt") == 1928
	assert day_9_p2("test.txt") == 2858

test_day_9()

p1 = day_9_p1("input.txt")
p2 = day_9_p2("input.txt")
print("Part 1: ", p1)
print("Part 2: ", p2)