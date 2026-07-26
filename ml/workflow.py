from ml.profiler import DataProfiler
from ml.quality import DataQualityAnalyzer
from ml.cleaner import DataCleaner


class MLPipeline:

    def __init__(self):

        self.profiler = DataProfiler()
        self.quality = DataQualityAnalyzer()
        self.cleaner = DataCleaner()

    def run(self, df):

        profile = self.profiler.profile(df)

        quality = self.quality.analyze(df)

        clean_df = self.cleaner.clean(df)

        return {
            "profile": profile,
            "quality": quality,
            "clean_data": clean_df
        }