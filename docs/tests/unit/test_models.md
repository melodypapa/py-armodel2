# Unit Test Cases - Models Module
## py-armodel2 - AUTOSAR ARXML Processing Library

**Module**: `armodel.models`
**Test Files**: `tests/unit/models/test_*.py`
**Version**: 1.0
**Date**: 2026-02-17

---

## 1. Test Overview

This document describes unit tests for the `armodel.models` module, which contains automatically generated AUTOSAR model classes. The models module includes:

- **M2**: AUTOSAR M2 model definitions (1,900+ classes)
  - AUTOSARTemplates: Core AUTOSAR templates
  - MSR: Measurement, Systems, and Requirements classes

### 1.1 Test Scope
- Core model classes (ARObject, AUTOSAR, ARPackage)
- Serialization/deserialization
- Builder pattern
- Type safety and validation
- Inheritance hierarchy
- XML member metadata

### 1.2 Test Strategy
Due to the large number of generated classes (1,900+), we use a **stratified testing approach**:

1. **Core Classes**: Full test coverage for foundational classes
   - ARObject (base class)
   - AUTOSAR (root element, singleton)
   - ARPackage (package container)

2. **Representative Classes**: Sample tests for each major category
   - Primitive types
   - Data types
   - SW components
   - System elements
   - Diagnostic elements

3. **Generated Code Tests**: Automated tests for code generation
   - Verify all classes can be instantiated
   - Verify all classes have serialize/deserialize
   - Verify all classes have builders

### 1.3 Test Framework
- **Framework**: pytest
- **Python Version**: 3.9+
- **Execution**: `PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/`

---

## 2. Unit Test Cases - Core Classes

### SWUT_MODELS_001: ARObject Instantiation
**Objective**: Verify ARObject base class can be instantiated

**Requirements**: SWR_MODELS_001

**Test Steps**:
1. Create ARObject instance
2. Verify object is not None
3. Verify object type is ARObject

**Test Code**:
```python
def test_ar_object_instantiation():
    """Test that ARObject can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject

    obj = ARObject()
    assert obj is not None
    assert isinstance(obj, ARObject)
```

**Expected Result**: ARObject instance created successfully

**Status**: ✅ Implemented

---

### SWUT_MODELS_002: ARObject Serialization
**Objective**: Verify ARObject can serialize to XML

**Requirements**: SWR_MODELS_002

**Test Steps**:
1. Create ARObject instance
2. Set checksum attribute
3. Call `serialize()` with namespace
4. Verify XML element is created
5. Verify tag and namespace are correct

**Test Code**:
```python
def test_ar_object_serialize():
    """Test that ARObject can be serialized to XML."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    import xml.etree.ElementTree as ET

    obj = ARObject()
    obj.checksum = "test_checksum"
    namespace = "http://autosar.org/schema/r4.0"

    element = obj.serialize(namespace)

    assert element is not None
    assert isinstance(element, ET.Element)
    assert element.tag == f"{{{namespace}}}AROBJECT"
    assert element.get("CHECKSUM") == "test_checksum"
```

**Expected Result**: Valid XML element with correct attributes

**Status**: ✅ Implemented

---

### SWUT_MODELS_003: ARObject Deserialization
**Objective**: Verify ARObject can deserialize from XML

**Requirements**: SWR_MODELS_003

**Test Steps**:
1. Create XML element with checksum attribute
2. Call `ARObject.deserialize()`
3. Verify object is created
4. Verify checksum is correctly set

**Test Code**:
```python
def test_ar_object_deserialize():
    """Test that ARObject can be deserialized from XML."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    import xml.etree.ElementTree as ET

    namespace = "http://autosar.org/schema/r4.0"
    element = ET.Element(f"{{{namespace}}}AROBJECT")
    element.set("CHECKSUM", "test_checksum")

    obj = ARObject.deserialize(element)

    assert obj is not None
    assert isinstance(obj, ARObject)
    assert obj.checksum == "test_checksum"
```

**Expected Result**: ARObject instance with correct attributes

**Status**: ✅ Implemented

---

### SWUT_MODELS_004: ARObject XMLMember Metadata
**Objective**: Verify ARObject has correct XMLMember metadata

**Requirements**: SWR_MODELS_004

