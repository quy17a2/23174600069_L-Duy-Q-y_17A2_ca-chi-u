# Tạo từ điển inventory ban đầu
inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# Thêm key 'pocket' vào từ điển và gán giá trị là một danh sách
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sắp xếp các phần tử trong key 'backpack'
inventory['backpack'].sort()

# Loại bỏ phần tử 'dagger' khỏi key 'backpack'
inventory['backpack'].remove('dagger')

# Thêm 50 vào giá trị của key 'gold'
inventory['gold'] += 50

# In ra kết quả
print(inventory)
