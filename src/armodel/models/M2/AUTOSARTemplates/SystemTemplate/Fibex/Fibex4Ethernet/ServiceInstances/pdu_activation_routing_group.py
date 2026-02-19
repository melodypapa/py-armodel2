"""PduActivationRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 488)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_group_ref: Optional[ARRef]
    i_pdu_identifiers: list[SoConIPduIdentifier]
    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[ARRef] = None
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []
    def serialize(self) -> ET.Element:
        """Serialize PduActivationRoutingGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduActivationRoutingGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_group_ref
        if self.event_group_ref is not None:
            serialized = ARObject._serialize_item(self.event_group_ref, "EventGroupControlTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize i_pdu_identifiers (list to container "I-PDU-IDENTIFIERS")
        if self.i_pdu_identifiers:
            wrapper = ET.Element("I-PDU-IDENTIFIERS")
            for item in self.i_pdu_identifiers:
                serialized = ARObject._serialize_item(item, "SoConIPduIdentifier")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduActivationRoutingGroup":
        """Deserialize XML element to PduActivationRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduActivationRoutingGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduActivationRoutingGroup, cls).deserialize(element)

        # Parse event_group_ref
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_ref_value = EventGroupControlTypeEnum.deserialize(child)
            obj.event_group_ref = event_group_ref_value

        # Parse i_pdu_identifiers (list from container "I-PDU-IDENTIFIERS")
        obj.i_pdu_identifiers = []
        container = ARObject._find_child_element(element, "I-PDU-IDENTIFIERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_identifiers.append(child_value)

        return obj



class PduActivationRoutingGroupBuilder:
    """Builder for PduActivationRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()

    def build(self) -> PduActivationRoutingGroup:
        """Build and return PduActivationRoutingGroup object.

        Returns:
            PduActivationRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
