#include <WiFi.h>
#include <WiFiUDP.h>

const char* ssid     = "fukyaboi";
const char* password = "fukyaboi";

const uint16_t port = 8090;
const char * host = "192.168.4.2";

WiFiUDP udp;

long long num1 = 0;
long long num2 = 0;
const uint8_t * num1_ptr = (const uint8_t*) &num1;
const uint8_t * num2_ptr = (const uint8_t*) &num2;

void setup() {
  Serial.begin(115200);
  Serial.print("Setting AP (Access Point)…");
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  Serial.print("Setting up UDP: ");
  int temp = udp.begin(WiFi.localIP(), port);
  Serial.println(temp);
}

void loop() {

//  int send_len = 16;
//  byte send_buf[send_len];
//  for (byte j=0; j<send_len; j++){
//    send_buf[j] = j;
//  }

  num1 += 1;
  num2 += 1;
  int send_len = 8;
  udp.beginPacket(host, port);
  udp.write(num1_ptr, send_len);
  udp.write(num2_ptr, send_len);
  udp.endPacket();
//  delayMicroseconds(500);
}
