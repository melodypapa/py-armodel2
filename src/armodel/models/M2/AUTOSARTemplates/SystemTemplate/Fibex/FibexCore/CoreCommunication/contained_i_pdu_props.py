"""ContainedIPduProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainedIPduProps(ARObject):
    """AUTOSAR ContainedIPduProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("collection", None, False, False, any (ContainedIPdu)),  # collection
        ("contained_pdu", None, False, False, PduTriggering),  # containedPdu
        ("header_id_long", None, True, False, None),  # headerIdLong
        ("header_id_short", None, True, False, None),  # headerIdShort
        ("offset", None, True, False, None),  # offset
        ("priority", None, True, False, None),  # priority
        ("timeout", None, True, False, None),  # timeout
        ("trigger", None, False, False, PduCollectionTriggerEnum),  # trigger
        ("update", None, True, False, None),  # update
    ]

    def __init__(self) -> None:
        """Initialize ContainedIPduProps."""
        super().__init__()
        self.collection: Optional[Any] = None
        self.contained_pdu: Optional[PduTriggering] = None
        self.header_id_long: Optional[PositiveInteger] = None
        self.header_id_short: Optional[PositiveInteger] = None
        self.offset: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.timeout: Optional[TimeValue] = None
        self.trigger: Optional[PduCollectionTriggerEnum] = None
        self.update: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ContainedIPduProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainedIPduProps":
        """Create ContainedIPduProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ContainedIPduProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ContainedIPduProps since parent returns ARObject
        return cast("ContainedIPduProps", obj)


class ContainedIPduPropsBuilder:
    """Builder for ContainedIPduProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainedIPduProps = ContainedIPduProps()

    def build(self) -> ContainedIPduProps:
        """Build and return ContainedIPduProps object.

        Returns:
            ContainedIPduProps instance
        """
        # TODO: Add validation
        return self._obj
