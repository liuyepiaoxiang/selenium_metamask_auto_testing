import time
import wallet
import zkSync2_run_test as zkSync
import muteSwitch_run_test as muteSwitch

filename = 'address.xlsx'
address_list = wallet.getAddress(filename)
result = open('./result.txt', mode='a', encoding='utf-8')
for i in range(1, 1001):
    address = address_list[i]
    try:
        zkSync.runTest(filename, address)
        time.sleep(3)
        muteSwitch.runMuteSwitchTestnet(filename, address)
        time.sleep(3)
    except Exception as e:
        print(e)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行失败")
        print(address + " run test failed", file=result)
        continue
    else:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 第" + str(i) + "次执行成功")
        print(address + " run test success", file=result)
