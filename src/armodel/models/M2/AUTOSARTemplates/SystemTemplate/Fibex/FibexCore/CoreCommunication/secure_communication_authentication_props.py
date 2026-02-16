"""SecureCommunicationAuthenticationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecureCommunicationAuthenticationProps(Identifiable):
    """AUTOSAR SecureCommunicationAuthenticationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("auth_info_tx", None, True, False, None),  # authInfoTx
    ]

    def __init__(self) -> None:
        """Initialize SecureCommunicationAuthenticationProps."""
        super().__init__()
        self.auth_info_tx: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecureCommunicationAuthenticationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecureCommunicationAuthenticationProps":
        """Create SecureCommunicationAuthenticationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecureCommunicationAuthenticationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecureCommunicationAuthenticationProps since parent returns ARObject
        return cast("SecureCommunicationAuthenticationProps", obj)


class SecureCommunicationAuthenticationPropsBuilder:
    """Builder for SecureCommunicationAuthenticationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecureCommunicationAuthenticationProps = SecureCommunicationAuthenticationProps()

    def build(self) -> SecureCommunicationAuthenticationProps:
        """Build and return SecureCommunicationAuthenticationProps object.

        Returns:
            SecureCommunicationAuthenticationProps instance
        """
        # TODO: Add validation
        return self._obj
