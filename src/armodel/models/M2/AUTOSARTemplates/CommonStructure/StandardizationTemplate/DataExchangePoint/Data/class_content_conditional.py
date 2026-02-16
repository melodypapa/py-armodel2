"""ClassContentConditional AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.constraint_tailoring import (
    ConstraintTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.sdg_tailoring import (
    SdgTailoring,
)


class ClassContentConditional(Identifiable):
    """AUTOSAR ClassContentConditional."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("attributes", None, False, True, AttributeTailoring),  # attributes
        ("condition", None, False, False, AbstractCondition),  # condition
        ("constraints", None, False, True, ConstraintTailoring),  # constraints
        ("sdg_tailorings", None, False, True, SdgTailoring),  # sdgTailorings
    ]

    def __init__(self) -> None:
        """Initialize ClassContentConditional."""
        super().__init__()
        self.attributes: list[AttributeTailoring] = []
        self.condition: Optional[AbstractCondition] = None
        self.constraints: list[ConstraintTailoring] = []
        self.sdg_tailorings: list[SdgTailoring] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClassContentConditional to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassContentConditional":
        """Create ClassContentConditional from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClassContentConditional instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClassContentConditional since parent returns ARObject
        return cast("ClassContentConditional", obj)


class ClassContentConditionalBuilder:
    """Builder for ClassContentConditional."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassContentConditional = ClassContentConditional()

    def build(self) -> ClassContentConditional:
        """Build and return ClassContentConditional object.

        Returns:
            ClassContentConditional instance
        """
        # TODO: Add validation
        return self._obj
