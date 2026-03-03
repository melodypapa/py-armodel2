# AUTOSAR Model Data Analysis Report
**Generated:** 2026-03-02
**Source:** `docs/json/packages/`

---
## Executive Summary

This report provides a comprehensive analysis of all AUTOSAR model classes,enumerations, and primitive types defined in the JSON schema mapping files.

### Key Statistics

| Metric | Count |
|--------|-------|
| **Total Classes** | 1,623 |
| **Total Enumerations** | 265 |
| **Total Enumeration Literals** | 969 |
| **Total Primitives** | 50 |
| **Total JSON Files** | 349 |

## 1. Classes Analysis

### 1.1 Overview

- **Total Classes:** 1,623
- **Total Files:** 254
- **Abstract Classes:** 235 (14.5%)
- **Concrete Classes:** 1,388 (85.5%)
- **Average Attributes per Class:** 2.6

### 1.2 Maturity Levels

| Maturity | Count | Percentage |
|----------|-------|------------|
| **Reviewed** | 30 | 1.8% |
| **Draft** | 1,592 | 98.1% |

### 1.3 Special Patterns

- **atp_variant Classes:** 0
- **atp_mixed Classes:** 0
- **Polymorphic Classes:** 232

#### Polymorphic Classes (Top 20)

| Class Name | Package | Subclasses |
|------------|---------|------------|
| `Identifiable` | Identifiable | 224 |
| `ARElement` | ARPackage | 121 |
| `DiagnosticCommonElement` | CommonDiagnostics | 45 |
| `AtpBlueprint` | AbstractBlueprintStructure | 37 |
| `AtpBlueprintable` | AbstractBlueprintStructure | 36 |
| `AtpInstanceRef` | AbstractStructure | 36 |
| `DiagnosticServiceClass` | CommonService | 32 |
| `ServiceNeeds` | ServiceNeeds | 29 |
| `AtpStructureElement` | AbstractStructure | 29 |
| `DiagnosticServiceInstance` | CommonService | 25 |
| `DiagnosticMapping` | DiagnosticMapping | 23 |
| `DiagnosticCapabilityElement` | ServiceNeeds | 23 |
| `Paginateable` | PaginationAndView | 22 |
| `Referrable` | Identifiable | 20 |
| `FibexElement` | FibexCore | 20 |
| `RTEEvent` | RTEEvents | 16 |
| `Describable` | Identifiable | 13 |
| `BswScheduleEvent` | BswBehavior | 10 |
| `IPdu` | CoreCommunication | 9 |
| `TpConfig` | TransportProtocols | 9 |

### 1.4 Top Packages by Class Count (Top 20)

| Rank | Package | Classes |
|------|---------|---------|
| 1 | EthernetTopology | 79 |
| 2 | ServiceNeeds | 71 |
| 3 | CoreCommunication | 41 |
| 4 | ECUCParameterDefTemplate | 40 |
| 5 | BswBehavior | 37 |
| 6 | TransportProtocols | 32 |
| 7 | PortInterface | 31 |
| 8 | TimingDescription | 30 |
| 9 | Dds | 25 |
| 10 | SecurityExtractTemplate | 24 |
| 11 | Data | 23 |
| 12 | Transformer | 23 |
| 13 | Constants | 23 |
| 14 | Communication | 23 |
| 15 | NetworkManagement | 23 |
| 16 | SecureCommunication | 22 |
| 17 | ServiceInstances | 20 |
| 18 | LinCommunication | 20 |
| 19 | CommonDiagnostics | 18 |
| 20 | RTEEvents | 18 |

### 1.5 Top Templates by Class Count (Top 20)

| Rank | Template | Classes |
|------|----------|---------|
| 1 | AUTOSARTemplates | 1479 |

### 1.6 Classes with Most Attributes (Top 20)

