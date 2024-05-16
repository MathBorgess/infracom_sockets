#include <iostream>

#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <errno.h>

#include <thread>

int handleClient(int clientSocket)
{
    char buffer[2048] = {0};
    recv(clientSocket, buffer, sizeof(buffer), 0);
    std::cout << "Message from client: " << buffer << std::endl;
    std::string msgHeader = "HTTP/1.1 200 OK\r\nDate: Tue, 09 Aug 2022 13:23:35 GMT\r\nServer: MyServer/0.0.1 (Ubuntu)\r\nContent-Type: text/html\r\n\r\n";
    std::string msgBody = "<html><head><title>Hello, World</title></head><body><h1> Your first web server!</h1><h3>Congratulation!!</h3></body></html>";
    const void *msg = (msgHeader + msgBody).c_str();
    send(clientSocket, msg, sizeof(msg), 0);
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
        // t->join();
        arr[len] = t;
        len++;
    }
    for (int i = 0; i < len; i++)
    {
        arr[i]->join();
    }
    return 0;
}