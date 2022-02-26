import geocoder
import folium

g = geocoder.ip("42.114.110.66")

myAddress = g.latlng

my_map1 = folium.Map(location=myAddress,
                     zoom_start=12)



folium.CircleMarker(location=myAddress,
                     radius=50,popup="Yorkshire").add_to(my_map1)


folium.Market(myAddress,
              popup="Yorkshire").add_to(my_map1)

my_map1.save("my_map.html ")