"""SecuredIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SecuredIPdu(IPdu):
    """AUTOSAR SecuredIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, any (SecureCommunication)),  # authentication
        ("dynamic", None, True, False, None),  # dynamic
        ("freshness_props", None, False, False, any (SecureCommunication)),  # freshnessProps
        ("payload", None, False, False, PduTriggering),  # payload
        ("secure", None, False, False, any (SecureCommunication)),  # secure
        ("use_as", None, True, False, None),  # useAs
        ("use_secured_pdu", None, False, False, SecuredPduHeaderEnum),  # useSecuredPdu
    ]

    def __init__(self) -> None:
        """Initialize SecuredIPdu."""
        super().__init__()
        self.authentication: Optional[Any] = None
        self.dynamic: Optional[Boolean] = None
        self.freshness_props: Optional[Any] = None
        self.payload: Optional[PduTriggering] = None
        self.secure: Optional[Any] = None
        self.use_as: Optional[Boolean] = None
        self.use_secured_pdu: Optional[SecuredPduHeaderEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SecuredIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecuredIPdu":
        """Create SecuredIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SecuredIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SecuredIPdu since parent returns ARObject
        return cast("SecuredIPdu", obj)


class SecuredIPduBuilder:
    """Builder for SecuredIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecuredIPdu = SecuredIPdu()

    def build(self) -> SecuredIPdu:
        """Build and return SecuredIPdu object.

        Returns:
            SecuredIPdu instance
        """
        # TODO: Add validation
        return self._obj