**Test Steps**:
1. Access `_xml_members` class attribute
2. Verify it is a dictionary
3. Verify checksum and timestamp are defined
4. Verify metadata values are correct

**Test Code**:
```python
def test_ar_object_xml_members():
    """Test that ARObject has correct XMLMember metadata."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    from armodel2.serialization.metadata import XMLMember

    assert hasattr(ARObject, '_xml_members')
    assert isinstance(ARObject._xml_members, dict)

    # Verify checksum member
    assert 'checksum' in ARObject._xml_members
    checksum_member = ARObject._xml_members['checksum']
    assert isinstance(checksum_member, XMLMember)
    assert checksum_member.multiplicity == "0..1"
    assert checksum_member.is_attribute is True

    # Verify timestamp member
    assert 'timestamp' in ARObject._xml_members
    timestamp_member = ARObject._xml_members['timestamp']
    assert isinstance(timestamp_member, XMLMember)
    assert timestamp_member.multiplicity == "0..1"
    assert timestamp_member.is_attribute is True
```

**Expected Result**: Correct XMLMember metadata defined

**Status**: ✅ Implemented

---

### SWUT_MODELS_005: AUTOSAR Singleton Pattern
**Objective**: Verify AUTOSAR is a singleton

**Requirements**: SWR_MODELS_005

**Test Steps**:
1. Create two AUTOSAR instances
2. Verify they are the same object (using `is` operator)
3. Verify only one instance exists

**Test Code**:
```python
def test_autosar_singleton():
    """Test that AUTOSAR is a singleton."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

    obj1 = AUTOSAR()
    obj2 = AUTOSAR()
    assert obj1 is obj2
```

**Expected Result**: Both instances are the same object

**Status**: ✅ Implemented

---

### SWUT_MODELS_006: AUTOSAR Package Management
**Objective**: Verify AUTOSAR can manage ARPackage collections

**Requirements**: SWR_MODELS_006

**Test Steps**:
1. Create AUTOSAR instance
2. Create ARPackage instance
3. Add package to AUTOSAR.ar_packages
4. Verify package is in list

**Test Code**:
```python
def test_autosar_package_management():
    """Test that AUTOSAR can manage packages."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
        ARPackageBuilder,
    )

    autosar = AUTOSAR()
    pkg = ARPackageBuilder().with_short_name("TestPackage").build()

    autosar.ar_packages.append(pkg)

    assert len(autosar.ar_packages) == 1
    assert autosar.ar_packages[0].short_name == "TestPackage"
```

**Expected Result**: Package added successfully

**Status**: ✅ Implemented

---

### SWUT_MODELS_007: AUTOSAR Serialization
**Objective**: Verify AUTOSAR can serialize with packages

**Requirements**: SWR_MODELS_002

**Test Steps**:
1. Create AUTOSAR instance
2. Add package with elements
3. Call `serialize()` with namespace
4. Verify XML contains packages

**Test Code**:
```python
def test_autosar_serialize():
    """Test that AUTOSAR can serialize with packages."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
        ARPackageBuilder,
    )
    import xml.etree.ElementTree as ET

    autosar = AUTOSAR()
    pkg = ARPackageBuilder().with_short_name("TestPackage").build()
    autosar.ar_packages.append(pkg)

    namespace = "http://autosar.org/schema/r4.0"
    element = autosar.serialize(namespace)

    assert element is not None
    assert isinstance(element, ET.Element)
    # Verify AR-PACKAGES element exists
    ar_packages_elements = element.findall(f"{{{namespace}}}AR-PACKAGES")
    assert len(ar_packages_elements) == 1
```

**Expected Result**: Valid XML with packages

**Status**: ✅ Implemented

---

### SWUT_MODELS_008: AUTOSAR Get Splitable Elements
**Objective**: Verify AUTOSAR can identify splitable elements

**Requirements**: SWR_MODELS_007

**Test Steps**:
1. Create AUTOSAR instance
2. Call `get_splitable_elements()`
3. Verify return type is list
4. Verify list is not None

**Test Code**:
```python
def test_autosar_get_splitable_elements():
    """Test getting splitable elements."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

    autosar = AUTOSAR()
    splitable = autosar.get_splitable_elements()

    assert isinstance(splitable, list)
    assert splitable is not None
```

**Expected Result**: List of splitable elements

**Status**: ✅ Implemented

