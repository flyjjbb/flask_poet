FROM python:slim-bookworm

COPY . /root/files
# 使用国内安装源，加快下载速度
RUN mv /root/files/debian.sources /etc/apt/sources.list.d/debian.sources; \
apt update; \
# 安装认证中心、语言设置工具和fortunes中文库
apt install -y ca-certificates locales net-tools fortunes-zh; \
# 设置中文语言支持环境
localedef -c -f UTF-8 -i zh_CN zh_CN.utf8; \
# 整理中文数据库，只保留和生成唐诗宋词
rm /usr/share/games/fortunes/chinese*

# 中文环境变量
ENV LANG="zh_CN.UTF-8" LANGUAGE="zh_CN:zh"  LC_ALL="zh_CN.UTF-8"

# 使用国内安装源，加快pip下载安装速度
WORKDIR /code
RUN mv /root/files/pip.conf /etc/pip.conf; \
mv /root/files/requirements.txt requirements.txt; \
pip install -r requirements.txt

CMD ["flask", "run"]
