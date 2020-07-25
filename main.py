from googletrans import Translator
xunhuan = int(1)
userinput = str(input("翻译前文本："))
language = ['none', 'ja', 'fr', 'co', 'ht', 'hmn', 'ig', 'kk', 'ms', 'gl', 'mg', 'pl', 'es', 'sw', 'xh', 'zu', 'am', 'pt', 'ne', 'my', 'zh-cn']
while xunhuan < 20:
    print("正在执行第" + str(xunhuan) + "次翻译（共20次）")
    xunhuan = xunhuan + 1
    trans = Translator(service_urls=['translate.google.cn'])
    result = trans.translate(userinput, dest=language[xunhuan%len(language)])
    result = str(result)
    resultlist = result.split(",")
    finallyresult1 = resultlist[2]
    output = finallyresult1.replace(" text=", "", 1)
    userinput = output
print("翻译完成，以下为最终结果\n==========\n" + output + "\n==========")