| Rank | Class Name | Attributes |
|------|------------|------------|
| 1 | `FlexrayCluster` | 33 |
| 2 | `SwDataDefProps` | 30 |
| 3 | `FlexrayCommunicationController` | 28 |
| 4 | `EcuInstance` | 26 |
| 5 | `SystemMapping` | 24 |
| 6 | `BswInternalBehavior` | 22 |
| 7 | `NvBlockNeeds` | 22 |
| 8 | `Area` | 22 |
| 9 | `FlexrayArTpChannel` | 19 |
| 10 | `RunnableEntity` | 18 |
| 11 | `EndToEndTransformationDescription` | 18 |
| 12 | `SwcInternalBehavior` | 17 |
| 13 | `CanControllerXlConfigurationRequirements` | 16 |
| 14 | `CanTpConnection` | 16 |
| 15 | `TcpProps` | 15 |
| 16 | `Graphic` | 15 |
| 17 | `Implementation` | 15 |
| 18 | `CouplingPort` | 14 |
| 19 | `ConsumedServiceInstance` | 14 |
| 20 | `BswModuleDescription` | 14 |

## 2. Enumerations Analysis

### 2.1 Overview

- **Total Enumeration Types:** 265
- **Total Files:** 88
- **Total Literals:** 969
- **Average Literals per Enum:** 3.7

### 2.2 Maturity Levels

| Maturity | Count | Percentage |
|----------|-------|------------|
| **Reviewed** | 0 | 0% |
| **Draft** | 265 | 100% |

### 2.2 Largest Enumerations (Top 20)

| Rank | Enum Name | Package | Literals |
|------|-----------|---------|----------|
| 1 | `LEnum` | LanguageDataModel | 136 |
| 2 | `ServiceProviderEnum` | ServiceNeeds | 26 |
| 3 | `CycleRepetitionType` | CoreTopology | 14 |
| 4 | `GraphicFitEnum` | Figure | 14 |
| 5 | `IEEE1722TpAafNominalRateEnum` | IEEE1722TpAv | 12 |
| 6 | `IEEE1722TpRvfColorSpaceEnum` | IEEE1722TpAv | 9 |
| 7 | `GraphicNotationEnum` | Figure | 9 |
| 8 | `DiagnosticResponseOnEventActionEnum` | ResponseOnEvent | 7 |
| 9 | `TtcanTriggerType` | TtcanCommunication | 7 |
| 10 | `SwImplPolicyEnum` | DataDefProperties | 7 |
| 11 | `MemorySectionType` | AuxillaryObjects | 7 |
| 12 | `DataFilterTypeEnum` | Filter | 7 |
| 13 | `SecurityEventReportingModeEnum` | SecurityExtractTemplate | 7 |
| 14 | `DataTypePolicyEnum` | DataMapping | 7 |
| 15 | `FlexrayNmScheduleVariant` | NetworkManagement | 7 |
| 16 | `LogTraceDefaultLogLevelEnum` | Dlt | 7 |
| 17 | `CanTpAddressingFormatType` | TransportProtocols | 7 |
| 18 | `FrameEnum` | OasisExchangeTable | 6 |
| 19 | `FullBindingTimeEnum` | ModelRestrictionTypes | 6 |
| 20 | `OperationCycleTypeEnum` | ServiceNeeds | 6 |

### 2.3 Smallest Enumerations (Top 20)

| Rank | Enum Name | Package | Literals |
|------|-----------|---------|----------|
| 1 | `DiagnosticRoutineTypeEnum` | ServiceNeeds | 0 |
| 2 | `ServiceDiagnosticRelevanceEnum` | ServiceNeeds | 0 |
| 3 | `EndToEndProfileBehaviorEnum` | Transformer | 0 |
| 4 | `DiagPduType` | CoreCommunication | 0 |
| 5 | `DiagnosticEventCombinationReportingBehaviorEnum` | DiagnosticCommonProps | 1 |
| 6 | `DdsDurabilityKindEnum` | Dds | 1 |
| 7 | `DdsDurabilityServiceHistoryKindEnum` | Dds | 1 |
| 8 | `DdsOwnershipKindEnum` | Dds | 1 |
| 9 | `DdsLivenessKindEnum` | Dds | 1 |
| 10 | `DdsReliabilityKindEnum` | Dds | 1 |
| 11 | `DdsDestinationOrderKindEnum` | Dds | 1 |
| 12 | `DdsHistoryKindEnum` | Dds | 1 |
| 13 | `IEEE1722TpRvfPixelDepthEnum` | IEEE1722TpAv | 1 |
| 14 | `IEEE1722TpRvfPixelFormatEnum` | IEEE1722TpAv | 1 |
| 15 | `ServerArgumentImplPolicyEnum` | PortInterface | 1 |
| 16 | `ModeErrorReactionPolicyEnum` | ModeDeclaration | 1 |
| 17 | `LetDataExchangeParadigmEnum` | ExecutionOrderConstraint | 1 |
| 18 | `PulseTestEnum` | ApplicationAttributes | 1 |
| 19 | `DataExchangePointKind` | DataExchangePoint | 1 |
| 20 | `ExecutionTimeTypeEnum` | ExecutionTimeConstraint | 1 |

