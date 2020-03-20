#include <SoftwareSerial.h>
#include <TinyGPS.h>

#define GPS_RX_PIN 6
#define GPS_TX_PIN 5

#define GPS_BAUD 9600

TinyGPS gps;
SoftwareSerial uart_gps(GPS_RX_PIN, GPS_TX_PIN);



String get_gps_hardness();
/*    gps 경도값 가져오기
   return : (String)경도값
   // float 형의 값을 string 형으로 변환에서 리턴
*/
String get_gps_latitude();
/*    gps 위도값 가져오기
   return : (String)위도값
   // float 형의 값을 string 형으로 변환에서 리턴
*/

void setup(){
  Serial.begin(9600);
  uart_gps.begin(GPS_BAUD);

}

void loop() {
   Serial.println(get_gps_hardness());
   Serial.println(get_gps_latitude());

}

String get_gps_hardness() { //gps 경도값 가져오기
    float hardness, latitude; // 위도, 경도값을 전달할 변수

    if(uart_gps.available()) {  //버퍼에 데이터가 있는지 확인
        int c = uart_gps.read(); //버퍼에 들어가 있는 값을 c에 저장
        gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    gps.f_get_position(&hardness, &latitude); //위도, 경도갑을 변수에 삽입

    return String.valueOf(hardness); //경도값을 string 형으로 형 변환 하여 리턴
}

String get_gps_latitude() { //gps 위도값 가져오기
    float hardness, latitude; // 위도, 경도값을 전달할 변수

    if(uart_gps.available()) {  //버퍼에 데이터가 있는지 확인
        int c = uart_gps.read(); //버퍼에 들어가 있는 값을 c에 저장
        gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    gps.f_get_position(&hardness, &latitude); //위도, 경도갑을 변수에 삽입

    return String.valueOf(latitude); //위도값을 string 형으로 형 변환 하여 리턴
}
