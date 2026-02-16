"""ReferenceBase AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
    ARPackage,
)


class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("global_elements", None, False, True, None),  # globalElements
        ("global_ins", None, False, True, ARPackage),  # globalIns
        ("is_default", None, True, False, None),  # isDefault
        ("package", None, False, False, ARPackage),  # package
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.global_elements: list[ReferrableSubtypesEnum] = []
        self.global_ins: list[ARPackage] = []
        self.is_default: Boolean = None
        self.package: Optional[ARPackage] = None
        self.short_label: Identifier = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReferenceBase to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Create ReferenceBase from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReferenceBase instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReferenceBase since parent returns ARObject
        return cast("ReferenceBase", obj)


class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
