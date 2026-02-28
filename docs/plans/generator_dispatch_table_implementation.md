# Generator Dispatch Table Implementation Plan

**Created:** 2026-02-28
**Status:** Ready for Implementation
**Based on:** `docs/plans/serialization_dispatch_optimization.md`

---

## Objective

Update `tools/generate_models/generators.py` to generate ~2,200 AUTOSAR model classes with pre-computed `_XML_TAG` constants and `_DESERIALIZE_DISPATCH` tables for O(1) deserialization performance.

## Implementation Steps with Quality Checks

### Step 1: Add `_generate_xml_tag_constant()` function

**Location**: `tools/generate_models/generators.py` after line 625

**Purpose**: Generate `_XML_TAG = "XML-TAG"` constant for each class

**Implementation**:
```python
def _generate_xml_tag_constant(class_name: str) -> str:
    """Generate _XML_TAG constant for a class.
    
    Args:
        class_name: Name of the class
        
    Returns:
        String containing _XML_TAG constant definition
    """
    from armodel2.serialization.name_converter import NameConverter
    xml_tag = NameConverter.to_xml_tag(class_name)
    return f'    _XML_TAG = "{xml_tag}"\n'
```

**Quality Check**:
```bash
# Regenerate a single class to verify
python -m tools.generate_models --classes
grep -r "_XML_TAG" src/armodel2/models/M2/ | head -5
```

---

### Step 2: Add `_build_dispatch_handler()` function

**Location**: `tools/generate_models/generators.py`

**Purpose**: Main handler builder with decorator and type handling

**Implementation**:
```python
def _build_dispatch_handler(
    attr_name: str,
    attr_info: Dict[str, Any],
    package_data: Dict[str, Dict[str, Any]],
    class_name: str,
) -> Optional[str]:
    """Build dispatch handler lambda for an attribute.
    
    Args:
        attr_name: Python attribute name
        attr_info: Attribute metadata
        package_data: Package data for type resolution
        class_name: Name of the class
        
    Returns:
        String containing lambda handler or None if attribute should be excluded
    """
    from armodel2.serialization.name_converter import NameConverter
    from tools.generate_models.type_utils import is_primitive_type, is_enum_type
    
    attr_type = attr_info["type"]
    multiplicity = attr_info["multiplicity"]
    is_ref = attr_info.get("is_ref", False)
    kind = attr_info.get("kind", "attribute")
    decorator_name = attr_info.get("decorator_name")
    
    # Build base XML tag
    xml_tag = NameConverter.to_xml_tag(attr_name)
    
    # --- EXCLUDE from dispatch table ---
    
    # Skip xml_attribute and lang_abbr (handled via super().deserialize())
    if kind == "xml_attribute" or decorator_name == "xml_attribute":
        return None
    if decorator_name == "lang_abbr":
        return None
    
    # --- SPECIAL HANDLERS ---
    
    # Handle IRef (kind == "iref")
    if kind == "iref":
        return _build_iref_handler(attr_name, attr_info, xml_tag, attr_type, multiplicity, decorator_name)
    
    # Handle @ref_conditional
    if decorator_name == "ref_conditional":
        container_tag = attr_info.get("decorator_params", xml_tag)
        type_xml_tag = NameConverter.to_xml_tag(attr_type)
        conditional_tag = f"{type_xml_tag}-REF-CONDITIONAL"
        ref_tag = f"{type_xml_tag}-REF"
        return f'''        "{container_tag}": lambda obj, elem: setattr(
            obj, "_{attr_name}",
            [ARRef.deserialize(SerializationHelper.find_child_element(child, "{ref_tag}"))
             for child in elem
             if (child.tag.split('}}', 1)[1] if child.tag.startswith('{{') else child.tag) == "{conditional_tag}"]
        ),'''
    
    # Handle @lang_prefix
    if decorator_name == "lang_prefix":
        wrapper_tag = attr_info.get("decorator_params", xml_tag)
        return f'        "{wrapper_tag}": lambda obj, elem: obj._{attr_name}.append(LParagraph.deserialize(elem)),'
    
    # Handle @atp_variant
    if decorator_name == "atp_variant":
        from armodel2.serialization.serialization_helper import SerializationHelper
        wrapper_path = SerializationHelper.get_atp_variant_wrapper_path(class_name)
        return f'''        "{wrapper_path.split('/')[0]}": lambda obj, elem: setattr(
            obj, "_{attr_name}",
            SerializationHelper.unwrap_atp_variant(elem, "{xml_tag}")
        ),'''
    
    # Handle @xml_element_name
    if decorator_name == "xml_element_name":
        custom_tag = attr_info.get("decorator_params", xml_tag)
        return f'''        "{custom_tag}": lambda obj, elem: setattr(
            obj, "_{attr_name}",
            [SerializationHelper.deserialize_by_tag(child, None) for child in elem]
        ),'''
    
    # --- STANDARD HANDLERS ---
    
    # Handle TRef (kind == "tref") - use -TREF suffix
    if is_ref and kind == "tref":
        xml_tag = f"{xml_tag}-TREF"
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", ARRef.deserialize(elem)),'
    
    # Handle regular REF (kind == "ref") - use -REF suffix
    if is_ref and kind == "ref":
        xml_tag = f"{xml_tag}-REF"
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", ARRef.deserialize(elem)),'
    
    # Handle primitives
    if is_primitive_type(attr_type, package_data):
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", elem.text),'
    
    # Handle enums
    if is_enum_type(attr_type, package_data):
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", {attr_type}.deserialize(elem)),'
    
    # Handle lists (non-ref)
    if multiplicity in ("*", "0..*"):
        return _build_list_handler(attr_name, xml_tag, attr_type, package_data)
    
    # Handle single objects
    return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", SerializationHelper.deserialize_by_tag(elem, "{attr_type}")),'
```

