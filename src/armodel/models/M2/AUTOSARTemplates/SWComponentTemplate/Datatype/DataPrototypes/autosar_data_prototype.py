"""AutosarDataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.autosar_data_type import (
    AutosarDataType,
)


class AutosarDataPrototype(DataPrototype):
    """AUTOSAR AutosarDataPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type", None, False, False, AutosarDataType),  # type
    ]

    def __init__(self) -> None:
        """Initialize AutosarDataPrototype."""
        super().__init__()
        self.type: Optional[AutosarDataType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AutosarDataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AutosarDataPrototype":
        """Create AutosarDataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AutosarDataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AutosarDataPrototype since parent returns ARObject
        return cast("AutosarDataPrototype", obj)


class AutosarDataPrototypeBuilder:
    """Builder for AutosarDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AutosarDataPrototype = AutosarDataPrototype()

    def build(self) -> AutosarDataPrototype:
        """Build and return AutosarDataPrototype object.

        Returns:
            AutosarDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