---

### SWUT_MODELS_009: ARPackage Instantiation
**Objective**: Verify ARPackage can be instantiated

**Requirements**: SWR_MODELS_001

**Test Steps**:
1. Create ARPackage instance using builder
2. Verify object is created
3. Verify short_name is set

**Test Code**:
```python
def test_ar_package_instantiation():
    """Test that ARPackage can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
        ARPackageBuilder,
    )

    pkg = ARPackageBuilder().with_short_name("TestPackage").build()

    assert pkg is not None
    assert isinstance(pkg, ARPackage)
    assert pkg.short_name == "TestPackage"
```

**Expected Result**: ARPackage instance created successfully

**Status**: ✅ Implemented

---

### SWUT_MODELS_010: ARPackage Element Management
**Objective**: Verify ARPackage can manage element collections

**Requirements**: SWR_MODELS_006

**Test Steps**:
1. Create ARPackage instance
2. Add element to package
3. Verify element is in list
4. Verify element is accessible

**Test Code**:
```python
def test_ar_package_element_management():
    """Test that ARPackage can manage elements."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
        ARPackageBuilder,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
        ARObject,
    )

    pkg = ARPackageBuilder().with_short_name("TestPackage").build()
    element = ARObject()
    pkg.elements.append(element)

    assert len(pkg.elements) == 1
    assert pkg.elements[0] is element
```

**Expected Result**: Element added successfully

**Status**: ✅ Implemented

---

## 3. Unit Test Cases - Representative Classes

### SWUT_MODELS_011: SwBaseType Instantiation
**Objective**: Verify SwBaseType can be instantiated

**Category**: Base Types

**Test Code**:
```python
def test_sw_base_type_instantiation():
    """Test that SwBaseType can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.PrimitiveTypes.sw_base_type import (
        SwBaseType,
        SwBaseTypeBuilder,
    )

    obj = SwBaseTypeBuilder().with_short_name("TestType").with_category("FIXED").build()

    assert obj is not None
    assert isinstance(obj, SwBaseType)
    assert obj.short_name == "TestType"
    assert obj.category == "FIXED"
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_012: ImplementationDataType Instantiation
**Objective**: Verify ImplementationDataType can be instantiated

**Category**: Data Types

**Test Code**:
```python
def test_implementation_data_type_instantiation():
    """Test that ImplementationDataType can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.SwComponentTemplate.Datatype.Datatypes.implementation_data_type import (
        ImplementationDataType,
        ImplementationDataTypeBuilder,
    )

    obj = ImplementationDataTypeBuilder().with_short_name("TestType").build()

    assert obj is not None
    assert isinstance(obj, ImplementationDataType)
    assert obj.short_name == "TestType"
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_013: SwComponentType Instantiation
**Objective**: Verify SwComponentType can be instantiated

**Category**: SW Components

**Test Code**:
```python
def test_sw_component_type_instantiation():
    """Test that SwComponentType can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.SwComponentTemplate.SwComponentTypes.sw_component_type import (
        SwComponentType,
        SwComponentTypeBuilder,
    )

    obj = SwComponentTypeBuilder().with_short_name("TestComponent").build()

    assert obj is not None
    assert isinstance(obj, SwComponentType)
    assert obj.short_name == "TestComponent"
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_014: RunnableEntity Instantiation
**Objective**: Verify RunnableEntity can be instantiated

**Category**: SW Components

**Test Code**:
```python
def test_runnable_entity_instantiation():
    """Test that RunnableEntity can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.SwComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
        RunnableEntityBuilder,
    )

    obj = RunnableEntityBuilder().with_short_name("TestRunnable").build()

    assert obj is not None
    assert isinstance(obj, RunnableEntity)
    assert obj.short_name == "TestRunnable"
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_015: DiagnosticTroubleCode Instantiation
**Objective**: Verify DiagnosticTroubleCode can be instantiated

**Category**: Diagnostic

**Test Code**:
```python
def test_diagnostic_trouble_code_instantiation():
    """Test that DiagnosticTroubleCode can be instantiated."""
    from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code_uds import (
        DiagnosticTroubleCodeUDS,
        DiagnosticTroubleCodeUDSBuilder,
    )

    obj = DiagnosticTroubleCodeUDSBuilder().with_short_name("TestDTC").build()

    assert obj is not None
    assert isinstance(obj, DiagnosticTroubleCodeUDS)
    assert obj.short_name == "TestDTC"
