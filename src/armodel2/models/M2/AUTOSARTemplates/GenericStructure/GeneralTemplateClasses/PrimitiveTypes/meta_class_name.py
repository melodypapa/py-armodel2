"""MetaClassName AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# Name of a class in the AUTOSAR Meta-Model. Tags: xml.xsd.customType=META-CLASS-NAME xml.xsd.pattern=[A-Z][a-zA-Z0-9_]* xml.xsd.type=string Table 4.36: MetaClassName 102 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 4.7 Model Restriction Types [TPS_GST_00376] Purpose of Model Restriction Types (cid:100)Model Restriction Types specify rules that restrict the content of AUTOSAR models. Those restrictions are e.g. used in the context of Special Data Group Definitions or Data Exchange Points [2].(cid:99)() Corresponding details to Special Data Group Definitions are given in 4.6.2. AbstractMultiplicityRestriction + lowerMultiplicity: PositiveInteger [0..1] + upperMultiplicity: PositiveInteger [0..1] + upperMultiplicityInfinite: Boolean [0..1] AbstractValueRestriction + max: Limit [0..1] + maxLength: PositiveInteger [0..1] + min: Limit [0..1] + minLength: PositiveInteger [0..1] «enumeration» + pattern: RegularExpression [0..1] FullBindingTimeEnum blueprintDerivationTime systemDesignTime AbstractVariationRestriction codeGenerationTime + validBindingTime: FullBindingTimeEnum [0..*] preCompileTime + variation: Boolean [0..1] linkTime postBuild Figure 4.12: Model Restriction Types 4.7.1 Restriction of Simple Primitive Values [TPS_GST_00377] Purpose of AbstractValueRestriction (cid:100) The Abstract- ValueRestriction defines constraints on the value space of a simple primitive data type. The attributes of this class represent constraining facets according to the XML Schema Specification [11]. A value is valid if it is valid according to all defined con- straints.(cid:99)()
class MetaClassName(ARPrimitive):
    """AUTOSAR MetaClassName primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize MetaClassName.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