**Quality Check**: Verify handler logic for all attribute types by reading generated code

---

### Step 3: Add `_build_iref_handler()` function

**Location**: `tools/generate_models/generators.py`

**Purpose**: Handle 3 IRef patterns

**Implementation**:
```python
def _build_iref_handler(
    attr_name: str,
    attr_info: Dict[str, Any],
    xml_tag: str,
    attr_type: str,
    multiplicity: str,
    decorator_name: Optional[str],
) -> Optional[str]:
    """Build dispatch handler for IRef attributes.
    
    Handles 3 patterns:
    1. Multi-wrapper list (list_type=multi): Container tag with wrapper matching
    2. Single-wrapper (flattened): Wrapper tag, direct deserialize
    3. Single-wrapper (non-flattened): Wrapper tag, list comprehension
    """
    # Parse decorator params
    should_flatten = False
    list_type = "single"
    
    if decorator_name == "instance_ref":
        decorator_params = attr_info.get("decorator_params", "")
        param_list = [p.strip() for p in decorator_params.split(",")]
        for param in param_list:
            if param == "flatten=True":
                should_flatten = True
            elif param == "list_type=multi":
                list_type = "multi"
    
    # Multi-wrapper list (e.g., COMPONENT-IREFS)
    if multiplicity in ("*", "1..*") and list_type == "multi":
        singular_tag = xml_tag[:-1] if xml_tag.endswith("S") else xml_tag
        container_tag = f"{singular_tag}-IREFS"
        wrapper_tag = f"{singular_tag}-IREF"
        return f'''        "{container_tag}": lambda obj, elem: setattr(
            obj, "_{attr_name}",
            [SerializationHelper.deserialize_by_tag(child, None) 
             for child in elem 
             if (child.tag.split('}}', 1)[1] if child.tag.startswith('{{') else child.tag) == "{wrapper_tag}"]
        ),'''
    
    # Single IRef (0..1 or 1)
    if multiplicity in ("0..1", "1"):
        wrapper_tag = f"{xml_tag}-IREF"
        if should_flatten:
            return f'        "{wrapper_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", SerializationHelper.deserialize_by_tag(elem, None)),'
        else:
            return f'        "{wrapper_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", [SerializationHelper.deserialize_by_tag(child, None) for child in elem]),'
    
    # Single-wrapper list (flattened or not)
    wrapper_tag = f"{xml_tag}-IREF"
    if should_flatten:
        return f'        "{wrapper_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", SerializationHelper.deserialize_by_tag(elem, None)),'
    else:
        return f'        "{wrapper_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", [SerializationHelper.deserialize_by_tag(child, None) for child in elem]),'
```

