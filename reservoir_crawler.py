def reservoir_crawler(msg):
    url  = "https://www.taiwanstat.com/waters/latest"
    re   = requests.get(url)
    data = re.json()
    data = data[0]

    reservoir = []
    # ���w�W��
    for d in data:
        reservoir.append(d)

    for r in reservoir:
        if msg in reservoir:
            name = data[str(msg)]["name"]
            volu = data[str(msg)]["volumn"]
            perc = data[str(msg)]["percentage"]
        else:
            continue

    content = ""
    content += f"�W��: {name}\n�W���ʤ���: {perc}%\n���ĻW���q: {volu}"

    return content