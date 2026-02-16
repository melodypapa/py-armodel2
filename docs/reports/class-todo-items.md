# Class Hierarchy Analysis Report

## Overview

This document analyzes the class hierarchy for elements found in `demos/arxml/AUTOSAR_Datatypes.arxml` based on the AUTOSAR M2 model definitions in `docs/json/hierarchy.json` and `docs/json/packages/`.

## Classes Found in AUTOSAR_Datatypes.arxml

The following AUTOSAR element types were identified in the ARXML file:

1. **SW-BASE-TYPE** - Base type definitions (float32, float64, sint16, sint8, uint16, uint8, void, etc.)
2. **COMPU-METHOD** - Computation methods (boolean_Literals)
3. **DATA-CONSTR** - Data constraints (sint16, sint32, sint8, uint16, uint32, uint8, etc.)
4. **IMPLEMENTATION-DATA-TYPE** - Implementation data types (boolean, float32, float64, sint16, sint32, sint8, uint16, uint32, uint8, etc.)

## Class Hierarchy Table

| Class Name | Parent Class | Package Path | Notes |
|------------|--------------|--------------|-------|
| **SwBaseType** | BaseType | M2::MSR::AsamHdo::BaseTypes | Represents a base type used within ECU software |
| **BaseType** | ARElement | M2::MSR::AsamHdo::BaseTypes | Abstract base class for platform dependent base types |
| **CompuMethod** | ARElement | M2::MSR::AsamHdo::ComputationMethod | Specifies computation from internal to physical values |
| **DataConstr** | ARElement | M2::MSR::AsamHdo::Constraints::GlobalConstraints | Represents constraints on data |
| **DataConstrRule** | ARObject | M2::MSR::AsamHdo::Constraints::GlobalConstraints | One specific data constraint rule |
| **ImplementationDataType** | AbstractImplementationDataType | M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes | Reusable data type on implementation level |
| **AbstractImplementationDataType** | AutosarDataType | M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes | Abstract base class for ImplementationDataType |
| **AutosarDataType** | ARElement | M2::AUTOSARTemplates::GenericStructure::Datatype | Base class for AUTOSAR data types |
| **ARElement** | Identifiable | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage | AUTOSAR-specific element |
| **Identifiable** | MultilanguageReferrable | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable | Adds identifier properties |
| **MultilanguageReferrable** | Referrable | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable | Supports multilingual references |
| **Referrable** | ARObject | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable | Base class for referable objects |
| **ARObject** | (base) | M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject | Root base class for all AUTOSAR objects |

## Complete Inheritance Chains

### SwBaseType
```
ARObject
  └── Referrable
      └── MultilanguageReferrable
          └── Identifiable
              └── ARElement
                  └── BaseType (abstract)
                      └── SwBaseType
```

### CompuMethod
```
ARObject
  └── Referrable
      └── MultilanguageReferrable
          └── Identifiable
              └── ARElement
                  └── CompuMethod
```

### DataConstr
```
ARObject
  └── Referrable
      └── MultilanguageReferrable
          └── Identifiable
              └── ARElement
                  └── DataConstr
```

### ImplementationDataType
```
ARObject
  └── Referrable
      └── MultilanguageReferrable
          └── Identifiable
              └── ARElement
                  └── AutosarDataType
                      └── AbstractImplementationDataType (abstract)
                          └── ImplementationDataType
```

## Class Members/Attributes

### SwBaseType
- **Inherited from BaseType**: `baseType` (BaseTypeDefinition)

### BaseTypeDirectDefinition (referenced by SwBaseType)
- `baseTypeEncoding` (BaseTypeEncodingString)
- `baseTypeSize` (PositiveInteger)
- `byteOrder` (ByteOrderEnum)
- `memAlignment` (PositiveInteger)
- `native` (NativeDeclarationString)

### CompuMethod
- `compuInternal` (Compu)
- `compuPhysTo` (Compu)
- `displayFormatString` (DisplayFormatString)
- `unit` (Unit)

### DataConstr
- `dataConstrRules` (DataConstrRule[*])

### DataConstrRule
- `constrLevel` (Integer)
- `internalConstrs` (InternalConstrs)
- `physicalConstrs` (PhysConstrs)

### ImplementationDataType
- `dynamicArray` (String)
- `subElements` (ImplementationData[*])
- `symbolProps` (SymbolProps)
- `typeEmitter` (NameToken)
- **Inherited from AutosarDataType**: `swDataDefProps` (SwDataDefProps)

### SwDataDefProps (used by ImplementationDataType)
- `baseType` (SwBaseType)
- `compuMethod` (CompuMethod)
- `dataConstr` (DataConstr)
- `implementation` (AbstractImplementationDataType)
- `unit` (Unit)
- And many more properties for calibration, access, etc.

## Action Items

Based on the analysis, the following updates need to be made to the codebase:

1. **Verify class inheritance** - Ensure all classes have the correct parent classes as shown in the hierarchy
2. **Update class members** - Verify all attributes/properties are defined according to the package JSON files
3. **Check serialization/deserialization** - Ensure all attributes are properly handled in serialize() and deserialize() methods
4. **Update builder classes** - Verify all attributes have corresponding builder methods

## Related Files

- Source ARXML: `demos/arxml/AUTOSAR_Datatypes.arxml`
- Hierarchy definition: `docs/json/hierarchy.json`
- Type mapping: `docs/json/mapping.json`
- Package definitions: `docs/json/packages/*.json`

## Generation Date

2026-02-16