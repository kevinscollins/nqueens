import os

from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

class SolutionSet:
    """Data model to initialize, add to and count a set of solutions"""

    def __init__(self, n, table_prefix=None):
        self.n = n
        table_name = 'solution_n{}'.format(str(n))
        if table_prefix:
            table_name = '_'.join([table_prefix, table_name])
        engine = create_engine(os.environ['POSTGRES_URL'])

        # Using SQL owing to non-obvious bit string column creation in SQLAlchemy
        # Maybe switch to bytea or other type if translating to bit-strings is slow
        with engine.connect() as con:
            # TODO Fail fast and cleanly here
            rs = con.execute('DROP TABLE IF EXISTS {}'.format(table_name))
            rs = con.execute('CREATE TABLE {} (queens BIT({}) PRIMARY KEY)'.format(table_name, str(n * n)))

        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.Solution = Base.classes[table_name]
        SessionFactory = sessionmaker(bind=engine)
        self.session = SessionFactory()

    def add(self, solution_bit_string):
        """Add solution to this set"""
        solution = self.Solution(queens=solution_bit_string)
        self.session.add(solution)

    def count(self):
        """Count solutions in this set"""
        return self.session.query(func.count(self.Solution.queens)).scalar()

    def __del__(self):
        if self.session:
            self.session.close()
