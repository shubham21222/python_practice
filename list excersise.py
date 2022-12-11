favsub=["english","hindi","maths","science"]
dislike=input("which sub you dont like")
getrid=favsub.index(dislike)
favsub.remove(dislike)
print(favsub)