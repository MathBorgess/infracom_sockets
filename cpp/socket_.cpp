#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <thread>

int handleClient(int clientSocket)
{
    for (int i = 0; i < 3; i++)
    {
        char buffer[1024] = {0};
        recv(clientSocket, buffer, sizeof(buffer), 0);
        std::cout << "Message from client: " << buffer << std::endl;

        send(clientSocket, "Hello World from CPP", sizeof("Hello World from CPP"), 0);
    }
    close(clientSocket);
    return 0;
}

int main()
{
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in serverAddress;
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8000);
    serverAddress.sin_addr.s_addr = INADDR_ANY;

    bind(serverSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress));

    listen(serverSocket, 5);
    std::thread **arr = new std::thread *[5];
    int len = 0;

    while (true)
    {
        int clientSocket = accept(serverSocket, nullptr, nullptr);
        std::thread *t = new std::thread(handleClient, clientSocket);
        arr[len] = t;
        len++;
    }
    for (int i = 0; i < len; i++)
    {
        arr[i]->join();
    }
    return 0;
}