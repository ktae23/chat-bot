import pickle

f = open('setting.txt', 'wb')
try:
    setting = [ {'title' : 'pyton program'}, {'author' : 'kei'}]
    pickle.dump(setting, f)
except Exception as e:
    print(e)
finally:
    f.close()
