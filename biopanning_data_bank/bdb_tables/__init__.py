from biopanning_data_bank.bdb_tables.tables import (
    BDB_Entry,
    BDB_Database)

from biopanning_data_bank.bdb_tables.library import (
    Library,
    LibraryDatabase)

from biopanning_data_bank.bdb_tables.mimoset import (
    Mimoset,
    MimosetDatabase)

from biopanning_data_bank.bdb_tables.soc import (
    SOC,
    SOCDatabase)

from biopanning_data_bank.bdb_tables.sotmc import (
    SOTMC,
    SOTMCDatabase)

from biopanning_data_bank.bdb_tables.sottc import (
    SOTTC,
    SOTTCDatabase)

from biopanning_data_bank.bdb_tables.target import (
    Target,
    TargetDatabase)

from biopanning_data_bank.bdb_tables.template import (
    Template,
    TemplateDatabase)

from biopanning_data_bank.bdb_tables.fields import (
    LIBRARY_FIELDS,
    MIMOSET_FIELDS,
    SOC_FIELDS,
    SOTMC_FIELDS,
    SOTTC_FIELDS,
    TARGET_FIELDS,
    TEMPLATE_FIELDS)


BDB_DATABASES = {
    'library': LibraryDatabase,
    'mimoset': MimosetDatabase,
    'soc': SOCDatabase,
    'sotmc': SOTMCDatabase,
    'sottc': SOTTCDatabase,
    'target': TargetDatabase,
    'template': TemplateDatabase}

BDB_ENTRIES = {
    'library': Library,
    'mimoset': Mimoset,
    'soc': SOC,
    'sotmc': SOTMC,
    'sottc': SOTTC,
    'target': Target,
    'template': Template}

BDB_FIELDS = {
    'library': LIBRARY_FIELDS,
    'mimoset': MIMOSET_FIELDS,
    'soc': SOC_FIELDS,
    'sotmc': SOTMC_FIELDS,
    'sottc': SOTTC_FIELDS,
    'target': TARGET_FIELDS,
    'template': TEMPLATE_FIELDS}
