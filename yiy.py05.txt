

def insect1():#這是宏與醫療器材店的電話
    import urllib.request as req
    url = "https://www.omronhealthcare.com.tw/location/ins.php?index_id=2009"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("div", class_="Txt").text.replace("(瀏覽地圖)","").replace("區域：新北市板橋區　　類別：醫療器材","").replace("地址：新北市板橋區南雅南路2段134號1樓","").strip()
    return titles
#print(insect1())

def insect2():#杏一醫療器材店電話
    import urllib.request as req
    url = "https://www.google.com/search?q=%E6%9D%8F%E4%B8%80%E9%86%AB%E7%99%82%E5%99%A8%E6%9D%90%E5%BA%97%20%E4%BA%9E%E6%9D%B1%E5%88%86%E5%BA%97&sxsrf=AOaemvJ5bkCCIJWvRa9d9RhH7NpJZ_V6XA:1632115572723&ei=rRpIYaGmMpmLr7wP8ouDmAI&oq=%E6%9D%8F%E4%B8%80%E9%86%AB%E7%99%82%E5%99%A8%E6%9D%90%E5%BA%97+&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzoHCCMQsAMQJ0oECEEYAVChR1ihR2CLVGgBcAB4AIABUogBUpIBATGYAQCgAQHIAQPAAQE&sclient=gws-wiz&tbs=lf:1,lf_ui:4&tbm=lcl&rflfq=1&num=10&rldimm=4871600551970665464&lqi=CiLmnY_kuIDphqvnmYLlmajmnZDlupcg5Lqe5p2x5YiG5bqXIgOIAQFaIyIh5p2PIOS4gCDphqvnmYIg5Zmo5p2QIOW6lyDkup4g5p2xkgEUbWVkaWNhbF9zdXBwbHlfc3RvcmWqASEQASodIhnmnY8g5LiAIOmGq-eZgiDlmajmnZAg5bqXKEU&ved=2ahUKEwie3Man6IzzAhXAG7kGHUajAH4QvS56BAgPECc&rlst=f#rlfi=hd:;si:4871600551970665464,l,CiLmnY_kuIDphqvnmYLlmajmnZDlupcg5Lqe5p2x5YiG5bqXIgOIAQFaIyIh5p2PIOS4gCDphqvnmYIg5Zmo5p2QIOW6lyDkup4g5p2xkgEUbWVkaWNhbF9zdXBwbHlfc3RvcmWqASEQASodIhnmnY8g5LiAIOmGq-eZgiDlmajmnZAg5bqXKEU;mv:[[24.997280300000003,121.45296080000001],[24.996976699999998,121.45193669999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titlesa=root.find("div", class_="rllt__details").text.replace("Banqiao District, New Taipei City, Taiwan · +886 2 ","").replace("Open ⋅ Closes 10PMIn-store shopping","")#.strip()
    return "02 " + titlesa
#print(insect2())
def insect3():#這是台灣確診數
    import urllib.request as req
    url = "https://covid-19.nchc.org.tw/"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("div", class_="col-lg-3 col-sm-6 col-6 text-center my-5").text.replace("\n","").strip().replace("累計確診","累計確診數:").replace("本土病例","\n本土病例數:")
    return "\n" + titles
def insect4():#疫情資訊標題
    import urllib.request as req
    url = "https://covid-19.nchc.org.tw/"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("div", class_="col-lg-12 main").text.strip().replace("More","").replace("\n","").replace("Updated on","更新時間:").replace("UTC +8","").replace("[","\n[").replace("更","\n更")
    return titles 
def insect5():#今日新增病例
    import urllib.request as req
    url = "https://event.gvm.com.tw/202003_COVID-19/"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("div", class_="data_box col-lg-3 col-5").text.strip().replace("\n","")
    return  titles +"例\n"
#print(insect5())
def insect6():#今日新增病例的標題
    import urllib.request as req
    url = "https://event.gvm.com.tw/202003_COVID-19/"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find("p").text.strip()#.replace("\n","").replace("From","資料來源:").replace("Last updated","\n資料更新時間").replace("days","天").replace("day","天").replace("hours","小時").replace("hour","小時").replace("minutes","分鐘").replace("minute","分鐘").replace("ago","前")
    return  titles

print(insect6())