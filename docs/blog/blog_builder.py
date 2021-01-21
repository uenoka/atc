import os


def read_blogs():
    article_path = "./docs/blog/"
    file_list = os.listdir(article_path)
    titles = []
    for file in file_list:
        if file.count("md"):
            # read articles
            # get title
            # add title to title list
            file_content = open(article_path + file, encoding='utf-8')
            contents = file_content.readlines()
            for line in contents:
                if line.count("title") > 0:
                    title_name = (line.splitlines()[0].split(":")[1], file)
                    titles.append(title_name)
                    break
    return titles


def write_index(blogs):
    index_path = "./docs/index.md"
    os.remove(index_path)  # 削除
    index = open(index_path, mode='x', encoding='utf-8')
    index.write('---\r\n')
    index.write('title: "index"\r\n')
    index.write('---\r\n')
    index.write('## このリポジトリは\r\n')
    index.write('競技プログラミングに参加した記録や、学んだアルゴリズム・データ構造についての記事を記録していきます。\r\n')
    index.write('\r\n')
    for blog in blogs:
        index.write('['+blog[0]+']'+'(blog/'+blog[1][:-3]+')\r\n')


blogs = read_blogs()
write_index(blogs)