```

**Status**: 🚧 To Implement

---

## 4. Unit Test Cases - Generated Code Validation

### SWUT_MODELS_100: All Classes Can Be Instantiated
**Objective**: Verify all generated classes can be instantiated

**Category**: Automated Validation

**Test Steps**:
1. Iterate through all generated classes
2. Attempt to instantiate each class
3. Verify no instantiation errors
4. Report failures

**Test Code**:
```python
def test_all_classes_instantiable():
    """Test that all generated classes can be instantiated."""
    import inspect
    from armodel2.models.M2 import AUTOSARTemplates, MSR

    # Collect all classes from AUTOSARTemplates and MSR
    all_classes = []
    for module_name in dir(AUTOSARTemplates):
        module = getattr(AUTOSARTemplates, module_name)
        if inspect.ismodule(module):
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and hasattr(obj, '__init__'):
                    all_classes.append(obj)

    # Try to instantiate each class
    failures = []
    for cls in all_classes:
        try:
            # Skip abstract classes (usually detected by having only abstract methods)
            # Skip classes that require mandatory parameters
            instance = cls()
        except Exception as e:
            failures.append((cls.__name__, str(e)))

    if failures:
        pytest.fail(f"Failed to instantiate {len(failures)} classes: {failures[:5]}")
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_101: All Classes Have Serialize Method
**Objective**: Verify all generated classes have serialize method

**Category**: Automated Validation

**Test Steps**:
1. Iterate through all generated classes
2. Verify serialize method exists
3. Verify serialize method signature is correct

**Test Code**:
```python
def test_all_classes_have_serialize():
    """Test that all generated classes have serialize method."""
    import inspect
    from armodel2.models.M2 import AUTOSARTemplates

    # Collect all classes
    all_classes = []
    for module_name in dir(AUTOSARTemplates):
        module = getattr(AUTOSARTemplates, module_name)
        if inspect.ismodule(module):
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    all_classes.append(obj)

    # Verify serialize method exists
    failures = []
    for cls in all_classes:
        if not hasattr(cls, 'serialize'):
            failures.append(cls.__name__)
        else:
            # Verify signature
            sig = inspect.signature(cls.serialize)
            if 'namespace' not in sig.parameters:
                failures.append(f"{cls.__name__} (invalid signature)")

    if failures:
        pytest.fail(f"Missing serialize method in {len(failures)} classes")
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_102: All Classes Have Deserialize Method
**Objective**: Verify all generated classes have deserialize method

**Category**: Automated Validation

**Test Steps**:
1. Iterate through all generated classes
2. Verify deserialize method exists
3. Verify deserialize is a classmethod

**Test Code**:
```python
def test_all_classes_have_deserialize():
    """Test that all generated classes have deserialize method."""
    import inspect
    from armodel2.models.M2 import AUTOSARTemplates

    # Collect all classes
    all_classes = []
    for module_name in dir(AUTOSARTemplates):
        module = getattr(AUTOSARTemplates, module_name)
        if inspect.ismodule(module):
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    all_classes.append(obj)

    # Verify deserialize method exists
    failures = []
    for cls in all_classes:
        if not hasattr(cls, 'deserialize'):
            failures.append(cls.__name__)
        else:
            # Verify it's a classmethod
            if not isinstance(inspect.getattr_static(cls, 'deserialize'), classmethod):
                failures.append(f"{cls.__name__} (not a classmethod)")

    if failures:
        pytest.fail(f"Missing or invalid deserialize method in {len(failures)} classes")
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_103: All Classes Have Builder
**Objective**: Verify all generated classes have builder class

**Category**: Automated Validation

**Test Steps**:
1. Iterate through all generated classes
2. Verify builder class exists
3. Verify builder naming convention

