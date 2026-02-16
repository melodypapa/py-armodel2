"""SignalServiceTranslationProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)


class SignalServiceTranslationProps(Identifiable):
    """AUTOSAR SignalServiceTranslationProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("controls", None, False, True, ConsumedEventGroup),  # controls
        ("control_pncs", None, False, True, PncMappingIdent),  # controlPncs
        ("control_provideds", None, False, True, EventHandler),  # controlProvideds
        ("service_control", None, False, False, any (SignalService)),  # serviceControl
        ("signal_service_event_propses", None, False, True, any (SignalService)),  # signalServiceEventPropses
    ]

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationProps."""
        super().__init__()
        self.controls: list[ConsumedEventGroup] = []
        self.control_pncs: list[PncMappingIdent] = []
        self.control_provideds: list[EventHandler] = []
        self.service_control: Optional[Any] = None
        self.signal_service_event_propses: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SignalServiceTranslationProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationProps":
        """Create SignalServiceTranslationProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SignalServiceTranslationProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SignalServiceTranslationProps since parent returns ARObject
        return cast("SignalServiceTranslationProps", obj)


class SignalServiceTranslationPropsBuilder:
    """Builder for SignalServiceTranslationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationProps = SignalServiceTranslationProps()

    def build(self) -> SignalServiceTranslationProps:
        """Build and return SignalServiceTranslationProps object.

        Returns:
            SignalServiceTranslationProps instance
        """
        # TODO: Add validation
        return self._obj
