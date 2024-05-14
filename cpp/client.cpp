#include <iostream>
#include <sys/socket.h>
#include <string>
#include <netinet/in.h>

int main()
{
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8000);
    serverAddress.sin_addr.s_addr = INADDR_ANY;

    connect(clientSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress));

    std::string message = "Hello from CPP client";
    const char *msgChar = message.c_str();
    for (int i = 0; i < 3; i++)
    {
        send(clientSocket, msgChar, sizeof(msgChar), 0);

        char buffer[1024] = {0};
        recv(clientSocket, buffer, sizeof(buffer), 0);

        std::cout << "Message from server: " << buffer << std::endl;
    }
    close(clientSocket);

    return 0;
}