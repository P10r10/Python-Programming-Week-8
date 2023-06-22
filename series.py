class Series:
    def __init__(self, title: str, seasons: int, genres: list[str]):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self) -> str:
        if len(self.ratings) == 0:
            answer = "no ratings"
        else:
            rate = sum(self.ratings) / len(self.ratings)
            answer = f"{len(self.ratings)} ratings, average {rate:.1f} points"
        return f"{self.title} ({self.seasons} seasons)\n" \
            f"genres: {', '.join(self.genres)}\n{answer}"

    def rate(self, rating: int):
        self.ratings.append(rating)


def minimum_grade(rating: float, series_list: list):
    return [serie for serie in series_list if sum(serie.ratings) >= rating]


def includes_genre(genre: str, series_list: list):
    return [serie for serie in series_list if genre in serie.genres]


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
