# serialization
bfs_order = ['1', '2', '3', '#', '#', '5']
print(','.join(bfs_order))
print("[%s]" % ','.join(bfs_order))    # "[1,2,3,#,#,5]" <class 'str'>

# deserialization
data = "[%s]" % ','.join(bfs_order)
print(data[1:-1].split(','))    # ['1', '2', '3', '#', '#', '5'] <class 'list'>

