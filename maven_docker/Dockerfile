# Step 1: Use the official Maven image to build the application
FROM maven:latest AS build

# Set the working directory inside the container
WORKDIR /app

# Copy the pom.xml and source code into the container
COPY pom.xml ./
COPY src ./src
COPY target ./target
# Run Maven to build the application
RUN mvn clean install -DskipTests

# Step 2: Use the official OpenJDK image to run the application
FROM openjdk:17-jdk-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the jar file from the Maven build step
COPY target/hello-world-1.0-SNAPSHOT.jar /app/hello-world-1.0-SNAPSHOT.jar

# Expose the port your app will run on (adjust if needed)
EXPOSE 8080

# Command to run the application
CMD ["java", "-jar", "hello-world-1.0-SNAPSHOT.jar"]


