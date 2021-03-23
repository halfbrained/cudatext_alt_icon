::-- > pyls initialize(1): {
    'capabilities': {
        'workspace': {
            'workspaceEdit': {
                'failureHandling': 'abort',
                'documentChanges': True
            },
            'applyEdit': True,
            'configuration': True,
            'symbol': {
                'dynamicRegistration': True,
                'symbolKind': {
                    'valueSet': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
                }
            },
            'executeCommand': {},
            'workspaceFolders': True,
            'didChangeConfiguration': {
                'dynamicRegistration': True
            }
        },
        'window': {
            'showMessage': {
                'messageActionItem': {
                    'additionalPropertiesSupport': True
                }
            },
            'workDoneProgress': True
        },
        'textDocument': {
            'hover': {
                'contentFormat': ['markdown', 'plaintext'],
                'dynamicRegistration': True
            },
            'codeAction': {
                'codeActionLiteralSupport': {
                    'codeActionKind': {
                        'valueSet': []
                    }
                },
                'dynamicRegistration': True
            },
            'typeDefinition': {
                'linkSupport': True,
                'dynamicRegistration': True
            },
            'documentHighlight': {
                'dynamicRegistration': True
            },
            'formatting': {
                'dynamicRegistration': True
            },
            '!!! interesting'
            'rangeFormatting': { # Document Range Formatting Request
                'dynamicRegistration': True
            },
            'signatureHelp': {
                'dynamicRegistration': True,
                'signatureInformation': {
                    'parameterInformation': {
                        'labelOffsetSupport': True
                    },
                    'documentationFormat': ['markdown', 'plaintext']
                }
            },
            'implementation': {
                'linkSupport': True,
                'dynamicRegistration': True
            },
            'colorProvider': {
                'dynamicRegistration': True
            },
            'definition': {
                'linkSupport': True,
                'dynamicRegistration': True
            },
            'synchronization': {
                'didSave': True,
                'willSaveWaitUntil': True,
                'dynamicRegistration': True,
                'willSave': True
            },
            'references': {
                'dynamicRegistration': True
            },
            'completion': {
                'completionItem': {
                    'snippetSupport': True
                },
                'dynamicRegistration': True,
                'completionItemKind': {
                    'valueSet': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
                }
            },
            '!!! interesting'
            'documentSymbol': {  # Document Symbols Request
                'hierarchicalDocumentSymbolSupport': True,
                'dynamicRegistration': True,
                'symbolKind': {
                    'valueSet': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
                }
            },
            'rename': {
                'dynamicRegistration': True
            },
            'publishDiagnostics': {
                'relatedInformation': True
            },
            'declaration': {
                'linkSupport': True,
                'dynamicRegistration': True
            }
        },
        'experimental': {}
    },
    'clientInfo': {
        'version': '0.14.3',
        'name': 'Sublime Text LSP'
    },
    'initializationOptions': {},
    'rootUri': None,
    'processId': 3556,
    'workspaceFolders': None,
    'rootPath': None
    
    
}:: << < pyls 1: {
    'capabilities': {
        'workspace': {
            'workspaceFolders': {
                'supported': True,
                'changeNotifications': True
            }
        },
        'textDocumentSync': {
            'save': {
                'includeText': True
            },
            'openClose': True,
            'change': 2
        },
        'documentRangeFormattingProvider': True,
        'executeCommandProvider': {
            'commands': []
        },
        'codeLensProvider': {
            'resolveProvider': False
        },
        'foldingRangeProvider': True,
        'definitionProvider': True,
        'completionProvider': {
            'resolveProvider': False,
            'triggerCharacters': ['.']
        },
        'documentHighlightProvider': True,
        'signatureHelpProvider': {
            'triggerCharacters': ['(', ',', '=']
        },
        'experimental': {},
        'codeActionProvider': True,
        'referencesProvider': True,
        'documentFormattingProvider': True,
        'documentSymbolProvider': True,
        'hoverProvider': True,
        'renameProvider': True
    }
    
    
}::- > pyls initialized: {}

 
::- > pyls textDocument / didOpen
 

