## Implementation Plan: Model Classes with Plural List Members

### Overview
Implement serialization/deserialization for AUTOSAR_Datatypes.arxml using member information from docs/requirements/packages/ with plural naming for lists.

### Classes to Update with Members (from packages directory)

**AUTOSAR (ARObject):**
- ar_packages: List[ARPackage]

**ARPackage (CollectableElement → Identifiable):**
- Inherits short_name from Referrable
- category: Optional[str]
- elements: List[Any] (holds SwBaseType, CompuMethod, DataConstr, ImplementationDataType)
- ar_packages: List[ARPackage]

**SwBaseType (BaseType → Identifiable):**
- Inherits short_name from Referrable
- category: str
- base_type_sizes: List[int]
- base_type_encodings: List[str]
- mem_alignments: List[int]
- native_declarations: List[str]

**CompuMethod (Identifiable):**
- Inherits short_name from Referrable
- category: str
- compu_internals: List[Compu]

**Compu (ARObject):**
- compu_contents: List[CompuContent]

**CompuScales (CompuContent):**
- compu_scales: List[CompuScale]

**CompuScale (ARObject):**
- lower_limits: List[Limit]
- upper_limits: List[Limit]
- compu_scale_contents: List[CompuScaleContents]

**CompuScaleConstantContents (CompuScaleContents):**
- compu_consts: List[CompuConst]

**CompuConst (ARObject):**
- compu_const_contents: List[CompuConstContent]

**CompuConstTextContent (CompuConstContent):**
- vts: List[str]

**DataConstr (ARElement → Identifiable):**
- Inherits short_name from Referrable
- data_constr_rules: List[DataConstrRule]

**DataConstrRule (ARObject):**
- internal_constrs: List[InternalConstrs]

**InternalConstrs (ARObject):**
- lower_limits: List[Limit]
- upper_limits: List[Limit]

**ImplementationDataType (AbstractImplementationDataType → Identifiable):**
- Inherits short_name from Referrable
- category: str
- type_emitters: List[str]
- sw_data_def_props: List[SwDataDefProps]

### Implementation Strategy

**Phase 1: Create Base Classes**
- Referrable (with short_name)
- Identifiable, CollectableElement, PackageableElement, ARElement
- BaseType, AutosarDataType, AbstractImplementationDataType
- CompuContent, CompuConstContent, CompuScaleContents

**Phase 2: Create/Update Helper Classes**
- Compu, CompuScales, CompuScaleConstantContents, CompuConstTextContent
- DataConstrRules, SwDataDefProps, SwDataDefPropsVariants, SwDataDefPropsConditional
- Limit (with interval_type attribute and value)

**Phase 3: Update Main Classes**
- Add members using plural forms for lists
- Use Optional[T] for 0..1 multiplicity
- Use List[T] for * multiplicity

**Phase 4: Implement Serialization/Deserialization**
- Use hyphenated XML names
- Handle naming conversion (snake_case ↔ UPPER-CASE)
- Serialize plural lists to multiple XML elements
- Deserialize multiple XML elements to plural lists

**Phase 5: Add Tests**
- Integration tests for AUTOSAR_Datatypes.arxml
- Verify all 47 elements parsed correctly

### Key Decisions
- Use plural forms for all list members (e.g., ar_packages, compu_scales)
- Follow packages directory for member definitions
- short_name is in Referrable base class
- Multiplicity 0..1 → Optional[T], * → List[T]