"""AbstractGlobalTimeDomainProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class AbstractGlobalTimeDomainProps(ARObject):
    """AUTOSAR AbstractGlobalTimeDomainProps."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AbstractGlobalTimeDomainProps."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractGlobalTimeDomainProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractGlobalTimeDomainProps":
        """Create AbstractGlobalTimeDomainProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractGlobalTimeDomainProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractGlobalTimeDomainProps since parent returns ARObject
        return cast("AbstractGlobalTimeDomainProps", obj)


class AbstractGlobalTimeDomainPropsBuilder:
    """Builder for AbstractGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractGlobalTimeDomainProps = AbstractGlobalTimeDomainProps()

    def build(self) -> AbstractGlobalTimeDomainProps:
        """Build and return AbstractGlobalTimeDomainProps object.

        Returns:
            AbstractGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