:: < -pyls textDocument / publishDiagnostics: {
    'diagnostics': [],
    'uri': 'file:///home/men/Documents/slow.py'

    
}::- > pyls textDocument / didChange

 
::-- > pyls textDocument / completion(2): {
    'textDocument': {
        'uri': 'file:///home/men/Documents/slow.py'
    },
    'position': {
        'line': 7,
        'character': 1
    }
    
    
}:: << < pyls 2: {
    'isIncomplete': False,
    'items': [{
        'kind': 14,
        'sortText': 'alambda',
        'label': 'lambda',
        'insertText': 'lambda',
        'documentation': 'Lambdas\n*******\n\n\xa0\xa0 lambda_expr\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0::= "lambda" [parameter_list] ":" expression\n\xa0\xa0 lambda_expr_nocond ::= "lambda" [parameter_list] ":" expression_nocond\n\nLambda expressions (sometimes called lambda forms) are used to create\nanonymous functions. The expression "lambda parameters: expression"\nyields a function object.\xa0\xa0The unnamed object behaves like a function\nobject defined with:\n\n\xa0\xa0 def <lambda>(parameters):\n\xa0\xa0\xa0\xa0\xa0\xa0 return expression\n\nSee section Function definitions for the syntax of parameter lists.\nNote that functions created with lambda expressions cannot contain\nstatements or annotations.',
        'detail': ''
    }, {
        'kind': 3,
        'sortText': 'alen',
        'label': 'len(o)',
        'insertText': 'len',
        'documentation': 'len(o: Sized, /) -> int\n\nReturn the number of items in a container.',
        'detail': 'builtins'
    }, {
        'kind': 3,
        'sortText': 'alicense',
        'label': 'license()',
        'insertText': 'license',
        'documentation': 'license() -> None\n\ninteractive prompt objects for printing the license text, a list of\ncontributors and the copyright notice.',
        'detail': 'builtins'
    }, {
        'kind': 7,
        'sortText': 'alist',
        'label': 'list',
        'insertText': 'list',
        'documentation': "list()\nlist(iterable: Iterable[_T])\n\nlist() -> new empty list\nlist(iterable) -> new list initialized from iterable's items",
        'detail': 'builtins'
    }, {
        'kind': 3,
        'sortText': 'alocals',
        'label': 'locals()',
        'insertText': 'locals',
        'documentation': "locals() -> Dict[str, Any]\n\nReturn a dictionary containing the current scope's local variables.\n\nNOTE: Whether or not updates to this dictionary will affect name lookups in\nthe local scope and vice-versa is *implementation dependent* and not\ncovered by any backwards compatibility guarantees.",
        'detail': 'builtins'
    }, {
        'kind': 7,
        'sortText': 'aLookupError',
        'label': 'LookupError',
        'insertText': 'LookupError',
        'documentation': 'LookupError(*args: object)\n\nBase class for lookup errors.',
        'detail': 'builtins'
    }, {
        'kind': 25,
        'sortText': 'alist',
        'label': 'list object',
        'insertText': 'list',
        'documentation': "list()\nlist(iterable: Iterable[_T])\n\nlist() -> new empty list\nlist(iterable) -> new list initialized from iterable's items",
        'detail': 'builtins'
    }, {
        'kind': 25,
        'sortText': 'aLookupError',
        'label': 'LookupError object',
        'insertText': 'LookupError',
        'documentation': 'LookupError(*args: object)\n\nBase class for lookup errors.',
        'detail': 'builtins'
    }]
    
    
}:: < -pyls textDocument / publishDiagnostics: {
    'diagnostics': [],
    'uri': 'file:///home/men/Documents/slow.py'
    
    
}::- > pyls textDocument / didChange
 
 
:: < -pyls textDocument / publishDiagnostics: {
    'diagnostics': [],
    'uri': 'file:///home/men/Documents/slow.py'
    
    
}::- > pyls textDocument / didChange
 
 
::-- > pyls textDocument / completion(3): {
    'textDocument': {
        'uri': 'file:///home/men/Documents/slow.py'
    },
    'position': {
        'line': 7,
        'character': 5
    }
    
    
}:: << < pyls 3: {
    'isIncomplete': False,
    'items': [{
        'kind': 3,
        'sortText': 'aappend',
        'label': 'append(self, object)',
        'insertText': 'append',
        'documentation': 'append(self, object: _T) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'aclear',
        'label': 'clear(self)',
        'insertText': 'clear',
        'documentation': 'clear(self) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'acopy',
        'label': 'copy(self)',
        'insertText': 'copy',
        'documentation': 'copy(self) -> List[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'acount',
        'label': 'count(self, object)',
        'insertText': 'count',
        'documentation': 'count(self, object: _T) -> int',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'aextend',
        'label': 'extend(self, iterable)',
        'insertText': 'extend',
        'documentation': 'extend(self, iterable: Iterable[_T]) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'aindex',
        'label': 'index(self, object, start, stop)',
        'insertText': 'index',
        'documentation': 'index(self, object: _T, start: int=..., stop: int=...) -> int',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'ainsert',
        'label': 'insert(self, index, object)',
        'insertText': 'insert',
        'documentation': 'insert(self, index: int, object: _T) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'amro',
        'label': 'mro()',
        'insertText': 'mro',
        'documentation': 'mro() -> List[type]',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'apop',
        'label': 'pop(self, index)',
        'insertText': 'pop',
        'documentation': 'pop(self, index: int=...) -> _T',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'aremove',
        'label': 'remove(self, object)',
        'insertText': 'remove',
        'documentation': 'remove(self, object: _T) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'areverse',
        'label': 'reverse(self)',
        'insertText': 'reverse',
        'documentation': 'reverse(self) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'asort',
        'label': 'sort(self, key, reverse)',
        'insertText': 'sort',
        'documentation': 'sort(self, *, key: Optional[Callable[[_T], Any]]=..., reverse: bool=...) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__add__',
        'label': '__add__(self, x)',
        'insertText': '__add__',
        'documentation': '__add__(self, x: List[_T]) -> List[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 14,
        'sortText': 'z__base__',
        'label': '__base__',
        'insertText': '__base__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__bases__',
        'label': '__bases__',
        'insertText': '__bases__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__basicsize__',
        'label': '__basicsize__',
        'insertText': '__basicsize__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__call__',
        'label': '__call__(args, kwds)',
        'insertText': '__call__',
        'documentation': '__call__(*args: Any, **kwds: Any) -> Any',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__class__',
        'label': '__class__',
        'insertText': '__class__',
        'documentation': '',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__contains__',
        'label': '__contains__(self, o)',
        'insertText': '__contains__',
        'documentation': '__contains__(self, o: object) -> bool',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__delattr__',
        'label': '__delattr__(self, name)',
        'insertText': '__delattr__',
        'documentation': '__delattr__(self, name: str) -> None',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__delitem__',
        'label': '__delitem__(self, i)',
        'insertText': '__delitem__',
        'documentation': '__delitem__(self, i: Union[int, slice]) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 14,
        'sortText': 'z__dict__',
        'label': '__dict__',
        'insertText': '__dict__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__dictoffset__',
        'label': '__dictoffset__',
        'insertText': '__dictoffset__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__dir__',
        'label': '__dir__(self)',
        'insertText': '__dir__',
        'documentation': '__dir__(self) -> Iterable[str]',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__eq__',
        'label': '__eq__(self, o)',
        'insertText': '__eq__',
        'documentation': '__eq__(self, o: object) -> bool',
        'detail': 'builtins.object'
    }, {
        'kind': 14,
        'sortText': 'z__flags__',
        'label': '__flags__',
        'insertText': '__flags__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__format__',
        'label': '__format__(self, format_spec)',
        'insertText': '__format__',
        'documentation': '__format__(self, format_spec: str) -> str',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__ge__',
        'label': '__ge__(self, x)',
        'insertText': '__ge__',
        'documentation': '__ge__(self, x: List[_T]) -> bool',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__getattribute__',
        'label': '__getattribute__(self, name)',
        'insertText': '__getattribute__',
        'documentation': '__getattribute__(self, name: str) -> Any',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__getitem__',
        'label': '__getitem__(self, i)',
        'insertText': '__getitem__',
        'documentation': '__getitem__(self, i: int) -> _T\n__getitem__(self, s: slice) -> List[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__gt__',
        'label': '__gt__(self, x)',
        'insertText': '__gt__',
        'documentation': '__gt__(self, x: List[_T]) -> bool',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__hash__',
        'label': '__hash__(self)',
        'insertText': '__hash__',
        'documentation': '__hash__(self) -> int',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__iadd__',
        'label': '__iadd__(self, x)',
        'insertText': '__iadd__',
        'documentation': '__iadd__(self: _S, x: Iterable[_T]) -> _S',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__imul__',
        'label': '__imul__(self, n)',
        'insertText': '__imul__',
        'documentation': '__imul__(self: _S, n: int) -> _S',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__init__',
        'label': '__init__(self)',
        'insertText': '__init__',
        'documentation': '__init__(self) -> None\n__init__(self, iterable: Iterable[_T]) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__init_subclass__',
        'label': '__init_subclass__(cls)',
        'insertText': '__init_subclass__',
        'documentation': '__init_subclass__(cls) -> None',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__instancecheck__',
        'label': '__instancecheck__(instance)',
        'insertText': '__instancecheck__',
        'documentation': '__instancecheck__(instance: Any) -> bool',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__itemsize__',
        'label': '__itemsize__',
        'insertText': '__itemsize__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__iter__',
        'label': '__iter__(self)',
        'insertText': '__iter__',
        'documentation': '__iter__(self) -> Iterator[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__le__',
        'label': '__le__(self, x)',
        'insertText': '__le__',
        'documentation': '__le__(self, x: List[_T]) -> bool',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__len__',
        'label': '__len__(self)',
        'insertText': '__len__',
        'documentation': '__len__(self) -> int',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__lt__',
        'label': '__lt__(self, x)',
        'insertText': '__lt__',
        'documentation': '__lt__(self, x: List[_T]) -> bool',
        'detail': 'builtins.list'
    }, {
        'kind': 14,
        'sortText': 'z__module__',
        'label': '__module__',
        'insertText': '__module__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__mro__',
        'label': '__mro__',
        'insertText': '__mro__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__mul__',
        'label': '__mul__(self, n)',
        'insertText': '__mul__',
        'documentation': '__mul__(self, n: int) -> List[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 14,
        'sortText': 'z__name__',
        'label': '__name__',
        'insertText': '__name__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__ne__',
        'label': '__ne__(self, o)',
        'insertText': '__ne__',
        'documentation': '__ne__(self, o: object) -> bool',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__new__',
        'label': '__new__(cls)',
        'insertText': '__new__',
        'documentation': '__new__(cls) -> Any',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__prepare__',
        'label': '__prepare__(name, bases, kwds)',
        'insertText': '__prepare__',
        'documentation': '__prepare__(name: str, bases: Tuple[type, ...], /, **kwds: Any) -> Mapping[str, Any]',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__qualname__',
        'label': '__qualname__',
        'insertText': '__qualname__',
        'documentation': '',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__reduce__',
        'label': '__reduce__(self)',
        'insertText': '__reduce__',
        'documentation': '__reduce__(self) -> Union[str, Tuple[Any, ...]]',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__reduce_ex__',
        'label': '__reduce_ex__(self, protocol)',
        'insertText': '__reduce_ex__',
        'documentation': '__reduce_ex__(self, protocol: int) -> Union[str, Tuple[Any, ...]]',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__repr__',
        'label': '__repr__(self)',
        'insertText': '__repr__',
        'documentation': '__repr__(self) -> str',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__reversed__',
        'label': '__reversed__(self)',
        'insertText': '__reversed__',
        'documentation': '__reversed__(self) -> Iterator[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__rmul__',
        'label': '__rmul__(self, n)',
        'insertText': '__rmul__',
        'documentation': '__rmul__(self, n: int) -> List[_T]',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__setattr__',
        'label': '__setattr__(self, name, value)',
        'insertText': '__setattr__',
        'documentation': '__setattr__(self, name: str, value: Any) -> None',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__setitem__',
        'label': '__setitem__(self, i, o)',
        'insertText': '__setitem__',
        'documentation': '__setitem__(self, i: int, o: _T) -> None\n__setitem__(self, s: slice, o: Iterable[_T]) -> None',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__sizeof__',
        'label': '__sizeof__(self)',
        'insertText': '__sizeof__',
        'documentation': '__sizeof__(self) -> int',
        'detail': 'builtins.object'
    }, {
        'kind': 3,
        'sortText': 'z__str__',
        'label': '__str__(self)',
        'insertText': '__str__',
        'documentation': '__str__(self) -> str',
        'detail': 'builtins.list'
    }, {
        'kind': 3,
        'sortText': 'z__subclasscheck__',
        'label': '__subclasscheck__(subclass)',
        'insertText': '__subclasscheck__',
        'documentation': '__subclasscheck__(subclass: type) -> bool',
        'detail': 'builtins.type'
    }, {
        'kind': 3,
        'sortText': 'z__subclasses__',
        'label': '__subclasses__()',
        'insertText': '__subclasses__',
        'documentation': '__subclasses__() -> List[_TT]',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__text_signature__',
        'label': '__text_signature__',
        'insertText': '__text_signature__',
        'documentation': 'NoneType()',
        'detail': 'builtins.type'
    }, {
        'kind': 14,
        'sortText': 'z__weakrefoffset__',
        'label': '__weakrefoffset__',
        'insertText': '__weakrefoffset__',
        'documentation': '',
        'detail': 'builtins.type'
    }]
    
    
}:: < -pyls textDocument / publishDiagnostics: {
    'diagnostics': [],
    'uri': 'file:///home/men/Documents/slow.py'
}
