import json

print('---str to dict------------')
nw='{"no":1,"name":"banner","budget":3000,"media":"網路"}'  #string
print(type(nw)) #<class 'str'>

nwInfo=json.loads(nw)
print(type(nwInfo)) #<class 'dict'>

print("\n-----走訪----------------")
for k in nwInfo:
    print(k,'->',nwInfo.get(k))

print('---dict to str------------')
nw2={"no":1,"name":"banner","budget":3000,"media":"網路"}
print(type(nw2))    #<class 'dict'>
print(nw2)

nwInfo2=json.dumps(nw2)
print(type(nwInfo2))    #<class 'str'>
print(nwInfo2)

#讀取suppliers.json, 輸出,encoding='utf-8'
print("\n---read JSON File------------------------")
with open('.\\sample\suppliers.json','r',encoding='utf-8') as rf:
    print(rf)
    print('----------------------')
    suppliers=json.load(rf)
    print(suppliers)
    print(type(suppliers))#<class 'list'>

print('\n----走訪suppliers-----------------')
for e in suppliers:
    #print(e)
    for ee in e:
        #print(ee,'->',e.get(ee))
        print(f'{ee}->{e.get(ee)}\t',end='')
    print()