### 2.4 Top Packages by Enum Count (Top 20)

| Rank | Package | Enums |
|------|---------|-------|
| 1 | ServiceNeeds | 18 |
| 2 | EthernetTopology | 16 |
| 3 | SecureCommunication | 13 |
| 4 | TimingDescription | 12 |
| 5 | InlineAttributeEnums | 12 |
| 6 | CoreCommunication | 11 |
| 7 | IEEE1722TpAv | 9 |
| 8 | Dds | 7 |
| 9 | ServiceInstances | 6 |
| 10 | Transformer | 6 |
| 11 | DiagnosticTroubleCode | 6 |
| 12 | OasisExchangeTable | 5 |
| 13 | DiagnosticEvent | 5 |
| 14 | ApplicationAttributes | 5 |
| 15 | Communication | 5 |
| 16 | GlobalTime | 4 |
| 17 | RptSupport | 4 |
| 18 | ECUCParameterDefTemplate | 4 |
| 19 | PrimitiveTypes | 4 |
| 20 | BswInterfaces | 4 |

## 3. Primitives Analysis

### 3.1 Overview

- **Total Primitives:** 50
- **Total Files:** 7

### 3.2 Maturity Levels

| Maturity | Count | Percentage |
|----------|-------|------------|
| **Reviewed** | 0 | 0% |
| **Draft** | 50 | 100% |

### 3.2 Primitives by Category

| Category | Count |
|----------|-------|
| **Other** | 19 |
| **String-based** | 18 |
| **Numeric** | 7 |
| **Specialized Types** | 4 |
| **Enumeration Proxy** | 2 |

#### String-based Primitives

- `AnyVersionString`
- `BaseTypeEncodingString`
- `CategoryString`
- `DiagRequirementIdString`
- `DisplayFormatString`
- `Ip4AddressString`
- `Ip6AddressString`
- `MacAddressString`
- `MimeTypeString`
- `NativeDeclarationString`
- `RevisionLabelString`
- `String`
- `StrongRevisionLabelString`
- `SymbolString`
- `TableSeparatorString`
- `UriString`
- `VerbatimString`
- `VerbatimStringPlain`

#### Numeric Primitives

- `Boolean`
- `Float`
- `Integer`
- `Numerical`
- `PositiveInteger`
- `PositiveUnlimitedInteger`
- `UnlimitedInteger`

### 3.3 Primitives by Package

| Rank | Package | Primitives |
|------|---------|------------|
| 1 | PrimitiveTypes | 42 |
| 2 | RecordLayout | 3 |
| 3 | PaginationAndView | 1 |
| 4 | InlineTextElements | 1 |
| 5 | BaseTypes | 1 |
| 6 | OasisExchangeTable | 1 |
| 7 | InlineAttributeEnums | 1 |

## 4. Summary Statistics

### 4.1 File Distribution

| File Type | Count |
|-----------|-------|
| **Classes Files (*.classes.json)** | 254 |
| **Enums Files (*.enums.json)** | 88 |
| **Primitives Files (*.primitives.json)** | 7 |
| **Total** | 349 |

### 4.2 AUTOSAR Templates Coverage

The following AUTOSAR templates are represented in the JSON data:

- **AUTOSARTemplates**: 1479 classes

