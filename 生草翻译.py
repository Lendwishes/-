start = int(0)
print("退出请在输入次数时输入小于等于1的数")
while start < 1:
    from googletrans import Translator
    import random
    trans = Translator(service_urls=['translate.google.cn'])
    xunhuan = int(1)
    userinput = str(input("翻译前文本："))
    times = int(input("请输入次数："))
    language = ['af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn', 'zh-tw', 'co','hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw', 'hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'he', ]
    if times <= 1:
        print("正在退出。。。")
        xunhuan = int(2)
        start = int(1)
    else:
        while xunhuan < times:
            print("正在执行第" + str(xunhuan) + "次翻译（共" + str(times) + "次）")
            xunhuan = xunhuan + 1
            result = str(trans.translate(userinput, dest=language[random.randint(0,104)]))
            resultlist = result.split(",")
            finallyresult1 = resultlist[2]
            output = finallyresult1.replace(" text=", "", 1)
            userinput = output
        print("正在执行第" + str(times) + "次翻译（共" + str(times) + "次）")
        result = trans.translate(userinput, dest="zh-cn")
        result = str(result)
        resultlist = result.split(",")
        finallyresult1 = resultlist[2]
        output = finallyresult1.replace(" text=", "", 1)
        userinput = output
        print("翻译完成，以下为最终结果\n==========\n" + output + "\n==========")