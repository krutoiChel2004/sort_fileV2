def create_file(name_f, n, path):
    for i in range(n):
        my_file = open(f"{path}//{name_f+str(i)}.txt", "w")
        my_file.close()