**Quality Check**: Verify IRef patterns by checking generated IRef classes

---

### Step 4: Add `_build_list_handler()` function

**Location**: `tools/generate_models/generators.py`

**Purpose**: Handle list attributes with XSD namespace filtering

**Implementation**:
```python
def _build_list_handler(
    attr_name: str,
    xml_tag: str,
    attr_type: str,
    package_data: Dict[str, Dict[str, Any]],
) -> str:
    """Build dispatch handler for list attributes.
    
    Filters out XSD namespace tags: {http://www.w3.org/2001/XMLSchema-instance} and {http://www.w3.org/2001/XMLSchema}
    """
    from tools.generate_models.type_utils import is_primitive_type, is_enum_type
    
    if is_primitive_type(attr_type, package_data):
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", [child.text for child in elem]),'
    elif is_enum_type(attr_type, package_data):
        return f'        "{xml_tag}": lambda obj, elem: setattr(obj, "_{attr_name}", [{attr_type}.deserialize(child) for child in elem]),'
    else:
        return f'''        "{xml_tag}": lambda obj, elem: setattr(
            obj, "_{attr_name}",
            [SerializationHelper.deserialize_by_tag(child, None) for child in elem if child.tag not in ("{{http://www.w3.org/2001/XMLSchema-instance}}", "{{http://www.w3.org/2001/XMLSchema}}")]
        ),'''
```

**Quality Check**: Verify list filtering in generated code

---

### Step 5: Add `_generate_dispatch_table()` function

**Location**: `tools/generate_models/generators.py`

**Purpose**: Generate `_DESERIALIZE_DISPATCH = {...}` table

**Implementation**:
```python
def _generate_dispatch_table(
    attribute_types: Dict[str, Dict[str, Any]],
    package_data: Dict[str, Dict[str, Any]],
    class_name: str,
) -> str:
    """Generate _DESERIALIZE_DISPATCH table for a class.
    
    Args:
        attribute_types: Dictionary of attribute metadata
        package_data: Package data for type resolution
        class_name: Name of the class
        
    Returns:
        String containing _DESERIALIZE_DISPATCH table definition
    """
    dispatch_lines = ['    _DESERIALIZE_DISPATCH = {']
    
    for attr_name, attr_info in attribute_types.items():
        handler = _build_dispatch_handler(attr_name, attr_info, package_data, class_name)
        if handler:
            dispatch_lines.append(handler)
    
    dispatch_lines.append('    }')
    return '\n'.join(dispatch_lines) + '\n'
```

**Quality Check**: Verify table generation format

---

### Step 6: Integrate into `generate_class_code()`

**Location**: `tools/generate_models/generators.py:650` (after class definition)

**Changes**:
```python
# Add _XML_TAG constant
code += _generate_xml_tag_constant(class_name)

# Add _DESERIALIZE_DISPATCH table (if class has attributes)
if attribute_types:
    code += _generate_dispatch_table(attribute_types, package_data, class_name)
```

**Quality Check**:
```bash
# Regenerate classes
python -m tools.generate_models --members --classes --enums --primitives

# Verify constants
grep -r "_XML_TAG" src/armodel2/models/M2/ | head -10
grep -r "_DESERIALIZE_DISPATCH" src/armodel2/models/M2/ | head -10
```

---

### Step 7: Update `_generate_serialize_method()`

**Location**: `tools/generate_models/generators.py:2990`

**Change**:
```python
# Before:
tag = SerializationHelper.get_xml_tag(self.__class__)
elem = ET.Element(tag)

# After:
elem = ET.Element(self._XML_TAG)  # Use pre-computed constant
```

**Quality Check**: Verify serialization produces correct XML

---

### Step 8: Update `_generate_deserialize_method()`

**Location**: `tools/generate_models/generators.py:1060`

