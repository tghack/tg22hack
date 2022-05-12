#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <pthread.h>

void *conn_handler(void *);
int main()
{
	int socket_desc, client_sock, c, *new_sock;
	struct sockaddr_in server, client;

	// Create socket
	socket_desc = socket(AF_INET, SOCK_STREAM, 0);
	if(socket_desc == -1)
	{
		printf("Could not create socket!\n");
		exit(1);
	}
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(5000);

	if (bind(socket_desc, (struct sockaddr *)&server, sizeof(server)) < 0)
	{
		printf("Could not bind to interface");
		exit(1);
	}
	listen(socket_desc, 3);
	printf("Waiting for incomming connections...\n");
	c = sizeof(struct sockaddr_in);

	while((client_sock = accept(socket_desc, (struct sockaddr*)&client, (socklen_t*)&c)))
	{
		printf("Got connection\n");
		pthread_t sniffer_thread;
		new_sock = malloc(1);
		*new_sock = client_sock;
		if(pthread_create(&sniffer_thread, NULL, conn_handler, (void*) new_sock)<0)
		{
			printf("Could not create thread in response to connection!\n");
			exit(1);
		}
	}
	if(client_sock < 0)
	{
		printf("Accept failure...\n");
		exit(1);
	}
	return 0;
}

void send_hello(int *sock)
{
	char *message = "WELCOME TO MOTHER DATANET\nPLEASE LOGON WITH USER PASSWORD: ";
	// sorry for downtime will fix neext block of tasks to be platinum certified
	write(*sock, message, strlen(message));
}

void flag(int *sock){
	char *flag = "T2e1f_trt1n}G{v5ub_yo502r__nucp__t";
	write(*sock, flag, strlen(flag));
}

void *conn_handler(void *socket_desc)
{
	int sock = *(int*)socket_desc;
	int read_size;
	char giantbuff[1024];
	volatile int auth = 0;
	char *message, buffer[20];
	// don't know this refrence, then you should join hacking movie nights ;)
	char pw[] = "red_pencil_is_used_for_marking_errors";
	send_hello(&sock);
	while((read_size=recv(sock, buffer, 1024, 0))> 0)
	{
		if(strncmp(buffer, "EXIT", 4) == 0 || strncmp(buffer, "exit", 4) == 0)
		{
			printf("Got \'exit\' from client\n");
			break;
		}
		if(!strncmp(buffer, pw, strlen(pw)))
		{
			printf("Got correct password\n");
			printf("Here take a flag.");
			flag(&sock);
			printf("\n");
			auth = 1;
		}
		if(auth)
		{
			message = "\nOH NO! YOU BREACHED THE MAINFRAME!\n";
			write(sock, message, strlen(message));
			printf("Client breached the mainframe! Disconnecting him\n");
			fflush(stdout);
			close(sock);
			free(socket_desc);
			return 0;
		}
		else
			send_hello(&sock);
	}
	if(read_size == 0)
		printf("Client disconnected\n");
	else if(read_size==-1)
		printf("Recv failed\n");
	close(sock);
	free(socket_desc);
	fflush(stdout);
	return 0;
}