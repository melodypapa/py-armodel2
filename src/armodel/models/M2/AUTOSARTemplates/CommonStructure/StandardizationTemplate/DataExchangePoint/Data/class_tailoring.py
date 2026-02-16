"""ClassTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_content_conditional import (
    ClassContentConditional,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)


class ClassTailoring(ARObject):
    """AUTOSAR ClassTailoring."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("class_contents", None, False, True, ClassContentConditional),  # classContents
        ("multiplicity", None, False, False, any (MultiplicityRestriction)),  # multiplicity
        ("variation", None, False, False, VariationRestrictionWithSeverity),  # variation
    ]

    def __init__(self) -> None:
        """Initialize ClassTailoring."""
        super().__init__()
        self.class_contents: list[ClassContentConditional] = []
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ClassTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClassTailoring":
        """Create ClassTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ClassTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ClassTailoring since parent returns ARObject
        return cast("ClassTailoring", obj)


class ClassTailoringBuilder:
    """Builder for ClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClassTailoring = ClassTailoring()

    def build(self) -> ClassTailoring:
        """Build and return ClassTailoring object.

        Returns:
            ClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
