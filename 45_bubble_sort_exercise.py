#Bubble sort using python


def bubble_sort(data, key='name'):

    for i in data:
        print(i)

    for j in range(len(data) - 1):
        for i in range(1, len(data)):

            if data[i-1][key] > data[i][key]:
                tmp = data[i]
                data[i] = data[i-1]
                data[i-1] = tmp
    return data
            


# test_array = [ 76,23,45,12,345,657,98,34,44,23,534]
data = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

bubble_sort(data)
print()
for i in data:
    print(i)
# print("Sorted Array: ", bubble_sort(test_array))
# print(data[0]['transaction_amount'])