# 위치 정보 시각화하기 folium

# Map([위도, 경도]) -> 지도는 이 명령어가 존재한다.해당 위치를 중심으로 지도가 만들어진다.
import folium

# lat, long = 37.52860, 126.93431 # 여의도 한강 공원
# lat1, long1 = 37.52400, 126.91889 # 여의도 공원
# lat2, long2 = 37.51865, 126.92041  # 샛강생태공원
lat = [37.52860, 37.52400, 37.51865]
long = [126.93431, 126.91889, 126.92041]
names = ['여의도 한강 공원', '여의도공원', '샛강생태공원']
icons = ['automobile', 'balance-scale', 'ban']
colors = ['red', 'blue', 'purple']

map_y = folium.Map([lat[0], long[0]], zoom_start = 15) # zoom_start 줌기능
# folium.Marker([lat, long], tooltip='여의도 한강공원', icon=folium.Icon(color='red', icon='automobile', prefix='fa')).add_to(map_y) # 마커 # prefix는 awsome아이콘을 사용한다는 의미
# folium.Marker([lat1, long1], tooltip='여의도공원', icon=folium.Icon(color='blue', icon='home')).add_to(map_y) # 마커 # tooltip으로 글씨가 깨지면 popup이용
# folium.Marker([lat2, long2], tooltip='샛강생태공원',  icon=folium.Icon(color='purple', icon='flag')).add_to(map_y) # 마커 # tooltip으로 글씨가 깨지면 popup이용 
for i in range(len(lat)):
    folium.Marker(
        [lat[i], long[i]], tooltip=names[i], icon=folium.Icon(color=colors[i], icon=icons[i], prefix='fa')
    ).add_to(map_y)

map_y.save('./map1.html')