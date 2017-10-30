# animals_master.py
from openerp.osv import osv, fields

# Tabelle Tiere
class animals(osv.Model):
    _name = "animals"
    
    _columns = {
        'name': fields.char('Bezeichnung', size=64, required=True),
        'image': fields.binary("Image"),
        'birthday': fields.date('Geburtsdatum'),
        'classification_id': fields.many2one('animals.classification', 'Tierart'),
        'breed_id': fields.many2one('animals.breed', 'Tierrasse'),
        'tags_ids': fields.many2many('animals.tags', 'rel_animals_tags', 'animals_id', 'tags_id', string="Tags"),
        'notes_ids': fields.one2many('animals.notes', 'animal_id', 'Taetigkeiten/Notizen')

}
animals()

# Tabelle Tierart
class animals_classification(osv.Model):
    _name = "animals.classification"
    
    _columns = {
        'name': fields.char('Bezeichnung',size=64, required=True)
}
animals_classification()

# Tabelle Tierrasse
class animals_breed(osv.Model):
    _name = "animals.breed"
    
    _columns = {
        'name': fields.char('Bezeichnung', size=64, required=True),
        'classification_id': fields.many2one('animals.classification', 'Tierart')
}
animals_breed()

# Tabelle Tiere Tags
class animals_tags(osv.Model):
    _name = "animals.tags"
    
    _columns = {
        'name': fields.char('Bezeichnung',size=64)
}
animals_tags()

# Tabelle Tiere Taetigkeiten/Notizen
class animals_notes(osv.Model):
    _name = "animals.notes"
    
    _columns = {
        'animal_id': fields.integer('Tier ID'),
        'date': fields.date('Datum'),
        'note': fields.text('Taetigkeit/Notiz')
}
animals_notes()

# Tabelle Tiere Standort
class animals_locaton(osv.Model):
    _name = "animals.location"
    
    _columns = {
        'animal_id': fields.integer('Tier ID'),
        'date_from': fields.date("Datum von"),
        'date_to': fields.date("Datum bis"),
        'name': fields.char('Standort',size=64)
}
animals_locaton()

# Tabelle Tiere Behandlungen
class animals_treatment(osv.Model):
    _name = "animals.treatment"
    
    _columns = {
        'animal_id': fields.integer('Tier ID'),
        'date': fields.date('Datum'),
        'treatment': fields.char('Behandlung', char=64)
}
animals_treatment()

# Tabelle Tiere Fuetterung
class animals_feed(osv.Model):
    _name = "animals.feed"
    
    _columns = {
        'animal_id': fields.integer('Tier ID'),
        'date': fields.date('Datum'),
        'feed': fields.char('Fuetterung', char=64),
        'quantity': fields.float('Menge', digits=(6,2))
}
animals_feed()

# Tabelle Tiere Ernte
class animals_crop(osv.Model):
    _name = "animals.crop"
    
    _columns = {
        'animal_id': fields.integer('Tier ID'),
        'date': fields.date('Datum'),
        'crop': fields.char('Ernte', char=64),
        'quantity': fields.float('Menge', digits=(6,2))
}
animals_crop()
