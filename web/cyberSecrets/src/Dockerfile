FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY index.html /usr/share/nginx/html/

# COPY logo.png /usr/share/nginx/html/

EXPOSE 5000

CMD ["nginx", "-g", "daemon off;"]