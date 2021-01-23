import os
import utils
import jinja2 as ji

C = utils.json_drill('src/content')
T = ji.FileSystemLoader('src/templates')
E = ji.Environment(loader=T)

for project in C['portfolio']['projects']:
  for img in project['img']:
    img.update({'src': '/img/portfolio/'+project['slug']+'/'+img['slug']+'.jpg'})

sorter = lambda e: e['no']
X = dict(
  default      = C['default'],
  navitems     = C['pages'],
  contacts     = C['contacts'],
  about        = C['about'],
  services     = C['services'],
  portfolio    = C['portfolio'],
  testimonials = C['testimonials'],
)

utils.log('saving',1)
for page in C['pages']:
  page.update({
    'href': page['slug'],
    'template': page['slug'],
  })
  utils.page_save(E,T,page,**X)
for project in C['portfolio']['projects']:
  project.update({
    'href': 'portfolio/'+project['slug'],
    'template': 'project',
  })
  utils.page_save(E,T,project,**X)