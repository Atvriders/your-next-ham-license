FROM nginx:alpine

COPY build/index.html /usr/share/nginx/html/index.html
COPY build/your-next-ham-license.txt build/your-next-ham-license.pdf /usr/share/nginx/html/
COPY build/practice.html build/flashcards.html /usr/share/nginx/html/
COPY chapters/ /usr/share/nginx/html/chapters/
COPY audiobook/ /usr/share/nginx/html/audiobook/
COPY docker/audiobook-index.html /usr/share/nginx/html/audiobook/index.html