## 5. Quality Metrics

### 5.1 Code Quality Indicators

| Metric | Value | Assessment |
|--------|-------|------------|
| **Classes Maturity** | 1.8% reviewed | ✗ Low |
| **Enumerations Maturity** | 0% reviewed | ✗ Low |
| **Primitives Maturity** | 0% reviewed | ✗ Low |
| **Overall Maturity** | 1.5% reviewed | ✗ Low |
| **Abstract Classes** | 14.5% | ⚠ Review |
| **Avg Attributes/Class** | 2.6 | ✓ Reasonable |
| **Avg Literals/Enum** | 3.7 | ✓ Concise |

## 6. Key Findings

### 6.1 Scale and Complexity

- The AUTOSAR model defines **1,623 classes**, indicating a comprehensive  and detailed meta-model covering all aspects of automotive software architecture.
- With **265 enumerations** containing **969 literals**,  the model provides rich type safety and semantic clarity.
- **50 primitive types** form the foundation of the type system.

### 6.2 Maturity Status

- **Classes:** Only 1.8% (30 out of 1,623) are marked as 'reviewed', 98.1% remain in 'draft' status
- **Enumerations:** All 265 enumerations (100%) are in 'draft' status
- **Primitives:** All 50 primitives (100%) are in 'draft' status
- **Overall:** Only 1.5% (30 out of 1,938 total elements) are marked as 'reviewed'
- This indicates ongoing development with significant room for improvement across all element types

### 6.3 Special Patterns

- **0 classes** use the atp_variant pattern for variation point handling.
- **0 classes** use the atp_mixed pattern for mixed content.
- **232 classes** exhibit polymorphic behavior with multiple subclasses.

### 6.4 Template Distribution

The most represented templates in the meta-model:

1. **AUTOSARTemplates**: 1479 classes (91.1%)

## 7. Recommendations

### 7.1 Improve Maturity Status

- Prioritize review of the remaining draft elements to increase overall maturity:
  - **Classes:** 1,593 classes remaining in draft status (98.1%)
  - **Enumerations:** 265 enumerations remaining in draft status (100%)
  - **Primitives:** 50 primitives remaining in draft status (100%)
- Focus on elements in frequently used templates (SWComponentTemplate, SystemTemplate, etc.)
- Establish a formal review process for new elements added to the meta-model
- Create a maturity review schedule with milestones for high-priority elements

### 7.3 Documentation

- Ensure all classes have comprehensive documentation, especially polymorphic ones.
- Document the usage patterns for atp_variant and atp_mixed classes.
- Provide examples for complex enumeration values.

## 8. Review Items Lists

### 8.1 Classes Review Items (30 classes)

The following 30 classes have been marked as "reviewed" and are considered production-ready:

