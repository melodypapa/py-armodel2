# AUTOSAR Model Data Analysis Report
**Generated:** 2026-03-17
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
| **Overall Maturity** | 12.3% reviewed (239/1,938), 87.7% draft (1,699/1,938) |

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
| **Reviewed** | 222 | 13.7% |
| **Draft** | 1,401 | 86.3% |

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
| **Reviewed** | 15 | 5.7% |
| **Draft** | 250 | 94.3% |

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
| **Reviewed** | 2 | 4.0% |
| **Draft** | 48 | 96.0% |

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
| **Classes Maturity** | 13.7% reviewed | ✓ Improved |
| **Enumerations Maturity** | 5.7% reviewed | ⚠ Low |
| **Primitives Maturity** | 4.0% reviewed | ⚠ Low |
| **Overall Maturity** | 12.3% reviewed | ⚠ Moderate |
| **Abstract Classes** | 14.5% | ⚠ Review |
| **Avg Attributes/Class** | 2.6 | ✓ Reasonable |
| **Avg Literals/Enum** | 3.7 | ✓ Concise |

## 6. Key Findings

### 6.1 Scale and Complexity

- The AUTOSAR model defines **1,623 classes**, indicating a comprehensive  and detailed meta-model covering all aspects of automotive software architecture.
- With **265 enumerations** containing **969 literals**,  the model provides rich type safety and semantic clarity.
- **50 primitive types** form the foundation of the type system.

### 6.2 Maturity Status

- **Classes:** 13.7% (222 out of 1,623) are marked as 'reviewed', 86.3% (1,401) remain in 'draft' status
- **Enumerations:** 5.7% (15 out of 265) are marked as 'reviewed', 94.3% (250) remain in 'draft' status
- **Primitives:** 4.0% (2 out of 50) are marked as 'reviewed', 96.0% (48) remain in 'draft' status
- **Overall:** 12.3% (239 out of 1,938 total elements) are marked as 'reviewed'
- Significant improvement from previous analysis with 192 additional classes marked as reviewed

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
  - **Classes:** 1,401 classes remaining in draft status (86.3%)
  - **Enumerations:** 250 enumerations remaining in draft status (94.3%)
  - **Primitives:** 48 primitives remaining in draft status (96.0%)
- Focus on elements in frequently used templates (SWComponentTemplate, SystemTemplate, etc.)
- Establish a formal review process for new elements added to the meta-model
- Create a maturity review schedule with milestones for high-priority elements

### 7.3 Documentation

- Ensure all classes have comprehensive documentation, especially polymorphic ones.
- Document the usage patterns for atp_variant and atp_mixed classes.
- Provide examples for complex enumeration values.

## 8. Maturity Summary

### 8.1 Reviewed Elements Summary

| Type | Count | Percentage |
|------|-------|------------|
| **Classes** | 222 | 13.7% |
| **Enumerations** | 15 | 5.7% |
| **Primitives** | 2 | 4.0% |
| **Total** | 239 | 12.3% |

### 8.2 Draft Elements Summary

| Type | Count | Percentage |
|------|-------|------------|
| **Classes** | 1,401 | 86.3% |
| **Enumerations** | 250 | 94.3% |
| **Primitives** | 48 | 96.0% |
| **Total** | 1,699 | 87.7% |

---

*For detailed lists of reviewed and draft items, refer to the `docs/reports/maturity-analysis.txt` file generated by `tools/analyze_maturity.py`.*

---

*This report was automatically generated by analyzing JSON schema mapping files.*
