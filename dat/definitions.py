# ./dat.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2015-09-05 16:17:00.558006 by PyXB version 1.2.4 using Python 3.4.3.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c60aa80a-53d8-11e5-ad2d-000acd1eb9c1')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: typesDecription
class typesDecription (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typesDecription')
    _XSDLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 3, 1)
    _Documentation = None
typesDecription._CF_pattern = pyxb.binding.facets.CF_pattern()
typesDecription._CF_pattern.addPattern(pattern='((list|ref)\\|)*(bool|byte|short|int|uint|long|ulong|string)')
typesDecription._InitializeFacetMap(typesDecription._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'typesDecription', typesDecription)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 17, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element field uses Python identifier field
    __field = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'field'), 'field', '__AbsentNamespace0_CTD_ANON_field', True, pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 8, 1), )

    
    field = property(__field.value, __field.set, None, None)

    
    # Attribute file uses Python identifier file
    __file = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'file'), 'file', '__AbsentNamespace0_CTD_ANON_file', pyxb.binding.datatypes.string, required=True)
    __file._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 21, 3)
    __file._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 21, 3)
    
    file = property(__file.value, __file.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_CTD_ANON_length', pyxb.binding.datatypes.nonNegativeInteger)
    __length._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 22, 3)
    __length._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 22, 3)
    
    length = property(__length.value, __length.set, None, None)

    _ElementMap.update({
        __field.name() : __field
    })
    _AttributeMap.update({
        __file.name() : __file,
        __length.name() : __length
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 26, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element records uses Python identifier records
    __records = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'records'), 'records', '__AbsentNamespace0_CTD_ANON__records', False, pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 28, 4), )

    
    records = property(__records.value, __records.set, None, None)

    _ElementMap.update({
        __records.name() : __records
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 29, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element record uses Python identifier record
    __record = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'record'), 'record', '__AbsentNamespace0_CTD_ANON_2_record', True, pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 16, 1), )

    
    record = property(__record.value, __record.set, None, None)

    _ElementMap.update({
        __record.name() : __record
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_3_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 10, 3)
    __id._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 10, 3)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_3_type', typesDecription, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 11, 3)
    __type._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 11, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute description uses Python identifier description
    __description = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'description'), 'description', '__AbsentNamespace0_CTD_ANON_3_description', pyxb.binding.datatypes.string)
    __description._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 12, 3)
    __description._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 12, 3)
    
    description = property(__description.value, __description.set, None, None)

    
    # Attribute isUser uses Python identifier isUser
    __isUser = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'isUser'), 'isUser', '__AbsentNamespace0_CTD_ANON_3_isUser', pyxb.binding.datatypes.boolean)
    __isUser._DeclarationLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 13, 3)
    __isUser._UseLocation = pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 13, 3)
    
    isUser = property(__isUser.value, __isUser.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __description.name() : __description,
        __isUser.name() : __isUser
    })



record = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'record'), CTD_ANON, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 16, 1))
Namespace.addCategoryObject('elementBinding', record.name().localName(), record)

definitions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'definitions'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 25, 1))
Namespace.addCategoryObject('elementBinding', definitions.name().localName(), definitions)

field = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field'), CTD_ANON_3, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 8, 1))
Namespace.addCategoryObject('elementBinding', field.name().localName(), field)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'field'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 8, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 19, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'field')), pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 19, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'records'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 28, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, 'records')), pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 28, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'record'), CTD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 16, 1)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 31, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'record')), pyxb.utils.utility.Location('/home/henrik/dev/poedb2/DatDefinitions.xsd', 31, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

