CFLAGS = -O2 -Wall
LDFLAGS = -s
CC = gcc
LD = ld
MAKE = make


SERVER_CFLAGS=`xmlrpc-c-config  abyss-server --cflags`
SERVER_LDFLAGS=`xmlrpc-c-config abyss-server --libs`

all: server 

#server: server.c
#	$(CC) $(CFLAGS) -c $<
#	$(CC) $(LDFLAGS) $< -o $@


server: server.c
	$(CC) $(SERVER_CFLAGS)	$(CFLAGS)  -c $<
	$(CC) $(SERVER_LDFLAGS)	$(LDFLAGS) $< -o $@

clean:
	rm -f client server *.o 