**Test Code**:
```python
def test_all_classes_have_builder():
    """Test that all generated classes have builder class."""
    import inspect
    from armodel2.models.M2 import AUTOSARTemplates

    # Collect all classes
    all_classes = []
    for module_name in dir(AUTOSARTemplates):
        module = getattr(AUTOSARTemplates, module_name)
        if inspect.ismodule(module):
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    all_classes.append(obj)

    # Verify builder exists
    failures = []
    for cls in all_classes:
        builder_name = f"{cls.__name__}Builder"
        module = inspect.getmodule(cls)
        if module and not hasattr(module, builder_name):
            failures.append(cls.__name__)

    if failures:
        pytest.fail(f"Missing builder for {len(failures)} classes")
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_104: All Classes Have XMLMember Metadata
**Objective**: Verify all generated classes have _xml_members metadata

**Category**: Automated Validation

**Test Steps**:
1. Iterate through all generated classes
2. Verify _xml_members attribute exists
3. Verify it's a dictionary

**Test Code**:
```python
def test_all_classes_have_xml_members():
    """Test that all generated classes have _xml_members metadata."""
    import inspect
    from armodel2.models.M2 import AUTOSARTemplates

    # Collect all classes
    all_classes = []
    for module_name in dir(AUTOSARTemplates):
        module = getattr(AUTOSARTemplates, module_name)
        if inspect.ismodule(module):
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    all_classes.append(obj)

    # Verify _xml_members exists
    failures = []
    for cls in all_classes:
        if not hasattr(cls, '_xml_members'):
            failures.append(cls.__name__)
        else:
            if not isinstance(cls._xml_members, dict):
                failures.append(f"{cls.__name__} (not a dict)")

    if failures:
        pytest.fail(f"Missing or invalid _xml_members in {len(failures)} classes")
```

**Status**: 🚧 To Implement

---

## 5. Unit Test Cases - Primitive Types

### SWUT_MODELS_200: Primitive Type Definitions
**Objective**: Verify all primitive types are defined

**Category**: Primitive Types

**Test Steps**:
1. Import primitive types module
2. Verify expected types exist
3. Verify type mappings are correct

**Test Code**:
```python
def test_primitive_types_defined():
    """Test that all primitive types are defined."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
        String,
        Integer,
        Float,
        Boolean,
    )

    # Verify types are defined
    assert String is not None
    assert Integer is not None
    assert Float is not None
    assert Boolean is not None

    # Verify they map to Python types
    assert String == str
    assert Integer == int
    assert Float == float
    assert Boolean == bool
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_201: String Primitive Usage
**Objective**: Verify String primitive can be used in attributes

**Category**: Primitive Types

**Test Code**:
```python
def test_string_primitive_usage():
    """Test that String primitive can be used."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
        ARObject,
    )
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String

    obj = ARObject()
    obj.checksum = String("test_checksum")

    assert obj.checksum == "test_checksum"
    assert isinstance(obj.checksum, str)
```

**Status**: 🚧 To Implement

---

## 6. Unit Test Cases - Type Safety

### SWUT_MODELS_300: Optional Type Initialization
**Objective**: Verify Optional types initialize to None

**Category**: Type Safety

**Test Code**:
```python
def test_optional_initialization():
    """Test that Optional types initialize to None."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import (
        ARObject,
    )

    obj = ARObject()

    # checksum is Optional[String]
    assert obj.checksum is None
    # timestamp is Optional[DateTime]
    assert obj.timestamp is None
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_301: List Type Initialization
**Objective**: Verify list types initialize to empty list

**Category**: Type Safety

**Test Code**:
```python
def test_list_initialization():
    """Test that list types initialize to empty list."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

    autosar = AUTOSAR()

    # ar_packages is list[ARPackage]
    assert autosar.ar_packages == []
    assert isinstance(autosar.ar_packages, list)
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_302: Type Annotations Correctness
**Objective**: Verify type annotations are correct

**Category**: Type Safety

**Test Code**:
```python
def test_type_annotations():
    """Test that type annotations are correct."""
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR
    from typing import get_type_hints
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

    hints = get_type_hints(AUTOSAR)

    # Verify ar_packages is list[ARPackage]
    assert 'ar_packages' in hints
    assert hints['ar_packages'] == list[ARPackage]
```

**Status**: 🚧 To Implement

---

## 7. Unit Test Cases - Inheritance

### SWUT_MODELS_400: ARObject Inheritance Chain
**Objective**: Verify inheritance from ARObject

**Category**: Inheritance

