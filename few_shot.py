import json
import pandas as pd


class Few_Shot_Posts:
    def __init__(self, file_path = "data/processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.file_path = file_path
        self.load_posts()

    def load_posts(self):
        with open(self.file_path, encoding="utf-8") as file:
            posts = json.load(file)
        self.df = pd.json_normalize(posts)
        # self.df["engagement"] = self.df["likes"].apply(self.categorize_engagement)
        self.df["length"] = self.df["line_count"].apply(self.categorize_length)
        all_tags = self.df["tags"].sum()
        self.unique_tags = set(all_tags)


    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5<= line_count <= 8:
            return "Medium"
        else:
            return "Long"
    
    # def categorize_engagement(self, likes):

    #     if  likes < 500:
    #         return "Low"
    #     elif 500 < likes <= 750:
    #         return "Medium"
    #     elif 750 < likes <= 1000:
    #         return "High"
    #     else:
    #         return "Very High"

    def get_unique_tags(self):
        return self.unique_tags    
        

    def get_filtered_posts(self, length, tag):
        df_filtered = self.df[
            (self.df["length"] == length) &
            # (self.df["engagement"] == engagement) &
            # (self.df["language"] == language) &
            (self.df["tags"].apply(lambda tags: tag in tags)) 
        ]

        return df_filtered.to_dict(orient="records")

if __name__ == "__main__":
    Fs = Few_Shot_Posts()
    posts = Fs.get_filtered_posts("Short", "Digital Summit")
    print(posts)
    