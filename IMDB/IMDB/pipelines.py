from sqlalchemy.orm import sessionmaker
from IMDB.spiders.models import IMDB_DATABASE, db_connect, create_table


class ScrapySpiderPipeline(object):
    
    # Bu Fonksiyon Veritabanı bağlantısını ve oturum oluşturucuyu başlatır ve bir İlişkisel Veritabanı tablosu oluşturur.
    def __init__(self):
        
        engine = db_connect()
        create_table(engine)
        
        self.Session = sessionmaker(bind=engine)

    # Bu Fonksiyon Spiderdan Gelen Dataları Models.py Dosyasındaki Model Şablonuna Göre İşleme Sokarak Verileri Database İçine Kaydeder
    def process_item(self, item, spider):

        session = self.Session()
        
        ım_db = IMDB_DATABASE()
        
        ım_db.MOVIE_CODE = item["MOVIE_CODE"]
        
        ım_db.MOVIE_NAME = item["MOVIE_NAME"]

        ım_db.YEAR = item["YEAR"]

        ım_db.RANK = item["RANK"]

        ım_db.IMDB_RATING = item["IMDB_RATING"]



        # Buradaki Try Except istisna blokları datalar kaydedilirken varsa oluşan hataları ayıklayarak bizlere mesaj olarak döner
        try:
            session.add(ım_db)
            session.commit()
        
        except:
            session.rollback()
            raise
        
        finally:
            session.close()

        return item
