#include "Sensor.h"

Sensor::Sensor() {
    _hardness = "0";      //경도값
    _latitude = "0";      //위도값
    _altitud_gps = "0";   //gps고도값
    _altitud = "0";       //고도값
    _temperature = "0";   //온도값

    SoftwareSerial serialGPS(GPS_RX_PIN, GPS_TX_PIN);
    serialGPS.begin(9600);
    _serialGPS = serialGPS;
}
void Sensor::begin(int rate) { // 초기화
    Serial.println("센서들 초기화 중....");
//    if(!bmp.begin(BMP085_ULTRAHIGHRES)) {
//        Serial.println("BMP180 센서를 찾을 수 없습니다. 연결을 확인해 주세요!");
//        return
//    }

    Serial.println("센서들 초기화 완료....");
}

void Sensor::sening(void) { //sening 해서 내부 필드에 값 저장
    Serial.println("센싱중... ");
    delay(300);
    _hardness = Sensing_gps_hardness();
    _latitude = Sensing_gps_latitude();
    _altitud_gps = Sensing_gps_altitud_gps();
//    _altitud = Sensing_altitude_altitude();
//    _temperature = Sensing_altitude_temperature();
    Serial.println("센싱 완료... ");
}

String Sensor::Sensing_gps_hardness(void) {  //gps 경도값 센싱
    /*    gps 경도값 가져오기
       return : (String)경도값
       // float 형의 값을 string 형으로 변환에서 리턴
    */
    float hardness, latitude; // 위도, 경도값을 전달할 변수

    if(_serialGPS.available()) {  //버퍼에 데이터가 있는지 확인
        int c = _serialGPS.read(); //버퍼에 들어가 있는 값을 c에 저장
        _gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    _gps.f_get_position(&hardness, &latitude); //위도, 경도갑을 변수에 삽입
    String result(hardness)
    return result //경도값을 string 형으로 형 변환 하여 리턴
}

String Sensor::Sensing_gps_latitude(void) { //gps 위도값 센싱
   /*    gps 위도값 가져오기
      return : (String)위도값
      // float 형의 값을 string 형으로 변환에서 리턴
   */
   float hardness, latitude; // 위도, 경도값을 전달할 변수

   if(_serialGPS.available()) {  //버퍼에 데이터가 있는지 확인
       int c = _serialGPS.read(); //버퍼에 들어가 있는 값을 c에 저장
       _gps.encode(c); // gps 레퍼런스에 gps값 삽입
   }
   else { //없을 경우 오류 메세지 리턴
       return "gps 수신 오류";
   }

   _gps.f_get_position(&hardness, &latitude); //위도, 경도값을 변수에 삽입

    String result(latitude)
    return result //경도값을 string 형으로 형 변환 하여 리턴
}
String Sensor::Sensing_gps_altitud(void) {
    /*    gps 고도값 가져오기
       return : (String)고도값
       // float 형의 값을 string 형으로 변환에서 리턴
    */
    if(_serialGPS.available()) {  //버퍼에 데이터가 있는지 확인
        int c = _serialGPS.read(); //버퍼에 들어가 있는 값을 c에 저장
        _gps.encode(c); // gps 레퍼런스에 gps값 삽입
    }
    else { //없을 경우 오류 메세지 리턴
        return "gps 수신 오류";
    }

    String result(_gps.f_altitude())
    return result //경도값을 string 형으로 형 변환 하여 리턴
}
//String Sensor::Sensing_altitude_altitude(void) { //고도 센서에서 고도값 센싱
//    /*  고도 센서에서 고도값 가져오기
//        //기상청에서 우리나라 해면 기압 확인해서 코드에 반영한다.
//            -이유: 고도센서에서 설정한 디폴트 값이 우리 나라의 해면 기압이 아니라서 오차 있음
//        return : (String)고도값
//        // float 형의 값을 string 형으로 변환에서 리턴
//    */
//    return String.valueOf(bmp.readAltitude(100560));
//}
//String Sensor::Sensing_altitude_temperature(void) { //고도 센서에서 온도값 센싱
//    /*  고도 센서에서 온도값 가져오기
//        return : (String)온도값
//        // float 형의 값을 string 형으로 변환에서 리턴
//    */
//     return String.valueOf(bmp.readTemperature());
//}

String Sensor::get_gps_hardness(void) { //gps 경도값 가져오기
    return _hardness;
}
String Sensor::get_gps_latitude(void) { //gps 위도값 가져오기
    return _latitude;
}
String Sensor::get_gps_altitud_gps(void) { //gps고도값 가져오기
    return _altitud_gps;
}
String Sensor::get_altitude_altitude(void) { //고도 센서에서 고도값 가져오기
    return _altitud;
}
String Sensor::get_altitude_temperature(void) { //고도 센서에서 온도값 가져오기
    return _temperature;
}


String Sensor::Sensing_altitude_altitude(void) {



     String result(_altitud);
    return result

return String.valueOf(bmp.readAltitude(100560));
}
String Sensor::Sensing_altitude_temperature(void) {

 String result(_temperature);
    return result
//        // float 형의 값을 string 형으로 변환에서 리턴
//    */
//     return String.valueOf(bmp.readTemperature());
//}