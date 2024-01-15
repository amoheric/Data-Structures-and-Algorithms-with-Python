import folium

# Create a folium map centered at a specific location
map_center = [33.748997, -84.387985]  # Replace with the desired coordinates
mymap = folium.Map(location=map_center, zoom_start=15)

# Add green dots for interactive exhibit points
exhibit_points = [[33.74889, -84.387985], [33.74599, -84.387984], [33.748997, -94.38983]]  # Replace with exhibit coordinates
for point in exhibit_points:
    folium.Marker(location=point, icon=folium.Icon(color='green')).add_to(mymap)

# Add blue paths for recommended navigation routes
route_points = [[33.4897, -84.38795], [43.345997, -84.387984], [34.748975, -84.387983]]  # Replace with route coordinates
folium.PolyLine(route_points, color="blue", weight=2.5, opacity=1).add_to(mymap)

# Add red circles for points of interest
interest_points = [[73.24897, -84.38985], [33.783597, -84.387984], [33.748293, -88.38983]]  # Replace with interest points coordinates
for point in interest_points:
    folium.CircleMarker(location=point, radius=20, color='red', fill=True, fill_color='red').add_to(mymap)

# Save the map as an HTML file
mymap.save(' Amoh_Eric_sample_paper_map.html')
