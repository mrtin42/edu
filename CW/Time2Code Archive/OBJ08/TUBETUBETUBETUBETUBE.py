# LONDON UNDERGROUND PROGRAM LES GO 
victoriaLineStations = ["Brixton","Stockwell","Vauxhall","Pimlico","Victoria","Green Park","Oxford Circus","Warren Street","Euston","Kings Cross St Pancras", "Highbury & Islington", "Finsbury Park", "Seven Sisters", "Tottenham Hale", "Blackhorse Road", "Walthamstow Central"]

station1 = input("Enter the first station: ")
station2 = input("Enter the second station: ")

distanceBetweenStations = abs(victoriaLineStations.index(station1) - victoriaLineStations.index(station2))

print(f'The distance between these two stations is {distanceBetweenStations}')