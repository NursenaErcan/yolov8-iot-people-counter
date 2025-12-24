#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* mqtt_server = "broker.emqx.io";

WiFiClient espClient;
PubSubClient client(espClient);

#define LED_PIN 2
int limit_people = 5;
int occupancy = 0;

void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(100);
}

void callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (int i = 0; i < length; i++) msg += (char)payload[i];

  occupancy = msg.toInt();
  Serial.println("People Count: " + String(occupancy));

  digitalWrite(LED_PIN, occupancy >= limit_people ? HIGH : LOW);
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32-PeopleCounter")) {
      client.subscribe("iot/room/occupancy");
    } else {
      delay(500);
    }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);

  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();
}
