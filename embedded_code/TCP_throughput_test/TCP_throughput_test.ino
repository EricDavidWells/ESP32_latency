#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid     = "fukyaboi";
const char* password = "fukyaboi";

const uint16_t port = 8090;
const char * host = "192.168.4.2";

WiFiClient client;
WiFiServer wifiServer(port);

void setup() {
  Serial.begin(115200);
  Serial.print("Setting AP (Access Point)…");
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  wifiServer.begin();
}

void loop() {

  client = wifiServer.available();
  if (client) {

    client.setNoDelay(true);
 
    while (client.connected()) {
      int send_len = 16;
      byte send_buf[send_len];
      for (byte j=0; j<send_len; j++){
        send_buf[j] = j;
      }
      int totalbytesent = client.write(send_buf, send_len);
      client.flush();
//      Serial.print("Sent Number of Bytes: ");Serial.println(totalbytesent);
    }
 
    client.stop();
    Serial.println("Client disconnected");
  }
  
  else{
    Serial.println("No Client Found");
    delay(1000);
  }
}
