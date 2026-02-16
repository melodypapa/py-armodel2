"""Map AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.area import (
    Area,
)


class Map(ARObject):
    """AUTOSAR Map."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("area", None, False, False, Area),  # area
        ("class_", 'CLASS', True, False, None),  # class
        ("name", None, True, False, None),  # name
        ("onclick", None, True, False, None),  # onclick
        ("ondblclick", None, True, False, None),  # ondblclick
        ("onkeydown", None, True, False, None),  # onkeydown
        ("onkeypress", None, True, False, None),  # onkeypress
        ("onkeyup", None, True, False, None),  # onkeyup
        ("onmousedown", None, True, False, None),  # onmousedown
        ("onmousemove", None, True, False, None),  # onmousemove
        ("onmouseout", None, True, False, None),  # onmouseout
        ("onmouseover", None, True, False, None),  # onmouseover
        ("onmouseup", None, True, False, None),  # onmouseup
        ("title", None, True, False, None),  # title
    ]

    def __init__(self) -> None:
        """Initialize Map."""
        super().__init__()
        self.area: Area = None
        self.class_: Optional[String] = None
        self.name: Optional[NameToken] = None
        self.onclick: Optional[String] = None
        self.ondblclick: Optional[String] = None
        self.onkeydown: Optional[String] = None
        self.onkeypress: Optional[String] = None
        self.onkeyup: Optional[String] = None
        self.onmousedown: Optional[String] = None
        self.onmousemove: Optional[String] = None
        self.onmouseout: Optional[String] = None
        self.onmouseover: Optional[String] = None
        self.onmouseup: Optional[String] = None
        self.title: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Map to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Map":
        """Create Map from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Map instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Map since parent returns ARObject
        return cast("Map", obj)


class MapBuilder:
    """Builder for Map."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Map = Map()

    def build(self) -> Map:
        """Build and return Map object.

        Returns:
            Map instance
        """
        # TODO: Add validation
        return self._obj
