# Band Game Generator


print("What's the name of the city you grew up in?");
userCity=str(input());

print("What's your pet's name?");
userPetName=str(input());

result=str("Your band name could be {} & {}");

print(result.format(userCity,userPetName));
