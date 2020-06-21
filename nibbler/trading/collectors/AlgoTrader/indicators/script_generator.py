import ta
import inspect
import unidecode


def _script_generator(func,function_name,module):
    code       = inspect.getsource(func)
    class_name = code.splitlines()[1].replace(' ','').replace('"','').replace('/','')
    class_name = unidecode.unidecode(class_name)
    list_of_lines = [
    'from .class_Indicator import Indicator\n',
    'import ta\n',        
    'class {}(Indicator):\n'.format(class_name),
    '    def __init__(self,*args,**kwargs):\n',
    '        self.function = ta.{}.{}\n'.format(module,function_name),
    '        super({},self).__init__(*args,**kwargs)'.format(class_name)
    ]
    
    filename =  'subclass_'+ class_name + '.py'
    with open(filename,'w') as filehande:
        filehande.writelines(list_of_lines)
        
function_names = [func for func in dir(ta.others)\
                  if all(['__' not in func,
                          'math' not in func,
                          'np' not in func,
                          'pd' not in func,
                          'dropna' not in func,
                          ])]

for function_name in function_names:
    func = getattr(ta.others,function_name)
    _script_generator(func,function_name, 'others') 

__all__ = [
    '_script_generator'
]