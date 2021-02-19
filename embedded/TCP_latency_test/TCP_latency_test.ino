#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid     = "ESP32";
const char* password = "ericiscool";

const uint16_t port = 8090;
const char * host = "192.168.4.2";

int msg_size = 16;

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

    client.setNoDelay(true);  // disable Nagles algorithm
 
    while (client.connected()) {
      byte send_buf[msg_size];
      for (byte j=0; j<msg_size; j++){
        send_buf[j] = j;
      }
      int totalbytesent = client.write(send_buf, msg_size);
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
