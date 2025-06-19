
webSocket = new WebSocket("ws://localhost:8765");

webSocket.onopen = (_) => {
  console.log("[Client] Connected!")
  window.pythonClientOnOpen()
};

webSocket.onmessage = async (event) => {
  // console.log("[Client] Message received:", event.data)
  window.pythonClientOnMessage(event.data)
};

webSocket.onclose = (_) => {
  console.log("[Client] Disconnected")
  window.pythonClientOnClose()
};

const encoder = new TextEncoder();
function pythonClientSend(data)
{
  // console.log("[Client] Sending:", data)
  //TODO: do we need the encoder?
  webSocket.send(encoder.encode(data).buffer)
}