class Collection:
    def ___init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList 

    def AddGame(self, game):
        if game in self.gameList:
            print("Game is already in collection")
        else:
            self.gameList.append(game)

    def Addmovie(self, movie):
        if movie in self.movieList:
            print("movie is already in collection")
        else:
            self.movieList.append(movie)

    def RemoveGame(self, game):
        if game in self.gameList:
            self.gameList.remove(game)

        else:
            print("Game Not Found")

    def DisplayGames(self):
        for game in self.gameList:
            print(game)
    def DisplayMovies(self):
        for movie in self.movieList:
            print(movie)
    def DisplayFavGame(self):
        print(self.gameList)

    def DisplayFavMovie(self):
            print('Fav Movie: {self.favMovie}')

    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovies()
        self.DisplayFavMovie()

    def SetFavMovie(self, movie): 
        if movie not in self.movieList:
            self.Addmovie(movie)
        self.favMovie = movie

    def SetFavGame(self, game):
        if game not in self.gameList:
            self.AddGame(game)
        self.favGame = game