**Test Code**:
```python
def test_arobject_inheritance():
    """Test that classes inherit from ARObject."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

    autosar = AUTOSAR()
    assert isinstance(autosar, ARObject)
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_401: Method Resolution Order
**Objective**: Verify MRO is correct

**Category**: Inheritance

**Test Code**:
```python
def test_method_resolution_order():
    """Test that MRO is correct."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import ARPackage

    mro = ARPackage.__mro__
    assert ARObject in mro
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_402: XMLMember Inheritance
**Objective**: Verify XMLMember metadata is inherited

**Category**: Inheritance

**Test Code**:
```python
def test_xml_member_inheritance():
    """Test that XMLMember metadata is inherited correctly."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    from armodel2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.autosar import AUTOSAR

    # AUTOSAR should inherit ARObject's _xml_members
    assert 'checksum' in ARObject._xml_members

    # The serialization framework should collect from entire hierarchy
    autosar = AUTOSAR()
    namespace = "http://autosar.org/schema/r4.0"
    element = autosar.serialize(namespace)

    # Should be able to serialize inherited attributes
    assert element is not None
```

**Status**: 🚧 To Implement

---

## 8. Unit Test Cases - Error Handling

### SWUT_MODELS_500: Invalid XML Deserialization
**Objective**: Verify error handling for invalid XML

**Category**: Error Handling

**Test Code**:
```python
def test_invalid_xml_deserialization():
    """Test that invalid XML is handled gracefully."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
    import xml.etree.ElementTree as ET

    namespace = "http://autosar.org/schema/r4.0"
    element = ET.Element(f"{{{namespace}}}AROBJECT")

    # Element with invalid attribute
    element.set("INVALID_ATTR", "value")

    # Should handle gracefully (ignore unknown attributes)
    obj = ARObject.deserialize(element)
    assert obj is not None
```

**Status**: 🚧 To Implement

---

### SWUT_MODELS_501: Missing Required Attribute
**Objective**: Verify behavior when required attribute is missing

**Category**: Error Handling

**Test Code**:
```python
def test_missing_required_attribute():
    """Test behavior when required attribute is missing."""
    from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable.referrable import Referrable
    import xml.etree.ElementTree as ET

    namespace = "http://autosar.org/schema/r4.0"
    element = ET.Element(f"{{{namespace}}}REFERRABLE")

    # short_name is required (multiplicity 1)
    # XML is missing SHORT-NAME element

    # Should create object with None or empty value
    obj = Referrable.deserialize(element)
    assert obj is not None
    # short_name may be None or empty string
```

**Status**: 🚧 To Implement

---

## 9. Test Execution

### 9.1 Run All Models Unit Tests
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/ -v
```

### 9.2 Run Core Class Tests
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object.py tests/unit/models/test_autosar.py -v
```

### 9.3 Run Specific Test
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/test_ar_object.py::test_ar_object_serialize -v
```

### 9.4 Run with Coverage
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/ --cov=src/armodel2/models --cov-report=term
```

### 9.5 Run Generated Code Validation
```bash
PYTHONPATH=/Users/ray/Workspace/py-armodel2/src python -m pytest tests/unit/models/ -k "test_all_classes" -v
```

---

## 10. Test Coverage Summary

| Category                  | Test Cases | Implemented | Status   |
| ------------------------- | ---------- | ----------- | -------- |
| Core Classes              | 10         | 2           | 🚧 20%    |
| Representative Classes    | 5          | 0           | 🚧 0%     |
| Generated Code Validation | 5          | 0           | 🚧 0%     |
| Primitive Types           | 2          | 0           | 🚧 0%     |
| Type Safety               | 3          | 0           | 🚧 0%     |
| Inheritance               | 3          | 0           | 🚧 0%     |
| Error Handling            | 2          | 0           | 🚧 0%     |
| **Total**                 | **30**     | **2**       | **🚧 7%** |

**Note**: Coverage is intentionally low for generated classes. Focus is on:
1. Core functionality (ARObject, AUTOSAR, ARPackage)
2. Code generation validation
3. Type safety
4. Serialization framework

---

## 11. Requirements Traceability

| Requirement ID | Test Cases                                        | Coverage |
| -------------- | ------------------------------------------------- | -------- |
| SWR_MODELS_001 | SWUT_MODELS_001, SWUT_MODELS_009, SWUT_MODELS_100 | 🚧        |
| SWR_MODELS_002 | SWUT_MODELS_002, SWUT_MODELS_007, SWUT_MODELS_101 | 🚧        |
| SWR_MODELS_003 | SWUT_MODELS_003, SWUT_MODELS_102                  | 🚧        |
| SWR_MODELS_004 | SWUT_MODELS_004, SWUT_MODELS_104                  | 🚧        |
| SWR_MODELS_005 | SWUT_MODELS_005                                   | ✅        |
| SWR_MODELS_006 | SWUT_MODELS_006, SWUT_MODELS_010                  | 🚧        |
| SWR_MODELS_007 | SWUT_MODELS_008                                   | ✅        |
| SWR_MODELS_008 | SWUT_MODELS_011                                   | 🚧        |
| SWR_MODELS_009 | SWUT_MODELS_012                                   | 🚧        |
| SWR_MODELS_010 | SWUT_MODELS_013, SWUT_MODELS_014                  | 🚧        |
| SWR_MODELS_011 | SWUT_MODELS_015                                   | 🚧        |
| SWR_MODELS_012 | SWUT_MODELS_200                                   | 🚧        |
| SWR_MODELS_013 | SWUT_MODELS_300, SWUT_MODELS_301, SWUT_MODELS_302 | 🚧        |
| SWR_MODELS_014 | SWUT_MODELS_400, SWUT_MODELS_401, SWUT_MODELS_402 | 🚧        |

---

## 12. Testing Strategy for Generated Code

### 12.1 Why Not Test All 1,900+ Classes?

Testing every generated class would be:
- **Impractical**: 1,900+ classes × 3-5 tests each = 5,000-10,000 tests
- **Redundant**: All classes follow the same pattern
- **Unmaintainable**: Regenerating tests for every code change

### 12.2 Stratified Testing Approach

**Level 1: Core Classes (10 tests)**
- Full test coverage for ARObject, AUTOSAR, ARPackage
- Tests serialization, deserialization, builders
- Tests inheritance and type safety

**Level 2: Representative Classes (5 tests)**
- Sample tests from each major category
- Ensures generation works for different class types
- Catches category-specific issues

**Level 3: Automated Validation (5 tests)**
- Verify all classes can be instantiated
- Verify all classes have serialize/deserialize
- Verify all classes have builders
- Verify all classes have XMLMember metadata

**Level 4: Integration Tests (separate)**
- Test real-world ARXML files
- Test reader/writer integration
- Test complete workflows

### 12.3 Code Generation Tests

The code generator (`tools/generate_models.py`) should have its own tests:
- Test generation of different class types
- Test generation of serialize/deserialize methods
- Test generation of builder classes
- Test generation of XMLMember metadata

See `tests/test_generate_models.py` for code generator tests.

---

## 13. Best Practices for Model Testing

### 13.1 Use Builders for Complex Objects

```python
# Good
pkg = ARPackageBuilder().with_short_name("TestPackage").build()

# Avoid
pkg = ARPackage()
pkg.short_name = "TestPackage"
```

### 13.2 Test Serialization Round-Trip

```python
def test_serialization_round_trip():
    """Test that serialize/deserialize round-trip works."""
    original = ARPackageBuilder().with_short_name("TestPackage").build()

    namespace = "http://autosar.org/schema/r4.0"
    element = original.serialize(namespace)
    restored = ARPackage.deserialize(element)

    assert restored.short_name == original.short_name
```

### 13.3 Test Optional and List Types

```python
def test_optional_and_list_types():
    """Test Optional and list type handling."""
    autosar = AUTOSAR()

    # Optional types should initialize to None
    assert autosar.admin_data is None

    # List types should initialize to empty list
    assert autosar.ar_packages == []
```

### 13.4 Use Fixtures for Common Setup

```python
@pytest.fixture
def sample_autosar():
    """Create sample AUTOSAR object for testing."""
    autosar = AUTOSAR()
    pkg = ARPackageBuilder().with_short_name("TestPackage").build()
    autosar.ar_packages.append(pkg)
    return autosar

def test_with_fixture(sample_autosar):
    assert len(sample_autosar.ar_packages) == 1
```

---

**Document History**:
| Version | Date       | Author     | Changes                                          |
| ------- | ---------- | ---------- | ------------------------------------------------ |
| 1.0     | 2026-02-17 | melodypapa | Initial version with stratified testing approach |