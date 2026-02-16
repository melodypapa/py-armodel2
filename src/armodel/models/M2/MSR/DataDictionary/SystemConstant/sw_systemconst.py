"""SwSystemconst AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class SwSystemconst(ARElement):
    """AUTOSAR SwSystemconst."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
    ]

    def __init__(self) -> None:
        """Initialize SwSystemconst."""
        super().__init__()
        self.sw_data_def: Optional[SwDataDefProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwSystemconst to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwSystemconst":
        """Create SwSystemconst from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwSystemconst instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwSystemconst since parent returns ARObject
        return cast("SwSystemconst", obj)


class SwSystemconstBuilder:
    """Builder for SwSystemconst."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwSystemconst = SwSystemconst()

    def build(self) -> SwSystemconst:
        """Build and return SwSystemconst object.

        Returns:
            SwSystemconst instance
        """
        # TODO: Add validation
        return self._obj
