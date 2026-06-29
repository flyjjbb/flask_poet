FROM python:3-slim

# 使用国内安装源，加快下载速度
RUN cp -f /etc/apt/sources.list.d/debian.sources /etc/apt/sources.list.d/debian.sources.bak; \
sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources; \
echo "install mirrors.aliyun.com...done"; \
apt update; \
# 安装认证中心、语言设置工具和fortunes中文库
apt install -y ca-certificates locales net-tools fortunes-zh; \
# 设置中文语言支持环境
localedef -c -f UTF-8 -i zh_CN zh_CN.utf8; \
# 整理中文数据库，只保留和生成唐诗宋词
rm /usr/share/games/fortunes/chinese*; \
mkdir -p /app

# 中文环境变量
ENV LANG="zh_CN.UTF-8" LANGUAGE="zh_CN:zh"  LC_ALL="zh_CN.UTF-8"

# 使用国内安装源，加快pip下载安装速度
COPY --chown=root:users --chmod=644 ./pip.conf /etc/pip.conf

# 部署服务
WORKDIR /app
COPY --chown=root:users --chmod=644 ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

#CMD ["flask", "run"]