**Change**:
```python
@classmethod
def deserialize(cls, element: ET.Element) -> "{class_name}":
    # Call super().deserialize() first for inherited attributes
    obj = super({class_name}, cls).deserialize(element)
    
    # Process class-specific elements with dispatch table
    ns_split = '}'
    for child in element:
        tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
        handler = cls._DESERIALIZE_DISPATCH.get(tag)
        if handler is not None:
            handler(obj, child)
    
    return obj
```

**Special case for ARObject** (base class):
```python
# Use explicit class reference to avoid processing subclass elements
handler = ARObject._DESERIALIZE_DISPATCH.get(tag)
```

**Quality Check**: Verify deserialization works correctly

---

### Step 9: Full Regeneration and Testing

**Commands**:
```bash
# Regenerate all models
python -m tools.generate_models --members --classes --enums --primitives

# Verify constants
grep -r "_XML_TAG" src/armodel2/models/M2/ | wc -l
grep -r "_DESERIALIZE_DISPATCH" src/armodel2/models/M2/ | wc -l

# Run tests
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/ -v
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/ -v
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/integration/test_binary_comparison.py -v

# Linting and type checking
ruff check src/ tools/
mypy src/
```

**Expected Results**:
- ~2,200 `_XML_TAG` constants generated
- ~2,000 `_DESERIALIZE_DISPATCH` tables generated (classes with only xml_attributes excluded)
- All tests pass
- No linting errors
- No type checking errors

---

## Decorator Handling Summary

| Decorator | Action | Reason |
|-----------|--------|--------|
| `@xml_attribute` | EXCLUDE | Handled via `element.get("ATTR")` in parent |
| `@lang_abbr` | EXCLUDE | Handled via `element.get("L")` in parent |
| `@lang_prefix("L-1")` | INCLUDE | Wrapper tag, append to list |
| `@atp_variant` | INCLUDE | Wrapper path, unwrap logic |
| `@instance_ref` | INCLUDE | -IREF suffix, flatten parameter |
| `@ref_conditional` | INCLUDE | Container tag, unwrap -REF-CONDITIONAL |
| `@xml_element_name` | INCLUDE | Custom tag from params |
| `@polymorphic` | INCLUDE | Standard pattern |

---

## Reference Type Handling

| Type | Kind | Multiplicity | XML Tag | Handler Pattern |
|------|------|--------------|---------|-----------------|
| IRef multi | iref | * | COMPONENT-IREFS | Container key, tag matching in list comprehension |
| IRef single | iref | 0..1/1 | OPERATION-IREF | Wrapper key, direct deserialize |
| IRef list (flattened) | iref | * | DATA-ELEMENT-IREF | Wrapper key, direct deserialize |
| IRef list (non-flattened) | iref | * | INNER-PORT-IREF | Wrapper key, list comprehension |
| TRef | tref | 0..1/1 | TYPE-TREF | -TREF suffix, ARRef.deserialize() |
| REF | ref | 0..1/1 | SW-ADDR-METHOD-REF | -REF suffix, ARRef.deserialize() |

---

## Expected Performance Improvements

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Name conversion calls | ~10,000 per file | 0 | 100% |
| Namespace stripping calls | ~5,000 per file | ~1,000 | 80% |
| Child element lookup | O(n) linear | O(1) dict | 90% |
| Deserialization time | Baseline | ~30-50% faster | 30-50% |
| Serialization time | Baseline | ~10-20% faster | 10-20% |

---

## Risk Mitigation

1. **Incremental implementation**: Test after each step
2. **Binary comparison tests**: Ensure exact round-trip serialization
3. **Comprehensive test suite**: Unit + integration + binary comparison
4. **Linting and type checking**: Maintain code quality
5. **Pattern matching**: Follow existing skip class patterns exactly

---

## Success Criteria

- ✅ All ~2,200 classes regenerated with `_XML_TAG` constant
- ✅ All classes with child elements have `_DESERIALIZE_DISPATCH` table
- ✅ All unit tests pass
- ✅ All integration tests pass
- ✅ All binary comparison tests pass (exact round-trip)
- ✅ No linting errors
- ✅ No type checking errors
- ✅ Performance improvement verified (30-50% faster deserialization)