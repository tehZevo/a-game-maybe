//js-side of the websocket connection for the pygbag-wrapped game

function pythonClientConnect(url)
{
  webSocket = new WebSocket(url);

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
}

function pythonClientSend(data)
{
  webSocket.send(data)
}