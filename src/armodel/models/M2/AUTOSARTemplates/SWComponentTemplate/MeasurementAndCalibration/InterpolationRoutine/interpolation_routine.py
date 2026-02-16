"""InterpolationRoutine AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class InterpolationRoutine(ARObject):
    """AUTOSAR InterpolationRoutine."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("interpolation", None, False, False, BswModuleEntry),  # interpolation
        ("is_default", None, True, False, None),  # isDefault
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize InterpolationRoutine."""
        super().__init__()
        self.interpolation: Optional[BswModuleEntry] = None
        self.is_default: Optional[Boolean] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InterpolationRoutine to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InterpolationRoutine":
        """Create InterpolationRoutine from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InterpolationRoutine instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InterpolationRoutine since parent returns ARObject
        return cast("InterpolationRoutine", obj)


class InterpolationRoutineBuilder:
    """Builder for InterpolationRoutine."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InterpolationRoutine = InterpolationRoutine()

    def build(self) -> InterpolationRoutine:
        """Build and return InterpolationRoutine object.

        Returns:
            InterpolationRoutine instance
        """
        # TODO: Add validation
        return self._obj
