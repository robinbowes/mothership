from sqlalchemy import exc, orm, Table, MetaData

class Tag(object):
    def __init__(self, shipd):
        self.shipd = shipd
        self.tags = Table('tags', self.shipd.metadata, autoload=True)
        
    def return_tags(self):
        q = self.tags.select().execute()
        res = q.fetchall()
        tags = {'tag' : [] }
        for tag in res:
            tags['tag'].append(tag[0])
        return tags

    def return_tag(self, tag):
        class TG(object):
            pass

        tagmapper = orm.mapper(TG, self.tags)
        try:
            q = self.shipd.dbsess.query(TG).filter(TG.name==tag).one()
        except orm.exc.NoResultFound:
            return 'No results found'
        
        # p.id p.name p.security_level p.start_port p.stop_port
        res = {'id': q.id,
               'security_level' : q.security_level,
               'start_port': q.start_port,
               'stop_port' : q.stop_port
               }
        return res
