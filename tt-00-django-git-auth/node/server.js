const express = require('express');
const app = express();

const cors = require('cors');
app.use(cors({
    origin: '*',
}));

const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");

const io = new Server(server, {
  cors: {
    origin:'*',
  }
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});


io.on('connection', (socket) => {
  socket.on('new_data', (data) => {
    io.emit('new_data', data);
  });
  console.log('a user connected');
});


server.listen(process.env.PORT || 5000, function() {
  console.log('listening on ??? some port')
})

function send_message(){
  io.emit('new_data', {
    'number': Math.floor(Math.random() * (999 - 100 + 1) + 100) + '-' + Math.floor(Math.random() * (999 - 100 + 1) + 100)
  });

}


async function funq(){
  while (true){
    await new Promise(r => setTimeout(r, 5000));
    await send_message()
  }
}
funq()