| # | Class Name | Package | Note |
|---|------------|---------|------|
| 1 | `AbstractAccessPoint` | AccessCount | Access point abstraction |
| 2 | `AsynchronousServerCallPoint` | ServerCall | Async server call handling |
| 3 | `AutosarVariableRef` | DataElements | AUTOSAR variable reference |
| 4 | `BswServiceDependency` | BswInterfaces | BSW service dependency |
| 5 | `ClientServerOperation` | PortInterface | Client-server operation |
| 6 | `DataPrototype` | DataPrototypes | Data prototype definition |
| 7 | `DataReceivedEvent` | RTEEvents | Data received event |
| 8 | `Identifiable` | Identifiable | Identifiable base class |
| 9 | `MultilanguageReferrable` | Identifiable | Multilanguage support |
| 10 | `NvBlockDescriptor` | NvBlockComponent | NV block descriptor |
| 11 | `NvBlockNeeds` | ServiceNeeds | NV block configuration needs |
| 12 | `ParameterAccess` | DataElements | Parameter access definition |
| 13 | `PerInstanceMemory` | SwcInternalBehavior | Per-instance memory |
| 14 | `PortAPIOption` | PortAPIOptions | Port API options |
| 15 | `PortDefinedArgumentValue` | PortAPIOptions | Port argument value |
| 16 | `ROperationInAtomicSwcInstanceRef` | InstanceRefs | R-port instance reference |
| 17 | `RTEEvent` | RTEEvents | RTE event |
| 18 | `RVariableInAtomicSwcInstanceRef` | InstanceRefs | R-variable instance reference |
| 19 | `Referrable` | Identifiable | Referrable base class |
| 20 | `RoleBasedDataAssignment` | ServiceMapping | Role-based data assignment |
| 21 | `RoleBasedDataTypeAssignment` | ServiceMapping | Role-based data type assignment |
| 22 | `RunnableEntity` | SwcInternalBehavior | Runnable entity |
| 23 | `ServerCallPoint` | ServerCall | Server call point |
| 24 | `ServiceNeeds` | ServiceNeeds | Service needs base class |
| 25 | `SwcInternalBehavior` | SwcInternalBehavior | SWC internal behavior |
| 2 6 | `SwcModeSwitchEvent` | SwcInternalBehavior | SWC mode switch event |
| 27 | `SwcServiceDependency` | ServiceMapping | SWC service dependency |
| 28 | `SynchronousServerCallPoint` | ServerCall | Sync server call handling |
| 29 | `ValueSpecification` | FormulaLanguage | Value specification |
| 30 | `VariableAccess` | DataElements | Variable access definition |
| 31 | `VariableInAtomicSWCTypeInstanceRef` | InstanceRefs | Variable instance reference |

### 8.2 Enumerations Review Items (1 enumeration)

| # | Enum Name | Package | Literals |
|---|-----------|---------|----------|
| 1 | `RteApiReturnValueProvisionEnum` | SwcInternalBehavior | 3 literals |

### 8.3 Primitives Review Items (0 primitives)

No primitives have been marked as "reviewed" yet.

## 9. Draft Items Lists

### 9.1 Classes Draft Items (Top 20 of 1,593)

The following classes are in "draft" status and require review:

| # | Class Name | Package | Priority Recommendation |
|---|------------|---------|------------------------|
| 1 | `ARElement` | ArObject | High - Core base class |
| 2 | `ARList` | BlockElements | High - Documentation structure |
| 3 | `ARObject` | ArObject | Critical - Root base class |
| 4 | `ARPackage` | ARPackage | Critical - Package structure |
| 5 | `AUTOSAR` | AutosarTopLevelStructure | Critical - Root element |
| 6 | `AbsoluteTolerance` | TimingConstraint | Medium - Timing constraints |
| 7 | `AbstractCanCluster` | Fibex4Can | Medium - CAN communication |
| 8 | `AbstractCanCommunicationConnector` | Fibex4Can | Medium - CAN communication |
| 9 | `AbstractCanCommunicationController` | Fibex4Can | Medium - CAN communication |
| 10 | `AbstractCanCommunicationControllerAttributes` | Fibex4Can | Medium - CAN communication |
| 11 | `AbstractCanPhysicalChannel` | Fibex4Can | Medium - CAN communication |
| 12 | `AbstractClassTailoring` | BlueprintFormula | Low - Blueprint tailoring |
| 13 | `AbstractCondition` | InternalBehavior | Medium - Internal behavior |
| 14 | `AbstractDoIpLogicAddressProps` | DoIpLogicAddressProps | Low - DoIP addressing |
| 15 | `AbstractEnumerationValueVariationPoint` | VariantHandling | Medium - Variation points |
| 16 | `AbstractEthernetFrame` | Fibex4Ethernet | Medium - Ethernet frames |
| 17 | `AbstractEvent` | RTEEvents | High - Event handling |
| 18 | `AbstractGlobalTimeDomainProps` | GlobalTime | Medium - Time management |
| 19 | `AbstractImplementationDataType` | ImplementationDataTypes | High - Data types |
| 20 | `AbstractImplementationDataTypeElement` | ImplementationDataTypes | High - Data types |

**Note:** Only showing top 20 of 1,593 draft classes alphabetically. Full list available upon request.

### 9.2 Enumerations Draft Items (Top 20 of 265)

The following enumerations are in "draft" status and require review:

| # | Enum Name | Package | Literals | Priority Recommendation |
|---|-----------|---------|----------|------------------------|
| 1 | `AclScopeEnum` | RolesAndRights | 3 | Medium - Access control |
| 2 | `AdditionalBindingTimeEnum` | ModelRestrictionTypes | 2 | Low - Binding times |
| 3 | `AlignEnum` | DataDefProperties | 6 | Medium - Data alignment |
| 4 | `ApiPrincipleEnum` | PortInterface | 4 | Medium - API principles |
| 5 | `AreaEnumNohref` | InlineTextElements | 3 | Low - HTML area |
| 6 | `AreaEnumShape` | InlineTextElements | 4 | Low - HTML area shapes |
| 7 | `ArgumentDirectionEnum` | PrimitiveTypes | 3 | High - Argument direction |
| 8 | `ArrayImplPolicyEnum` | Datatypes | 3 | Medium - Array implementation |
| 9 | `ArraySizeHandlingEnum` | Datatypes | 3 | Medium - Array size handling |
| 10 | `ArraySizeSemanticsEnum` | Datatypes | 3 | Medium - Array size semantics |
| 11 | `AutoCollectEnum` | DataDefProperties | 3 | Medium - Data collection |
| 12 | `BindingTimeEnum` | VariantHandling | 2 | Medium - Binding times |
| 13 | `BswCallType` | BswBehavior | 6 | High - BSW calls |
| 14 | `BswEntryKindEnum` | BswInterfaces | 7 | High - BSW entry types |
| 15 | `BswEntryRelationshipEnum` | BswInterfaces | 6 | High - BSW relationships |
| 16 | `BswExecutionContext` | BswBehavior | 5 | High - BSW execution |
| 17 | `BswInterruptCategory` | BswBehavior | 7 | High - Interrupt categories |
| 18 | `ByteOrderEnum` | PrimitiveTypes | 2 | High - Byte ordering |
| 19 | `CSTransformerErrorReactionEnum` | ServiceMapping | 4 | Medium - Error handling |
| 20 | `CalprmAxisCategoryEnum` | CalibrationParameter | 6 | Medium - Calibration |

**Note:** Only showing top 20 of 265 draft enumerations alphabetically. Full list available upon request.

### 9.3 Primitives Draft Items (Top 20 of 50)

The following primitives are in "draft" status and require review:

| # | Primitive Name | Category | Priority Recommendation |
|---|-----------------|----------|------------------------|
| 1 | `Address` | Other | High - Memory addressing |
|  | | |  |
| 2 | `AlignmentType` | String-based | High - Memory alignment |
| 3 | `AnyServiceInstanceId` | String-based | Medium - Service IDs |
| 4 | `AnyVersionString` | String-based | Medium - Version strings |
| 5 | `AsamRecordLayoutSemantics` | Other | Low - Record layout |
| 6 | `AxisIndexType` | Other | Medium - Axis indexing |
| 7 | `BaseTypeEncodingString` | String-based | High - Base type encoding |
| 8 | `Boolean` | Numeric | Critical - Boolean values |
| 9 | `CIdentifier` | String-based | High - C identifiers |
| 10 | `CIdentifierWithIndex` | String-based | High - C identifiers with index |
| 11 | `CategoryString` | String-based | Medium - Categories |
| 12 | `CseCodeType` | Other | Low - CSE codes |
| 13 | `DateTime` | Other | Medium - Date/time values |
| 14 | `DiagRequirementIdString` | String-based | Medium - Diagnostic IDs |
| 15 | `DisplayFormatString` | String-based | Medium - Display formats |
| 16 | `ExtIdClassEnum` | Enumeration Proxy | Low - Extended IDs |
| 17 | `Float` | Numeric | Critical - Floating point |
| 18 | `Identifier` | String-based | Critical - Identifiers |
| 19 | `Integer` | Numeric | Critical - Integer values |
| 20 | `Ip4AddressString` | String-based | High - IPv4 addresses |

**Note:** Only showing top 20 of 50 draft primitives alphabetically. Full list available upon request.

---

*This report was automatically generated by analyzing JSON schema mapping files.*
