# Use official Nginx image
FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

# Copy your website files into Nginx web directory
COPY . /usr/share/nginx/html

# Expose port 80
EXPOSE 80
