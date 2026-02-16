"""HwAttributeValue AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_def import (
    HwAttributeDef,
)


class HwAttributeValue(ARObject):
    """AUTOSAR HwAttributeValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("annotation", None, False, False, Annotation),  # annotation
        ("hw_attribute_def", None, False, False, HwAttributeDef),  # hwAttributeDef
        ("v", None, True, False, None),  # v
        ("vt", None, True, False, None),  # vt
    ]

    def __init__(self) -> None:
        """Initialize HwAttributeValue."""
        super().__init__()
        self.annotation: Optional[Annotation] = None
        self.hw_attribute_def: Optional[HwAttributeDef] = None
        self.v: Optional[Numerical] = None
        self.vt: Optional[VerbatimString] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwAttributeValue to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeValue":
        """Create HwAttributeValue from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwAttributeValue instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwAttributeValue since parent returns ARObject
        return cast("HwAttributeValue", obj)


class HwAttributeValueBuilder:
    """Builder for HwAttributeValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeValue = HwAttributeValue()

    def build(self) -> HwAttributeValue:
        """Build and return HwAttributeValue object.

        Returns:
            HwAttributeValue instance
        """
        # TODO: Add validation
        return self._obj
