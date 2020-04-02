from fabric import Connection


fab_client = Connection(
        "root@49.232.47.246", connect_kwargs={"password": "Fhz&4546660"})  # 如果配置了免密， connect_kwargs可不写密码


# 上传文件
# fab_client.put('myfiles.tgz', '/opt/mydata')

# 执行命令
# fab_client.run('tar -C /opt/mydata -xzvf /opt/mydata/myfiles.tgz')

def fetch_blog():
    with fab_client.cd('/data/bolg/python-learnning/'):
        git = fab_client.run("git stash && git pull -r  origin master && git stash pop", hide=True)
        print(git.stdout.strip())
        fab_client.run("mkdocs build --clean")


if __name__ == "__main__":
    fetch_blog()
