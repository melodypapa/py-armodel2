"""ApplicationCompositeElementDataPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_data_type import (
    ApplicationDataType,
)


class ApplicationCompositeElementDataPrototype(DataPrototype):
    """AUTOSAR ApplicationCompositeElementDataPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type", None, False, False, ApplicationDataType),  # type
    ]

    def __init__(self) -> None:
        """Initialize ApplicationCompositeElementDataPrototype."""
        super().__init__()
        self.type: Optional[ApplicationDataType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationCompositeElementDataPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeElementDataPrototype":
        """Create ApplicationCompositeElementDataPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationCompositeElementDataPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationCompositeElementDataPrototype since parent returns ARObject
        return cast("ApplicationCompositeElementDataPrototype", obj)


class ApplicationCompositeElementDataPrototypeBuilder:
    """Builder for ApplicationCompositeElementDataPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeElementDataPrototype = ApplicationCompositeElementDataPrototype()

    def build(self) -> ApplicationCompositeElementDataPrototype:
        """Build and return ApplicationCompositeElementDataPrototype object.

        Returns:
            ApplicationCompositeElementDataPrototype instance
        """
        # TODO: Add validation
        return self._obj
