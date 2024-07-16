const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Store connected clients
let clients = [];

// WebSocket server listening
wss.on('connection', function connection(ws) {
    clients.push(ws);

    // When a message is received from a client
    ws.on('message', function incoming(message) {
        // Broadcast message to all clients
        clients.forEach(function each(client) {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    // When a client closes the connection
    ws.on('close', function close() {
        // Remove the client from the list
        clients = clients.filter(function(client) {
            return client !== ws;
        });
    });
});

console.log('WebSocket server started on port 8080');
