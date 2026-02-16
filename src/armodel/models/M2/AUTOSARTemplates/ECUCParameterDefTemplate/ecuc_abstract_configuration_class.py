"""EcucAbstractConfigurationClass AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class EcucAbstractConfigurationClass(ARObject):
    """AUTOSAR EcucAbstractConfigurationClass."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("config_class", None, False, False, EcucConfigurationClassEnum),  # configClass
        ("config_variant", None, False, False, any (EcucConfiguration)),  # configVariant
    ]

    def __init__(self) -> None:
        """Initialize EcucAbstractConfigurationClass."""
        super().__init__()
        self.config_class: Optional[EcucConfigurationClassEnum] = None
        self.config_variant: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EcucAbstractConfigurationClass to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractConfigurationClass":
        """Create EcucAbstractConfigurationClass from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EcucAbstractConfigurationClass instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EcucAbstractConfigurationClass since parent returns ARObject
        return cast("EcucAbstractConfigurationClass", obj)


class EcucAbstractConfigurationClassBuilder:
    """Builder for EcucAbstractConfigurationClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucAbstractConfigurationClass = EcucAbstractConfigurationClass()

    def build(self) -> EcucAbstractConfigurationClass:
        """Build and return EcucAbstractConfigurationClass object.

        Returns:
            EcucAbstractConfigurationClass instance
        """
        # TODO: Add validation
        return self._obj
