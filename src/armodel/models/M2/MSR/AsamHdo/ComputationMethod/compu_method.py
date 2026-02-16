"""CompuMethod AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DisplayFormatString,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu import (
    Compu,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class CompuMethod(ARElement):
    """AUTOSAR CompuMethod."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_internal", None, False, False, Compu),  # compuInternal
        ("compu_phys_to", None, False, False, Compu),  # compuPhysTo
        ("display_format_string", None, True, False, None),  # displayFormatString
        ("unit", None, False, False, Unit),  # unit
    ]

    def __init__(self) -> None:
        """Initialize CompuMethod."""
        super().__init__()
        self.compu_internal: Optional[Compu] = None
        self.compu_phys_to: Optional[Compu] = None
        self.display_format_string: Optional[DisplayFormatString] = None
        self.unit: Optional[Unit] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuMethod to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuMethod":
        """Create CompuMethod from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuMethod instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuMethod since parent returns ARObject
        return cast("CompuMethod", obj)


class CompuMethodBuilder:
    """Builder for CompuMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuMethod = CompuMethod()

    def build(self) -> CompuMethod:
        """Build and return CompuMethod object.

        Returns:
            CompuMethod instance
        """
        # TODO: Add validation
        return self._obj
