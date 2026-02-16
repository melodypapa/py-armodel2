"""HwAttributeDef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_literal_def import (
    HwAttributeLiteralDef,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class HwAttributeDef(Identifiable):
    """AUTOSAR HwAttributeDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("hw_attributes", None, False, True, HwAttributeLiteralDef),  # hwAttributes
        ("is_required", None, True, False, None),  # isRequired
        ("unit", None, False, False, Unit),  # unit
    ]

    def __init__(self) -> None:
        """Initialize HwAttributeDef."""
        super().__init__()
        self.hw_attributes: list[HwAttributeLiteralDef] = []
        self.is_required: Optional[Boolean] = None
        self.unit: Optional[Unit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwAttributeDef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeDef":
        """Create HwAttributeDef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwAttributeDef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwAttributeDef since parent returns ARObject
        return cast("HwAttributeDef", obj)


class HwAttributeDefBuilder:
    """Builder for HwAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeDef = HwAttributeDef()

    def build(self) -> HwAttributeDef:
        """Build and return HwAttributeDef object.

        Returns:
            HwAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
